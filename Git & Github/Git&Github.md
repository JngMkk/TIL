## Git & Github?
> 개발자들의 협업을 위한 도구

- Git : 버전 관리 프로그램
  - 컴퓨터 소프트웨어의 특정 상태들을 관리
  - 맨 나중 파일과, 이전 변경사항만 남겨서 관리
- Git을 이용한 버전 관리
  - 중앙 집중식 버전 관리
  - 분산 버전

![Git](https://user-images.githubusercontent.com/87686562/147811756-13e74e46-220c-436e-8a5f-b8e1152a9375.PNG)


- Github
  - 온라인 공유 저장소 (Social Coding)



## GUI & CLI
> GUI (Graphic User Interface)
>
> CLI (Command Line Interface)

- Git Bash 명령어

  | 명령어                                          | 설명                                                         |
  | ----------------------------------------------- | :----------------------------------------------------------- |
  | ls -a                                           | 숨긴 파일까지 리스트로 확인                                  |
  | touch [ ]                                       | 현재 디렉토리에 파일을 만듦 (확장자 기입)                    |
  | mkdir                                           | 현재 디렉토리에 폴더를 만듦                                  |
  | rm -r                                           | 빈 디렉토리가 아니어도 디렉토리 삭제 (**<span style = 'color : red'><u>삭제 전 디렉토리 확인하기</u></span>**) |
  | rm *.[ ]                                        | 파일 내 모든 .[ ] 파일 삭제                                  |
  | rm -rf [file / *]                               | 디렉토리 내 모든 파일, 폴더 삭제, .git 삭제                  |
  | git init                                        | 특정 폴더를 깃으로 관리하기 시작 (**<span style = 'color : red'><u>홈폴더에서 사용하지 말 것</u></span>**) |
  | git status                                      | 현재 상황 보기                                               |
  | git add [file]                                  | file을 git stage에 올림 ( .입력 시 : 모든파일 )              |
  | git commit -m '메시지'                          | '메시지' 저장소에 올림 (Local Repository) git commit만 입력한 경우 VIM 에디터 열림 |
  | git log / git log --oneline                     | 로그 확인                                                    |
  | git checkout [head~1 / hash name]               | 파일의 이전 버전 확인하기 (돌아오려면 git checkout master)   |
  | git remote add origin [http]                    | 원격 저장소에 추가함                                         |
  | git remote -v                                   | 원격 저장소 조회                                             |
  | git remote rm origin                            | 원격 저장소와 연결 끊음                                      |
  | git push [저장소 이름] [브랜치 이름]            | 로컬 저장소의 커밋을 원격 저장소에 업로드                    |
  | git push -u [브랜치 이름]                       | 두 번째 커밋부터는 저장소 이름 생략 가능                     |
  | touch .gitignore                                | 깃의 추적을 피하고 싶을 때 작성<br />필요한 git ignore 확인 : https://www.toptal.com/developers/gitignore |
  | git clone [repo 주소]                           | 최초 한번만,  깃의 관리를 받게 됨<br />허브에서 수정할 시 에러 발생 가능성 있음 |
  | [Error 시] git pull [저장소 이름] [브랜치 이름] | script 창에서 수정 후 add -> commit -> push                  |
  | git branch                                      | 현재 작업공간에 존재하는 branch 확인                         |
  | git branch [branch 이름]                        | 새로운 branch 생성 (작업 공간이 서로 다름)                   |
  | git switch [branch 이름]                        | branch 바꾸기                                                |
  | git merge [branch 이름]                         | branch 이름의 작업과 최초 branch와 결합                      |



## Markdown
> 개발자들의 문서 작성 양식 & 문법

- Markdown 문법

  ```
  # : 문서의 논리적 흐름 (h1 ~ h6)
  > : 인용문
  - : 리스트
  ``` : Block
  ` ` : Inline
  ![이미지 이름](이미지 주소) : 이미지 추가
  [링크 이름](링크 주소) : 링크 추가
  | | | : 표 작성
  *string* : 기울임
  **string** : 보드체
  ~~string~~ : 취소선
  ```

