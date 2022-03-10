# 연산자

## 문자열 연산자

```
문자열 연산자는 변수의 데이터 타입이 문자열인 경우에 주로 사용되는 연산자로
해당 연산자와 함께 사용하면 변수에 숫자가 되든,
파일명이나 디렉터리와 같은 객체형의 값이 저장되든 상관없이 모두 문자열로 취급.
```

| 연산자 | 사용법          | 설명                   |
| ------ | --------------- | ---------------------- |
| -z     | if [ -z $변수 ] | 문자열 길이가 0이면 참 |

- 예제 ) 문자열 변수가 NULL값인지 체크할 경우

  ```bash
  #!/bin/bash
  
  # 파라미터로 받은 변수값의 길이가 0이면 True, 아니면 False 출력
  
  if [ -z $1 ]
  then
      echo True
  else
      echo False
  fi
  ```

  ```bash
  $ sh 01_operString.sh 
  True
  
  $ sh 01_operString.sh hi
  False
  ```

## 비교 연산자

### 정수 비교 연산자

| 연산자 | 사용법                   | 설명                                          |
| ------ | ------------------------ | --------------------------------------------- |
| -eq    | if [ $변수1 -eq $변수2 ] | 변수1과 변수2의 값이 같으면 참                |
| -ne    | if [ $변수1 -ne $변수2 ] | 변수1과 변수2의 값이 다르면 참                |
| -gt    | if [ $변수1 -gt $변수2 ] | 변수1의 값이 변수2의 값보다 크면 참           |
| -ge    | if [ $변수1 -ge $변수2 ] | 변수1의 값이 변수2의 값보다 크거나 같으면 참  |
| -lt    | if [ $변수1 -lt $변수2 ] | 변수1의 값이 변수2의 값보다 작으면 참         |
| -le    | if [ $변수1 -le $변수2 ] | 변수1의 값이 변수2의 값보다 작거나 같으면 참  |
| >      | if (( $변수1 > $변수2 )) | > 기호를 사용할 경우 중첩소괄호를 사용해야 함 |
| >=     | if (( $변수1 >= 변수2 )) |                                               |
| <      |                          |                                               |
| <=     |                          |                                               |

- 예제 1) 변수값이 서로 같은지 체크할 때

  ```bash
  #!/bin/bash
  
  var1=10
  var2=10
  
  if [ $var1 -eq $var2 ]
  then
      echo True
  else
      echo False
  fi
  
  if [ $var1 = $var2 ]
  then
      echo True
  else
      echo False
  fi
  ```

  ```bash
  $ sh 02_oper.sh 
  True
  True
  ```

- 예제 2) 변수값이 서로 다른지 체크할 때

  ```bash
  #!/bin/bash
  
  var1=10
  var2=10
  
  if [ $var1 -ne $var2 ]
  then
      echo True
  else
      echo False
  fi
  
  if [ $var1 != $var2 ]
  then
      echo True
  else
      echo False
  fi
  ```

  ```bash
  $ sh 03_oper.sh 
  False
  False
  ```

- 예제 3) 변수값의 크기를 비교할 때 - 문자형 연산자를 사용할 경우

  ```bash
  #!/bin/bash
  
  var1=10
  var2=10
  
  if [ $var1 -gt $var2 ]
  then
      echo True
  else
      echo False
  fi
  
  if [ $var1 -ge $var2 ]
  then
      echo True
  else
      echo False
  fi
  
  if [ $var1 -lt $var2 ]
  then
      echo True
  else
      echo False
  fi
  
  if [ $var1 -le $var2 ]
  then
      echo True
  else
      echo False
  fi
  ```

  ```bash
  $ sh 04_oper.sh 
  False
  True
  False
  True
  ```

- 예제 4) 기호 연산자를 사용할 경우

  ```
  리눅스에는 터미널에 출력될 값을 파일에 저장해주는 리다이렉션 기호들이 있음.
  <> >> | 와 같은 기호.
  이런 기호들을 구분하기 힘들기 때문에 기호 연산자를 이용하여 두 변수의 크기를 비교할 때는 중첩 소괄호를 사용하여 표현.
  ```

  ```bash
  #!/bin/bash
  
  var1=10
  var2=10
  
  if (( $var1 > $var2 ))
  then
      echo True
  else
      echo False
  fi
  
  if (( $var1 >= $var2 ))
  then
      echo True
  else
      echo False
  fi
  
  if (( $var1 < $var2 ))
  then
      echo True
  else
      echo False
  fi
  
  if (( $var1 <= $var2 ))
  then
      echo True
  else
      echo False
  fi
  ```

  ```bash
  $ sh 05_oper.sh 
  False
  True
  False
  True
  ```

