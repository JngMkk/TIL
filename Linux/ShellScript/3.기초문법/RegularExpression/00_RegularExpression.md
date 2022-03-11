# 정규 표현식

```
정규 표현식은 리눅스나 유닉스에 특별한 특징을 부여하는 문자들과 메타 문자들의 집합임.
주로 텍스트 탐색과 문자열 조작에 쓰이며, 하나의 문자와 일치하거나,
혹은 문자열의 일부분이나 전체 문자열 중 특정 문자 집합을 표현할 때 사용
```

## POSIX 기본 및 확장 문법

```
정규 표현식은 일치하는 텍스트를 찾기 위한 패턴을 표현하기 위해 사용되는 특정 표준 텍스트의 문법을 의미함.
패턴을 기술하는 문자열 내의 각 문자들은 메타 문자(특별한 의미)나 정규 문자로 이해됨.
예를 들면 "a."을 표현했다고 하면 "a."는 a와 일치하는 문자 하나와 뉴라인을 제외한 모든 문자 하나를 갖는 문자열과 일치시키는 메타 문자임.
```

| 메타 문자 | 설명                                                         |
| --------- | ------------------------------------------------------------ |
| .         | 뉴라인을 제외한 한 개의 문자와 일치함                        |
| ?         | 자신 앞에 나오는 정규 표현식이 없거나 하나가 일치하며, 대부분 한 개의 문자와 매칭할 때 사용 |
| *         | 바로 앞 문자열이나 정규 표현식에서 한 번 이상 반복되는 문자를 의미 |
| +         | 자신 앞에 나오는 하나 이상의 정규 표현식과 일치함. *과 비슷하게 동작하지만 반드시 하나 이상일 경우만 일치함 |
| {N}       | 정확히 N번 일치함                                            |
| {N,}      | N번 또는 그 이상 일치함                                      |
| {N,M}     | 적어도 N번 일치하지만, M번 일치를 넘지 않아야 함             |
| -         | A부터 Z를 A-Z로 표한하듯이 알파벳이나 숫자의 범위를 나타낼 때 사용 |
| ^         | 라인의 시작에서 공백 문자열을 의미함. 또한 목록의 범위에 없는 문자들을 의미함 |
| $         | 라인 마지막에서 공백 문자열을 의미함                         |
| ^$        | 빈 줄과 일치함                                               |
| [...]     | 대괄호는 단일 정규 표현식에서 문자들을 집합으로 묶어줌       |
| \         | 특수 문자를 원래 문자 의미대로 해석함                        |
| \b        | 단어 끝의 공백 문자열을 의미함 (문자와 공백 사이)            |
| \B        | 라인 끝의 공백 문자열을 의미함                               |
| \\<       | 단어 시작에서 공백 문자열을 의미함                           |
| \\>       | 단어 끝에서 공백 문자열을 의미함                             |

## POSIX 문자클래스

```
문자클래스에는 알파벳, 알파벳 소문자, 알파벳 대문자, 숫자 그리고 특수 문자들이 있음.
```

