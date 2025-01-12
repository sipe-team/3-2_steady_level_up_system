# Gmail 수신시 카카오톡으로 알림 받는 방법

1. 사용자에게 Google OAuth 인증을 통해 권한을 부여받는다.  
읽기 전용 권한 부여받기 (https://www.googleapis.com/auth/gmail.readonly)
3. GCP의 Pub/Sub Topic을 통해서 사용자의 이메일을 수신한다.
4. GCP의 Cloud Run(Servless Founction)을 통해서 AWS Lambda를 호출한다.
5. AWS Lambda에서 OpenAI를 통해 이메일을 요약한다.
6. AWS Lambda에서 요약된 이메일을 SNS에 개시한다.
7. AWS SNS를 각 Lambda가 구독해 Slack, 카카오톡에 전송하고, SMS 서비스로 문자 메시지에 전송한다.
