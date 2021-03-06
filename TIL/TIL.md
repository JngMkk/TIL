# 용어 정리

> 새롭게 알게 된 용어들 정리

## 데몬 (daemon)

```
멀티태스킹 운영 체제에서 사용자가 직접적으로 제어하지 않고, 백그라운드에서 돌면서 여러 작업을 하는 프로그램을 말함.
시스템 로그를 남기는 systemd처럼 보통 데몬을 뜻하는 'd'를 이름 끝에 달고 있으며 일반적으로 프로세스로 실행됨.
데몬은 대개 부모 프로세스를 갖지 않음. 즉 PPID가 1임.
```

## PID

```
PID(Process Identification Number)
프로세스 각각을 구별할 수 있는 유일한 데이터
```

## PPID

```
PPID(Parent Process Identification Number)
프로세르를 만든 부모 프로세스의 PID를 나타내는 값.
프로그램을 실행한 프로세스의 PID가 PPID로 할당됨.
쉘 프롬프트에서 명령어를 입력하여 프로그램을 실행했다면 쉘이 부모 프로세스가 되어 쉘의 PID가 프로세스의 PPID로 할당됨.
```

## 로드 밸런싱 (Load balancing)

```
트래픽을 분산시켜주는 컴퓨터 네트워크의 기법 (부하분산)
둘 혹은 셋 이상의 중앙처리장치 혹은 저장장치와 같은 컴퓨터 자원들에게 작업을 나누는 것
즉, 여러 서버가 분산 처리 하는 것을 로드 밸런싱이라고 함.
이로써 가용성 및 응답시간을 최적화 시킬 수 있음.
부하분산 서비스는 그에 적합한 하드웨어와 소프트웨어에 의해 제공됨.
이 기술은 보통 내부 네트워크를 이용한 병렬처리(특히, 고가용성의 병렬처리)에 사용됨.

인터넷 서비스를 위해서는 소프트웨어를 이용한 부하분산이 적용되며,
이 소프트웨어는 중간에 위치해 실제 서비스하는 서버와 클라이언트를 포트를 이용해 중개하고 있음
```

### 종류

```
OSI 7계층에 따라 나뉨.

L4 : Transport 계층을 사용, IP 주소와 포트 번호 부하 분산이 가능
L7 : Application 계층을 사용, URL 또는 HTTP 헤더에서 부하 분산이 가능
```

![434](https://user-images.githubusercontent.com/87686562/153221922-abbbdf95-5624-4960-818c-aeacd6ffd062.png)

---

## GateWay

```
컴퓨터 네트워크에서 서로 다른 통신망, 프로토콜을 사용하는 네트워크 간의 통신을 가능하게 하는 컴퓨터나 소프트웨어를 두루 일컫는 용어.
즉, 다른 네트워크로 들어가는 입구 역할을 하는 네트워크 포인트.
넓은 의미로는 종류가 다른 네트워크 간의 통로의 역할을 하는 장치임.
또한 게이트웨이를 지날 때마다 트래픽도 증가하기 때문에 속도가 느려질 수 있다.

게이트웨이는 서로 다른 네트워크 상의 통신 프로토콜(통신규약)을 적절히 변환해주는 역할을 함.
하나 이상의 프로토콜을 사용하여 통신한다는 면에서 라우터, 스위치와는 구별되며
OSI참조 모델의 7계층 가운데 어느 곳에서도 동작이 가능하므로 전송방식이 다른 통신망도 흡수함으로써 서로 다른 기종끼리도 접속을 가능하게 함

가장 잘 알려진 예로는 랜이나 무선 랜을 인터넷이나 다른 원거리 통신망에 연결하는 것.
이 경우 게이트웨이는 랜을 제공자 지정 네트워크에 연결함으로써 인터넷에 연결할 수 있게 됨.
```

## 라우터

```
라우터(Router 혹은 라우팅 기능을 갖는 공유기)
컴퓨터 네트워크 간에 데이터 패킷을 전송하는 네트워크 장치.
패킷의 위치를 추출하여, 그 위치에 대한 최적의 경로를 지정하며, 이 경로를 따라 데이터 패킷을 다음 장치로 전달함.
이 때 최적의 경로는 일반적으로는 가장 빠르게 통신이 가능한 경로이므로, 일반적으로는 최단 거리일 수 있지만,
돌아가는 경우라도 고속의 전송로를 통하여 전달 될 수 있음.
간단히 말해, 서로 다른 네트워크 간에 중계 역할을 해주는 장치
```

## ISO 8601

```
국제표준화기구에서 지정한 날짜, 시간 데이터에 대한 표준 규격.

그레고리력을 사용하며 연도는 네 자리인 YYYY로 월과 일은 두 자리인 MM과 DD로 나타냄.

24시간으로 나타내고 시는 hh 분은 mm 초는 ss이고 hhmmss 또는 hh:mm:ss로 나타냄
```



