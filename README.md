# Flask_login
Использование Flask-Login для обработки пользовательских сеансов в Flask.
Flask-Login, предназначен для обработки пользовательских сеансов, вход в систему и выход из системы.
Совместно с Flask-Login, используется Flask-SQLAlchemy и встраиваемую реляционную бд SQLite.

Документация
https://flask-login.readthedocs.io/en/latest/
http://flask-sqlalchemy.pocoo.org/2.3/quickstart/

Настройка окружения

1. virtualenv --python=/usr/bin/python3.5 venv - создание виртуального окружения
2. source venv/bin/activate - активируем
3. pip --version - проверим текущую версию python 
4. pip install -r requirement.txt - устанавливаем зависимости проекта из файла requirement.txt
4. sudo apt-get install sqlite - установим SQLite
5. sqlite3 login.db - > .tables - > .exit - создаем файл бд login.db

Создание таблиц

1. Запускаем консоль Python
2. from login_example import db - импортируем экземпляр класса SQLAlchemy
2. db.create_all() - исходя из описания класса User с помощью метода create_all() создаем таблицы в бд

Создание записей

1. Запускаем консоль Python
2. from login_example import db, User - импортируем экземпляр класса SQLAlchemy и класс User
3. user_1 = User(username='sungurov') - создаем экземпляр класса User, сохранив в переменной user_1
4. db.session.add(user_1) - для записи ее в бд, включим ее в сессию посредством метода add()
5. db.session.commit() - запишем сессию в бд посредством метода commit()

Поиск записей

result = User.query.all() - бращаемся к классу User, у которого есть объект query и метод all(), который вернет список сохраненный в переменной result
result[0].username - обратимся к первому элементу списка, сохраненного в переменной result







* python 3.5
* Sublime Text 3.1.1
