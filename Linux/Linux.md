# Linux

## 기본 Linux 명령

>Ubuntu 21.04 LTS

- pwd

  ```
  pwd 명령은 현재 작업 디렉토리를 보여준다.
  루트에서 현재 디렉토리까지의 절대 경로를 제공.
  ```

  ```
  $ pwd
  /home/JngMK
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
  cal
        1월 2022         
  일 월 화 수 목 금 토  
                     1  
   2  3  4  5  6  7  8  
   9 10 11 12 13 14 15  
  16 17 18 19 20 21 22  
  23 24 25 26 27 28 29  
  30 31
  ```

## Linux 파일 시스템을 탐색하는 명령

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
  $ unmae -v
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

  
