# Byte Ordering 
```
데이터가 저장되는 순서를 의미한다. Byte Ordering 방식에는 빅 엔디안(Big Endian)과 리틀 엔디안(Little Andian)이 있다.
```
![](https://images.velog.io/images/sangwoo24/post/9b85bbda-b8e3-4077-bec2-7aaa32024472/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-15%20%EC%98%A4%ED%9B%84%207.06.20.png)
<br><br><br>

### Big Endian
- `MSB` 가 가장 낮은 주소에 위치하는 저장 방식
- 네트워크에서 데이터를 전송할 때 주로 사용된다.
- 가장 낮은 주소에 `MSB` 가 저장되므로, Offset = 0 인 Byte 를 보면 양수/음수를 파악할 수 있다.
<br><br>

### Little Endian
- `MSB` 가 가장 높은 주소에 위치하는 저장 방식
- 마이크로프로세서 에서 주로 사용된다.
- 가장 낮은 주소에 부호값이 아닌 데이터가 먼저 오기 때문에, 바로 연산을 할 수 있다.