---

### 문자열 비교 연산자

```
변수의 값이 문자열일 경우에는 정수를 비교할 때와는 다르게 문자형 연산자를 사용하지 않고 기호 연산자를 사용.
문자열 비교 시 비교 연산자도 문자로 되어 있으면, 휴먼 에러가 발생할 확률이 높기 때문임.
그래서, 문자열 비교에서는 기호 연산자만 사용할 수 있으며, 리다이렉션 기호와 동일한 <> 기호를 사용할 경우에는 구분하기 위해 중첩 대괄호[[]]를 사용함.
```

| 연산자 | 사용법                   | 설명                                                 |
| ------ | ------------------------ | ---------------------------------------------------- |
| =      | if [ $변수1 = $변수2 ]   | 각 변수의 값이 같으면 참, 동일한 문자열일 경우 참    |
| ==     | if [ $변수1 == $변수2 ]  | 각 변수의 값이 같으면 참, 동일한 문자열일 경우 참    |
| !=     | if [ $변수1 != $변수2 ]  | 각 변수의 값이 다르면 참, 서로 다른 문자열일 경우 참 |
| <      | if [[ $변수1 > $변수2 ]] | 변수1의 ASCII 코드값이 변수2보다 크면 참             |
| >      | if [[ $변수1 < $변수2 ]] | 변수1의 ASCII 코드값이 변수2보다 작으면 참           |

- 예제 1) 문자열을 비교할 때

  ```bash
  #!/bin/bash
  
  var1="abc"
  var2="def"
  
  if [ $var1 = $var2 ]
  then echo True
  else echo False
  fi
  
  if [ $var1 == $var2 ]
  then echo True
  else echo False
  fi
  
  if [ $var1 != $var2 ]
  then echo True
  else echo False
  fi
  
  if [[ $var1 > $var2 ]]
  then echo True
  else echo False
  fi
  
  if [[ $var1 < $var2 ]]
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 06_oper.sh 
  False
  False
  True
  False
  True
  ```

## 논리 연산자

```
논리 연산자에는 AND 연산자와 OR 연산자가 있으며, and의 약자인 -a와 or의 약자인 -o를 사용할 수 있음.
또한 AND와 OR의 의미를 가진 &&과 || 기호를 사용할 수 있음.
```

| 연산자 | 사용법                                                       | 설명                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -a     | if [ 조건식1 -a 조건식2 ]                                    | AND 연산으로 조건식1도 참이고, 조건식2도 참이면 참           |
| -o     | if [ 조건식1 -o 조건식2 ]                                    | OR 연산으로 조건식1이 참이거나 조건식2가 참이면 참           |
| &&     | if [ 조건식1 ] && [ 조건식 2 ]<br>if [[ 조건식1 && 조건식2 ]] | AND 연산으로 && 기호를 쓸 경우 조건식 별로 대괄호를 사용하거나 <br>중첩 대괄호를 사용해야 함 |
| \|\|   | if [ 조건식1 ] \|\| [ 조건식 2 ]<br>if [[ 조건식1 \|\| 조건식2 ]] | OR 연산으로 \|\| 기호를 쓸 경우 조건식 별로 대괄호를 사용하거나<br>중첩 대괄호를 사용해야 함 |

- 예제 1) AND, OR 연산 - 문자형 연산자를 사용할 경우

  ```BASH
  #!/bin/bash
  
  var1=10; var2=20; var3=30
  
  if [ $var1 -lt $var2 -a $var2 -gt $var3 ]
  then echo True
  else echo False
  fi
  
  if [ $var1 -lt $var2 -o $var2 -gt $var3 ]
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 07_logiOper.sh 
  False
  True
  ```

- 예제 2) AND, OR 연산 - 기호 연산자와 단일 대괄호를 사용할 경우

  ```bash
  #!/bin/bash
  
  var1=10; var2=20; var3=30
  
  if [ $var1 -lt $var2 ] && [ $var2 -gt $var3 ]
  then echo True
  else echo False
  fi
  
  if [ $var1 -lt $var2 ] || [ $var2 -gt $var3 ]
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 08_logiOper.sh 
  False
  True
  ```

