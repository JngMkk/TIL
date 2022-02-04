# 도커 입문

## Install & Image Pull

- Linux에서 Docker 설치하기

  ```
  $ curl -s https://get.docker.com | sudo sh
  ```

- 설치 후 Docker version 확인

  ```
  $ docker -v
  Docker version 20.10.11, build dea9396
  ```

- 현재 실행중인 모든 컨테이너 목록 출력

  ```
  $ docker ps
  (permission denied)
  (Linux) $ sudo docker ps
  ```
  
- Linux에서 사용자 계정에서 도커를 직접 사용할 수 있게 docker 그룹에 사용자 추가하기

  ```
  $ sudo usermod -aG docker $USER
  $ sudo su - $USER
  ```

---

## Image 기초

```
이미지는 어떤 애플리케이션을 실행하기 위한 환경이라고 할 수 있다.
한 마디로 정의해보자면 이미지는 어떤 애플리케이션을 실행하기 위한 환경이라고 할 수 있다. 이 환경은 파일들의 집합.
도커에서는 애플리케이션을 실행하기 위한 파일들을 모아놓고, 애플리케이션과 함께 이미지로 만들 수 있다. 
그리고 이 이미지를 기반으로 애플리케이션을 바로 배포할 수 있다.
```

- centos 이미지 pull

  ```
  $ docker pull centos
  ```

- image 확인

  ```
  $ docker images
  REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
  centos                   latest    5d0da3dc9764   4 months ago   231MB
  ```

