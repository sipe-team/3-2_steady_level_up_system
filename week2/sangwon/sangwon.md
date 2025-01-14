# 스레드와 프로세스

![](/week2/sangwon/pic.png)

### 프로세스

- 프로그램을 실행하면 프로세스가 만들어지고 프로그램이 실행된다
- 운영체제 안에서 실행중인 프로그램을 프로세스라고 한다
- 실행중인 프로그램의 인스턴스이다
- 각 프로세스는 독립적인 메모리 공간을 가진다

### 스레드

- 프로세스 내에서 동작하고 프로세스 내에는 하나 이상의 스레드가 존재한다
- 프로세스 내의 스레드는 동일한 메모리를 공유한다
- 단일 스레드: 한 프로세스 내에 하나의 스레드만 존재
- 멀티 스레드: 한 프로세스 내에 여러 스레드가 존재

## 스레드와 스케줄링

### 단일 코어 스케줄링

- 운영체제는 스케줄링 큐를 가지고 있음
- 각 스레드는 스케줄링 큐에서 대기한다
- 큐에서 하나를 꺼내서 연산을 수행
- 코드 한 줄 한 줄 스레드가 수행한다

cpu에 어떤 프로그램이 얼마만큼 수행되는지 운영체제가 결정한다 이를 스케줄링이라고 한다

### 멀티 코어 스케줄링

- 두 개 이상의 코어로 동시에 스레드를 실행할 수 있다

## 컨텍스트 스위칭

- 멀티 태스킹이 반드시 효율적인 것은 아니다
- context switching 발생
- 진행중인 컨텍스트를 메모리에 잠깐 저장하고 이후에 다시 실행하는 시점에 저장한 값을 cpu에 다시 불러와야 한다
- context switching 에는 비용이 발생한다
- 따라서 멀티 태스킹은 효율적이지만 항상 효율적이지 않다.
