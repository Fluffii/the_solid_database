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

<!— <li class="nav-item">-->
<!— <a class="nav-link" href="{{ url_for('posts.create_post') }}">Create post</a>-->
<!— </li>-->

<li class="nav-item active">
<a class="nav-link" href="{{ url_for('posts.index') }}"><i class="fa fa-home" aria-hidden="true"></i> Главная<span class="sr-only">(current)</span></a>
</li>

Работа с Git команды:
git init
git add . - Стадия ожидания
git status
git rm —cached . - Удалить из стадии ожидания
git commit -m "Полный проект"
.gitignore
git log —oneline
git checkout <id>
git checkout master
git revert <id> - Отмена изменений
git reset <id> - Удаление коммита до id
git reset <id> —hard - Удаление с файлами
git branch <name> - Отдельная ветка
git checkout <name_branch>
git branch -a
git checkout - b <name_branch> - Создание ветки и сразу переход в нее
git merge <name_branch> - Объединение веток
git remote
Сначала добавление на локалку, затем на виртуалку

git add .
git status
git commit -m "Comments"
git remote add origin <url>
git push -u origin master

Основные команды для добавления на GitHub:
git add .
git status
git commit -m "Comments"
git push -u origin master
__________________________________________

git clone <url>
git pull - Скачать все новое