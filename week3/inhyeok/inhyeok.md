## Cursor AI 정리

### Cursor AI 가격
Cursur 가격은 월 20$(한화 29,482.50원), 연간 플랜으로 월 16$(한화 23,586원)이다.
현재 악랄한 환율로 인해 부담스러운 가격인 것은 사실이다.

하지만 시대의 흐름을 따라가야하기 때문에 비용을 지불하는 것은 쩔수 라고 볼 수 있다.

### Cursor AI 사용 방법

#### 채팅 인터페이스(Ctrl + L)
그냥 챗봇을 사용하는 것과 다르지 않다. 다만 몇가지 개발자에게 유용한 특화 기능을 제공하는데, 이 기능들이 아주 유용하다.
1. '@' 명령어를 통해 특정 파일, 폴더, 코드조각, Codebase, Web 검색 결과 등을 참고할 수 있다.
2. 하단에 claude-3.5-sonnet이나 o1-mini 등 다양한 모델을 사용할 수 있다.
3. 코드 수정에 대한 제안이 있으면, Apply 버튼을 눌러 코드를 수정할 수 있다.

#### Composer(Ctrl + I)
명령어를 입력하면 바로 코드 에디터에서 수정이 진행된다.
이때 마음에 안들면 Reject, 마음에 들면 Accept 버튼을 눌러 코드를 수정할 수 있다.


#### AI 명령 패널 열기(Ctrl + K)
특정 코드 조각을 드레그 해서 수정 명령을 내릴 수 있다.
다만 코드의 연결성을 무시하기 때문에 주의가 필요하다.

#### 자동완성
사용자의 의도를 파악해서 코드를 제안해준다. 이때 Tab을 통해서 코드를 자동완성할 수 있다.

#### 터미널에서 사용하는 방법
터미널에서 드래그만 하면 채팅 인터페이스/Composer로 해당 내용을 이동시킬 수 있다.


#### Roles For AI
AI에게 역할을 부여해서 코드를 작성할 수 있다.
우측 상단의 톱니바퀴 버튼을 눌르고, General 탭에서 해당 설정을 확인할 수 있다.

난 다음과 같은 Roles를 사용한다.
```
you are an expert AI programming assistant in VSCode that primarily focuses on producing clear, readable
code.
You are thoughtful, give nuanced answers, and are brilliant at reasoning.
You carefully provide accurate, factual, and thoughtful answers, and you are a genius at reasoning.

1. Follow the user's requirements carefully and precisely.
2. First, think step-by-step - describe your plan for what to build in pseudocode, written out in great detail.
3. Confirm, then write the code!
4. Always write correct, up-to-date, bug-free, fully functional and working, secure, performant, and efficient code.
5. Focus on readability over performance.
6. Fully implement all requested functionality.
7. Leave NO to-dos, placeholders, or missing pieces.
8. Ensure the code is complete! Thoroughly verify the final version.
9. Include all required imports, and ensure proper naming of key components.
10. Be concise. Minimize any unnecessary explanations.
11. If you think there might not be a correct answer, say so. If you do not know the answer, admit it instead of guessing.
12. Always provide concise answers.
13. Please answer in Korean
```


#### @NOTEPADS
메모장에 글을 작성해두고, 해당 내용을 AI 질문에 포함할 수 있다.
다만 이 메모장은 코드 조각이 아니기 때문에 자동으로 코드 조각으로 변환되지 않는다.

따라서 차라리 특정 폴더를 만들어서 하단에 필요한 내용을 xxx.md 방식으로 작성해두고 해당 파일을 포함시켜서 질문을 하는 편이 좋다.


#### @Docs기능
사용하는 LIB/기술/API 에 대한 문서를 추가해둘 수 있다. 이 문서를 저장해두면 해당 내용을 참고해서 답변과 코드작성을 할 수 있다.
이 방식의 장점은 최신의 기술 문서를 참조할 수 있기 때문에 오래된 사용법을 참고해서 답변을 하지 않게 되는 것이다.

#### @Web
웹 페이지를 참고해서 답변을 하는 것이다.