- [Docker에서 제공하는 공식 이미지](https://index.docker.io/search?q=&type=image)

- Ubuntu bionic pull

  ```
  $ docker pull ubuntu:bionic
  bionic: Pulling from library/ubuntu
  2f94e549220a: Pull complete
  Digest: sha256:37b7471c1945a2a12e5a57488ee4e3e216a8369d0b9ee1ec2e41db9c2c1e3d22
  Status: Downloaded newer image for ubuntu:bionic
  docker.io/library/ubuntu:bionic
  
  $ docker run -it ubuntu:bionic bash
  root@0439abcf7779:/#
  ```

---

## Container 이해하기

```diff
이미지는 어떤 환경이 구성되어 있는 상태를 저장해 놓은 파일 집합이다.
바로 이 이미지의 환경 위에서 특정한 프로세스를 격리시켜 실행한 것을 컨테이너라고 부른다.
컨테이너를 실행하려면 반드시 이미지가 있어야 한다.
- 이미지는 파일들의 집합이고, 컨테이너는 이 파일의 집합 위에서 실행된 특별한 프로세스이다.
```

- 컨테이너에서 bash 셸 실행하기

  ```
  $ docker run -it centos:lastest bash
  [root@588ec8830392 /]#
  ```

  ```
  이미지로부터 bash를 실행하라는 의미. 아직 이미지가 없다면, 도커의 공식 저장소에서 이 이미지를 pull 한다.
  그리고 이 이미지를 기반으로 bash 프로세스를 실행, 접속한다.
  접속했다는 말은, SSH를 통해 서버에 접속한 것이 아니라,
  호스트OS와 격리된 환경에서 bash 프로그램을 실행했다고 이해하는 것이 더 정확하다.
  컨테이너란 사실 프로세스에 불과하기 때문에 bash 대신 SSH 서버를 실행하고 SSH 클라이언트를 통해서 접속하는 것도 물론 가능하다.
  ```

- 실행 후 docker ps 확인

  ```
  $ docker ps
  CONTAINER ID   IMAGE           COMMAND   CREATED          STATUS          PORTS     NAMES
  6f2e357b1082   centos:latest   "bash"    13 seconds ago   Up 13 seconds             priceless_swartz
  ```

  ```
  맨 앞의 CONTAINER ID는 앞으로 도커에서 컨테이너를 조작할 때 사용하는 아이디이기 때문에 알아둘 필요가 있다.
  마지막 컬럼은 임의로 붙여진 컨테이너의 이름이다.
  컨테이너를 조작할 때는 컨테이너 아이디를 사용할 수도 있고, 이름을 사용할 수도 있다.
  이름은 docker run을 할 때 --name으로 옵션을 사용해 명시적으로 지정할 수 있다.
  지정하지 않으면 임의의 이름이 자동적으로 부여된다.
  
  위의 예제에서는 직접 명령어를 넘겨서 이미지를 컨테이너로 실행시켰지만, 보통 이미지들은 명령어 기본값이 지정되어 있다.
  컨테이너는 독립된 환경에서 실행되지만, 컨테이너의 기본적인 역할은 이미지 위에서 미리 규정된 명령어를 실행하는 일이다.
  이 명령어가 종료되면 컨테이너도 종료 상태에 들어간다. 죽은 컨테이너의 목록까지 확인하려면 docker ps -a 명령어를 사용한다.
  ```

- 셸 종료 후 docker ps -a (종료된 컨테이너 목록까지 확인)

  ```
  [root@6f2e357b1082 /]# exit
  exit
  
  $ docker ps -a
  CONTAINER ID   IMAGE        COMMAND     CREATED         STATUS                  PORTS     NAMES
  6f2e357b1082 centos:latest  "bash"   4 minutes ago   Exited (0) 33 seconds ago         priceless_swartz
  ```

  ```
  컨테이너는 SSH 서버가 아니라 배시 셸 프로세스이기 때문에, 셸을 종료하면 컨테이너도 종료된다.
  셸은 대화형으로 리눅스 머신에 명령을 실행하기 위한 커맨드라인 도구이다.
  프로세스이기 때문에 섈을 종료하면, 그걸로 끝이다.
  반면에 SSH는 외부에서 접속하기 위해 설치해두는 서버 프로세스이다.
  따라서 SSH 서버에 접속해서 셸을 사용하고 종료하더라도 SSH 서버는 그대로 살아서 다른 접속을 기다린다.
  겉보기에는 비슷하지만 도커로 셸을 직접 실행해서 사용하는 것과
  외부 서버에 SSH로 접속하는 것의 차이를 명확하게 이해해야 도커 컨테이너와 가상머신이 헷갈리지 않을 수 있다.
  ```

- restart 명령어로 이미지 되살리기

  ```
  $ docker restart 6f2e357b1082
  6f2e357b1082
  $ docker ps
  CONTAINER ID   IMAGE           COMMAND   CREATED          STATUS         PORTS     NAMES
  6f2e357b1082   centos:latest   "bash"    13 minutes ago   Up 8 seconds             priceless_swartz
  ```

  ```
  컨테이너가 되살아났다. 하지만 셸과 입출력을 주고받을 수 있는 상태는 아니다.
  컨테이너로 실행된 프로세스와 터미널 상에서 입출력을 주고 받으려면 attach 명령어를 사용해야 한다.
  ```

- attach

  ```
  $ docker attach 6f2e357b1082
  [root@6f2e357b1082 /]#
  ```

  ```diff
  이외에도 강제로 종료시키는 stop 명령어가 있으며, 종료된 컨테이너를 삭제하는 rm 명령어도 있다.
  run 명령어와 함께 사용한 --rm 플래그는 컨테이너가 종료 상태가 되면 자동으로 삭제를 해주는 옵션이다.
  ($ docker run -it --rm centos:latest bash)
  
  이미지가 미리 구성된 환경을 저장해 놓은 파일들의 집합이라면,
  컨테이너는 이러한 이미지를 기반으로 실행된 격리된 프로세스이다.
  이미지는 가상머신 이미지와 비슷하다. 하지만 가상머신에서는 저장된 이미지를 기반으로
  가상머신을 특정 상태로 복원한다. 컨테이너는 가상머신처럼 보이지만 가상머신은 아니다.
  가상머신이 컴퓨터라면, 컨테이너는 단지 격리된 프로세스에 불과하다.
  보통 도커 컨테이너를 처음 다루는 예제에서 셸을 많이 다루기 때문에
  컨테이너가 마치 가상머신처럼 보이는 착각을 일으킨다.
  - 컨테이너는 가상머신이라기보다는 프로세스이다.
  ```


---

## 도커와 버전 관리 시스템

```
도커에서 이미지는 불변한 저장 매체이다.
이미지는 불변이지만, 그 대신 도커에서는 이 이미지 위에 무언가를 더해서 새로운 이미지를 만들어내는 일이 가능하다.
이미지를 기반으로 만들어진 컨테이너는 변경 가능하기 때문이다.
도커의 또 하나 중요한 특징은 바로 계층화된 파일 시스템을 사용한다는 점이다.
특정한 이미지로부터 생성된 컨테이너에 어떤 변경사항을 더하고(파일들을 변경하고),
이 변경된 상태를 새로운 이미지로 만들어내는 것이 가능하다.
도커의 모든 이미지는 기본적으로 이 원리로 만들어진다.
이러한 점 때문에 도커에서는 저장소, 풀, 푸시, 커밋, 차분(diff) 등을 사용 가능하다.
```

- Git?

  ```
  우분투 기본 이미지에는 깃이 설치되어있지 않다.
  root@0439abcf7779:/# git --version
  bash: git: command not found
  ```

  ```
  도커는 마치 VCS(Version Control System)같이 어떤 컨테이너와 컨테이너의 부모 이미지 간 
  파일 변경사항을 확인할 수 있는 명령어를 제공한다. git diff 명령어로 프로젝트의 변경사항을 확인하듯이,
  docker diff 명령어로 부모 이미지와 여기서 파생된 컨테이너 파일 시스템 간의 변경사항을 확인할 수 있다.
  ```

- docker diff 명령어 실행해보기(우분투 셸이 실행된 컨테이너를 그대로 두고, 다른 셸에서 docker diff 명령어 실행)

  ```
  $ docker diff 0439abcf7779
  ```

  ```
  아무것도 출력되지 않았다!!
  왜냐하면 이 컨테이너는 아직 이미지 파일 시스템 상태 그대로이기 때문이다.
  ```

- Git 설치하기

  ```
  root@0439abcf7779:/# apt update
  ...
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  All packages are up to date.
  
  root@0439abcf7779:/# apt install -y git
  ...
  
  root@0439abcf7779:/# git --version
  git version 2.17.1
  ```

  ```
  공식 우분투 이미지는 사용자가 루트로 설정되어 있다.
  따라서 sudo와 같은 명령어 없이도 apt를 직접 사용해 패키지를 설치할 수 있다.
  우분투 패키지 관리자 apt를 사용해 버전 관리 시스템 Git을 설치했다.
  ```

- 다른 셸에서 diff 실행해보기

  ```
  $ docker diff 0439abcf7779 | head
  C /etc
  C /etc/alternatives
  C /etc/alternatives/pager
  A /etc/alternatives/rcp
  A /etc/alternatives/rlogin
  A /etc/alternatives/rsh
  A /etc/ca-certificates
  A /etc/ca-certificates/update.d
  A /etc/ssh
  A /etc/ssh/moduli
  ```
  
  ```
  A는 ADD, C는 Change, D는 Delete를 의미한다.
  ```
  
- ubuntu:bionic 이미지에 Git이 설치된 새로운 이미지 생성

  ```
  $ docker commit 0439abcf7779 ubuntu:git
  sha256:45a07c366cb7e77e67c451809ee99998d5acde7aa805d012976e3a14aef6616d
  
  $ docker images
  REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
  ubuntu                   git       45a07c366cb7   43 seconds ago   196MB
  ubuntu                   bionic    886eca19e611   2 weeks ago      63.1MB
  ```

  ```
  커밋을 하고 뒤에 이름을 붙여주면 바로 새로운 이미지가 생성된다.
  이미지로부터 컨테이너를 실행시키고 이 컨테이너의 수정사항을 통해서 새로운 이미지를 만들었다.
  그렇다면 이 이미지를 통해서 컨테이너를 실행하면 git 명령어가 있을까?
  ```

  ```
  $ docker run -i -t ubuntu:git bash
  root@b9cfce1f3105:/# git --version
  git version 2.17.1
  root@b9cfce1f3105:/# exit
  exit
  ```

  ```
  다시 이미지를 삭제해보자.
  하나 알아두어야 할 것은, 이미지에서 파생된 (종료 상태를 포함한) 컨테이너가 하나라도 남아있다면
  이미지는 삭제할 수 없다. 따라서 먼저 컨테이너를 종료하고, 삭제까지 해주어야 한다.
  docker rm은 컨테이너를 삭제하는 명령어이고, docker rmi는 이미지를 삭제하는 명령어이다.
  먼저 컨테이너를 지우고, 이미지를 삭제해보자.
  ```

  ```
  $ docker ps -a
  CONTAINER ID   IMAGE        COMMAND    CREATED       STATUS                 PORTS       NAMES
  b9cfce1f3105   ubuntu:git    "bash" 3 hours ago   Exited (0) 3 hours ago             hungry_shannon
  0439abcf7779   ubuntu:bionic "bash" 7 hours ago   Up 7 hours                         friendly_spence
  ```

  ```
  $ docker rm b9cfce1f3105
  b9cfce1f3105
  
  $ docker rmi ubuntu:git
  Untagged: ubuntu:git
  Deleted: sha256:45a07c366cb7e77e67c451809ee99998d5acde7aa805d012976e3a14aef6616d
  Deleted: sha256:30841ff1235d266a74b736dcfed85d4cf857bd8b31150dca5f198ca47f55de75
  ```

---

## DockerFile로 이미지 만들기

```
Docker image를 추가하는 방법은 크게 세 가지가 있다.
먼저 pull을 사용해 미리 만들어져 있는 이미지를 가져오는 방법이다.
그리고 컨테이너의 변경사항으로부터 이미지를 만드는 법에 대해서도 소개했다.
두 번째 방법은 아주 흥미롭지만, 이렇게 이미지를 만드는 경우는 거의 없다.
세 번째 방법은 DockerFile을 빌드하는 방법이다. DockerFile은 도커만의 특별한 DSL로 이미지를 정의하는 파일이다.
```

### Dockerfile로 Git이 설치된 우분투 이미지 정의

- DockerFile을 저장해놓기 위한 디렉터리 만들기

  ```
  $ mkdir git-from-dockerfile
  $ cd git-from-dockerfile
  ```

- Git이 설치된 우분투 이미지 정의

  ```
  FROM ubuntu:bionic
  RUN apt-get update
  RUN apt-get install -y git
  ```

  ```
  FROM : 어떤 이미지로부터? (필수 항목)
  RUN : 명령어 실행하라는 의미
  ```

- dockerfile로 이미지 빌드

  ```
  $ docker build -t ubuntu:git-from-dockerfile .
  ...
  ...
  Successfully built eab0dcfa39c9
  Successfully tagged ubuntu:git-from-dockerfile
  ```

- 새로 만든 이미지에 Git이 설치되었는지 확인

  ```
  $ docker run -it ubuntu:git-from-dockerfile bash
  root@aed54ed376aa:/# git --version
  git version 2.17.1
  ```

### 모니위키 도커 파일 작성하기

```
웹 애플리케이션 서버를 실행하기 위한 도커 이미지를 작성해보자.
예제로 사용해 볼 웹 애플리케이션은 PHP와 아파치 서버를 기반으로 동작하는 모니위키이다.
애플리케이션 실행을 위해 도커 이미지를 만드는 작업을 도커라이징이라고도 한다.
```

- 예제 도커파일 저장소 클론 받기

  ```
  $ git clone https://github.com/nacyot/docker-moniwiki.git
  $ cd docker-moniwiki/moniwiki
  ```

- 이 디렉터리에 포함된 Dockerfile 내용 살펴보기

  ```
  $ ls
  Dockerfile  LICENSE  README.md
  
  $ vim Dockerfile
  EXPOSE 80
  CMD bash -c "source /etc/apache2/envvars && /usr/sbin/apache2 -D FOREGROUND"
  ```

  ```
  FROM ubuntu:14.04 
  어떤 이미지로부터 새로운 이미지를 생성할 지 지정
  ```

  ```
  RUN apt-get update &&\
    apt-get -qq -y install git curl build-essential apache2 php5 libapache2-mod-php5 rcs
  ```

  ```
  RUN은 직접 명령어를 실행하는 지시자. RUN 바로 뒤에 명령어 실행
  위의 두 줄은 모니위키 실행을 위한 우분투 패키지들을 설치하는 명령어.
  RUN 명령어를 두 개로 명령어를 하나씩 실행해도 무방
  Dockerfile의 한 줄 한 줄은 레이어라는 형태로 저장되기 때문에 RUN을 줄이면 레이어가 줄어들고,
  캐시도 효율적으로 관리할 수 있다. 여기서 &&은 여러 명령어를 이어서 실행하기 위한 연산자이고,
  \은 명령어를 여러줄에 작성하기 위한 문자이다.
  ```

  ```
  WORKDIR /tmp 
  이후에 실행되는 모든 작업의 실행 디렉터리를 변경. 매번 실행 위치가 초기화되기 때문에
  ```

  ```
  RUN \
    curl -L -O https://github.com/wkpark/moniwiki/archive/v1.2.5p1.tar.gz &&\
    tar xf /tmp/v1.2.5p1.tar.gz &&\
    mv moniwiki-1.2.5p1 /var/www/html/moniwiki &&\
    chown -R www-data:www-data /var/www/html/moniwiki &&\
    chmod 777 /var/www/html/moniwiki/data/ /var/www/html/moniwiki/ &&\
    chmod +x /var/www/html/moniwiki/secure.sh &&\
    /var/www/html/moniwiki/secure.sh
  RUN a2enmod rewrite
  ```

  ```
  모니위키 설치. 여기서는 깃허브 저장소에 릴리스되어 있는 모니위키를 다운로드 받아 아파치2로 동작하도록 셋업한다.
  첫 번째 RUN은 모니위키를 셋업하는 내용이다. 여기서도 RUN 하나에 여러 명령어들을 &&로 연결해주었다.
  PHP 코드의 압축을 풀고, 아파치가 접근하는 디렉터리로 복사하고 접근 권한을 설정한다.
  두 번째 RUN은 아파치2의 모듈을 활성화하는 내용이다.
  ```

  ```
  ENV APACHE_RUN_USER www-data
  ENV APACHE_RUN_GROUP www-data
  ENV APACHE_LOG_DIR /var/log/apache2
  ENV는 컨테이너 실행 환경에 적용되는 환경변수의 기본값을 지정하는 지시자이다.
  ```

  ```
  EXPOSE 80
  CMD bash -c "source /etc/apache2/envvars && /usr/sbin/apache2 -D FOREGROUND"
  ```

  ```
  EXPOSE는 가상머신에 오픈할 포트를 지정해준다.
  마지막 줄의 CMD에는 컨테이너에서 실행될 명령어를 지정해준다.
  이 글의 앞선 예에서는 docker run을 통해서 bash를 실행했지만,
  여기서는 아파치 서버를 FOREGROUND에 실행한다. 이 명령어는 기본값이고 컨테이너 실행 시에 덮어쓸 수 있다.
  ```

- Dockerfile 빌드하기

  ```
  $ docker build -t nacyot/moniwiki:latest .
  Successfully built 6f8bf08497a9
  Successfully tagged nacyou/moniwiki:latest
  ```

- 모니위키 실행

  ```
  $ docker run -d -p 9999:80 nacyot/moniwiki:latest
  9256077a12b69648d549f7f58ecb65f47166af4be9eeb49a5f756b007e7b51cb
  ```

  ```
  -d 플래그는 -i의 반대 역할을 하는 옵션으로, 컨테이너를 백그라운드에서 실행한다.
  -p는 포트포워딩을 지정하는 옵션이다. :을 경계로 앞에는 외부 포트, 뒤에는 컨테이너 내부 포트를 지정한다.
  참고로 컨테이너 안에서 아파치가 80포트로 실행된다.
  따라서 여기서는 9999로 들어오는 연결을 컨테이너에서 실행된 서버의 80포트로 보낸다.
  ```

- 로컬 머신의 9999 포트에 접근해 모니위키 서버가 잘 실행중인지 확인

  ```
  http://127.0.0.1:9999/moniwiki/monisetup.php
  ```

  ![1](https://user-images.githubusercontent.com/87686562/151130473-916764e8-0ae9-4606-900d-5d2b0e010363.PNG)

  