| POSIX      | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| [:alnum]   | 알파벳이나 숫자로 이루어진 문자열로 [A-Za-z0-9]와 같은 표현  |
| [:alpha:]  | 알파벳 문자를 의미하며, [A-Za-z]와 같은 표현                 |
| [:blank:]  | 스페이스나 탭을 의미함                                       |
| [:cntrl:]  | 제어 문자들을 의미함, [\x00-\x1F\x7F] (\c)                   |
| [:digit:]  | 0 ~ 9 사이의 숫자를 의미하며, [0-9], \d와 같은 표현임 ( \D 숫자 이외의 문자 \[^0-9]) |
| [:graph:]  | 출력 가능한 그래픽 문자들로, ASCII 33~126 사이의 문자들과 일치함. 스페이스 및 제어 문자들을 제외한 [:print:]와 같음, [\x21-\x7E] (보여지는 문자) |
| [:lower:]  | 알파벳 소문자를 의미하며 [a-z]와 같은 표현                   |
| [:print:]  | 출력 가능한 문자들로 ASCII 32~126 사이의 문자들과 일치함 [:graph:]와 비슷하지만 스페이스 문자를 포함, [\x20-\7E], \p (보여지는 문자와 공백 문자) |
| [:punct:]  | 문장 부호 문자들을 의미함, [][!#$%&’()\*+,./:;<=>?@\^_`{\|}~-\] |
| [:space:]  | 뉴라인 줄바꿈, 스페이스, 탭과 같은 모든 공백 문자들을 의미함, \s와 같은 표현 ( \S는 공백문자 이외 문자 \[^ \t\r\n\v\f]) |
| [:upper:]  | 알파벳 대문자를 의미하며 [A-Z], \u 와 같은 표현              |
| [:xdigit:] | 16진수의 숫자와 문자를 의미하며 [0-9a-fA-F], \x 와 같은 표현임 |
| [:word:]   | 영문자와 숫자 그리고 밑줄 문자 \w [A-Za-z0-9_]               |

## 다양한 정규 표현식 예제

```
정규 표현식은 메타 문자 하나만 이용할 수도 있지만, 대부분은 여러 메타 문자와 문자클래스를 조합하여 사용함.
```

- ex.txt

  ```
  ====================
   Regular Expression
  ====================
    
  #===========================================#
  # Date: 2020-05-05
  # Author: NaleeJang
  # Description: regular expression test file
  #===========================================#
  
  
  Today is 05-May-2020.
  Current time is 6:04PM.
  This is an example file for testing regular expressions.	This example file includes control characters.
  
  # System Information
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  Memory size is 32GiB
  Disk is 512 GB
  IP Address is 192.168.35.7
  
  # Help
  Do you have any questions? or Do you need any help?
  If you have any questions, Please send a mail to the email below.
  
  # Contacts
  e-mail: nalee999@gmail.com
  phone: 010-2222-5668
  
  ```

- 예제 1) 메타 문자 .을 이용할 경우

  ```
  메타 문자 .은 뉴라인을 제외한 한 개의 문자를 의미함.
  특정 문자 사이에 오는 한 개의 글자로 어떤 문자가 와도 상관이 없으며,
  여러 글자를 표현할 경우에는 찾고자 하는 문자 개수에 의해 메타 문자 .을 사용해야 함
  ```

  ```bash
  # C로 시작해 U로 끝나는 세 글자 단어여야 하며, 가운데 한 개의 글자는 어떤 문자가 와도 상관 없음
  $ grep 'C.U' ex.txt
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  
  # C로 시작해 e로 끝나는 네글자 단어여야 하며, 가운데 두 글자는 어떤 문자가 와도 상관 없음
  $ grep 'C..e' ex.txt
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  ```

- 예제 2) 메타 문자 * \ ? 와 문자클래스 [:lower:]를 이용할 경우

  ```
  메타 문자 *은 문자와 문자 사이 또는 문자 뒤에 어떤 문자열이 와도 상관이 없을 경우 사용하며
  \는 특수 문자를 사용할 경우 해당 문자가 메타 문자가 아닌 일반 문자일 경우 \를 붙여주면 일반 문자로 인식.
  ?는 앞에서 검색한 단어 하나가 일치하거나 일치하지 않을 경우에도 검색할 수 있음
  문자클래스 [:lower:]는 알파벳 소문자를 의미하며, grep과 함께 쓰일 때는 중첩 대괄호를 사용해야 함.
  ```

  ```bash
  # q로 시작하며 ?로 끝나는 단어야야 하며 q와 ? 사이는 영문소문자인 단어
  $ grep -E 'q[[:lower:]]*\?' ex.txt
  Do you have any questions? or Do you need any help?
  $ grep -E 'q[a-z]*\?' ex.txt
  Do you have any questions? or Do you need any help?
  
  # q로 시작하며 ?로 끝나거나 그 외 한 문자로 끝나는 단어여야 하며 q와 ? 사이는 영문소문자인 단어
  $ grep -E 'q[[:lower:]]*\??' ex.txt
  Do you have any questions? or Do you need any help?
  If you have any questions, Please send a mail to the email below.
  $ grep -E 'q[a-z]*\??' ex.txt
  Do you have any questions? or Do you need any help?
  If you have any questions, Please send a mail to the email below.
  
  -E, --extended-regexp     PATTERNS are extended regular expressions
  ```

- 예제 3) 메타 문자 + 와 ^ 를 이용할 경우

  ```
  메타 문자 + 는 앞에서 검색한 문자 하나가 계속 반복되는 경우
  ^ 는 라인 시작 문자가 검색하고자 하는 단어일 경우
  ```

  ```bash
  # -2로 시작해 -로 끝나며, 2가 계속 반복되는 단어
  $ grep -E '\-2+\-' ex.txt
  phone: 010-2222-5668
  
  # 라인 시작 문자가 #으로 시작되는 라인
  $ grep -E '^#' ex.txt
  #===========================================#
  # Date: 2020-05-05
  # Author: NaleeJang
  # Description: regular expression test file
  #===========================================#
  # System Information
  # Help
  # Contacts
  ```

