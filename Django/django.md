# django

## 가상환경 만들기

```
$ conda create -n {name} python={version}
$ conda activate {name}
```

## Django 기초

```
$ pip install django
```

- project 만들기

  ```
  $ django-admin startproject {project name}
  ```

  ![image](https://user-images.githubusercontent.com/87686562/152450714-556266ed-0bcb-4768-8e42-6cd3003bc98e.png)

- server 요청(프로젝트 디렉터리 경로에서)

  ```
  $ python manage.py runserver
  ```

- project 안에 app 만들기

  ```
  $ python manage.py startapp {app name}
  ```

- app이 많아지면 project directory의 urls.py가 무거워지므로 각 app directory에 urls.py 만들어줌

- Server Side Rendering (SSR)

  ```
  요청이 들어오면 서버에서 그 요청에 맞는 '처리'를 한 후 document를 응답
  ```

- Client Side Rendering (CSR)

  ```
  요청이 들어오면 요청에 맞는 data를 바로 받아서 응답(Restful)
  ```

- Templates directory 만들 때

  ```
  settings.py 에서 TEMPLATES 경로 변경
  ```

  ![image](https://user-images.githubusercontent.com/87686562/152470094-3fb9baed-5129-4e60-bca2-d8cbf4969f43.png)

- 작동 방식

  ![image](https://user-images.githubusercontent.com/87686562/152470177-35e896d4-bd44-4ef6-86b7-84e6ad14bdef.png)

  ```
  app 만들 때마다 views.py, urls.py, templates, 루트의 urls.py 작업.
  ```

- WAS (Web Application Server) 동작

- render 함수

  ```python
  from django.shortcuts import render
  
  def index(request):
      return render(request, "경로")
  
  # render(request, "경로", [전달값])
  ```

- loop (templates engine이 처리)

  ```html
  {% for i in number %}
  <p>{{i}}</p>
  {% endfor %}
  ```

- {% url 'Hello' %}

  ```
  name이 Hello인 것을 찾아라.
  ```

- POST 방식일 때 {% csrf_token %}

  ```html
  <form action=... method="post">{% csrf_token %}
      ...
  </form>
  ```

  ```
  csrf : cross-site request forgery
  ```

- static app

  ```
  settings.py에서 STATICFILES_DIRS 경로 지정
  ```

  ![image](https://user-images.githubusercontent.com/87686562/152479189-d8fc07fb-e4de-4126-aab9-cf2ac96f6744.png)

- static 사용할 때 templatesyntax error 시 {% load static %}

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html>
      ...
      <link rel="stylesheet" href="{% static '...' %}">
      <script src="{% static '...' %}"></script>
  </html>
  ```

- db 사용할 때

  ```
  $ python manage.py migrate
  $ sqlite3 db.sqlite3
  ```

- .table : 현재 가지고 있는 table

- .exit : 나가기

- project 안에 models.py 만들기

  ```python
  from django.db import models
  
  class classname(models.Model):
      ...
  ```

- settings.py install_app에 project 추가

  ![image](https://user-images.githubusercontent.com/87686562/152486318-6c012e06-0524-4642-870a-cf232101be4b.png)

- 모델 만들기

  ```
  $ python manage.py makemigrations dbtest
  Migrations for 'dbtest':
    dbtest/migrations/0001_initial.py
      - Create model MyBoard
  ```

  ![image-20220204160838416](/home/jngmk/.config/Typora/typora-user-images/image-20220204160838416.png)

  ```
  PK 지정해주지 않으면 알아서 'id'라는 PK 만듦
  ```

- 확인

  ```
  $ python manage.py sqlmigrate dbtest 0001
  BEGIN;
  --
  -- Create model MyBoard
  --
  CREATE TABLE "dbtest_myboard" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "myname" varchar(100) NOT NULL, "mytitle" varchar(500) NOT NULL, "mycontent" varchar(2000) NOT NULL, "mydate" datetime NOT NULL);
  COMMIT;
  ```

- Apply

  ```
  $ python manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, dbtest, sessions
  Running migrations:
    Applying dbtest.0001_initial... OK
  ```

- python으로 data 삽입하기

  ```
  $ python manage.py shell
  Python 3.9.7 (default, Sep 16 2021, 13:09:58) 
  [GCC 7.5.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>> from dbtest.models import MyBoard
  >>> from django.utils import timezone
  >>> test = MyBoard(myname='testuser', mytitle='test title', mycontent='test 1234', mydate=timezone.now())
  >>> type(test)
  <class 'dbtest.models.MyBoard'>
  >>> test.save()
  >>> MyBoard.objects
  <django.db.models.manager.Manager object at 0x7f75d7e08a90>
  >>> MyBoard.objects.all()
  <QuerySet [<MyBoard: MyBoard object (1)>]>
  >>> exit()
  ```

- views.py 만들기

  ```python
  from django.shortcuts import render
  from .models import MyBoard
  
  def index(request):
      return render(request, 'index.html', {'list': MyBoard.objects.all()})
  ```

- app 안에 templates directory 만들었을 때

  ```
  project directory settings.py ->
  TEMPLATES = APP_DIRS : True 면 자동으로 templates 실행.
  ```

  

  
