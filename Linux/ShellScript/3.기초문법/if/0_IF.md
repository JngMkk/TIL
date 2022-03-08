# IF문

```BASH
if [ 조건식 ]
then
	수행문
elif [ 조건식 ]
then
	수행문
else
	수행문
fi
```

- 조건식 타입

  - 조건식은 변수의 타입이 숫자나 문자열 또는 파일과 같은 객체형이냐에 따라 사용되는 타입에 차이가 있음.
  - 연산의 종류에 따라서도 차이가 있을 수 있음.

  | 조건식 타입                      | 설명                                                         |
  | -------------------------------- | ------------------------------------------------------------ |
  | if [ $변수 연산자 $변수 ]; then  | 일반적인 조건식 타입으로 두 변수의 값을 비교할 때 쓰임       |
  | if [ $변수 연산자 조건값 ]; then | 조건값이 고정되어 있을 경우 변수와 조건값을 비교할 때 사용   |
  | if [ 연산자 $변수 ]; then        | 변수의 값이 문자열이거나 디렉터리와 같은 경우일 때 주로 사용 |
  | if [ 조건식 ] 연산자 [ 조건식 ]  | 여러 개의 조건식을 AND나 OR로 복합 연산할 때 사용            |

- 예제 1)

  ```bash
  #!/bin/bash
  
  # 변수 value1과 value2의 값이 동일한지 비교하는 조건문
  value1=10
  value2=10
  
  # 한줄로 사용할 경우 if [ $value1 = $value2 ]; then
  if [ $value1 = $value2 ]
  then
      echo True
  else
      echo False
  fi
  ```

- 예제 2)

  ```bash
  #!/bin/bash
  
  # 변수 value의 값이 0인지 비교하는 조건문
  
  value=0
  if [ $value = 0 ]
  then
      echo True
  else
      echo False
  fi
  ```

- 예제 3)

  ```bash
  #!/bin/bash
  
  # 변수 value의 길이가 0인지 비교하는 조건문
  # 연산자 -z는 변수에 저장된 값의 길이가 0인지 비교하여 0이면 True, 아니면 False 리턴하는 문자열 연산자
  
  value=""
  if [ -z $value ]
  then
      echo True
  else
      echo False
  fi
  ```

- 예제 4)

  ```bash
  #!/bin/bash
  
  # 변수 value의 값은 0보다 크고, 10보다 작은지를 비교하는 조건문
  # 연산자 -gt는 A가 B보다 큰지를 비교하는 연산자이며,
  # 연산자 -lt는 A가 B보다 작은지를 비교하는 연산자.
  # &&는 AND 연산을 의미함.
  
  value=5
  if [ $value -gt 0 ] && [ $value -lt 10 ]
  then
      echo True
  else
      echo False
  fi
  ```