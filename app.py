from flask import Flask, redirect, url_for, request, render_template
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin, AdminIndexView, form
from flask_admin.contrib import sqla
from jinja2 import Markup
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user, login_required, logout_user

import random
import os

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Admin panel
from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView, sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        url = url_for('static', filename=os.path.join('img/post_image/', model.path))

        if model.type in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup('<img src="%s" width="100">' % url)

    column_formatters = {
        'path': _list_thumbnail
    }

    form_extra_fields = {
        'file': form.FileUploadField('file',
                                     base_path='static/img/post_image/')
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                path = '%s.%s' % (hash, ext)

                storage_file.save(
                    os.path.join(app.config['UPLOADED_PATH'], path)
                )

                _form.name.data = _form.name.data or storage_file.filename
                _form.path.data = path
                _form.type.data = ext

                del _form.file

        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_path_data(
            super(PostAdminView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_path_data(
            super(PostAdminView, self).create_form(obj)
        )

    form_columns = ['title', 'short_description', 'body', 'tags', 'path', 'type', 'file']
    column_searchable_list = ['id']


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


class UserAdminView(ModelView):
    column_list = ('email', 'roles', 'active')
    excluded_columns = ('password',)
    can_edit = False


class FeedBackAdminView(ModelView):
    can_edit = False


class AllAdminView(ModelView):
    column_searchable_list = ['id']


admin = Admin(app, 'The Soil Database', url='/index', index_view=HomeAdminView(name='Главная'))
admin.add_view(PostAdminView(Post, db.session, name='Посты'))
admin.add_view(TagAdminView(Tag, db.session, name='Теги'))
admin.add_view(UserAdminView(User, db.session, name='Пользователи'))
admin.add_view(AdminView(Role, db.session, name='Роли'))
admin.add_view(FeedBackAdminView(Feedback, db.session, name='Отзывы'))
admin.add_view(AllAdminView(Tablenso, db.session, name='НСО'))
admin.add_view(AllAdminView(Aggregates, db.session, name='Структурность'))
admin.add_view(AllAdminView(Bulkweight, db.session, name='Равновесная плотность'))
admin.add_view(AllAdminView(Deflation, db.session, name='Дефляция'))
admin.add_view(AllAdminView(Erosion, db.session, name='Эрозия'))
admin.add_view(AllAdminView(Granulometry, db.session, name='Гранулометрический состав'))
admin.add_view(AllAdminView(Humus, db.session, name='Содержание гумуса'))
admin.add_view(AllAdminView(Moisture, db.session, name='Продуктивная влага'))
admin.add_view(AllAdminView(Ph, db.session, name='Кислотность'))
admin.add_view(AllAdminView(Phosphorus, db.session, name='Подвижный фосфор'))
admin.add_view(AllAdminView(Potassium, db.session, name='Подвижный калий'))
admin.add_view(AllAdminView(Power, db.session, name='Мощность гумусового горизонта'))
admin.add_view(AllAdminView(Salinization, db.session, name='Засоление почв'))
admin.add_view(AllAdminView(Solonetzes, db.session, name='Виды солонцов'))
admin.add_view(AllAdminView(Water_resistant, db.session, name='Водопрочные агрегаты'))
admin.add_view(AllAdminView(Xoz, db.session, name='Хозяйства'))

# Flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
