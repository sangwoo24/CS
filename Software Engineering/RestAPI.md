# REST (Representational State Transfer)
- 월드 와이드 웹 (World Wide Web a.k.a WWW) 과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식.
- "웹에 존재하는 모든 자원 (이미지, 동영상, DB자원 등) 에 고유한 `URI : Uniform Resource Idetifier` 를 부여해 활용" 하는 것으로, 자원을 정의하고 자원에 대한 주소를 지정하는 방법론을 의미한다.
- 자원 기반의 구조 (**ROA**, Resource Oriented Architecture) **설계의 중심에 자원**이 있고, **HTTP Method 를 통해 자원을 처리**하도록 설계된 아키텍처
<br><br><br><br>

## REST 의 구성요소

### 1. 자원 (Resource) : URI
- 모든 자원은 고유한 ID 가 존재하고, 이 자원은 Server 에 존재한다.
- 자원을 구별하는 ID 는 `HTTP URI` 이다.
- Client 는 URI 를 이용해서 자원을 지정하고, 해당 자원의 상태(정보) 에 대한 조작을 Server 에 요청한다.

### 2. 행위 (Verb) : HTTP Method
- Client 는 URI 를 이용해 자원을 지정 및 조작하기 위해 HTTP 프로토콜의 Method 를 사용한다.
- HTTP 프로토콜은 `POST(Create)`, `GET(Read)`, `PUT(Update)`, `DELETE(Delete)` 등의 Method 를 제공한다.

### 3. 표현 (Representation)
- Client 가 Server 로 요청을 보냈을 때 서버가 응답으로 보내주는 자원의 상태를 **Representation** 이라고 한다.
- REST 에서 하나의 자원은 `JSON`, `XML`, `TEXT` 등 여러 형태의 **Representation** 으로 나타낼 수 있다.
<br><br><br><br>

## REST 의 특징
### 1. Client-Server (클라이언트-서버)
- Server 는 자원을 갖고있고, Client 는 자원을 요청한다.

### 2. Stateless (무 상태)
- HTTP 프로토콜은 Stateless Protocol 이므로 REST 역시 `Stateless` 하다.
- Client 의 `Context` 를 Server 에 저장하지 않음으로, 구현이 단순해진다.

### 3. Cacheable (캐시 처리 가능)
- 웹 표준 HTTP 프로토콜을 그대로 사용하므로, 웹에서 사용하는 기존의 인프라를 그대로 활용할 수 있다.
- 전체 응답시간, 성능, 서버의 자원 이용률을 향상시킬 수 있다.

### 4. Layered System (계층화)
- API 서버는 순수 비즈니스 로직을 수행하고 그 앞단에 사용자 인증, 암호화, 로드밸런싱 등을 하는 계층을 추가하여 구조상의 유연성을 줄 수 있다.

### 5. Uniform Interface (인터페이스 일관성)
- URI 로 지정한 자원에 대한 조작을, 통일되고 한정적인 인터페이스로 수행한다.
- HTTP 표준 프로토콜을 따르는 모든 플랫폼에서 사용 가능하다.

### 6. Code On Demand [Optional]
- Server 로 부터 스크립트를 받아서 Client 에서 실행한다.
- 반드시 충족할 필요는 없다.
<br><br><br><br>

# RESTful API
- REST 를 기반으로 서비스 API 를 구현한 것.
- Open API, 마이크로 서비스(하나의 큰 애플리케이션을 여러개로 쪼갠 아키텍처) 등을 제공하는 업체 대부분은 REST API 를 제공한다.
<br><br>

## REST API 장단점

### 장점
1. Open API 를 제공하기 쉽다.
2. 멀티플랫폼 지원 및 연동이 용이하다.
3. 원하는 타입으로 데이터를 주고 받을 수 있다.
4. 기존 웹 인프라(HTTP) 를 이용할 수 있다.
<br>

### 단점
1. 사용할 수 있는 HTTP Method 의 수가 적다.
2. 분산 환경에는 부적합하다.
3. HTTP 통신 모델에 대해서만 지원한다.