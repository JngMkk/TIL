# Linux

## 기본 Linux 명령

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

  
