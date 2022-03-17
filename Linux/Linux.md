# Linux

> Ubuntu 20.04 LTS
>
> 실습하면서 배운 명령어 정리 & 궁금한거 구글링

- pwd

  ```
  pwd 명령은 현재 작업 디렉토리를 보여준다.
  루트에서 현재 디렉토리까지의 절대 경로를 제공.
  ```

  ```
  $ pwd
  /home/JngMK
  ```

- nautilus

  ```
  $ nautilus .
  현재 디렉터리 파일탐색기로 열기
  
  $ nautilus ~/TIL
  지정 디렉터리 파일탐색기로 열기
  ```
  
- whoami

  ```
  현재 Linux 터미널에 로그인 한 사용자의 사용자 이름을 표시
  ```

  ```
  $ whoami
  JngMK
  ```

- date

  ```
  현재 시간과 날짜 표시
  ```

  ```
  $ date
  2022. 01. 27. (목) 10:01:54 KST
  ```

- cal

  ```
  달력 표시. 기본적으로 현재 달의 달력을 표시함.
  올해의 달력을 표시하려면 cal-y
  특정 해의 달력을 표시하려면 cal 2023
  특정 해의 특정 월을 표시하려면 cal 3 2023
  이전 달, 이번 달 및 다음 달의 3개월 달력을 표시하려면 cal -3
  ```

  ```
  $ cal
        1월 2022         
  일 월 화 수 목 금 토  
                     1  
   2  3  4  5  6  7  8  
   9 10 11 12 13 14 15  
  16 17 18 19 20 21 22  
  23 24 25 26 27 28 29  
  30 31
  ```

- ls [options] [files]

  ```
  이 명령은 디렉토리 내용을 나열함.
  옵션과 파일을 제공하지 않고 ls 명령을 실행하면 현재 작업 디렉토리 아래에 있는 모든 디렉토리와 파일이 알파벳 순으로 나열됨.
  ```

  ```
  $ ls -l
  합계 144280
  drwxr-xr-x  2 joongmo joongmo     4096  1월 27 10:25 Desktop
  drwxr-xr-x  2 joongmo joongmo     4096  1월 26 23:31 Documents
  drwxr-xr-x  2 joongmo joongmo     4096  1월 27 02:20 Downloads
  drwxr-xr-x  2 joongmo joongmo     4096  1월 26 23:31 Music
  drwxr-xr-x  2 joongmo joongmo     4096  1월 26 23:31 Pictures
  drwxr-xr-x  2 joongmo joongmo     4096  1월 26 23:31 Public
  
  자세한 목록과 함께 컨텐츠가 표시됨. -l은 long을 의미
  ```
  
  ```
  $ ls -lh
  합계 141M
  drwxr-xr-x  2 joongmo joongmo 4.0K  1월 27 10:25 Desktop
  drwxr-xr-x  2 joongmo joongmo 4.0K  1월 26 23:31 Documents
  drwxr-xr-x  2 joongmo joongmo 4.0K  1월 27 02:20 Downloads
  -rw-rw-r--  1 joongmo joongmo 1.4K  1월 27 10:22 Linux.md
  drwxr-xr-x  2 joongmo joongmo 4.0K  1월 26 23:31 Music
  drwxr-xr-x  2 joongmo joongmo 4.0K  1월 26 23:31 Pictures
  drwxr-xr-x  2 joongmo joongmo 4.0K  1월 26 23:31 Public
  
  자세한 목록과 함께 알아보기 쉽게 파일 크기를 표시함. h는 human을 의미
  ```
  
  ```
  $ ls -a
  .conda               Desktop
  .condarc             Documents
  .config              Downloads
  
  숨겨진 파일을 포함하여 표시함. 
  ```
  
  ```
  $ ls /
  bin   cdrom  etc   lib    lib64   lost+found  mnt  proc  run   snap  sys  usr
  boot  dev    home  lib32  libx32  media       opt  root  sbin  srv   tmp  var
  
  /는 루트 디렉토리를 나타내므로 이 명령은 루트 디렉토리에 있는 모든 파일과 폴더를 표시함
  ```

- w

  ```
  현재 로그인 한 사용자에 대한 정보를 표시함.
  ```

  ```
  $ w
   11:17:13 up  2:10,  1 user,  load average: 1.38, 1.47, 1.54
  USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
  joongmo  :1       :1               10:23   ?xdm?   1:34m  0.01s /usr/lib/gdm3/g
  ```