- 예제 3) AND, OR 연산 - 기호 연산자와 중첩 대괄호를 사용할 경우

  ```BASH
  #!/bin/bash
  
  var1=10; var2=20; var3=30
  
  if [[ $var1 -lt $var2 && $var2 -gt $var3 ]]
  then echo True
  else echo False
  fi
  
  if [[ $var1 -lt $var2 || $var2 -gt $var3 ]]
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 09_logiOper.sh 
  False
  True
  ```

- 예제 4) AND, OR 연산 - 조건식도 기호 연산자를 사용할 경우

  ```bash
  #!/bin/bash
  
  var1=10; var2=20; var3=30
  
  if (( $var1 < $var2 )) && (( $var2 > $var3 ))
  then echo True
  else echo False
  fi
  
  if (( $var1 < $var2 || $var2 > $var3 ))
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 10_logiOper.sh
  False
  True
  ```

## 디렉터리 연산자

```
디렉터리 연산자는 변수 유형이 디렉터리일 경우에 사용할 수 있는 연산자로
특정 디렉터리 내의 파일 목록 중에 디렉터리가 있는지 체크할 경우 매우 유용하게 사용할 수 있음.
또한 디렉터리 내에 디렉터리나 파일이 있는지도 확인할 수 있음.
```

| 연산자 | 사용법          | 설명                                      |
| ------ | --------------- | ----------------------------------------- |
| -d     | if [ -d $변수 ] | 변수 유형이 디렉터리이면 참               |
| -e     | if [ -e $변수 ] | 디렉터리 내에 디렉터리나 파일이 있으면 참 |

- 예제) 디렉터리 연산

  ```
  환경변수 HOME을 이용하여 HOME의 값이 디렉터리인지,
  디렉터리라면 해당 디렉터리 내에 또 다른 디렉터리나 파일이 있는지를 -d와 -e를 이용하여 체크
  ```

  ```bash
  #!/bin/bash
  
  if [ -d $HOME ]
  then echo True
  else echo False
  fi
  
  if [ -e $HOME ]
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 11_dirOper.sh
  True
  True
  ```

## 파일 연산자

```
파일 연산자는 파일이 가지고 있는 다양한 속성들을 체크하는 연산자.
예를 들어 파일에 읽기 권한이 있는지, 쓰기 권한이 있는지 등을 파일 연산자를 통해 확인할 수 있음
```

| 연산자 | 설명                                                         |
| ------ | ------------------------------------------------------------ |
| -f     | 변수 유형이 파일이면 참                                      |
| -L     | 변수 유형이 파일이면서 심볼릭 링크이면 참                    |
| -r     | 변수 유형이 파일이거나 디렉터리이면서 읽기 권한이 있으면 참  |
| -w     | 변수 유형이 파일이거나 디렉터리이면서 쓰기 권한이 있으면 참  |
| -x     | 변수 유형이 파일이거나 디렉터리이면서 실행 권한이 있으면 참  |
| -s     | 변수 유형이 파일이거나 디렉터리이면서 사이즈가 0보다 크면 참 |
| -O     | 변수 유형이 파일이거나 디렉터리이면서 스크립트 실행 소유자와 동일하면 참 |
| -G     | 변수 유형이 파일이거나 디렉터리이면서 스크립트 실행 그룹과 동일하면 참 |

- 예제 1) 파일 여부를 체크할 경우

  ```bash
  #!/bin/bash
  
  FILE=/etc/localtime
  
  if [ -f $FILE ]
  then echo True
  else echo False
  fi
  
  if [ -L $FILE ]
  then echo True
  else echo False
  fi
  ```

  ```bash
  $ sh 12_fileOper.sh 
  True
  True
  ```

