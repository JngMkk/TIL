# 2장 명령어

## 관리 명령어

프로세스, 메모리, 파일시스템 관리를 위한 명령어. 시스템 운영을 위해 필요함

### 시스템 관리

| cmd     | description                                          |
| ------- | ---------------------------------------------------- |
| crontab | 정기적으로 지정한 시간에 실행하고 싶은 명령어를 등록 |
| free    | 메모리 사용량 확인                                   |
| ps      | 프로세스 정보를 표시                                 |
| top     | 프로세스 정보를 실시간으로 표시                      |
| uname   | 시스템 정보를 표시                                   |

---

#### crontab

##### 주요 옵션

| option | description               |
| ------ | ------------------------- |
| -l     | 등록된 명령어 리스트 확인 |
| -e     | 등록된 명령어 수정        |

##### 사용 예제

- crontab 등록

  ```
  -e 옵션으로 실행하면 크론탭을 등록하기 위한 파일이 열림.
  vi 에디터와 동일한 명령으로 필요한 명령어를 등록할 수 있음
  ```

  ```bash
  # 크론탭을 등록
  $ crontab -e
  
  # 등록된 크론탭 확인
  $ crontab -l
  no crontab for user
  ```

- crontab 주기

  ```
  크론탭을 등록할 때는 실행하고자 하는 주기와 명령어를 입력함.
  주기는 분, 시, 일, 월, 요일의 형태로 입력함.
  *는 모두를 의미함.
  ```

  | 주기 | 비고                  |
  | ---- | --------------------- |
  | 분   | 0 ~ 59                |
  | 시   | 0 ~ 23                |
  | 일   | 1 ~ 31                |
  | 월   | 1 ~ 12                |
  | 요일 | 0 ~ 7 (0, 7 : 일요일) |

  ```bash
  # 입력 형태
  분 시 일 월 요일 명령어
  
  # 매 50분에 time.sh 실행
  50 * * * * /mnt/usr/time.sh
  
  # 매일 1시에 log로 끝나는 파일을 찾아서 find.log 파일로 저장
  0 1 * * * find -name '*.log' ./ >> /test/log/fin.log
  
  # 5분 마다 program.sh 실행
  */5 * * * * /home/user/program.sh
  
  # 4-10시 사이에 1시간마다 program.sh 실행
  0 4-10/1 * * * /home/user/program.sh
  
  # 매일 1시, 3시에 program.sh를 실행하고 로그를 저장
  # 크론탭에 입력할 때 %는 오류가 발생하기 때문에 역슬래시로 감싸 주어야 함
  0 1,3 * * * /home/user/program.sh >> /home/user/logs/`date -u +\%Y\%m\%d.\%H\%M.log` 2>&1
  ```

- echo로 crontab 등록

  ```
  크론탭을 일괄로 등록하고 싶을 때 echo 명령을 이용하여 처리할 수 있음.
  /var/spool/cron/유저명에 유저별 크론탭이 있음. (우분투 /var/spool/cron)
  여기에 넣어주면 crontab -e와 동일한 효과를 얻을 수 있음
  ```

  ```bash
  sudo bash -c 'echo \"
  # hadoop log cleansing
  0 1 * * * find /var/log/hadoop -not -name \"*.gz\" -type f -mtime +2 -exec gzip {} \;
  0 1 * * * find /var/log/hadoop -name \"*.gz\" -mtime +14 -delete \" >> /var/spool/cron/user_name'
  ```

---

#### free

##### 주요 옵션

| option       | description                                         |
| ------------ | --------------------------------------------------- |
| -h           | 사람이 읽을 수 있는 GB, MB, KB 형태로 변경하여 출력 |
| -s  [second] | 지정한 초마다 이용량 출력                           |

##### 사용 예제

```bash
$ free
              total        used        free      shared  buff/cache   available
Mem:       16308148     5496468     1325664       92820     9486016    10384960
Swap:      15625212        2560    15622652

$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       5.2Gi       1.3Gi        93Mi       9.1Gi       9.9Gi
Swap:          14Gi       2.0Mi        14Gi
```

```
total : 전체 메모리 용량
used : 사용중인 메모리 용량
free : 유휴 메모리 용량
shared : 공유 메모리 용량. 프로세서, 스레드간 통신을 위해 사용.
buffers : 버퍼 메모리 용량. 파일 저장을 위한 임시 저장 공간 등.
cached : 캐시 메모리 용량. 자주 사용하는 데이터를 메모리에 캐싱하여 IO 속도 증가
```

##### 주기적인 메모리 사용량 확인

- -s 옵션 / watch 명령