- uname

  ```
  작업 중인 Linux 컴퓨터에 대한 정보를 표시함.
  ```

  ```
  $ uname -a
  Linux jm-ubuntu 5.13.0-27-generic #29~20.04.1-Ubuntu SMP Fri Jan 14 00:32:30 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
  
  Linux 컴퓨터에 대한 모든 정보를 표시함.
  ```

  ```
  $ uname -s
  Linux
  
  커널 유형 표시
  ```

  ```
  $ uname -r
  5.13.0-27-generic
  
  커널 릴리스 정보를 표시
  ```

  ```
  $ uname -v
  #29~20.04.1-Ubuntu SMP Fri Jan 14 00:32:30 UTC 2022
  
  커널 버전 표시
  ```

- top

  ```
  Linux 시스템에 대한 실시간 데이터를 표시함.
  컴퓨터가 실행되는 시간, 평균로드, 실행 중인 작업 수, CPU 정보, 메모리 정보, 프로세스 상태 등의 상태 요약이 표시됨.
  top 명령을 종료하려면 q를 눌러야 함.
  ```

  ```
  $ top
  top - 11:40:19 up  2:33,  1 user,  load average: 1.24, 1.34, 1.44
  Tasks: 414 total,   2 running, 411 sleeping,   0 stopped,   1 zombie
  %Cpu(s): 10.9 us,  3.4 sy,  0.0 ni, 85.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
  MiB Mem :  15926.3 total,   7538.2 free,   4896.6 used,   3491.5 buff/cache
  MiB Swap:   7629.0 total,   7629.0 free,      0.0 used.  10566.4 avail Mem 
  
      PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  
    22092 joongmo   20   0 5314500 433832 124576 S  15.9   2.7  13:25.79 gnome-s+ 
    22071 joongmo    9 -11 2944184  21500  16188 R  14.3   0.1  11:32.72 pulseau+ 
    21944 root      20   0   24.2g  84264  37248 S   8.0   0.5   5:14.13 Xorg     
    26492 joongmo   20   0   87.0g 365528 146184 S   7.0   2.2   3:40.24 Discord  
     1314 root     -51   0       0      0      0 S   4.3   0.0   6:02.23 irq/139+ 
    22499 joongmo   20   0  839320  66528  48088 S   4.0   0.4   0:30.32 gnome-t+ 
      184 root       0 -20       0      0      0 I   0.3   0.0   0:26.16 kworker+
  ```

- tar

  ```
  tar는 테이프 아카이브를 나타냄.
  다른 많은 파일로 구성된 아카이브 파일을 만드는 데 사용되거나 아카이브 파일에서 파일을 추출하는 데 사용.
  ```

  ```
  $ tar -cvf [name].tar [directory name]/
  
  -c : 아카이브 파일을 만드는 데 사용되는 만들기 옵션
  -v : 아카이브 창에 추가된 파일을 터미널 창에 나열하는 옵션
  -f : 아카이브 파일에 원하는 이름을 제공하는 데 사용. 파일 이름은 -f 옵션 바로 뒤에 와야한다.
  위에서는 아카이브 파일이 생성되었지만 압축되지는 않음.
  ```

  ```
  $ tar -cvzf [name].tar.gz [directory name]/
  
  -z : gzip 옵션. tar가 gzip 유틸리티를 사용하여 아카이브 파일을 압축하도록 지시함.
  	 적절한 압축과 합리적인 속도 제공.
  	 아카이브에서 파일을 추출하려고 할 때 압축 유형을 쉽게 알 수 있도록 파일 이름 뒤에 '.gz'를 추가
  ```

  ```
  $ tar -cvjf [name].tar.gz2 [directory name]/
  
  -j : bzip2 옵션. 압축을 위해 우수한 압축 알고리즘을 사용.
  	 더 나은 압축과 느린 속도를 제공.
  	 아카이브에서 파일을 추출하려고 할 때 압축 유형을 쉽게 알 수 있도록 파일 이름 뒤에 '.bz2'를 추가
  ```

  ```
  $ tar -xvf [name].tar
  
  - x : 추출 옵션
  ```

  ```
  $ tar -xvzf [name].tar.gz
  $ tar -xvjf [name].tar.bz2
  
  - 각 압축 유형에 대한 명령어
  ```

- tail

  ```
  파일의 마지막 10줄을 등록하는 데 사용.
  기본적으로 마지막 10줄을 표시하지만 -n 옵션으로 수를 지정할 수 있음
  ```

  ```
  $ tail test.txt
  HTML
  CSS
  JavaScript
  JQuery
  SQL
  Linux
  Docker
  Kubernetes
  AWS
  Ubuntu
  ```

  ```
  $ tail -n test.txt
  Kubernetes
  AWS
  Ubuntu
  ```

