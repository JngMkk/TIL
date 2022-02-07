# mysql django 연동

> Ubuntu 20.04 LTS 환경

- settings.py

    ```
    APP 추가, DATABASE 변경

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mysql',
            'USER' : 'root',
            'PASSWORD' : 'ubuntu',
            'HOST' : 'localhost',
            'PORT' : '3306'
        }
    }
    ```

- python manage.py makemigarations [project name]

    ```
    /tmp/mysql.sock을 찾을 수 없다는 에러가 발생...
    ```

    ```
    ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock

    임시 방편으로 해결..
    구글링 해보아도 해결 방법을 모르겠다..
    ```

- python manage.py migrate

- django와 연동된 테이블 삭제 방법

    ```
    mysql에서 테이블 삭제 -> django_migrations에서 해당 테이블 row 삭제 -> 다시 적용
    ```

    ![SQL1212](https://user-images.githubusercontent.com/87686562/152828290-9394dac3-7bdb-4920-8304-f6b049b13bf1.png)

    ![SQL123123](https://user-images.githubusercontent.com/87686562/152828309-8bdd4352-706b-4b9f-aa0a-7dd8a8a1fd7f.png)

    ![SQL2121](https://user-images.githubusercontent.com/87686562/152828312-722071cd-ab67-40b7-8f8c-f7d340d0faaa.png)