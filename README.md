### api_final
Социальная сеть YATUBE, в которой можно публиковать собственные посты, подписываться и просматривать посты других авторов, оставлять комментарии. Для создания проекта были использованы следующие технологии: 
```
Python 3.9.13    Django    Django Rest Framework    SimpleJWT    SQLite
```

Автор проекта:
```
[Enigmatica33](https://github.com/Enigmatica33)
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Enigmatica33/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

Получить список постов (GET):
```
http://127.0.0.1:8000/api/v1/posts/
```
Получить определенный пост (GET):
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Создать новый пост (POST):
```
http://127.0.0.1:8000/api/v1/posts/
```
Добавить комментарий к посту (POST):
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Получить список комментариев к посту (GET):
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```