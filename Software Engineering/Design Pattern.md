# Design Pattern

``` 
1. 올바른 설계를 빠르게 만들 수 있도록 도와주는 설계 기법
2. 기존 환경 내에서 반복적으로 일어나는 문제들을 어떻게 풀어나갈 것인가에 대한 일종의 솔루션.
3. SW 재사용성, 호환성, 유지 보수성을 보장한다.
```
<br><br><br><br>

## 1. 싱글톤 패턴 (Singleton)
> 전역 변수를 사용하지 않고 **객체를 하나만 생성** 하도록 하며, 생성된 객체를 어디에서든지 참조할 수 있도록 하는 패턴.

<br>

#### 장점
- 한개의 객체만 생성함으로써, 메모리 낭비를 방지할 수 있다.
- **전역** 이므로, 다르클래스의 인스턴스들이 데이터를 공유하는 것이 가능하다.

#### 단점
- 싱글톤 인스턴스가 혼자 너무 많은 일을 하거나, 많은 데이터를 공유시키면 클래들 간의 결합도가 높아지게 된다.
- `Thread-safe` 하게 작성하여 멀티스레드에서 사용해도 문제가 없도록 해야한다.

#### 구현
```swift
class Info {
    static let shared = Info()
}
```
<br><br><br><br>

## 2. MVC 패턴 (Model - View - Controller)
> 하나의 애플리케이션, 프로젝트를 구성할 때 구성 요소를 Model, View, Controller 세가지의 역할로 구분한 패턴.

![](https://images.velog.io/images/sangwoo24/post/c80c3fd0-49e7-4736-a910-05fa0f57f4a6/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-03%20%EC%98%A4%ED%9B%84%207.18.03.png)

<br>

#### Model
- 컨트롤러가 호출할 때, 요청에 맞는 역할을 수행한다. 
- 비즈니스 로직을 구현하는 영역으로, 응용프로그램에서 데이터를 처리하는 부분이다. 
- DB 에 연결하고 데이터를 추출하거나, 저장, 삭제, 업데이트 등의 작업을 수행하며 Controller 와 View 에 전달한다.

#### View
- Controller 로 부터 받은 Model 의 결과값을 가지고 사용자에게 출력할 화면을 만드는 일을 한다.
- 만들어진 화면을 웹 브라우저에 전송하여 웹 브라우저가 출력하게 하는 것이다.
- 사용자와의 상호작용을 위한 인터페이스를 표시하는 영역이다.

#### Controller
- Client 의 요청을 받았을 때, 그 요청에 대해 실제 업무를 수행하는 Model 을 호출한다. 
- Client 가 보낸 데이터가 있다면, Model 에 전달하기 쉽게 데이터를 가공한다.
<br>

### Flow
1. 사용자의 Action 은 Controller 로 들어온다.
2. Controller 는 사용자의 Action 을 확인하고, Model 을 업데이트 한다.
3. Controller 는 Model 을 나타내줄 View 를 선택한다.
4. View 는 Model 을 이용하여 화면을 나타낸다.

<br>

### MVC 의 장점
- 유연하고 확장하기 쉽다.
- 디자이너와 개발자의 협업이 용이하다.
- 유지보수 비용을 절감할 수 있다.
<br>

### MVC 의 단점
- 설계시간이 오래 걸리고, 숙련된 개발자가 필요하다.
- Model 과 View 사이의 의존성이 높다. View 와 Model 의 높은 의존성은 애플리케이션이 커질수록, 복잡하고 유지보수가 어렵게 만들 수 있다.
<br><br><br><br><br><br>

## 3. MVVM 패턴 (Model - View - ViewModel)
> MVC 패턴에서 Controller 가 ViewModel 로 바뀐 디자인 패턴. ViewModel 은 UI 단에 위치한다.


![](https://images.velog.io/images/sangwoo24/post/affe77c2-48be-4503-972a-299eef414c02/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-03%20%EC%98%A4%ED%9B%84%207.23.50.png)
<br><br><br>

### ViewModel
- View 와 Model 사이의 인터페이스 역활을 한다.
- View 와는 Binding, Command 로 연결하고, Model 과는 데이터를 주고 받는 역할을 한다.
<br>

### Flow
1. View 에 요청이 들어오면 Command 를 통해 ViewModel 로 보낸다.
2. ViewModel 은 Model 에 데이터를 요청한다. 그리고 Model 은 데이터를 응답한다.
3. 이를 받은 ViewModel 은 데이터를 가공한다.
4. View 는 ViewModel 과의 Data Binding 을 통해 데이터를 자동으로 갱신한다.
<br><br>

### MVVM의 장점
- View 와 Model 사이의 의존성이 없다.
- Command 패턴과 Data Binding 을 사용하여 View와 ViewModel 사이의 의존성 또한 없앤 디자인패턴이다.
- 각각의 부분은 독립적이기 때문에, 모듈화 하여 개발할 수 있다.

### MVVM의 단점
- View Model 의 설계가 어렵다.
<br><br><br><br><br><br>

## 4. MVP 패턴 (Model - View - Presenter)

> model 과 view 는 MVC 와 동일하며, controller 대신 presenter 가 존재. 

<br>
<div align = center>
<img src = "https://user-images.githubusercontent.com/56511253/138864050-bdb458c0-10ec-458e-a24b-989a47c4e64c.png">
</div><br>

### Presenter
- view에서 요청한 정보로 model 을 가공하여 view에 전달해주는 부분.
<br><br>

### Flow

1. action 은 view 를 통해 들어옴
2. view 는 presenter 에게 데이터를 요청
3. presenter 는 model 에게 데이터를 요청 및 model 이 응답
4. presenter 는 view 에게 응답
5. view 는 presenter 에게 받은 데이터를 이용하여 화면을 나타냄

<br>
> view 와 model 의 의존성을 없앴지만, view 와 presenter 사이의 의존성이 강해짐.
