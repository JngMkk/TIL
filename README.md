# TIL

> "Today I Learned"



- 작성 순서
  - 특강 내용 정리



## 과목

| 과목   | 수강 여부 |
| ------ | --------- |
| Git & Github    | ✔         |

---
## 2021.12.30 ~ 2021.12.31 Git & Github 특강
### Git & Github?
> 개발자들의 협업을 위한 도구

- Git : 버전 관리 프로그램
  - 컴퓨터 소프트웨어의 특정 상태들을 관리
  - 맨 나중 파일과, 이전 변경사항만 남겨서 관리
- Git을 이용한 버전 관리
  - 중앙 집중식 버전 관리
  - 분산 버전

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6f395559-9e08-47f9-ba79-c9106788e12f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211230T063418Z&X-Amz-Expires=86400&X-Amz-Signature=0712dcff8709a5e1c184c5e5a6aa0b5a12e304695dd9e0b048837b96713151de&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)


- Github
  - 온라인 공유 저장소 (Social Coding)



### GUI & CLI
> GUI (Graphic User Interface)
>
> CLI (Command Line Interface)

- Git Bash 명령어

  | 명령어                               | 설명                                                         |
  | ------------------------------------ | :----------------------------------------------------------- |
  | ls -a                                | 숨긴 파일까지 리스트로 확인                                  |
  | touch [ ]                            | 현재 디렉토리에 파일을 만듦 (확장자 기입)                    |
  | mkdir                                | 현재 디렉토리에 폴더를 만듦                                  |
  | rm -r                                | 빈 디렉토리가 아니어도 디렉토리 삭제 (**<span style = 'color : red'><u>삭제 전 디렉토리 확인하기</u></span>**) |
  | rm *.[ ]                             | 파일 내 모든 .[ ] 파일 삭제                                  |
  | rm -rf [file / *]                    | 디렉토리 내 모든 파일, 폴더 삭제, .git 삭제                  |
  | git init                             | 특정 폴더를 깃으로 관리하기 시작 (**<span style = 'color : red'><u>홈폴더에서 사용하지 말 것</u></span>**) |
  | git status                           | 현재 상황 보기                                               |
  | git add [file]                       | file을 git stage에 올림 ( .입력 시 : 모든파일 )              |
  | git commit -m '메시지'               | '메시지' 저장소에 올림 (Local Repository) git commit만 입력한 경우 VIM 에디터 열림 |
  | git log / git log --oneline          | 로그 확인                                                    |
  | git checkout [head~1 / hash name]    | 파일의 이전 버전 확인하기 (돌아오려면 git checkout master)   |
  | git remote add origin [http]         | 원격 저장소에 추가함                                         |
  | git remote -v                        | 원격 저장소 조회                                             |
  | git remote rm origin                 | 원격 저장소와 연결 끊음                                      |
  | git push [저장소 이름] [브랜치 이름] | 로컬 저장소의 커밋을 원격 저장소에 업로드                    |
  | git push -u [브랜치 이름]            | 두 번째 커밋부터는 저장소 이름 생략 가능                     |



### Markdown
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

---

## 2021.12.30 Git 특강 2일차

## GIT IGNORE

> 깃의 추적을 피하고 싶을 때 작성

- 방법
  - touch .gitignore
  - 필요한 gitignore 확인
    - https://www.toptal.com/developers/gitignore

## GIT CLONE

- git clone 'address'
  - 최초 한번만
  - clone을 하면 그 폴더는 깃의 관리를 받게 됨

- hub에서 commit change 하지 않고 수정할 시 에러 발생함
  - ![캡처](TIL/캡처.PNG)
  - git pull origin master 입력
  - script 창에서 수정
  - (master|MERGING) 뜰 시
    - 수정한 것 add -> commit -> push