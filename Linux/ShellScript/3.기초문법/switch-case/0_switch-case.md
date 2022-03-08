# switch-case문

> 변수에 값에 따라 분기를 해야 하는 경우에 주로 사용됨.

- 기본 사용법

    ```bash
    case $변수 in
        조건값1)
        수행문1 ;;
        조건값2)
        수행문2 ;;
        조건값3)
        수행문3 ;;
        *)
        수행문4
    esac
    ```

    - 예제)

        ```bash
        #!/bin/bash
        
        # 입력받은 파라미터에 따라 해당 문자열을 출력하는 예제
        
        case $1 in
            start)
            echo "start";;
            stop)
            echo "stop";;
            restart)
            echo "restart";;
            help)
            echo "help";;
            *)
            echo "Please input sub command"
        esac
        ```
        
        ```bash
        # 파라미터가 없어 Please input sub command를 출력
        $ sh 1_switch-case.sh 
        Please input sub command
        
        # 파라미터와 동일한 start에 해당되어, start 출력
        $ sh 1_switch-case.sh start
        start
        ```
        