- 예제 4) 메타 문자 ^, {N}, {N,}, 문자클래스 [:alpha:] 이용

  ```
  [:alpha:]는 알파벳 한 글자를 의미.
  {N}의 N은 앞에서 검색한 문자나 문자클래스가 몇 번 반복되는지를 숫자로 기입한 것이며,
  {N,}은 앞에서 검색한 문자나 문자클래스가 최소 N번 이상일 경우 이용
  ```

  ```bash
  # 라인 시작 시 알파벳 5글자로 시작하며, 알파벳 뒤에 : 으로 끝나는 단어가 있는 라인
  $ grep -E '^[[:alpha:]]{5}:' ex.txt
  phone: 010-2222-5668
  $ grep -E '^[A-Za-z]{5}:' ex.txt
  phone: 010-2222-5668
  
  # 라인 시작 시 알파벳 5글자 이상이며, 뒤에 공백을 가진 단어가 있는 라인
  $ grep -E '^[[:alpha:]]{5,}[[:space:]]' ex.txt
  Today is 05-May-2020.
  Current time is 6:04PM.
  Memory size is 32GiB
  $ grep -E '^[A-Za-z]{5,}\s' ex.txt
  Today is 05-May-2020.
  Current time is 6:04PM.
  Memory size is 32GiB
  ```

- 예제 5) 메타 문자 {N,M}, $, 문자 클래스 [:alpha:], [:digit:] 을 이용할 경우

  ```
  {N,M}은 앞에서 검색한 문자나 문자클래스가 N번 이상, M번 이하
  $는 라인 종료를 의미함
  [:digit:]은 0-9 사이의 정수를 의미
  ```

  ```bash
  # 라인 종료 시 알파벳 4글자 이상 6글자 이하인 단어가 있는 라인
  $ grep -E '[[:alpha:]]{4,6}$' ex.txt
   Regular Expression
  # Author: NaleeJang
  # Description: regular expression test file
  # System Information
  # Help
  # Contacts
  $ grep -E '[A-Za-z]{4,6}$' ex.txt
   Regular Expression
  # Author: NaleeJang
  # Description: regular expression test file
  # System Information
  # Help
  # Contacts
  
  # 라인 종료 시 숫자 4글자 이상 6글자 이하와 .으로 이루어진 단어가 있는 라인
  $ grep -E '[[:digit:]]{4,6}.$' ex.txt
  Today is 05-May-2020.
  $ grep -E '[0-9]{4,6}.$' ex.txt
  Today is 05-May-2020.
  ```

- 예제 6) 메타 문자 ^, ^$를 이용할 경우

  ```
  ^는 라인 시작을 알려줌.
  ^$는 라인 시작을 알려주는 ^와 종료를 알려주는 $가 합쳐서 라인의 공백을 의미함
  ```

  ```bash
  # 라인 시작 시 #으로 시작하고, 공백인 라인 제거
  $ cat ex.txt | grep -v '^#' | grep -v '^$'
  ====================
   Regular Expression
  ====================
    
  Today is 05-May-2020.
  Current time is 6:04PM.
  This is an example file for testing regular expressions.	This example file includes control characters.
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  Memory size is 32GiB
  Disk is 512 GB
  IP Address is 192.168.35.7
  Do you have any questions? or Do you need any help?
  If you have any questions, Please send a mail to the email below.
  e-mail: nalee999@gmail.com
  phone: 010-2222-5668
  
  -v, --invert-match        select non-matching lines
  ```

- 예제 7) 메타 문자 \, \b, \B를 이용

  ```
  \는 메타 문자와 동일한 문자를 검색할 경우 해당 문자가 메타 문자가 아닌 일반 문자임을 알리기 위해 사용함.
  \b는 단어의 끝을 의미함
  \B는 라인의 끝을 의미함 ($)
  ```

  ```bash
  # . 으로 끝나는 단어가 있는 라인
  $ grep '\.\b' ex.txt
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  IP Address is 192.168.35.7
  e-mail: nalee999@gmail.com
  
  # . 가 있는 라인
  $ grep '\.' ex.txt
  Today is 05-May-2020.
  Current time is 6:04PM.
  This is an example file for testing regular expressions.	This example file includes control characters.
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  IP Address is 192.168.35.7
  If you have any questions, Please send a mail to the email below.
  e-mail: nalee999@gmail.com
  $ ip address show | grep '\.'
      inet 127.0.0.1/8 scope host lo
      inet 192.168.75.228/24 brd 192.168.75.255 scope global dynamic noprefixroute enp0s31f6
      inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
      
  # . 으로 끝나는 라인
  $ grep '\.\B' ex.txt
  Today is 05-May-2020.
  Current time is 6:04PM.
  This is an example file for testing regular expressions.	This example file includes control characters.
  If you have any questions, Please send a mail to the email below.
  ```

