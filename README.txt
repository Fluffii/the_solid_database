Для начала необходимо создать базу данных. Для этого в консоли прописываем команды:
python
from app import db
db.create_all()
exit()

Запуск приложения с файла main.py

Команды для миграции БД:
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

<!--            <li class="nav-item">-->
<!--                <a class="nav-link" href="{{ url_for('posts.create_post') }}">Create post</a>-->
<!--            </li>-->

<li class="nav-item active">
    <a class="nav-link" href="{{ url_for('posts.index') }}"><i class="fa fa-home" aria-hidden="true"></i> Главная<span class="sr-only">(current)</span></a>
</li>