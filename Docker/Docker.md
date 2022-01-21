# 도커

## Install & Image Pull

- Linux에서 Docker 설치하기

  ```
  $ curl -s https://get.docker.com | sudo sh
  ```
<br>
- 설치 후 Docker version 확인

  ```
  $ docker -v
  Docker version 20.10.11, build dea9396
  ```
<br>
- 현재 실행중인 모든 컨테이너 목록 출력

  ```
  $ docker ps
  (permission denied 시)
  (Window) Powershell 관리자 권한으로 실행
  (Linux) $ sudo docker ps
  ```
<br>
- Linux에서 사용자 계정에서 도커를 직접 사용할 수 있게 docker 그룹에 사용자 추가하기

  ```
  $ sudo usermod -aG docker $USER
  $ sudo su - $USER
  ```
<br>
## Image 기초

```
이미지는 어떤 애플리케이션을 실행하기 위한 환경이라고 할 수 있다.
한 마디로 정의해보자면 이미지는 어떤 애플리케이션을 실행하기 위한 환경이라고 할 수 있다. 이 환경은 파일들의 집합.
도커에서는 애플리케이션을 실행하기 위한 파일들을 모아놓고, 애플리케이션과 함께 이미지로 만들 수 있다. 
그리고 이 이미지를 기반으로 애플리케이션을 바로 배포할 수 있다.
```
<br>
- centos 이미지 pull

  ```
  $ docker pull centos
  ```
<br>
- image 확인

  ```
  $ docker images
  REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
  centos                   latest    5d0da3dc9764   4 months ago   231MB
  ```
<br>
- [Docker에서 제공하는 공식 이미지](https://index.docker.io/search?q=&type=image)
<br>
## Container 이해하기

```diff
이미지는 어떤 환경이 구성되어 있는 상태를 저장해 놓은 파일 집합이다.
바로 이 이미지의 환경 위에서 특정한 프로세스를 격리시켜 실행한 것을 컨테이너라고 부른다.
컨테이너를 실행하려면 반드시 이미지가 있어야 한다.
- 이미지는 파일들의 집합이고, 컨테이너는 이 파일의 집합 위에서 실행된 특별한 프로세스이다.
```
<br>
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
<br>
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
<br>
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
<br>
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
<br>
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

  