- 예제 8) 메타 문자 \\<, \\> 를 이용할 경우

  ```
  \< 는 단어의 시작
  \> 는 단어의 끝을 의미
  ```

  ```bash
  # C로 시작하는 단어가 있는 라인
  $ grep '\<C' ex.txt
  Current time is 6:04PM.
  CPU model is Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  # Contacts
  
  # n으로 끝나는 단어가 있는 라인
  $ grep 'n\>' ex.txt
   Regular Expression
  # Description: regular expression test file
  This is an example file for testing regular expressions.	This example file includes control characters.
  # System Information
  ```

- 예제 9) 문자클래스 [:cntrl:], [:graph:]를 이용하는 경우

  ```
  문자클래스 [:cntrl:]은 특수 문자를 의미
  예를 들어 탭이나 캐리지 리턴 등 눈으로 볼 수 없는 문단 부호들을 의미
  문자클래스 [:graph:]는 스페이스를 제외한 아스키 코드를 의미
  ```

  ```bash
  # 특수 문자가 포함된 라인. expressions와 This 사이에는 tab 문자가 있음
  $ grep '[[:cntrl:]]' ex.txt
  This is an example file for testing regular expressions.	This example file includes control characters.
  
  # 아스키 코드가 있는 모든 라인
  $ grep '[[:graph:]]' ex.txt | head -n 10
  ====================
   Regular Expression
  ====================
  #===========================================#
  # Date: 2020-05-05
  # Author: NaleeJang
  # Description: regular expression test file
  #===========================================#
  Today is 05-May-2020.
  Current time is 6:04PM.
  ```

- 예제 10) 문자클래스 [:print:] 를 이용

  ```
  [:print:]는 스페이스를 포함한 아스키 코드를 의미
  ```

  ```bash
  # 스페이스를 포함한 아스키 코드가 있는 모든 라인
  $ grep '[[:print:]]' ex.txt | head -n 10
  ====================
   Regular Expression
  ====================
    
  #===========================================#
  # Date: 2020-05-05
  # Author: NaleeJang
  # Description: regular expression test file
  #===========================================#
  Today is 05-May-2020.
  ```

- 예제 11) 메타 문자 {N,}과 문자클래스 [:alpha:], [:punct:]를 이용할 경우

  ```
  문자클래스 [:punct:]는 문장 부호를 의미.
  예를 들어, 문장을 나타낼 때 쓰이며 마침표(.), 쉼표(,), 물음표(?), 세미콜론(:) 등을 의미
  ```

  ```bash
  # 알파벳 6글자 이상이며, 문장 부호로 끝나는 단어가 있는 라인
  $ grep -E '[[:alpha:]]{6,}[[:punct:]]' ex.txt
  # Author: NaleeJang
  # Description: regular expression test file
  This is an example file for testing regular expressions.	This example file includes control characters.
  Do you have any questions? or Do you need any help?
  If you have any questions, Please send a mail to the email below.
  ```

- 예제 12) 메타 문자 \\<, \\>, *, {N}과 문자클래스 [:xdigit:]을 이용

  ```
  문자클래스 [:xdigit:]은 16진수에 해당하는 문자들만 허용.
  따라서 다음과 같이 IPv6와 같은 주소를 검색할 경우
  단어 시작과 끝을 의미하는 메타 문자 \<, \>와 검색한 문자클래스가 몇 번 반복되는지를 메타 문자 {N}을 사용하면 쉽게 검색할 수 있음
  ```

  ```bash
  # 16진수 2글자로 시작하며, 16진수 2글자로 끝나는 단어가 있는 라인
  $ ip a | grep -E '\<[[:xdigit:]]{2}:*:[[:xdigit:]]{2}\>'
      link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      link/ether 18:31:bf:4d:cb:5a brd ff:ff:ff:ff:ff:ff
      link/ether 02:42:60:84:16:77 brd ff:ff:ff:ff:ff:ff
      link/ether 6a:8b:2f:0d:90:71 brd ff:ff:ff:ff:ff:ff link-netnsid 0
      link/ether 0a:00:27:00:00:00 brd ff:ff:ff:ff:ff:ff
      link/ether 6a:1d:9a:4f:3e:38 brd ff:ff:ff:ff:ff:ff link-netnsid 1
  ```

  
