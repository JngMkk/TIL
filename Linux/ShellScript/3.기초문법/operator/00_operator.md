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