- sudo

  ```
  super user do의 줄임말.
  다른 사용자의 암호 변경 등과 같이 root 또는 super user 권한이 필요한 작업을 수행하는 데 사용.
  ```

- ps

  ```
  현재 shell에서 실행중인 프로세스를 보여줌.
  특정 사용자에 대해 실행중인 프로세스를 보려면 -u 옵션을 사용.
  실행중인 모든 프로세스를 표시하려면 -e 옵션 사용
  ```

  ```
  $ ps -u [name]
      PID TTY          TIME CMD
     8043 ?        00:00:00 systemd
     8044 ?        00:00:00 (sd-pam)
     8234 ?        00:00:02 fcitx
     9084 ?        00:00:00 code
  	...
  ```

  ```
  $ ps -e
      PID TTY          TIME CMD
        1 ?        00:00:02 systemd
        2 ?        00:00:00 kthreadd
        3 ?        00:00:00 rcu_gp
        4 ?        00:00:00 rcu_par_gp
        6 ?        00:00:00 kworker/0:0H-events_highpri
        9 ?        00:00:00 mm_percpu_wq
       10 ?        00:00:00 rcu_tasks_rude_
       11 ?        00:00:00 rcu_tasks_trace
       12 ?        00:00:00 ksoftirqd/0
       13 ?        00:00:10 rcu_sched
       ...
  ```

- ping

  ```
  네트워크 문제를 해결하는 데 매우 유용한 명령.
  다른 네트워크 컴퓨터와 네트워크 연결이 있는지 확인할 수 있음.
  대상 컴퓨터를 향해 일정 크기의 패킷을 보낸 후,
  대상 컴퓨터가 이에 대한 응답 메세지를 보내면 이를 수신하여 대상 컴퓨터 동작 여부 혹은 네트워크 상태 파악.
  TCP/IP 프로토콜 중에 ICMP 프로토콜을 통해 동작함.
  ICMP 프로토콜을 지원하지 않는 기기(흔히 IP주소를 갖지 않는 일부 스위치, 허브 등)을 대상으로는 실행할 수 없음.
  ping 명령의 출력을 중지하려면 ctrl+c
  ```

  ```
  $ ping www.google.com
  64 bytes from nrt12s28-in-f4.1e100.net (172.217.174.100): icmp_seq=12 ttl=56 time=32.4 ms
  64 bytes from nrt12s28-in-f4.1e100.net (172.217.174.100): icmp_seq=13 ttl=56 time=32.9 ms
  ^C
  --- www.google.com ping statistics ---
  13 packets transmitted, 13 received, 0% packet loss, time 12013ms
  rtt min/avg/max/mdev = 32.237/33.679/34.913/0.923 ms
  
  Google IP 주소 172.217.174.100이 ping 요청에 응답하고 64 바이트의 패킷을 보내기 시작했음을 알 수 있음
  ttl : Time To Live 패킷이 영원히 네트워크 상에서 돌아다니는 것을 방지하기 위해 만들어 놓은 패킷 생존값
  icmp_seq : 누락된 응답이나 패킷 손실이 없음을 알려줌.
  time : 요청이 컴퓨터에서 Google에 도달한 다음 다시 컴퓨터로 전달되는 데 걸리는 시간.
  ```

  ```
  $ ping -c 3 -D google.com
  PING google.com (142.250.196.110) 56(84) bytes of data.
  [1643264839.301279] 64 bytes from nrt12s35-in-f14.1e100.net (142.250.196.110): icmp_seq=1 ttl=113 time=35.5 ms
  [1643264840.298714] 64 bytes from nrt12s35-in-f14.1e100.net (142.250.196.110): icmp_seq=2 ttl=113 time=37.3 ms
  [1643264841.300028] 64 bytes from nrt12s35-in-f14.1e100.net (142.250.196.110): icmp_seq=3 ttl=113 time=37.3 ms
  
  --- google.com ping statistics ---
  3 packets transmitted, 3 received, 0% packet loss, time 2003ms
  rtt min/avg/max/mdev = 35.522/36.680/37.261/0.819 ms
  
  -c : 전송할 요청 패킷의 횟수를 정하는 옵션
  -D : 타임스탬프([1643264 ...])
  ```

  ```
  $ nslookup google.com
  Server:		127.0.0.53
  Address:	127.0.0.53#53
  
  Non-authoritative answer:
  Name:	google.com
  Address: 216.58.197.206
  Name:	google.com
  Address: 2404:6800:4004:801::200e
  ```

  ```
  $ dig google.com
  ; <<>> DiG 9.16.1-Ubuntu <<>> google.com
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11406
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
  
  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 65494
  ;; QUESTION SECTION:
  ;google.com.			IN	A
  
  ;; ANSWER SECTION:
  google.com.		59	IN	A	142.251.42.206
  
  ;; Query time: 3 msec
  ;; SERVER: 127.0.0.53#53(127.0.0.53)
  ;; WHEN: 목  1월 27 15:20:52 KST 2022
  ;; MSG SIZE  rcvd: 55
  ```

  ```
  $ host google.com
  google.com has address 142.251.42.174
  google.com has IPv6 address 2404:6800:4004:81d::200e
  google.com mail is handled by 20 alt1.aspmx.l.google.com.
  google.com mail is handled by 50 alt4.aspmx.l.google.com.
  google.com mail is handled by 40 alt3.aspmx.l.google.com.
  google.com mail is handled by 30 alt2.aspmx.l.google.com.
  google.com mail is handled by 10 aspmx.l.google.com.
  ```

