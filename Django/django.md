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

- app이 많아지면 project의 urls.py가 무거워지므로 각 app 디렉터리에 urls.py 만들어줌

- path 설정시 path함수 뒤에 , 필수
