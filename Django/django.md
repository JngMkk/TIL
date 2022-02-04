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

  

  
