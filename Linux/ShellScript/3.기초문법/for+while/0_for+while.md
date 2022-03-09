# for, while문

## for

- 기본 사용법 1

    ```
    첫 번째 기본 사용법은 python의 for문 사용법과 같이 in을 사용하여 리스트나 배열과 같은
    특정 범위의 값들을 하나씩 꺼내어 변수에 저장하고,
    리스트나 배열의 해당 값을 모두 사용할 때까지 특정 수행문을 처리하는 방식.
    셸 스크립트에서는 2보다 1을 더 많이 사용함
    ```

    ```bash
    for 변수 in [범위(리스트 또는 배열, 묶음 등)]
    do
        반복할 수행문
    done
    ```

- 기본 사용법 2

    ```
    두 번째 사용법은 JAVA나 C 언어와 같이 초기값이 특정 조건에 해당할 때까지
    값을 증가시키면서 특정 수행문을 계속 반복하는 방법.
    ```

    ```bash
    for ((변수=초기값; 조건식; 증가값))
    do
        반복할 수행문
    done
    ```

- 예제 1)

    ```bash
    #!/bin/bash

    # 숫자 1 2 3을 바로 for문에 사용

    for num in 1 2 3
    do
        echo $num;
    done
    ```

    ```bash
    $ sh 1_for.sh
    $ sh 1_for.sh 
    1
    2
    3
    ```

- 예제 2)

    ```bash
    #!/bin/bash

    # 숫자 1 2 3을 변수에 저장하고 변수를 for문에 사용

    numbers="1 2 3"

    for num in $numbers
    do
        echo $num;
    done
    ```

    ```bash
    $ sh 2_for.sh 
    1
    2
    3
    ```

- 예제 3) 범위를 디렉터리로 사용할 경우

    ```bash
    #!/bin/bash

    # 환경변수를 사용하여 데릭터리 경로를 for문에 사용

    for file in $GOROOT/*
    do
        echo $file;
    done
    ```

    ```bash
    $ sh 3_for.sh
    /bin
    /cmd
    /dev
    /etc
    /git-bash.exe
    /git-cmd.exe
    /LICENSE.txt
    /mingw64
    /proc
    /ReleaseNotes.html
    /tmp
    /unins000.dat
    /unins000.exe
    /unins000.msg
    /usr
    ```

- 예제 4) 범위를 중괄호로 사용할 경우

    ```
    범위값을 사용할 때 연속된 숫자를 나열할 경우가 있음.
    이런 경우에는 중괄호{}를 사용하여 초기값과 마지막값을 입력하고 중간에 생략한다는 의미의 ..을 이용하면
    모든 숫자를 나열하지 않아도 되므로 좀 더 효율적으로 반복문을 사용할 수 있음.
    중괄호를 사용할 경우 증가값이 1이 아니라 그 이상일 경우
    {초기값..최종값..증가값}으로 표현할 수 있음.
    ```

    ```bash
    #!/bin/bash

    # 중괄호를 사용하면 범위에 해당하는 모든 숫자를 나열하지 않고 생략할 수 있음

    for num in {1..5}
    do
        echo $num;
    done
    ```

    ```bash
    $ sh 4_for.sh 
    1
    2
    3
    4
    5
    ```

    ```bash
    #!/bin/bash

    # 범위를 숫자로 사용할 경우 특정 값으로 증감 표현 가능

    for num in {1..10..2}
    do
        echo $num;
    done
    ```

    ```bash
    $ sh 5_for.sh 
    1
    3
    5
    7
    9
    ```

- 예제 5) 범위를 배열로 사용하는 경우

    ```
    범위를 배열로 사용할 경우에는 배열 선언 시 값과 값 사이에 쉼표 ,를 사용해서는 안됨.
    또한 for문에 배열의 모든 아이템을 범위로 사용할 경우 ${배열[@]}을 사용하여 배열의 모든 아이템을 사용한다고 명시해 줘야 함.
    이는 위치 매개변수 $@를 사용하면 파라미터로 넘어오는 모든 매개변수를 의미하는 것과 동일한 의미
    ```

    ```bash
    #!/bin/bash

    # 배열을 사용할 때는 ${배열[@]}로 표현해야 배열의 모든 아이템을 사용할 수 있음

    array=("apple" "banana" "pineapple")

    for fruit in ${array[@]}
    do
        echo $fruit;
    done
    ```

    ```bash
    $ sh 6_for.sh
    apple
    banana
    pineapple
    ```

- 예제 6)

    ```bash
    #!/bin/bash

    # 반드시 ()소활호를 더블(())로 사용해야 함

    for ((num=0; num<3; num++))
    do
        echo $num;
    done
    ```

    ```bash
    $ sh 7_for.sh 
    0
    1
    2
    ```

## while

- 기본 사용법

    ```bash
    while [$변수1 연산자 $변수2]
    do
        반복할 수행문
    done
    ```

- 예제

    ```bash
    #!/bin/bash

    # 변수 num이 3보다 작은 경우에 num 값을 출력하는 예

    num=0

    while [ $num -lt 3 ]
    do
        echo $num
        num=$((num+1))
    done
    ```

    ```bash
    $ sh 8_while.sh 
    0
    1
    2
    ```
