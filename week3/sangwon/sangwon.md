# Runnable을 사용해서 스레드 생성하기

실무에서는 보통 Runnable을 사용해서 스레드를 관리한다.

Thread 상속 보다는 Runnable 인터페이스를 구현해서 사용하는 것이 좋다

- Thread는 단일 상속만 가능하기 때문에 다른 클래스를 상속 받고 있으면 Thread를 상속 받을 수 없다
- 추가 extends 불가

Runnable 인터페이스 상속

- 상속이 자유롭다.
- 스레드와 실행할 작업을 분리해서 코드를 깔끔하게 유지할 수 있다
- 여러 스레드가 동일한 Runnable을 공유할 수 있어서 자원 관리를 효율적으로 할 수 있다
- 단 약간 코드가 복잡해 질 수 있다

---

# EC2 Https로 배포하기

### 필요한 것

- vpc
- ec2
- target group
- application load balancer
- aws certificate manager
- route 53
- domain

### 가비아 도메인 구매

- 도메인을 하나 구입해 준다.

### 도메인 등록

- 구매한 도메인에 대해 호스팅 영역을 추가해 준다
- 도메인을 입력 후 발급되는 네임 서버를 가비아의 도메인 네임 서버에 등록한다

### 도메인 인증서 발급(aws certificate manager)

- ACM 에서 구매한 도메인에 대해 인증을 받는다.
- \*.example.com 형식으로 인증서 발급을 요청한다 (sub domain으로 사용할 경우)
- Route53에 record를 추가해준다
- 좀만 기다리면 인증서가 발급된다

### EC2 생성

- ec2를 생성한다
- 이번 구성에서는 EC2 하나만 사용한다

### Target Group 생성

- EC2에 spring boot 애플리케이션이 들어가는데 ALB를 통해 서버를 호출할 수 있도록 만들어줘야 한다.
- EC2 안에서 서버를 호출 할 수 있는 PORT를 지정하고 서버 health check를 할 수 있도록 health check 경로를 만들어 줘야 한다.
- spring boot를 사용하기 때문에 actuator를 사용해서 health check api를 열어준다

### Application Load Balancer 생성

- ALB를 생성한다
- 도메인 인증서를 발급해 뒀으니 443 port로 listener rule을 설정한다
- 생성한 target group을 지정한다

### Route 53 설정하기

- sub domain을 추가하고 record type을 지정
- route traffic을 EC2 가 있는 region에 ALB를 지정한다
- route policy는 Simple routing으로 설정한다