```bash
# 1초에 한 번씩 메모리 사용량 출력
$ free -h -s 1
              total        used        free      shared  buff/cache   available
Mem:           15Gi       5.2Gi       1.3Gi        94Mi       9.1Gi       9.9Gi
Swap:          14Gi       2.0Mi        14Gi

$ watch free -h
Every 2.0s: free -h
ubuntu: Wed Feb  9 22:41:24 2022

              total        used        free      shared  buff/cache   available
Mem:           15Gi       5.2Gi       1.3Gi        94Mi       9.1Gi       9.9Gi
Swap:          14Gi       2.0Mi        14Gi
```

---

#### htop

```
htop은 top보다 상세하게 운영체제의 상태를 모니터링할 수 있는 도구.
설치되어 있지 않은 경우 따로 설치.
```

```bash
# centos
$ yum install htop

# ubuntu
$ apt install htop
```

##### 실행

```
펑션키를 이용하여 트리구조로 프로세스를 확인하거나 목록으로 확일할 수 있음.
메모리, CPU 사용률로 프로세스를 정렬할 수도 있음.
```

---

#### jobs

```
현재 계정에서 실행중인 작업을 표시함
```

##### 주요 옵션

| option | description          |
| ------ | -------------------- |
| -l     | 프로세스 ID를 표시함 |

##### 사용예제

```bash
$ sleep 50&
[1] 83535

$ jobs
[1]+  Running                 sleep 50 &

$ jobs -l
[1]+ 83535 Running                 sleep 50 &

$ jobs -l
[1]+ 83535 Done                    sleep 50
```

```
Running : 실행중
Stopped : 일시 중단(Ctrl + Z 입력)
Terminated : 강제 종료(kill 명령 종료)
Done : 정상 종료
[ ]로 표시되는 것은 작업의 순서. -는 이전 프로세스, +는 현재 프로세스
```

---

#### journalctl

```
systemctl로 실행한 systemd의 로그를 확인할 수 있는 명령어
```

##### 주요 옵션

| option | description                         |
| ------ | ----------------------------------- |
| -u     | 로그를 출력할 유닛을 지정           |
| -o     | 출력 형식을 지정 (short, short-iso) |
| -f     | 신규로 추가되는 로그를 출력         |

##### 출력 형식

| option          | description                                           |
| --------------- | ----------------------------------------------------- |
| short           | 기본값. 한 행에 하나의 log만 출력                     |
| short-iso       | 기본값에 ISO 8601의 시간 형식으로 출력                |
| short-precise   | 기본값에 마이크로 초 단위로 시간 출력                 |
| short-monotonic | 기본값에 단조로운 시간 형식으로 출력                  |
| verbose         | 전체 log를 모두 자세하게 출력                         |
| json            | json 형식                                             |
| json-pretty     | json 형식을 보기 편하게 출력                          |
| json-see        | json 형식을 Server-Sent Events에 적합한 형식으로 출력 |
| cat             | 간결하게 출력                                         |

##### 사용예제

```bash
# 시스템 데몬 로그 출력
$ sudo journalctl -u mysql.service -o short-iso
-- Logs begin at Fri 2022-01-28 21:37:42 KST, end at Wed 2022-02-09 23:16:53 KST. --
2022-02-07T13:39:14+0900 ubuntu systemd[1]: Starting MySQL Community Server...
2022-02-07T13:39:15+0900 ubuntu systemd[1]: Started MySQL Community Server.
2022-02-07T13:45:24+0900 ubuntu systemd[1]: mysql.service: Main process exited, code=kill>
2022-02-07T13:45:24+0900 ubuntu systemd[1]: mysql.service: Failed with result 'signal'.
```



### 파일 시스템

| cmd  | description                             |
| ---- | --------------------------------------- |
| df   | 파일시스템의 디스크 사용량을 표시       |
| find | 파일을 검색할 때 사용                   |
| ls   | 파일 엔트리(파일, 디렉터리) 정보를 표시 |

---

### 압축 명령어

| cmd    | description                        |
| ------ | ---------------------------------- |
| gzip   | gzip 형식으로 파일을 압축          |
| gunzip | gzip 형식 파일의 압축 해제         |
| tar    | 여러개의 파일을 하나의 파일로 묶음 |

---

## 처리 명령어

업무 처리를 위한 명령어. 쉘스크립트에 사용 가능하고, 반복작업을 효율적으로 처리하기 위한 명령어

### 문자열 처리 명령어

| cmd  | description                                 |
| ---- | ------------------------------------------- |
| awk  | 입력을 주어진 분리자로 분리하여 명령을 처리 |
| diff | 파일 두개를 비교하여 다른 부분을 출력       |
| echo | 문자열이나 변수를 출력                      |
| grep | 지정한 문자열을 포함하고 있는 행을 검색     |
| sed  | 텍스트 데이터를 패턴 매칭하여 처리          |
| sort | 텍스트를 정렬                               |

### 날짜 명령어

| cmd  | description       |
| ---- | ----------------- |
| date | 일자, 시간을 처리 |