- 예제 2) 파일 권한을 체크할 경우

  ```bash
  #!/bin/bash
  
  ls -l /etc/localtime
  
  # 원파일 속성 확인
  ls -l /usr/share/zoneinfo/Asia/Seoul
  
  FILE=/etc/localtime
  
  # 파일에 읽기 권한이 있으면 True, 아니면 False
  if [ -r $FILE ]
  then echo True; else echo False; fi
  
  # 파일에 쓰기 권한이 있으면 True, 아니면 False
  if [ -w $FILE ]
  then echo True; else echo False; fi
  
  # 파일에 실행 권한이 있으면 True, 아니면 False
  if [ -x $FILE ]
  then echo True; else echo False; fi
  
  # 파일의 크기가 0보다 크면 True, 아니면 False
  if [ -s $FILE ]
  then echo True; else echo False; fi
  ```

  ```bash
  $ sh 13_fileOper.sh 
  lrwxrwxrwx 1 root root 30  1월 28 21:45 /etc/localtime -> /usr/share/zoneinfo/Asia/Seoul
  -rw-r--r-- 1 root root 645 10월 26 08:58 /usr/share/zoneinfo/Asia/Seoul
  True
  False	# 원파일에 쓰기 권한이 없음
  False	# 원파일에 실행 권한이 없음
  True
  ```

- 예제3) 파일 소유권을 체크할 경우

  ```
  -O 연산자와 -G 연산자를 이용해 스크립트가 수행되는 프롬프트의 소유자 및 그룹이
  변수에 정의된 파일의 소유자 및 그룹과 동일한지 여부를 확인할 수 있음
  ```

  ```bash
  #!/bin/bash
  
  # /etc/localtime의 파일 속성 확인
  ls -l /etc/localtime
  
  # /etc/localtime 원파일의 속성 확인
  ls -l /usr/share/zoneinfo/Asia/Seoul
  
  FILE=/etc/localtime
  
  # 스크립트 실행 소유자와 같은지
  if [ -O $FILE ]
  then echo True; else echo False; fi
  
  # 소유 그룹이 같은지
  if [ -G $FILE ]
  then echo True; else echo False; fi
  ```

  ```bash
  $ sh 14_fileOper.sh 
  lrwxrwxrwx 1 root root 30  1월 28 21:45 /etc/localtime -> /usr/share/zoneinfo/Asia/Seoul
  -rw-r--r-- 1 root root 645 10월 26 08:58 /usr/share/zoneinfo/Asia/Seoul
  False	# 루트 계정이 아니므로 False
  False	# 루트 계정이 아니므로 False
  
  # 루트 계정으로 할 경우
  # sh 14_fileOper.sh 
  lrwxrwxrwx 1 root root 30  1월 28 21:45 /etc/localtime -> /usr/share/zoneinfo/Asia/Seoul
  -rw-r--r-- 1 root root 645 10월 26 08:58 /usr/share/zoneinfo/Asia/Seoul
  True
  True
  ```

## 파일 비교 연산자

```
파일 비교 연산자는 두 개의 변수에 정의된 파일을 비교하는 연산자로 어떤 파일이 더 최근에 생성된 것인지,
어떤 파일이 더 오래된 파일인지 확인할 수 있음.
또한 -ef 연산자를 이용하여 두 개의 파일이 동일한 파일인지를 확인할 수 있음
```

| 연산자 | 사용법                   | 설명                                                       |
| ------ | ------------------------ | ---------------------------------------------------------- |
| -nt    | if [ $변수1 -nt $변수2 ] | 변수 유형이 파일이면서, 변수1이 변수2보다 최신 파일이면 참 |
| -ot    | if [ $변수1 -ot $변수2 ] | 변수 유형이 파일이면서, 변수1이 변수2보다 이전 파일이면 참 |
| -ef    | if [ $변수1 -ef $변수2 ] | 변수 유형이 파일이면서, 변수1과 변수2가 동일 파일이면 참   |

- 예제 1) 파일을 비교할 때

  ```bash
  #!/bin/bash
  
  # 비교할 파일 생성
  echo "AAA" > test1.txt
  sleep 1s
  echo "BBB" > test2.txt
  
  FILE1=test1.txt
  FILE2=test2.txt
  
  # 최신 파일인지 비교
  if [ $FILE1 -nt $FILE2 ]
  then echo True; else echo False; fi
  
  # 예전 파일인지 비교
  if [ $FILE1 -ot $FILE2 ]
  then echo True; else echo False; fi
  
  # 심볼릭 링크로 연결된 두 개의 파일명을 각각의 변수에 저장
  FILE1=/etc/localtime
  FILE2=/usr/share/zoneinfo/Asia/Seoul
  
  # 동일한 파일인지 비교
  if [ $FILE1 -ef $FILE2 ]
  then echo True; else echo False; fi
  ```

  ```bash
  $ sh 15_fileOper.sh 
  False
  True
  True
  ```

  