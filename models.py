from app import db
from sqlalchemy import *
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    short_description = db.Column(db.Text)
    path = db.Column(db.Unicode(128))
    type = db.Column(db.Unicode(3))
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format(self.name)


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                       )


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    messages = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.now())


# Flask-security
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '{}'.format(self.email)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '{}'.format(self.name)


# Модели всех таблиц
# Почвенная база данных НСО
class Tablenso(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_tip = db.Column(db.Integer())
    index_tip = db.Column(db.Text)
    name_tip_podtip = db.Column(db.Text)
    granulometry = db.Column(db.Integer())
    power = db.Column(db.Integer())
    humus_1 = db.Column(db.Integer())
    humus_2 = db.Column(db.Text)
    ph_water1 = db.Column(db.Integer())
    ph_water2 = db.Column(db.Text)
    water_sm = db.Column(db.Integer())
    water_mm = db.Column(db.Text)
    ground_water = db.Column(db.Integer())


# Структурность
class Aggregates(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.String(50))
    id_tip = db.Column(db.String(50))
    note = db.Column(db.Text)


# Равновесная плотность
class Bulkweight(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Дефляция
class Deflation(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Эрозия
class Erosion(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Гранулометрический состав
class Granulometry(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Содержание гумуса
class Humus(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Продуктивная влага
class Moisture(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Кислотность
class Ph(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion_1 = db.Column(db.Text)
    criterion_2 = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Подвижный фосфор
class Phosphorus(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Подвижный калий
class Potassium(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Мощность гумусового горизонта
class Power(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Засоление почв
class Salinization(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion_1 = db.Column(db.Text)
    criterion_2 = db.Column(db.Text)
    criterion_3 = db.Column(db.Text)
    criterion_4 = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Виды солонцов
class Solonetzes(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Водопрочные агрегаты
class Water_resistant(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer())
    gradation = db.Column(db.Text)
    criterion = db.Column(db.Text)
    id_tip = db.Column(db.Text)
    note = db.Column(db.Text)


# Почвенная база данных хозяйств
class Xoz(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_type = db.Column(db.Integer())
    id_soil = db.Column(db.Integer())
    podtype = db.Column(db.Text)
    name_soil = db.Column(db.Text)
    index_map = db.Column(db.Text)
    index_base = db.Column(db.Text)
    location = db.Column(db.Text)
    raion = db.Column(db.Text)
    power = db.Column(db.Integer())
    humus = db.Column(db.Float())
    clay = db.Column(db.Integer())
    ph = db.Column(db.Float())
    phoshorus = db.Column(db.Integer())
    potassium = db.Column(db.Integer())
    aggregates = db.Column(db.Integer())
    bulkweight = db.Column(db.Float())
    code_power = db.Column(db.Integer())
    code_humus = db.Column(db.Integer())
    code_gran = db.Column(db.Integer())
    code_ph = db.Column(db.Integer())
    code_phoshorus = db.Column(db.Integer())
    code_potassium = db.Column(db.Integer())
    code_aggregates = db.Column(db.Integer())
    code_bulkweight = db.Column(db.Integer())
    code_erosia = db.Column(db.Integer())
    code_solonetzes = db.Column(db.Integer())
    code_salinisation = db.Column(db.Integer())
    code_drain = db.Column(db.Integer())
    kpower = db.Column(db.Float())
    khumus = db.Column(db.Float())
    kclay = db.Column(db.Float())
    kph = db.Column(db.Float())
    kerosion = db.Column(db.Float())
    ksolon = db.Column(db.Float())
    ksalin = db.Column(db.Float())
    kdrain = db.Column(db.Float())
    ksoil = db.Column(db.Float())
    bonitet = db.Column(db.Text)
    pei = db.Column(db.Text)
    standard_yield = db.Column(db.Float())