- passwd

  ```
  암호 변경 명령어.
  직접 변경하는 경우 passwd 명령만 입력하면 됨.
  다른 사용자 암호 변경인 경우 sudo passwd
  ```

- mv

  ```
  이동 명령어.
  이 명령을 사용하면 한 디렉터리에서 다른 디렉터리로 파일과 폴더를 이동할 수 있음.
  이 명령을 사용하여 파일의 이름을 바꿀 수도 있음
  
  $ mv [filename] [target directory]
  file을 target directory로 이동
  
  $ mv [filename] [new_filename]
  change name
  
  $ mv [filename] [target directory]/[new_filename]
  move & change name
  ```

- mkdir

  ```
  make directory
  mkdir [option] [directory]
  ```

  ```
  $ mkdir -v testDir
  mkdir: 'testDir' 디렉터리를 생성함
  
  -v : 생성된 디렉터리에 대한 메시지 표시
  ```

  ```
  $ mkdir -vp test/test1
  mkdir: 'test' 디렉터리를 생성함
  mkdir: 'test/test1' 디렉터리를 생성함
  
  -p : 새로 생성된 디렉터리에 대해 부모 디렉터리가 없는 경우 부모 디렉터리를 생성하는 데 사용
  ```

  ```
  $ mkdir -m a=rwx [directory]
  -m : 디렉터리에 대한 권한을 설정하는 데 사용
  
  $ mkdir -vm a=r test2
  mkdir: 'test2' 디렉터리를 생성함
  
  a=r : 디렉터리에 대해 읽기 권한만 부여함
  
  $ ls -l
  dr--r--r--  2 joongmo joongmo     4096  1월 27 15:57 test2
  
  dr--r--r-- : 읽기 권한만 가짐.
  ```

- alias

  ```
  명령 또는 명령 조합에 이름을 지정하는 데 사용됨.
  시스템 재부팅 후 초기화됨.
  홈디렉터리에 있는 .bashrc 또는 .bash_aliases 파일에 직접 등록해서 바꾸는 방법도 있음
  alias만 입력하면 등록된 별칭을 모두 보여줌
  
  alias [-p] [name[=value]...]
  ex) $ alias mv=move
  
  unalias [alias name]
  별칭 삭제
  ```

- cat

  ```
  concatenate.
  파일에서 데이터를 읽고 그 내용을 터미널 창에 출력.
  
  cat [file1] [file2] ...
  입력받은 파일들의 내용을 연결하고 출력
  
  cat -n [file name]
  줄 번호와 함께 파일 내용 출력
  
  cat > [newfilename]
  새 파일을 만드는 데 사용
  내용 입력 후 ctrl+d로 저장
  
  cat [source_file]>[destination_file]
  한 파일의 내용을 다른 파일로 복사하는 데 사용.
  대상 파일의 내용을 원본 파일의 내용으로 바꿈
  
  cat >> [file]
  내용 입력 후 ctrl+d로 저장
  > 기호는 기존에 있는 파일 내용을 지우고 저장
  >> 기호는 사용하던 기존 파일 내용 뒤에 연속해서 기록
  
  cat [file1]>>[file2]
  file1의 내용을 file2의 내용 끝에 추가
  
  tac [file name]
  파일의 내용을 역순으로 출력
  
  cat -E [file name]
  줄 끝을 강조 표시하는 데 사용
  ```

