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
    $ ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock
    
    임시 방편으로 해결..
    구글링 해보아도 해결 방법을 모르겠다..
    rc.local에 명령 추가하여 부팅 시 자동으로 명령 입력하게 하려고 한다.
    
    $ sudo vi /etc/rc.local
    없다..!?
    
    일단.. 입력
    #!/bin/bash
    ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock
    exit 0
    
    $ sudo chmod +x /etc/rc.local
    ```

- [참고 URL](https://linuxhint.com/use-rc-local-on-ubuntu/)

    ```
    Now we have to verify the status of the rc.local file.
    To verify the status,run the below-displayed command on the terminal window of your Ubuntu 20.04 system
    
    $ sudo systemctl status rc-local
    ● rc-local.service - /etc/rc.local Compatibility
         Loaded: loaded (/lib/systemd/system/rc-local.se>
        Drop-In: /usr/lib/systemd/system/rc-local.servic>
                 └─debian.conf
         Active: inactive (dead)
           Docs: man:systemd-rc-local-generator(8)
    lines 1-6/6 (END)
    
    inactive인 것을 확인.
    
    if you want to enable /etc/rc.local, you have to execute the flowing listed command
    
    $ sudo systemctl enable rc-local
    The unit files have no installation config (WantedBy=, RequiredBy=, Also=,
    Alias= settings in the [Install] section, and DefaultInstance= for template
    units). This means they are not meant to be enabled using systemctl.
     
    Possible reasons for having this kind of units are:
    • A unit may be statically enabled by being symlinked from another unit's
      .wants/ or .requires/ directory.
    • A unit's purpose may be to act as a helper for some other unit which has
      a requirement dependency on it.
    • A unit may be started when needed via activation (socket, path, timer,
      D-Bus, udev, scripted systemctl call, ...).
    • In case of template units, the unit is meant to be enabled with some
      instance name specified.
      
    뭐.. 안된다는 뜻 같다. there is no [Install] part in the unit file.
    First, we must create a file by running the command below.
    
    $ sudo vi /lib/systemd/system/rc-local.service
    제일 아래에 추가
    [Install]
    WantedBy=multi-user.target
    
    $ sudo systemctl enable rc-local
    Created symlink /etc/systemd/system/multi-user.target.wants/rc-local.service → /lib/systemd/system/rc-local.service.
    
    $ sudo systemctl start rc-local.service
    
    $ sudo systemctl status rc-local.service
    ● rc-local.service - /etc/rc.local Compatibility
         Loaded: loaded (/lib/systemd/system/rc-local.service; enabled; vendor preset: enabled)
        Drop-In: /usr/lib/systemd/system/rc-local.service.d
                 └─debian.conf
         Active: active (exited) since Tue 2022-02-08 10:15:58 KST; 6s ago
           Docs: man:systemd-rc-local-generator(8)
        Process: 34906 ExecStart=/etc/rc.local start (code=exited, status=0/SUCCESS)
    
    Active 된 것을 확인.
    ```

- python manage.py migrate

- django와 연동된 테이블 삭제 방법

    ```
    mysql에서 테이블 삭제 -> django_migrations에서 해당 테이블 row 삭제 -> 다시 적용
    ```

    ![SQL1212](https://user-images.githubusercontent.com/87686562/152828290-9394dac3-7bdb-4920-8304-f6b049b13bf1.png)

    ![SQL123123](https://user-images.githubusercontent.com/87686562/152828309-8bdd4352-706b-4b9f-aa0a-7dd8a8a1fd7f.png)

    ![SQL2121](https://user-images.githubusercontent.com/87686562/152828312-722071cd-ab67-40b7-8f8c-f7d340d0faaa.png)