### Git bash에서 conda 명령어 사용하기

> Window 10 환경

```
Anaconda3 설치 디렉터리 찾기
Anaconda3 > etc > profile.d
Git Bash Here
echo ". ${PWD}/conda.sh" >> ~/.bashrc

경로에 공백이 있는 경우
echo ". '${PWD}'/conda.sh" >> ~/.bashrc
single quotes 붙여줌.
```