- chmod

  ```
  chmod [option] [mode] [file]
  파일 또는 디렉터리에 대한 권한을 설정하는 데 사용.
  파일이나 디렉터리에서 ls -l을 수행하면 출력이 -rwxrwxrwx와 같은 문자가 표시됨.
  r은 읽기(read), w는 쓰기(write), x는 실행(execute)을 의미.
  rwx대신 -가 표시되면 파일 권한이 부여되지 않았음을 의미.
  
  [option]
  -v : 모든 파일에 대해 모드가 적용되는 진단(diagnostic) 메시지 출력
  -f : 에러 메시지를 출력하지 않음
  -c : 기존 파일 모드가 변경되는 경우만 진단(diagnostic) 메시지 출력
  -R : 지정한 모드를 파일과 디렉토리에 대해 재귀적으로 적용
  
  [mode]
  u, g, o, a : 소유자(u), 그룹(g), 그 외 사용자(o), 모든 사용자(a) 지정
  +, -, = : 현재 모드에 권한 추가(+), 현재 모드에서 권한 제거(-), 현재 모드로 권한 지정(=)
  r, w, x : r은 읽기(read), w는 쓰기(write), x는 실행(execute)을 의미
  X : 디렉터리 또는 실행 권한이 있는 파일에 실행 권한 적용
  s : 실행 시 사용자 또는 그룹 ID 지정
  t : 공유모드에서의 제한된 삭제 플래그를 나타내는 sticky(t) bit
  0 : 비허가
  1 : 실행
  2 : 쓰기
  3 : 작성 및 실행
  4 : 읽기
  5 : 읽고 실행
  6 : 읽고 쓰기
  7 : 읽기, 쓰기 및 실행
  나 자신에 대한 권한 - 그룹에 대한 권한 - 다른 사용자에 대한 권한
  ```

  ```
  $ ls -l test.txt
  -rw-rw-r-- 1 joongmo joongmo 139  1월 27 13:56 test.txt
  
  $ chmod -R 745 test.txt
  $ ls -l test.txt
  -rwxr--r-x 1 joongmo joongmo 139  1월 27 13:56 test.txt
  
  rwx : user read, write, execute
  r-- : group read
  r-x : other read, execute
  ```

- chown

  ```
  chown [option] [owner][:[group]] file/directory ...
  파일이나 디렉터리의 소유자를 변경하는 명령어
  
  chown [user name] file/directory
  
  sudo chown [owner name]:[group name] file/directory
  그룹 소유자를 변경하려면 sudo 명령과 함께 사용
  
  -R, --recursive : 하위 디렉터리까지 변경할 경우
  -h, --no-dereference : symbolic link도 변경
  ```

- df(disk free)

  ```
  컴퓨터의 파일 시스템에 대한 크기, 사용된 공간, 사용 가능한 공간, 사용 비율 및 마운트된 세부 사항을 표시함.
  -h : 사람이 읽을 수 있는 형식 (GB 및 MB)로 크기를 표시함.
  -x : 관심이 없는 파일 시스템을 제외하는 데 사용
  
  파일시스템, 디스크 크기, 사용량, 여유공간, 사용률, 마운트지점 순으로 나타남
  ```

  ```
  $ df
  Filesystem     1K-blocks     Used Available Use% Mounted on
  udev             8120836        0   8120836   0% /dev
  tmpfs            1630852     2300   1628552   1% /run
  /dev/sda3      223920820 24919916 187556680  12% /
  tmpfs            8154248    86200   8068048   2% /dev/shm
  tmpfs               5120        4      5116   1% /run/lock
  tmpfs            8154248        0   8154248   0% /sys/fs/cgroup
  /dev/loop0        113152   113152         0 100% /snap/core/12603
  /dev/loop1         56832    56832         0 100% /snap/core18/2128
  ...
  ```

  ```
  $ df -h
  Filesystem      Size  Used Avail Use% Mounted on
  udev            7.8G     0  7.8G   0% /dev
  tmpfs           1.6G  2.3M  1.6G   1% /run
  /dev/sda3       214G   24G  179G  12% /
  tmpfs           7.8G   80M  7.7G   1% /dev/shm
  tmpfs           5.0M  4.0K  5.0M   1% /run/lock
  tmpfs           7.8G     0  7.8G   0% /sys/fs/cgroup
  /dev/loop0      111M  111M     0 100% /snap/core/12603
  /dev/loop1       56M   56M     0 100% /snap/core18/2128
  /dev/loop2       66M   66M     0 100% /snap/gtk-common-themes/1519
  ```

- du(disk usage)

  ```
  특정 디렉터리를 기준으로 디스크 사용량 확인
  
  -h : 사람이 읽을 수 있는 형식 (GB 및 MB)로 크기 표시
  -s : 요약된 정보 출력(서브 디렉터리 출력 x)
  ```

  ```
  $ du -sh /home
  8.4G	/home
  ```

- diff / cmp / diff3 / comm

  ```
  cmp(compare) : 비교해서 단순한 결과를 보여줌
  			   파일들의 다른 내용을 비교하여 결과를 알려줌.
  			   cmp는 단순히 내용이 서로 다른지 확인하는 용도이며 어떻게 다른지는 확인할 수 없음
  
  diff(diffrences) : 두 파일 사이의 내용을 비교하는 명령어. cmp보다 직관적이고 명확하게 결과를 알려줌.
  				   -u : unified context
    -i, --ignore-case               ignore case differences in file contents
    -b, --ignore-space-change       ignore changes in the amount of white space
    -w, --ignore-all-space          ignore all white space
    -E, --ignore-tab-expansion      ignore changes due to tab expansion
    -B, --ignore-blank-lines        ignore changes where lines are all blank  
    -Z, --ignore-trailing-space     ignore white space at line end
    대소문자 차이, 탭문자 차이, 공백의 차이 등은 제외(무시)하도록 함.
    
    
  diff3 : 세 파일 사이의 차이점 비교할 수 있음
  
  comm : 두 파일에서 공통적인 부분과 한쪽에만 있는 부분을 찾아낼 수 있음
  	   -1 - 두 파닝릉 비교하여 첫번째 파일과 다른 두번째 파일의 내용과 공통 부분
  	   -2 - 두번째 파일과 다른 부분의 첫번째 파일내용과 공통 부분
  	   -3 - 두 파일의 공통된 부분 제외한 나머지 차이 부분
  ```

- find

  ```
  파일 시스템에서 파일 및 디렉터리를 검색하는 데 사용.
  파일 이름, 디렉터리 이름, 작성 날짜, 수정 날짜, 파일 소유자, 파일 권한 등을 제공하여 찾을 수 있음.
  검색 표현식에 와일드카드를 사용할 수도 있음.
  
  find [검색 시작지점] [검색 표현식] [option] [찾을 내용]
  ```

  ```
  $ find . -name "*file*"
  4.0K	./anaconda3/mkspecs/solaris-cc-stlport
  4.0K	./anaconda3/mkspecs/common/qnx
  4.0K	./anaconda3/mkspecs/common/bsd
  4.0K	./anaconda3/mkspecs/common/winrt_winphone/manifests/10.0
  8.0K	./anaconda3/mkspecs/common/winrt_winphone/manifests
  4.0K	./anaconda3/mkspecs/common/winrt_winphone/assets
  16K	./anaconda3/mkspecs/common/winrt_winphone
  ...
  
  파일 이름에 문자열 'file'을 포함하는 현재 디렉터리(.)에서 모든 파일을 검색
  
  $ find . -type f -name "*.py"
  ./anaconda3/lib/python3.9/site-packages/networkx/algorithms/chordal.py
  ./anaconda3/lib/python3.9/site-packages/networkx/algorithms/tournament.py
  ./anaconda3/lib/python3.9/site-packages/networkx/algorithms/clique.py
  ./anaconda3/lib/python3.9/site-packages/networkx/algorithms/asteroidal.py
  ...
  
  $ find . -type d -name "*go"
  ./.local/kitty.app/lib/kitty/logo
  ./anaconda3/pkgs/sphinx-4.2.0-pyhd3eb1b0_1/site-packages/sphinx/themes/agogo
  ...
  ```

- history

  ```
  이전에 명령 줄에서 실행한 명령을 표시 ex) history 3 : 마지막으로 실행한 3개의 명령
  !EventNumber : 특정 명령 실행
  ```

- gzip

  ```
  파일 압축하는 데 사용됨.
  
  gzip [option] filename
    -c, --stdout      write on standard output, keep original files unchanged
    -d, --decompress  decompress
    -f, --force       force overwrite of output file and compress links
    -h, --help        give this help
    -k, --keep        keep (don't delete) input files
    -l, --list        list compressed file contents
    -L, --license     display software license
    -n, --no-name     do not save or restore the original name and timestamp
    -N, --name        save or restore the original name and timestamp
    -q, --quiet       suppress all warnings
    -r, --recursive   operate recursively on directories
        --rsyncable   make rsync-friendly archive
    -S, --suffix=SUF  use suffix SUF on compressed files
        --synchronous synchronous output (safer if system crashes, but slower)
    -t, --test        test compressed file integrity
    -v, --verbose     verbose mode
    -V, --version     display version number
    -1, --fast        compress faster
    -9, --best        compress better
  ```
  
- cd -

  ```
  전에 작업한 디렉터리를 불러옴.
  
  $ cd -
  /home/jngmk/TIL/Linux
  
  $ cd -
  /home/jngmk
  ```

- which

  ```
  내가 지금 실행하고자 하는 프로그램이 어디에 설치되어 있는지 어디에 설정되어 있는지 경로 확인
  
  $ which code
  /usr/bin/code
  
  $ which typora
  /usr/bin/typora
  ```

- echo

  ```
  > : 덮어 씌움
  >> : append
  
  $ echo "Hello, world!" > test.txt
  
  $ cat test.txt
  Hello, world!
  
  $ echo "Bye, world!" >> test.txt
  $ cat test.txt
  Hello, world!
  Bye, world!
  ```

- cp

  ```
  copy.
  
  cp [option] [file...] [directory]
  
  -p : 시간, 권한 변함 없이 원본 그대로 복사
  -r : 디렉터리 복사
  ```

- grep

  ```
  Global regular expression print
  
  grep [option] pattern [file...]
  
  -n : 검색 결과 출력 라인 앞에 라인 번호 출력.
  -i : 대소문자 구분 x
  -r : recursive
  -H : 검색 결과 출력 라인 앞에 파일 이름 표시.
  ```

  ```
  $ grep "world" *.txt
  Hello, world!
  Bye, world!
  
  $ grep -n "world" *.txt
  1:Hello, world!
  2:Bye, world!
  
  $ grep -ni "world" *.txt
  1:Hello, world!
  2:Bye, world!
  3:seeya, World!
  
  $ grep -nir "world" .
  ./test.txt:1:Hello, world!
  ./test.txt:2:Bye, world!
  ./test.txt:3:seeya, World!
  ./dir1/test2.txt:1:Hello World
  ```

- 환경 변수 설정 (export/env/unset)

  ```
  $ export MY_DIR="TIL"
  
  설정된 모든 환경변수 보기 : env
  
  $ env
  SHELL=/bin/bash
  MY_DIR=TIL
  ...
  PATH=/home/jngmk/anaconda3/bin:/home/jngmk/anaconda3/condabin:/home/jngmk/anaconda3/condabin:/home/jngmk/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/spark/bin:/opt/spark/sbin
  ...
  
  $ cd $MY_DIR
  jngmk@ubuntu:~/TIL$ 
  
  $PATH로 내가 지정한 디렉터리로 이동할 수 있음
  
  $ unset MY_DIR
  지정된 환경변수 삭제
  ```

- ssh

  ```
  ssh -p {port} user@ipaddress

  $ ssh -p 60010 root@127.0.0.1
  root@127.0.0.1's password: 
  [root@m-k8s ~]# 
  ```

- /bin

  ```
  bin은 binary(기계어)라는 뜻으로 보통 실행 파일을 의미함.
  ls, cp, mv 등의 기본적인 콘솔 명령어가 이 곳에 위치함.
  
  멀티 사용자 운영체제에서 단일 사용자 모드로 실행할 수 있는 필수 명령어들이 집합되어 있음.
  관리자를 포함한 모든 사용자를 위한 공통 명령어가 저장.
  이 폴더에 있는 명령어는 다른 파일 시스템이 마운트되지 않아도 사용 가능
  ```

- /sbin

  ```
  system binaries
  /bin 폴더와 같지만 루트 권한이 있어야만 실행할 수 있는 명령어가 저장되어 있음.
  잘못 조작할 경우 전체 시스템에 이상을 초래할 수 있음
  ```

- /usr/bin

  ```
  단일 사용자 모드에 필요한 명령어를 제외한 명령어들이 저장되어 있음.
  /usr 디렉터리가 마운트 되어야만 사용할 수 있고, 모든 사용자가 공통으로 사용할 수 있는 명령어가 저장되어 있음.
  일반적인 유틸리티, 프로그래밍 툴과 함께 대부분의 사용자 명령어.
  ```

- /usr/sbin

  ```
  /usr/bin 폴더와 같지만 루트 권한이 있어야만 실행할 수 있는 명령어가 저장되어 있음.
  ```

- /usr/local/bin

  ```
  직접 작성한 스크립트 파일 또는 프로그램이나, package manager에 의해 관리되지 않는 소프트웨어들이 저장됨.
  ```

- /usr/local/sbin

  ```
  루트 권한이 있어야만 실행할 수 있는 명령어가 저장되어 있음.
  ```

- /dev

  ```
  device의 약자로 컴퓨터에 연결된 모든 장치가 파일로 표현되어 있음.
  키보드, 마우스, 프린터 등과 같은 디바이스들을 파일 또는 디렉터리의 형태로
  dev 폴더 안에 존재하므로 표준 입출력을 통해 읽기, 쓰기도 가능하며 디렉터리 어디에서든 접근할 수 있음.
  ```

- /etc

  ```
  etc 디렉터리에는 대부분의 설정 파일들이 저장됨.
  시스템 전체에서 사용하는 설정과 같은 데이터들이 저장되는 폴더
  ```

- /lib, /lib32, /lib64

  ```
  커널 모듈, 시스템에 필요한 라이브러리 등이 위치
  ```

- /proc

  ```
  실제 디스크 공간에는 존재하지 않는 가상의 디렉터리. 리눅스의 가상 파일 시스템
  현재 cpu 사용값, IO포트 등 프로세스에 대한 다양한 정보가 들어있음.
  ```

- /media , /mnt

  ```
  파일시스템이 마운팅 되는 포인트.
  media는 OS에서 자동으로 마운팅해주는 포인트로 주로 사용되며
  mnt는 사용자가 직접 마운트하는 경로로 사용됨.
  ```

- /srv

  ```
  srv 디렉터리는 서버를 위한 폴더.
  주로 FTP, SFTP, RSync와 같은 프로토콜을 이용하여 외부 사용자와의 공유를 위해 사용되며
  다른 디렉터리에 비해 비교적 외부 사용자들이 쉽게 접근할 수 있음.
  ```

- /sys

  ```
  리눅스 시스템이 필요로 하는 파일들이 있는 디렉터리.
  ```

- /lost+found

  ```
  파일 시스템을 체크하는 경우 잃어버린 파일..?을 찾아서 이곳에 위치시킴
  ```

- /opt

  ```
  상용 프로그램이 위치하는 장소
  크롬브라우저 같은 써드파티 어플리케이션에 대한 설치 디렉터리로 사용됨
  ```

- /tmp

  ```
  임시 저장 파일을 담고 있음.
  ```

- /usr

  ```
  /usr 계층은 파일시스템의 주요 섹션 중 하나.
  이 계층에는 시스템이 아닌 사용자가 실행할 프로그램들이 저장되며, 해당 계층에는 반드시 read-only 데이터만 존재해야 함.
  FHS(파일시스템 계층 구조) 간에 데이터의 공유가 가능한 데이터들이 포함되는데,
  특정 호소트에 따라 달라지거나 시간에 따라 달라지는 정보들은 다른 계층에 저장됨.
  또한 규모가 큰 소프트웨어 패키지들이 /usr 계층의 하위 디렉터리들을 직접적으로 사용해선 안됨.
  /usr 계층 하위의 디렉터리들은 다음과 같은 디렉터리와 심볼릭 링크들이 필요함.
  ```

  - /usr/bin

  - /usr/include

    ```
    c 컴파일러에 대한 헤더 파일들이 위치.
    ```

  - /usr/lib

    ```
    라이브러리들이 위치.
    ```

  - /usr/local

    ```
    기본 os에서는 필요하지 않는 실행 가능한 파일들, 라이브러리들이 위치함.
    ```

  - /usr/sbin

  - /usr/share

    ```
    아키텍처에서 독립된 데이터 파일들이 위치함. (vim, zsh 등)
    ```

  - /usr/src

    ```
    이 디렉터리는 컴파일 되지 않은 다양한 프로그램 소스들이 들어 있음.
    이 곳에서 비디오 드라이버 모듈을 만들기도 하고 RPM을 만들어 내기도 함.
    리눅스 커널 소스도 이 곳에 위치함.
    ```

- /var

  ```
  시스템 운영 도중에 파일 크기가 변하는 요소들을 담고 있는 디렉터리.
  그 외에 시스템 유지에 필요한 중요한 파일들이 이 곳에 위치.
  ```

  
