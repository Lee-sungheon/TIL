# 모던 자바스크립트 Deep Dive 정리

> '모던 자바스크립트 Deep Dive' 라는 서적을 공부하며 자바스트립트의 원리와 개념에 대한 이해를 높이고 900page라는 방대한 양을 나중에 다시 공부하기 쉽게 내가 몰랐던 점, 이해한 바를 정리한 문서입니다.



## 01. 프로그래밍

- 프로그래밍 
  - 컴퓨터에게 실행을 요구하는 일종의 커뮤니케이션
  - 기계에게 정확하고 상세하게 요구사항을 설명하는 작업 => 컴퓨팅 사고 필요
  - 요구사항의 집합을 분석해서 적절한 자료구조와 함수의 집합으로 변환한 후, 그 흐름을 제어하는 것
- 컴파일러<sup>compiler</sup>(혹은 인터프리터<sup>interpreter</sup>) : 사람이 이해할 수 있는 약속된 구문으로 구성된 `프로그래밍 언어`를 사용해 프로그램을 작성한 후, 그것을 컴퓨터가 이해할 수 있는 기계어로 변환하는 일종의 번역기



## 02. 자바스크립트

- 자바스크립트의 표준화
  - 자바스크립트의 파편화(크로스 브라우징 이슈 발생)를 방지하고 모든 브라우저에서 정상적으로 동작하는 표준화된 자바스크립트의 필요성이 대두
  - ECMAScript로 명명
  - ES5 (2009) 
    - HTML5와 함께 출현한 표준안
    - JSON, strict mode, 접근자 프로퍼티, 프로퍼티 어트리뷰트 제어, 향상된 배열 조작 기능
  - ES6 (2015)
    - 범용 프로그래밍 언어로서 갖춰야 할 기능들을 대거 도입
    - let/const, 클래스, 화살표 함수, 템플릿 리터럴, 디스트럭처링 할당, 스프레드 문법, rest 파라미터, 심벌, 프로미스, Map/Set, 이터러블, for...of, 제너레이터, Proxy, 모듈 import/export
  - ES11(2020)
    - 가장 최근 버전
    - 옵셔널 체인닝 연산자, BigInt, globalThis, null 병합 연산자, String.prototype.matchAll
- Ajax<sup>Asynchronous JavaScript and XML</sup>
  - 자바스크립트를 이용해 서버와 브라우저가 비동기 방식으로 데이터를 교환할수 있는 통신 기능
  - 웹페이지에서 변경할 필요가 없는 부분은 다시 렌더링하지 않고, 서버로부터 필요한 데이터만 전송받아 변경해야 하는 부분만 한정적으로 렌더링이 가능해짐
- V8 자바스크립트 엔진
  - 구글에서 등장한 빠르게 동작하는 자바스크립트 엔진
  - V8의 등장으로 과거 웹 서버에서 수행되는 로직들이 대거 클라이언트로 이동했고, 이는 웹 개발에서 프론트엔드 영역이 주목받는 계기로 작용
- Node.js
  - 2009년, 라이언 달이 발표한 구글 V8로 빌드된 자바스크립트 런타임 환경
  - 자바스크립트 엔진을 브라우저에서 독립시킨 자바스크립트 실행 환경
  - SSR에 주로 사용되며, 이에 필요한 모듈, 파일 시스템, HTTP 등 빌드인 API를 제공
  - 비동기 I/O를 지원하며 단일 스레드 이벤트 루프 기반으로 동작 
    - 요청 처리 성능이 좋음
    - 데이터를 실시간으로 처리하기 위해 I/O가 빈번하게 발생하는 SPA에 적합
    - CPU 사용률이 높은 애플리케이션에서는 권장 X
- 자바스크립트의 특징
  - 웹 브라우저에서 동작하는 유일한 프로그래밍 언어
  - 개발자가 별도의 컴파일 작업을 수행하지 않는 **인터프리터 언어**
  - 명령형, 함수형, 프로토타입 기반 객체지향 프로그래밍을 지원하는 **멀티 패러다임 프로그래밍 언어**
  - 클래스 기반 객체지향 언어보다 효율적이면서 강력한 **프로토타입 기반의 객체지향 언어**



## 03. 개발 환경과 실행 방법

- 실행 환경
  - 브라우저와 Node.js는 자바스크립트 엔진을 내장하고 있으므로 브라우저 환경 또는 Node.js 환경에서 실행 가능
  - 공통적으로 ECMAScript를 실핼할 수 있음
  - But, 브라우저와 Node.js는 용도가 다름
    - 브라우저는 클라이언트  사이드 Web API를 지원
    - Node.js는 Node.js 고유의 API를 지원
- 개발자 도구
  - Elements : 로딩된 웹페이지의 DOM과 CSS를 편집해서 렌더링된 뷰를 확인 가능
  - Console : 로딩된 웹페이지의 에러를 확인하거나 자바스크립트 소스코드에 작성한 console.log 메서드의 실행 결과를 확인할 수 있음
  - Sources : 로딩된 웹페이지의 자바스크립트 코드를 디버깅할 수 있음
  - Network : 로딩된 웹페이지에 관련된 네트워크 요청 정보와 성능을 확인할 수 있음
  - Application : 웹 스토리지, 세션, 쿠키를 확인하고 관리할 수 있음

- npm<sup>node package manager</sup> 
  - 자바스크립트 패키지 매니저
  - Node.js에서 사용할 수 있는 모듈들을 패키지화해서 모아둔 저장소 역할*
  - 패키지 설치 및 관리를 위한 CLI 를 제공
  - 자신이 작성한 패키지를 공개할 수도 있고, 필요한 패키지를 검색해 재사용할 수도 있음



## 04. 변수

- 변수<sup>variable</sup>
  - 하나의 값을 저장하기 위해 확보한 메모리 공간 자체 또는 그 메모리 공간을 식별하기 위해 붙인 이름
  - 값을 위치를 가리키는 상징적인 이름
  - 프로그래밍 언어의 컴파일러 또는 인터프리터에 의해 값이 저장된 메모리 공간의 주소로 치환되어 실행
  - **할당** : 변수에 값을 저장하는 것
  - **참조** : 변수에 저장된 값을 읽어들이는 것
  - 명확한 네이밍을 통해 코드를 이해하기 쉽게 만들고, 협업과 품질 향상에 도움을 줄 수 있음

- 식별자<sup>identifier</sup>

  - 식별자는 어떤 값을 구별해서 식별할 수 있는 고유한 이름
  - 식별자는 값이 아니라 메모리 주소를 기억하고 있음

- 변수 선언

  - 변수를 사용하기 위해 선언이 필요
  - `var`, `let`, `const` 키워드를 사용
  - 선언하지 않은 식별자에 접근하면 ReferenceError(참조 에러)가 발생

- 변수 호이스팅 

  - 변수 선언은 소스코드가 순차적으로 샐행되는 런타임 이전 단계에서 먼저 실행
  - 변수 선언문이 코드의 선두로 끌어올려진 것처럼 동작하는 자바스크립트 고유의 특징
  - 변수 선언은 소스코드가 순차적으로 실행되는 시점인 런타임 이전에 먼저 실행되지만 값의 할당은 소스코드가 순차적으로 실행되는 시점인 런타임에 실행

- 네이밍 컨벤션

  ```js
  // 카멜 케이스(camelCase)
  var firstName;
  
  // 스네이크 케이스(snake_case)
  var first_name;
  
  // 파스칼 케이스(PascalCase)
  var FisrtName;
  
  // 헝가리언 케이스(typeHungarianCase)
  var strFisrtName;
  var $elem = document.getElementById('myId');
  var observable$ = fromEvent(document, 'click');
  ```

  - 일반적으로 변수나 함수의 이름에는 **카멜 케이스** / 생성자 함수, 클래스의 이름에는 **파스칼 케이스**를 사용



## 05. 표현식과 문

- 값(value)
  - 식이 평가되어 생성된 결과
  - 변수는 **하나의 값**을 저장하기 위해 확보한 메모리 공간 자체 또는 그 메모리 공간을 식별하기 위해 붙인 이름
  - 변수에 할당되는 것은 값임 

- 리터럴(literal)
  - 사람이 이해할 수 있는 문자 또는 약속된 기호를 사용해 값을 생성하는 표기법
  - (아라비아 숫자, 알파벳, 한글) 또는 (' ', " ", [], {}, //)

- 표현식(expression)
  - 값으로 평가될 수 있는 문
  - 표현식이 평가되면 새로운 값을 생성하거나 기존 값을 참조
- 문(statement)
  - 프로그램을 구성하는 기본 단위이자 최소 실행 단위
  - 여러 토큰으로 구성
  - 토큰 : 문법적인 의미를 가지며, 문법적으로 더 이상 나눌 수 없는 코드의 기본 요소 (키워드, 식별자, 리터럴, 세미콜론, 마침표 등)
- 표현식인 문과 표현식이 아닌 문의 구별
  - 가장 간단하고 명료한 방법은 변수에 할당해 보는 것

- 세미콜론(;)
  - 문의 종료를 나타냄
  - 0개 이상의 문을 중괄호로 묶은 코드 블록(`{ ... }`) 뒤에는 세미콜론을 붙이지 않음
    - 코드 블록은 언제나 문의 종료를 의미하는 자체 종결성을 갖기 때문
  - 생략 가능 -> 자바스크립트 엔진의 세미콜론 자동 삽입 기능(ASI)
  - ESLint 및 TC39(ECMA 기술 위원회)에서 세미콜론 사용을 권장하는 분위기이므로 사용하는 것을 추천



## 06. 데이터 타입

- 데이터 타입

  - 원시 타입

    - 숫자 타입

      - 주로 산술 연산을 위해 사용
      - 배정밀도 64비터 부동소수점 형식
      - 모든 수를 실수로 처리, 정수로 표현하기 위한 데이터 타입이 별도로 존재하지 않음
      - Infinity(양의 무한대) / -Infinity(음의 무한대) / NaN(산술 연산 불가) 도 표현 가능

    - 문자열 타입

      - 텍스트 데이터를 나타내는데 사용
      - 0개 이상의 16비트 유니코드 문자(UTF-16)의 집합
      - ' ', " ", `` 으로 텍스트를 감쌈

    - 불리언 타입

      - 논리적 참, 거짓을 나타내는 `true` 와 `false`로 구성

    - undefined 타입

      - var 키워드로 선언한 변수는 암묵적으로 undefined로 초기화됨
      - 변수 선언에 의해 확보된 메모리 공간을 처음 할당이 이뤄질 때까지 빈 상태(대부분 쓰레기 값)로 내버려두지 않기 위함
      - 자바스크립트 엔진이 변수를 초기화할 때 사용하는 값이므로 개발자가 의도적으로 변수에 할당하는 것은 권장하지 않음 => `null`로 대체

    - null 타입

      - 변수에 값이 없다는 것을 의도적으로 명시할 때 사용
      - 함수가 유효한 값을 반환할 수 없는 경우 명시적으로 null을 반환하기도 함
        - ex) `document.querySelector`

    - 심벌 타입

      - ES6에서 추가된 7번째 타입
      - 외부에 노출되지 않으며, 다른 값과 절대 중복되지 않는 유일무이한 값

      ```js
      var key = Symbol('key');
      var obj = {};
      obj[key] = 'value';
      console.log(obj[key]); //value
      ```

  - 객체 타입

    - 자바스크립트는 객체 기반의 언어
    - 자바스크립트를 이루고 있는 거의 모든 것이 객체
    - 원시 타입 외에는 모두 객체 타입

- 템플릿 리터럴

  - 멀티라인 문자열

    - 이스케이프 시퀀스를 사용하지 않고도 줄바꿈이 허용되며, 모든 공백도 있는 그대로 적용됨

    ```js
    var template = `<ul>
    	<li><a href="#">Home</a></li>
    </ul>`;
    ```

  - 표현식 삽입

    - 표현식 삽입을 통해 간단히 문자열을 삽입할 수 있음
    - 문자열 연산자보다 가독성 좋고 간편하게 문자열을 조합할 수 있음

    ```js
    var first = "Lee";
    var last = "Sungheon";
    
    console.log(`My name is ${first} ${last}`);
    console.log(`1 + 2 = ${1 + 2}`);
    ```

- 데이터 타입이 필요한 이유

  - 값을 저장할 때 확보해야 하는 **메모리 공간의 크기**를 결정하기 위해
  - 값을 참조할 때 한 번에 읽어 들여야 할 **메모리 공간의 크기**를 결정하기 위해
  - 메모리에서 읽어 들인 **2진수를 어떻게 해석**할지 결정하기 위해

- 동적 타입 언어
  - 자바스크립트는 변수를 선언할 때 타입을 선언하지 않음
  - 어떠한 데이터 타입의 값이라도 자유롭게 할당할 수 있음
  - 자바스크립트의 변수는 선언이 아닌 할당에 의해 타입이 결정(타입 추론<sup>type inference</sup>)
  - 재할당에 의해 변수의 타입은 언제든지 동적으로 변할 수 있음 => 동적 타이핑
  - 동적 타입 언어는 유연성은 높지만 신뢰성이 떨어짐
  - 주의 사항
    - 변수는 꼭 필요한 경우에 한해 제한적으로 사용
    - 변수의 유효 범위(스코프)는 최대한 좁게 만들어 변수의 부작용 억제
    - 전역 변수는 최대한 사용하지 않도록 함
    - 변수보다는 상수(`const`) 를 사용해 값의 변경을 억제
    - 변수 이름은 변수의 목적이나 의미를 파악할 수 있도록 네이밍



> 컴퓨터가 이해하는 코드는 어떤 바보도 쓸 수 있다. 하지만 훌륭한 프로그래머는 사람이 이해할 수 있는 코드를 쓴다.
>
> -마틴 파울러, <리팩토링>의 저자



## 07. 연산자

- 산술 연산자

  - 피연산자를 대상으로 수학적 계산을 수행해 새로운 숫자 값을 만듬
  - 산술 연산이 불가능한 경우, `NaN`을 반환
  - 이항 산술 연산자
    - +, -, *, /, %
    - 2개의 피연산자를 산술 연산하여 숫자 값을 만듬
    - 모든 이항 산술 연산자는 피연산자의 값을 변경하는 부수 효과가 없음
  - 단항 산술 연산자
    - ++, --, +, -
    - 1개의 피연산자를 산술 연산하여 숫자 값을 만듬
    - `++`, `--` 연산자는 피연산자의 값을 변경하는 부수 효과가 있음
  - 문자열 연결 연산자
    - `+` 연산자는 피연산자 중 하나 이상이 문자열인 경우 문자열 연결 연산자로 동작

- 할당 연산자

  - +=, -=, *=, /=, %=
  - 좌항의 변수에 값을 할당하므로 변수 값이 변하는 부수 효과가 있음

- 비교 연산자

  - 좌항과 우항의 피연산자를 비교한 다음 그 결과를 불리언 값으로 반환
  - if 문이나 for 문과 같은 제어문의 조건식에서 주로 사용
  - 동등 비교 연산자(==)
    - 좌항과 우항의 피연산자를 비교할 때 먼저 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
    - 예측하기 어려운 결과를 만들어내므로 사용하지 않는 편이 좋음

  - 일치 비교 연산자(===)

    - 좌항과 우항의 피연산자가 타입도 같고 값도 같은 경우에 한하여 true를 반환

    - `NaN`은 자신과 일치하지 않는 유일한 값이므로 숫자가 `NaN`인지 조사하려면 빌트인 함수 `isNaN`를 사용해야함

      ```js
      NaN === NaN; // -> false
      isNaN(NaN); // -> true
      isNaN(10); // -> false
      isNaN(1 + undefined) // -> true
      Object.is(NaN, NaN); // -> true
      ```

    - 양의 0과 음의 0을 비교하면 true를 반환

      ```js
      0 === -0; // -> true
      Object.is(-0, +0); // -> false
      0 == -0; // -> true
      ```

  - 대소 관계 비교 연산자

    - 피연산자의 크기를 비교하여 불리언 값을 반환

- 삼항 조건 연산자

  - `조건식 ? 조건식이 true일 때 반환할 값 : 조건식이 false일 때 반환할 값`

  - 삼항 조건 연산자 표현식은 값으로 평가할 수 있는 표현식인 문
  - 조건에 따라 어떤 값을 결정해야 한다면 **삼항 조건 연산자**
  - 조건에 따라 수행해야 할 문이 하나가 아니라 여러개면 **if ...else**

- 논리 연산자

  - 우항과 좌항의 피연산자를 논리 연산함
  - ||, &&, !

- 쉼표 연산자

  - 왼쪽 피연산자부터 차례대로 피연산자를 평가하고 마지막 피연산자의 평가가 끝나면 마지막 피연산자의 평과 결과를 반환

    ```js
    var x, y, z;
    x = 1, y = 2, z = 3; // 3
    ```

- 그룹 연산자

  - 연산자 우선순위가 가장 높음
  - 그룹 연산자를 사용하면 연산자의 우선 순위를 조절할 수 있음

- typeof 연산자

  - 피연산자의 데이터 타입을 문자열로 반환
  - string, number, boolean, undefined, symbol, object, function 중 하나를 반환
  - null 은 object로 반환

- 지수 연산자

  - 좌항의 피연산자를 밑으로, 우항의 피연산자를 지수로 거듭 제곱하여 숫자 값을 반환
  - ES7에서 도입

- 연산자 우선순위

  | 우선순위 | 연산자                                    |
  | :------: | :---------------------------------------- |
  |    1     | ()                                        |
  |    2     | new(매개변수 존재), ., [], (), ?.         |
  |    3     | new(매개변수 미존재)                      |
  |    4     | x++, x--                                  |
  |    5     | !x, +x, -x, ++x, --x, typeof, delete      |
  |    6     | **(이항 연산자 중에서 우선순위 가장 높음) |
  |    7     | *, /, %                                   |
  |    8     | +, -                                      |
  |    9     | <, <=, >, >=, in, instanceof              |
  |    10    | ==, !=, ===, !==                          |
  |    11    | ?? (null 병합 연산자)                     |
  |    12    | &&                                        |
  |    13    | \|\|                                      |
  |    14    | ? ... : ...                               |
  |    15    | 할당 연산자(=, +=, -=, ....)              |
  |    16    | ,                                         |



## 08. 제어문

- break 문

  - 중첩된 for 문의 내부 for 문에서 외부 for 문을 탈출하기 위해 레이블 문을 사용

    ```js
    outer: for (var i = 0; i < 3; i++) {
    	for (var j = 0; j < 3; j++) {
            if (i + j === 3) break outer;
        }
    }
    ```



## 09. 타입 변환과 단축 평가

- Falsey 값

  - false
  - undefined
  - null
  - 0, -0
  - NaN
  - ''

- 명시적 타입 변환

  - 문자열 타입으로 변환

    1. String 생성자 함수를 new 연산자 없이 호출하는 방법	

       ```js
       String(1);
       String(NaN);
       String(Infinity);
       String(true);
       ```

    2. Object.prototype.toString 메서드를 사용하는 방법

       ```js
       (1).toString();
       (NaN).toString();
       (true).toString();
       ```

    3. 문자열 연결 연산자를 이용하는 방법

       ```js
       1 + '';
       true + '';
       ```

  - 숫자 타입으로 변환

    1. Number 생성자 함수를 new 연산자 없이 호출하는 방법

       ```js
       Number('0');
       Number('-1');
       Number(true);
       ```

    2. parseInt, parseFloat 함수를 사용하는 방법 (문자열만 가능)

       ```js
       parseInt('0');
       parseFloat('10.53');
       ```

    3. `+` 단항 산술 연산자를 이용하는 방법

       ```js
       +'0';
       +'10.53';
       +true;
       ```

    4. `*` 산술 연산자를 이용하는 방법

       ```js
       '0'*1;
       '10.53'*1;
       true*1;
       ```

  - 불리언 타입으로 변환

    1. Boolean 생성자 함수를 new 연산자 없이 호출하는 방법

       ```js
       Boolean('x');
       Boolean(NaN);
       ```

    2. ! 부정 논리 연산자를 두 번 사용하는 방법

       ```js
       !!'x';
       !!NaN;
       ```

- 옵셔널 체이닝 연산자

  - ES11 에서 도입

  - `?.` 는 좌항의 피연산자가 null 또는 undefined인 경우 undefined를 반환하고, 그렇지 않으면 우항의 프로퍼티 참조를 이어감

    ```js
    var elem = null;
    var value = elem?.value;
    console.log(value); // undefined
    ```

- null 병합 연산자

  - ES11 에서 도입

  - `??` 는 좌항의 피연산자가 null 또는 undefined인 경우 우항의 피연산자를 반환하고, 그렇지 않으면 좌항의 피연산자를 반환

  - 변수에 기본값을 설정할 때 유용

    ```js
    var foo = null ?? 'default string';
    console.log(foo); // "defalut string"
    ```



## 10. 객체 리터럴

- 객체
  - 자바스크립트는 객체 기반의 프로그래밍 언어
  - 자바스크립트를 구성하는 거의 모든 것이 객체
  - 객체는 0개 이상의 프로퍼티로 구성된 집합이며, 프로퍼티는 키와 값으로 구성됨
    - 프로퍼티: 객체의 상태를 나타내는 값(data)
  - 함수로 이루어진 프로퍼티는 `메서드` 라고 명칭함
    - 메서드: 프로퍼티(상태 데이터)를 참고하고 조작할 수 있는 동작(behavior)
- 객체 생성법
  - 객체 리터럴
    - 객체를 생성하는 가장 일반적이고 간단한 방법
    - `{ ... }`  내에 0개 이상의 프로퍼티를 정의
    - 객체 리터럴의 중괄호는 코드 블록을 의미하는 것이 아니므로 뒤에 세미콜론`(;)` 을 붙임 
  - Object 생성자 함수
  - 생성자 함수
  - Object.create 메서드
  - 클래스(ES6)

- 프로퍼티

  - **객체는 프로퍼티의 집합이며, 키와 값으로 구성됨**

  - 프로퍼티 키: 빈 문자열을 포함하는 모든 문자열 또는 심벌 값

  - 프로퍼티 값: 자바스크립트에서 사용할 수 있는 모든 값

  - 식별자 네이밍 규칙을 따르면 따옴표가 생략 가능하나, 따르지 않는 이름에는 반드시 따옴표를 사용해야함

    ```js
    var person = {
      firstName: 'Ung-mo',
      'last-name': 'Lee'
    };
    ```

  - 프로퍼티 키에 문자열이나 심벌 값 외의 값을 사용하면 암묵적 타입 변환을 통해 문자열이 됨
  - 이미 존재하는 프로퍼티 키를 중복 선언하면 나중에 선언한 프로퍼티가 먼저 선언한 프로퍼티를 덮어씀

- 프로퍼티 접근

  - 마침표 프로퍼티 접근 연산자(.)를 사용하는 **마침표 표기법**
  - 대괄호 프로퍼티 접근 연산자([...])를 사용하는 **대괄호 표기법**
    - 대괄호 프로퍼티 접근 연산자 내부에 지정하는 프로퍼티 키는 반드시 따옴표로 감싼 문자열
    - 객체에 존재하지 않는 프로퍼티에 접근하면 undefined 반환

- 프로퍼티 축약 표현

  - ES6 에서는 프로퍼티 값으로 변수를 사용하는 경우 변수 이름과 프로퍼티 키가 동일한 이름일 때 프로퍼티 키를 생략할 수 있음

  - 이 때 프로퍼티 키는 변수 이름으로 자동 생성

    ```js
    // ES5
    var x = 1, y = 2;
    var obj = {
      x: x,
      y: y
    };
    
    // ES6
    let x = 1, y = 2;
    const obj = { x, y };
    console.log(obj); // { x: 1, y: 2 }
    ```

- 계산된 프로퍼티 이름

  - ES6에서는 객체 리터럴 내부에서 계산된 프로퍼티 이름으로 프로퍼티 키를 동적 생성할 수 있음

    ```js
    // ES5
    var prefix = 'prop';
    var i = 0;
    var obj = {};
    obj[prefix + '-' + ++i] = i;
    obj[prefix + '-' + ++i] = i;
    obj[prefix + '-' + ++i] = i;
    
    // ES6
    const prefix = 'prop';
    let i = 0;
    
    const obj = {
      [`${prefix}-${++i}`]: i,
      [`${prefix}-${++i}`]: i,
      [`${prefix}-${++i}`]: i
    };
    
    console.log(obj); // { pro-1: 1, prop-2: 2, prop-3: 3 }
    ```

- 메서드 축약 표현

  - ES6에서는 메서드를 정의할 때 function 키워드를 생략한 축약 표현을 사용할 수 있음

    ```js
    // ES5
    var obj = {
      name: 'Lee',
      sayHi: function() {
        console.log('Hi' + this.name);
      }
    };
    
    // ES6
    const obj = {
      name: 'Lee',
      sayHi() {
        console.log('HI' + this.name);
      }
    };
    ```

    

## 11. 원시 값과 객체의 비교

- 원시 값
  - 원시 타입의 값, 즉 변경 불가능한 값<sup>immutable value</sup>
  - 변경 불가능하다는 것은 변수가 아니라 값에 대한 진술
  - 값에 의한 전달
    - 변수에는 값이 전달되는 것이 아니라 메모리 주소가 전달되기 때문
    - "값에 의한 전달"도 사실은 값을 전달하는 것이 아니라 메모리 주소를 전달
    - 단, 메모리 주소를 통해 메모리 공간에 접근하면 값을 참조할 수 있음
    - 두 변수의 원시 값은 서로 다른 메모리 공간에 저장된 별개의 값이 되어 어느 한쪽에서 재할당을 통해 값을 변경하더라도 서로 간섭할 수 없음
- 객체
  - 객체는 원시 값과 같이 확보해야 할 메모리 공간의 크기를 사전에 정해 둘 수 없음
  - 프로퍼티 키를 인덱스로 사용하는 해시 테이블 자료 구조를 사용
  - 자바스크립트는 클래스 없이 객체를 생성할 수 있으며 객체가 생성된 이후라도 동적으로 프로퍼티와 메서드를 추가할 수 있음 => 사용하긴 편리하지만 성능 면에서는 이론적으로 클래스 기반 객체지향 프로그래밍 언어의 객체보다 생성과 프로퍼티 접근에 비용이 더 많이 드는 비효율적인 방식
  - V8 엔진은 **히든 클래스** 방식을 사용해 C++ 객체 정도의 성능을 보장함
    - [참고 자료](https://meetup.toast.com/posts/78)
  - 객체 타입의 값은 변경 가능한 값<sup>mutable value</sup>
  - 객체를 할당한 변수는 재할당 없이 객체를 직접 변경할 수 있음
  - 여러 개의 식별자가 하나의 값을 객체를 공유할 수 있다는 단점이 있음 (얕은 복사, 깊은 복사)



## 12. 함수

- 함수란?
  - 일련의 과정을 문으로 구현하고 코드 블록으로 감싸사 하나의 실행단위로 정의한 것
  - 함수 내부로 입력을 전달받는 변수를 **매개변수**<sup>parameter</sup>, 입력을 **인수**<sup>argument</sup>, 출력을 **반환값**<sup>return value</sup> 라고 함
  - 함수는 코드의 중복을 억제하고 재사용성을 높이는 **유지보수의 편의성**을 높이고 실수를 줄여 **코드의 신뢰성**을 높이는 효과가 있음
  - 적절한 함수 이름은 함수 내부의 코드를 이해하지 않고도 함수의 역할을 파악하게 돕기 때문에 **코드의 가독성**을 향상시킴
  - 자바스크립트의 함수는 **객체 타입**의 값
  
- 함수 선언문

  - 함수 선언문은 함수 리터럴과 형태가 동일

    ```js
    function add(x, y) {
      return x + y;
    }
    ```

  - 함수 리터럴은 함수  이름을 생략할 수 있으나 함수 선언문은 **함수 이름을 생략할 수 없음**

  - 함수 선언문은 표현식이 아닌 문임

  - 자바 스크립트 엔진은 함수 선언문을 함수 표현식으로 변환해 함수 객체를 생성함

    ```js
    // 함수 선언문
    // 기명 함수 리터럴을 단독으로 사용하면 함수 선언문으로 해석
    function foo() { console.log('foo'); }
    
    // 함수 리터럴을 피연산자로 사용하면 함수 리터럴 표현식으로 해석
    (function bar() { console.log('bar'); });
    bar(); // ReferenceError: bar is not defined
    
    // 함수 표현식
    var foo = function foo() { console.log('foo'); }
    ```

- 함수 표현식

  - 자바스크립트의 함수는 일급 객체 => 함수는 값처럼 변수에 할당할 수 있고 프로퍼티 값이 될 수 도 있으며 배열의 요소가 될 수도 있음

  - 함수 표현식은 표현식인 문임

    ```js
    var add = function foo (x, y) {
      return x + y;
    };
    
    console.log(add(2, 5)); // 7
    console.log(foo(2, 5)); // ReferenceError: foo is not defined
    ```

- 화살표 함수

  - ES6 에서 도입됐으며, function 키워드 대신 화살표(=>)를 사용해 좀 더 간략한 방법으로 함수를 선언

    ```js
    const add = (x, y) => x + y;
    console.log(add(2, 5)); // 7
    ```

  - 기존의 함수보다 표현만 간략한 것이 아니라 내부 동작 또한 간략화 되어 있음

    - 생성자 함수로 사용할 수 없음
    - 기존 함수와 `this` 바인딩 방식이 다름
    - `prototype` 프로퍼티가 없음
    - `arguments` 객체를 생성하지 않음

- 함수 호이스팅<sup>function hoisting</sup>

  - 함수 선언문으로 정의한 함수와 함수 표현식으로 정의한 함수의 생성 시점이 다름

  - 함수 선언문이 코드의 선두로 끌어 올려진 것처럼 동작하는 자바스크립트 고유의 특징을 **함수 호이스팅**이라고 함

    ```js
    console.dir(add); // f add(x, y)
    console.dir(sub); // undefined
    
    console.log(add(2, 5)); // 7
    console.log(sub(2, 5)); // TypeError: sub is not a function
    
    function add(x, y) {
      return x + y;
    }
    
    var sub = function (x, y) {
      return x - y;
    };
    ```

  - 함수 호이스팅과 변수 호이스팅은 차이가 있음

    - 변수 할당문의 값은 할당문이 실행되는 시점, 즉 런타임에 평가되므로 함수 표현식의 리터럴도 할당문이 실행되는 시점에 평가되어 함수 객체가 됨
    - 함수 표현식으로 함수를 정의하면 함수 호이스팅이 발생하는 것이 아니라 변수 호이스팅이 발생함

- 인수 확인

  - 자바스크립트 함수는 매개변수와 인수의 개수가 일치하는지 확인하지 않는다.
  - 자바스크립트는 동접 타입 언어이다. 따라서 자바스트립트 함수는 매개변수의 타입을 사전에 지정할 수 없다.

- 매개변수의 최대 개수
  - 매개변수의 최대 개수에 대해 명시적으로 제한하고 있지 않음
  - 매개변수는 순서에 의미가 있으므로 이상적인 매개변수는 0개이며 적을수록 좋음
  - 이상적인 함수는 한 가지 일만 해야 하며 가급적 작게 만들어야 함
  - 매개변수는 최대 3개 이상을 넘기지 않는 것을 권장
  - 그 이상의 매개변수가 필요하다면 객체를 인수로 전달하는 것이 유리

- 즉시 실행 함수 (IIFE, Immediately Invoked Function Expression)

  - 함수 정의와 동시에 즉시 호출되는 함수

  - 즉시 싱행 함수는 단 한번만 호출되며 다시 호출할 수 없음

    ```js
    // 즉시 실행 함수
    (function() {
      var a = 3;
      var b = 5;
      return a * b;
    }());
    
    // 일반 함수처럼 값을 반환할 수 있음
    var res = (function() {
      var a = 3;
      var b = 5;
      return a * b;
    }());
    console.log(res); // 15
    
    // 인수 전달도 가능
    res = (function(a, b) {
      return a * b;
    }(3, 5));
    console.log(res); // 15
    ```

-  콜백 함수

  - 콜백 함수 : 함수의 매개변수를 통해 다른 함수의 내부로 전달되는 함수
  - 고차 함수<Sup>Higher-Order Function, HOF</Sup> : 매개변수를 통해 함수의 외부에서 콜백 함수를 전달받은 함수 (map, setTimeout 등)
  - 고차 함수는 콜백 함수를 자신의 일부분으로 합성
  - 고차 함수는 매개변수를 통해 전달받은 콜백 함수의 호출 시점을 결정해서 호출
  - 즉, 콜백 함수는 고차 함수에 의해 호출되며 이때 고차 함수는 필요에 따라 콜백 함수에 인수를 전달 할 수 있음 

- 순수 함수와 비순수 함수

  - 순수 함수 : 부수 효과가 없는 함수(외부 상태에 의존하지도 않고 변경하지도 않음)

  - 비순수 함수 : 부수 효과가 있는 함수(외부 상태에 의존하거나 외부 상태를 변경)

    ```js
    // 순수 함수
    var count = 0;
    function increase(n) {
      return ++n;
    }
    
    count = increase(count);
    
    // 비순수 함수
    var count = 0;
    function increase() {
      return ++count;
    }
    
    increse();
    ```

  - 함수의 외부 상태를 변경하면 상태 변화를 추적하기 어려워짐

  - 함수형 프로그래밍은 순수 함수를 통해 부수 효과를 최대한 억제해 오류를 피하고 프로그램의 안정성을 높임

  - 자바스크립트는 멀티 패러다임 언어이므로 객체지향 프로그래밍뿐만 아니라 함수형 프로그래밍을 적극 활용하고 있음



## 13. 스코프

- 스코프란?

  - 식별자가 유효한 범위
  - 모든 식별자(변수 이름, 함수 이름, 클래스 이름 등)는 자신이 선언된 위치에 의해 다른 코드가 식별자 자신을 참조할 수 있는 유효 범위가 결정
  - 전역 스코프
    - 전역에 변수를 선언하면 전역 스코프를 갖는 전역 변수가 됨
    - 전역 변수는 어디든지 참조 가능
  - 지역 스코프
    - 함수 몸체 내부를 말하는 지역이 만든 스코프
    - 지역에 변수를 선언하면 지역 스코프를 갖는 지역 변수가 됨
    - 지역 변수는 자신의 지역 스코프와 하위 지역 스코프에서 유효함 => **스코프 체인**에 의한 변수 검색

- 함수 레벨 스코프

  - 블록 레벨 스코프 : 함수 몸체만이 아니라 모든 코드 블록(if, for, while, try/catch 등)이 지역 스코프를 만듬
  - 함수 레벨 스코프 : var 키워드로 선언된 변수는 오로지 함수의 코드 블록(함수 몸체)만을 지역 스코프로 인정
  - let, const 키워드는 블록 레벨 스코프를 지원

- 렉시컬 스코프

  - 동적 스코프 : **함수를 어디서 호출** 했는지에 따라 함수의 상위 스코프를 결정

  - 렉시컬 스코프(= 정적 스코프) : **함수를 어디서 정의** 했는지에 따라 상위 스코프를 결정

  - 자바스크립트는 **렉시컬 스코프**를 따르므로 함수의 상위 스코프는 언제나 자신의 정의된 스코프

    ```js
    var x = 1;
    
    function foo() {
      var x = 10;
      bar();
    }
    
    function bar() {
      console.log(x);
    }
    
    foo(); // 1 => 동적 스코프였다면 10
    bar(); // 1
    ```



## 14. 전역 변수의 문제점

- 변수의 생명 주기

  - 지역 변수
    - 지역 변수의 생명 주기는 함수의 생명 주기와 일치
    - 호이스팅은 스코프를 단위로 동작
  - 전역 변수
    - var 키워드로 선언한 전역 변수의 생명 주기는 전역 객체의 생명 주기와 일치
    - 브라우저 환경에서 전역 객체는 window이므로 브라우저 환경에서 var 키워드로 선언한 전역 변수는 전역 객체 window의 프로퍼티
    - 전역 객체 window는 웹페이지를 닫기 전까지 유효
  - 전역 객체
    - 전역 객체는 코드가 싱핼되기 이전 단계에 자바스크립트 엔진에 의해 어떤 객체보다도 먼저 생성되는 특수한 객체
    - 클라이언트 사이드 환경(브라우저)에서는 `window`, 서버 사이드 환경(Node.js)에서는 `global` 객체를 의미

- 전역 변수의 문제점

  - 암묵적 결합
    - 모든 코드가 전역 변수를 참조하고 변경할 수 있는 **암묵적 결합**<sup>implicit coupling</sup> 을 허용
    - 변수의 유효 범위가 크면 클수록 코드의 가독성은 나빠지고 의도치 않게 상태가 변경될 수 있는 위험성도 높아짐
  - 긴 생명 주기
    - 전역 변수는 생명 주기가 김
    - 메모리 리소스도 오랜 기간 소비하고 전역 변수의 상태를 변경할 수 있는 시간도 길고 기회도 많음
    - 변수 이름이 중복될 가능성이 있어 의도치 않은 재할당이 이루어짐
  - 스코프 체인 상에서 종점에 존재
    - 변수를 검색할 때 전역 변수가 가장 마지막에 검색됨
    - 즉, 전역 변수의 검색 속도가 가장 느림
  - 네임스페이스 오염
    - 자바스크립트의 가장 큰 문제점 중 하나는 파일이 분리되어 있다 해도 하나의 전역 스코프를 공유함
    - 다르파일 내에서 동일한 이름으로 명명된 전역 변수나 전역 함수가 같은 스코프 내에 존재할 경우 예상치 못한 결과를 가져올 수 있음

- 전역 변수의 사용을 억제하는 방법

  - 전역 변수를 반드시 사용해야 할 이유가 없다면 지역 변수를 사용해야 함

  - 변수의 스코프는 좁을수록 좋음

  - 즉시 실행 함수

    - 모든 코드를 즉시 실행 함수로 감싸면 모든 변수는 즉시 실행 함수의 지역 변수가 됨
    - 이 방법을 사용하면 전역 변수를 생성하지 않으므로 라이브러리 등에 자주 사용됨

  - 네임스페이스 객체

    -  전역에 네임스페이스 역할을 담당할 객체를 생성하고 전역 변수처럼 사용하고 싶은 변수를 프로퍼티로 추가하는 방법

      ```js
      var MYAPP = {};
      MYAPP.name = 'Lee';
      console.log(MYAPP.name); // Lee
      ```

    - 식별자 충돌을 방지하는 효과는 있으나 네임스페이스 객체 자체가 전역 변수에 할당되므로 그다지 유용하지 않음

  - 모듈 패턴

    - 모듈 패턴은 클래스를 모방해서 관련이 있는 변수와 함수를 모아 즉시 실행 함수로 감싸 하나의 모듈을 만듬

    - 클로저를 기반으로 작동 -> 전역 변수의 억제는 물론 캡슐화까지 구현 가능

    - 자바스크립트는 접근 제한자를 제공하지 않으므로 정보 은닉을 구현하기 위해 사용

      ```js
      var Counter = (function () {
        // private 변수
        var num = 0;
        // 외부로 공개할 데이터나 메서드를 프로퍼티로 추가한 객체를 반환
        return {
          increase() {
      			return ++num;
          },
          decrease() {
            return --num;
          }
        }
      }());
      
      // private 변수는 외부로 노출되지 않음
      console.log(Counter.num); //undefined
      
      console.log(Counter.increase()); //1
      console.log(Counter.increase()); //2
      console.log(Counter.decrease()); //1
      console.log(Counter.decrease()); //0
      ```

  - ES6 모듈

    - ES6 모듈은 파일 자체의 독자적인 모듈 스코프를 제공

    - 모듈 내에서 var 키워드로 선언한 변수는 더는 전역 변수가 아니며 window 객체의 프로퍼티도 아님

    - 모던 브라우저(Chrome 61, FF 60, SF 10.1, Edge 16 이상)에서는 ES6 모듈을 사용할 수 있음

      ```html
      <script type="module" src="lib.mjs"></script>
      <script type="module" src="app.mjs"></script>
      ```

    - ES6 모듈 기능을 사용하더라도 트랜스파일링이나 번들링이 필요하기 때문에 아직까지는 브라우저의 ES6 모듈 기능보다는 Webpack 등의 모듈 번들러를 사용하는 것이 일반적임



## 15. let, const 키워드와 블록 레벨 스코프

- `var` 키워드 선언 변수의 문제점

  1. 변수 중복 선언 허용

     ```js
     var x = 1;
     var x = 100;
     console.log(x); // 100
     ```

  2. 함수 레벨 스코프

     - `var` 키워드로 선언한 변수는 오로지 함수의 코드 블록만을 지역 스코프로 인정

     ```js
     var i = 1;
     for (var i = 0; i < 5; i++) {
       console.log(i); // 0 1 2 3 4
     }
     console.log(i); // 5
     ```

  3. 변수 호이스팅
     - `var` 키워드로 변수를 선언하면 변수 호이스팅에 의해 변수 선언문이 스코프의 선두로 끌어올려진 것처럼 동작
     - 단, 할당문 이전에 변수를 참조하면 언제나 `undefined` 를 반환

- `let` 키워드

  - 변수 중복 선언 금지

    ```js
    let bar = 123;
    let bar = 456; // SyntaxError: Identifier 'bar' has already been declared
    ```

  - 블록 레벨 스코프

    ```js
    let foo = 1;
    {
      let foo = 2;
      let bar = 3;
    }
    console.log(foo); // 1
    console.log(bar); // ReferenceError: bar is not defined
    ```

  - 변수 호이스팅

    - 변수 호이스팅이 발생하지만, 발생하지 않는 것처럼 동작

    ```js
    console.log(foo); // ReferenceError: foo is not defined
    let foo;
    ```

    - `let` 키워드로 선언한 변수는 "선언 단계"와 "초기화 단계"가 분리되어 진행
    - 스코프의 시작 지점부터 초기화 시작 지점까지 변수를 참조할 수 없는 구간을 **일시적 사각지대** 라고 부름

    ```js
    // 런타임 이전에 선언 단계 실행
    // 초기화 이전의 일시적 사각지대에서는 변수 참조 불가
    console.log(foo); // ReferenceError: foo is not defined
    
    let foo;	// 변수 선언문에서 초기화 단계가 실행
    console.log(foo);	// undefined
    
    foo = 1;	// 할당문에 할당 단계가 실행
    console.log(foo);	// 1
    ```

    ```js
    let foo = 1;	// 전역 변수
    {
      console.log(foo);	// ReferenceError: Cannot access 'foo' before initialization
      let foo = 2;	// 지역 변수
    }
    ```

  - 전역 객체와 let

    - `var` 키워드로 선언한 전역 변수와 전역 함수, 선언하지 않은 변수에 값을 할당한 암묵적 전역은 객체 window의 프로퍼티가 됨
    - `let` 키워드로 선언한 전역 변수는 전역 객체의 프로퍼티가 아님
    - `let` 전역 변수는 보이지 않는 개념적인 블록 내에 존재

    ```js
    var x = 1;
    y = 1;
    function foo() {}
    console.log(window.x, x); // 1 1
    console.log(window.y, y); // 1 1
    console.log(window.foo, foo); // f foo() {} f foo() {}
    
    let z = 1;
    console.log(window.z); // undefined
    console.log(z); // 1
    ```

- `const` 키워드

  - 보통 상수를 선언하기 위해 사용

  - `let` 과 특징이 거의 비슷

  - 선언과 초기화

    - `const` 키워드로 선언한 변수는 반드시 선언과 동시에 초기화해야 함

    ```js
    const foo = 1;
    const foo; // SyntaxError: Missing initializer in const declaration
    ```

  - 재할당 금지

    - `const` 키워드로 선언한 변수는 재할당이 금지됨

    ```js
    const foo = 1;
    foo = 2;	// TypeError: Assignment to constant variable
    ```

  - 상수로 사용

    - 상수의 이름은 스네이크 케이스`(_)`로 표현하는 것이 일반적
    - 상태 유지와 가독성, 유지보수가 용이해짐

  - `const` 키워드와 객체

    - `const` 키워드로 선언된 변수에 객체를 할당한 경우 값을 변경할 수 있음
    - `const` 키워드는 재할당을 금지할 뿐 "불변"을 의미하는 것은 아님

- `var` vs `let` vs `const`

  - ES6 를 사용한다면 `var` 키워드는 사용하지 않기
  - 재할당이 필요한 경우에 한정히 `let` 키워드를 사용. 이 때 변수의 스코프는 최대한 좁게 만들기
  - 변경이 발생하지 않고 읽기 전용으로 사용하는(재할당이 필요 없는 상수) 원시 값과 객체에는 `const` 사용. `const` 키워드는 재할당을 금지하므로 `var`, `let` 보다 안전



## 16. 프로퍼티 어트리뷰트

- 객체 변경 방지
  - 자바스크립트는 객체의 변경을 방지하는 다양한 메서드를 제공함
  - 객체 확장 금지
    - `Object.preventExtensions`
    - 객체의 확장이 금지 (값 갱신, 삭제, 어트리뷰트 재정의 가능)
    - 즉, 프로퍼티 추가가 금지
  - 객체 밀봉
    - 밀봉된 객체는 읽기와 쓰기만 가능 (값 갱신만 가능)
  - 객체 동결
    - 동결된 객체는 읽기만 가능
  - 객체 변경 방지 메서드들은 얕은 변경 방지로 직속 프로퍼티만 변경이 방지되고 중첩 객체까지는 영향을 주지 못함



## 17. 생성자 함수에 의한 객체 생성

- 생성자 함수를 정의하고 `new` 연산자와 함께 호출하면 해당 함수는 생성자 함수로 동작

- `new` 연산자 없이 호출하면 해당 함수는 일반 함수로 호출

- 일반 객체는 호출할 수 없지만 함수는 호출할 수 있다

- constructor 은 함수 선언문과 함수 표현식으로 정의된 함수

- non-constructo 은 화살표 함수와 메서드 축약 표현으로 정의된 함수

- `new.target`

  - 생성자 함수가 new 연산자 없이 호출되는 것을 방지하기 위함

  - new 연산자와 함께 생성자 함수로서 호출되면 함수 내부의 new.target은 자기 자신을 가리킴

  - new 연산자 없이 일반 함수로서 호출된 함수 내부의 new.target은 `undefined`

  - IE에선 지원하지 않으므로 스코프 세이프 생성자 패턴을 사용

    ```js
    function Circle(radius){
      if (!new.target) {
        return new Circle(radius);
      }
      this.radius = radius;
      this.getDiameter = function () {
        return 2 * this.radius;
      };
    }
    
    // new 연산자 없이 생성자 함수를 호출하여도 new.target을 통해 생성자 함수로서 호출됨
    const circle = Circle(5);
    ```

  - 대부분의 빌트인 생성자 함수(Object, String, Number, Boolean, Function, Array, Date, RegExp, Promise 등) 는 new 연산자와 함께 호출되었는지를 확인 후 적절한 값을 반환



## 18. 함수와 일급 객체

- 일급 객체

  - 무명의 리터럴로 생성할 수 있음. 즉, 런타임에 생성이 가능
  - 변수나 자료구조(객체, 배열 등)에 저장할 수 있음
  - 함수의 매개변수에 전달할 수 있음
  - 함수의 반환값으로 사용할 수 있음

- 함수 객체의 프로퍼티

  - arguments 프로퍼티

    - arguments 객체는 매개변수를 확정할 수 없는 **가변 인자 함수**를 구현할 때 유용

    - Rest 파라미터(ES6)

      ```js
      // arguments
      function sum() {
        const array = Array.prototype.slice.call(arguments);
        return array.reduce(function (pre, cur) {
          return pre + cur;
        }, 0);
      }
      
      console.log(sum(1, 2));
      
      // Rest 파라미터 도입
      function sum(...args) {
        return args.reduce((pre, cur) => pre + cur, 0);
      }
      
      console.log(sum(1, 2));
      ```

  - length 프로퍼티

    - 함수를 정의할 때 선언한 매개변수의 개수를 가리킴
    - arguments 객체의 length 프로퍼티는 인자의 개수를 가르키고, 함수 객체의 length 프로퍼티는 매개변수의 개수를 가르킴

  - name 프로퍼티

    - 함수 객체의 name 프로퍼티는 함수 이름을 나타냄

    - ES6 이후로 정식 표준이 됨

      ```js
      var nameFunc = function foo() {};
      console.log(nameFunc.name);	// foo;
      
      var anonymousFunc = function() {};
      // ES5: name 프로퍼티는 빈 문자열을 값으로 가짐
      // ES6: name 프로퍼티는 함수 객체를 가리키는 변수 이름을 값으로 가짐
      console.log(anoymousFunc.name);	// anonymousFunc
      
      function bar() {}
      console.log(bar.name);	// bar
      ```

  - `__proto__` 접근자 프로퍼티

    - [[Prototype]] 내부 슬롯이 가리키는 프로토타입 객체에 접근하기 위해 사용하는 접근자 프로퍼티

    - 내부 슬롯에는 직접 접근할 수 없고 접근자 프로퍼티를 통해 간접적으로 접근이 가능

    - `hasOwnProperty` 메서드 : 인수로 전달받은 프로퍼티 키가 객체 고유의 프로퍼티 키인 경우에만 true를 반환하고 상속받은 프로토타입의 프로퍼티 키인 경우 false를 반환

      ```js
      const obj = { a: 1 };
      
      // 객체 리터럴 방식으로 생성한 객체의 프로토타입 객체는 Object.prototype
      console.log(obj.__proto__ === Object.prototype);	// true
      
      // hasOwnProperty 메서드는 Object.prototype의 메서드
      console.log(obj.hasOwnProperty('a'));	// true
      console.log(obj.hasOwnProperty('__proto__'));	// false
      ```

  - Prototype 프로퍼티

    - 생성자 함수로 호출할 수 없는 함수 객체, 즉 constructor만이 소유하는 프로퍼티

      ```js
      // 함수 객체는 prototype 프로퍼티를 소유
      (function () {}).hasOwnProperty('prototype');	// -> true
      
      // 일반 객체는 prototype 프로퍼티를 소유하지 않음
      ({}).hasOwnProperty('prototype');	// -> false
      ```



## 19. 프로토타입

- 객체지향 프로그래밍
  - 객체의 집합으로 프로그래밍을 표현하려는 프로그래밍 패러다임
  - 추상화 : 다양한 속성 중에서 프로그램에 필요한 속성만 간추려 내어 표현하는 것
  - 객체
    - 속성을 통해 여러 개의 값을 하나의 단위로 구성한 복합적인 자료 구조
    - 상태 데이터(프로퍼티)와 동작(메서드)을 하나의 논리적인 단위로 묶은 복합적인 자료 구조
  - 프로퍼티 : 객체의 상태를 나타내는 데이터
  - 메서드 : 상태 데이터를 조작할 수 있는 동작

- 상속과 프로토타입

  - 상속은 객체지향 프로그래밍의 핵심 개념

  - 자바스크립트는 **프로토타입을 기반으로 상속을 구현**하여 불필요한 중복을 제거

    ```js
    function Circle(radius) {
      this.radius = radius;
      this.getArea = function () {
        return Math.PI * this.radius ** 2;
      };
    }
    
    const circle1 = new Circle(1);
    const circle2 = new Circle(2);
    
    console.log (circle1.getArea === circle2.getArea)	// false
    
    function Circle(radius) {
      this.radius = radius;
    }
    // 프로토타입은 Circle 생성자 함수의 prototype 프로퍼티에 바인딩되어 있음
    Circle.prototype.getArea = function () {
      return Math.PI * this.radius ** 2;
    };
    
    const circle1 = new Circle(1);
    const circle2 = new Circle(2);
    
    console.log(circle1.getArea === circle2.getArea)	// true
    ```

- 프로토타입 객체

  - 객체 간 상속을 구현하기 위해 사용됨
  - 모든 객체는 하나의 프로토타입을 갖음
  - 프로토타입은 생성자 함수가 생성되는 시점에 더불어 생성됨

- 프로토타입 체인

  - 자바스크립트는 객체의 프로퍼티(메서드 포함)에 접근하려고 할 때 해당 객체에 접근하려는 프로퍼티가 없다면 [[Prototype]] 내부 슬롯의 참조를 따라 자신의 부모 역할을 하는 프로토타입의 프로퍼티를 순차적으로 검색함
  - 프로토타입 체인은 자바스크립트가 객체지향 프로그래밍의 상속을 구현하는 메커니즘
  - `Object.prototye` 을 프로토타입 체인의 종점이라고 하며, [[Prototype]] 내부 슬롯의 값은 null 임

- `instanceof` 연산자

  ```js
  객체 instanceof 생성자 함수
  ```

  - 이항 연산자로서 좌변에 객체를 가리키는 식별자, 우변에 생성자 함수를 가리키는 식별자를 피연산자로 받음
    - 우변의 피연산자가함수가 아닌 경우 TypeError가 발생
    - 우변의 생성자 함수의 prototype에 바인딩된 객체가 좌변의 객체의 프로토타입 체인 상에 존재하면 true로 평가되고, 그렇지 않은 경우에는 false로 평가됨

- 프로퍼티 존재 확인

  - `in` 연산자

    - 객체 내에 특정 프로퍼티가 존재하는지 여부를 확인함

    - 상속받은 모든 프로토타입의 프로퍼티도 확인하므로 주의가 필요

      ```js
      key in object
      ```

  - `Object.prototype.hasOwnProperty` 메서드

    - 인수로 전달 받은 프로퍼티 키가 객체 고유의 프로퍼티 키인 경우만 true를 반환
    - 상속받은 프로토타입의 프로퍼티 키인 경우 false를 반환

- 프로퍼티 열거

  - `for...in` 문

    ```js
    for (변수선언문 in 객체) { ... }
    ```

    - 객체의 프로퍼티 개수만큼 순회하며 for...in 문의 변수 선언문에서 선언한 변수에 프로퍼티 키를 할당
    - `in` 연산자처럼 순회 대상 객체의 프로퍼티 뿐만 아니라 상속받은 프로토타입의 프로퍼티까지 열거
    - 즉, for...in 문은 객체의 프로토타입 체인 상에 존재하는 모든 프로토타입의 프로퍼티 중에서 프로퍼티 어트리뷰트 [[Enumerable]]의 값이 true인 프로퍼티를 순회하며 열거함
    - 프로퍼티를 열거할 때 순서를 보장하지 않으므로 주의가 필요(대부분의 모던 브라우저는 순서를 보장하고 있음)
    - **배열에는 for 문이나 for...of 문 또는 forEach 메서드를 사용하기를 권장**
      - 배열도 객체이므로 프로퍼티와 상속받은 프로퍼티가 포함될 수 있음

  - `Object.keys/values/enries` 메서드

    - `for...in` 문은 객체 자신의 고유 프로퍼티뿐 아니라 상속받은 프로퍼티도 열거하므로 `Object.prototype.hasOwnProperty` 메서드를 사용하여 객체 자신의 프로퍼티인지 확인하는 추가 처리가 필요함
    - 객체 자신의 고유 프로퍼티만 열거하기 위해서는 `object.keys/values/entries` 메서드를 사용하는 것을 권장



## 20. strict mode

- strict mode

  - 자바스크립트 언어의 문법을 좀 더 엄격히 적용하여 오류를 발생시킬 가능성이 높거나 자바스크립트 엔진의 최적화 작업에 문제를 일으킬 수 있는 코드에 대해 명시적인 에러를 발생시킴
  - `'use strict';` 를 전역의 선두 또는 함수 몸체의 선두에 추가하여 적용
  - 전역에 strict mode를 적용하는 것은 피하는 것이 좋음 => 외부 서드파티 라이브러리를 사용하는 경우 non-strict mode와 혼용되어 오류를 발생시킬 수 있음
  - 함수단위로 strict mode를 적용하는 것도 좋지 않음 => 즉시 실행 함수로 감싼 스크립트 단위로 적용하는 것을 추천

- strict mode가 밸싱시키는 에러

  - 암묵적 전역

    - 선언하지 않은 변수를 참조하면 ReferenceError가 발생

      ```js
      (function () {
        'use strict';
        
        x = 1;
        console.log(x);	// ReferenceError: x is not defined
      }());
      ```

  - 변수, 함수, 매개변수의 삭제

    - delete 연산자로 변수, 함수, 매개변수를 삭제하면 SyntaxError가 발생

      ```js
      (function () {
        'use strict';
        
        var x = 1;
        delete x;	// SyntaxError: Delete of an unqualified identifier in strict mode.
        
        function foo(a) {
          delete a;	// SyntaxError: Delete of an unqualified identifier in strict mode.
        }
        delete foo;	// SyntaxError: Delete of an unqualified identifier in strict mode.
      }());
      ```

  - 매개변수 이름의 중복

    - 중복된 매개변수 이름을 사용하면 SyntaxError가 발생

      ```js
      (function () {
        'use strict';
        
        // SyntaxError: Duplicate parameter name not allowed in this context
        function foo(x, x) {
          return x + x;
        }
        console.log(foo(1, 2));
      }());
      ```

  - with 문의 사용

    - With 문은 성능과 가독성이 나빠지는 문제가 있으므로 SyntaxError가 발생

      ```js
      (function () {
        'use strict';
        
        // SyntaxError: Strict mode code may not include a with statment
        with({ x: 1 }) {
          console.log(x);
        }
      }());
      ```

- strict mode 적용에 의한 변화

  - 일반 함수의 this

    - strict mode에서 함수를 일반 함수로 호출하면 this에 undefined가 바인딩 됨

    - 에러는 발생하지 않음

      ```js
      (function () {
        'use strict';
        
        function foo() {
          console.log(this);	// undefined
        }
        foo();
        
        function Foo() {
          console.log(this);	// Foo
        }
        new Foo();
      }());
      ```

  - arguments 객체

    - strict mode에서는 매개변수에 전달된 인수를 재할당하여 변경해도 arguments 객체에 반영되지 않음

      ```js
      (function (a) {
        'use strict';
        a = 2;
        console.log(arguments);	// { 0: 1, length: 1 }
      }(1));
      ```




## 21. 빌트인 객체

- 표준 빌트인 객체

  - ECMAScript 사양에 정의된 객체, 애플리케이션 전역의 공통 기능을 제공

  - 자바스크립트 실행 환경과 관계없이 언제나 사용할 수 있음

  - 전역 객체의 프로퍼티로서 제공되므로 별도의 선언 없이 전역 변수처럼 언제나 참조할 수 있음

  - 자바스크립트는 Object, String, Number, Symbol, RegExp, Array, Function, Promise, JSON, Error 등 40여 개의 표준 빌트인 객체를 제공

  - Math, Reflect, JSON을 제외한 표준 빌트인 객체는 모두 인스턴스를 생성할 수 있는 생성자 함수 객체

    ```js
    const strObj = new String('Lee');	// String {"Lee"}
    console.log(typeof strObj);	// object
    ```

  - 생성자 함수인 표준 빌트인 객체가 생성한 인스턴스의 프로토타입은 표준 빌트인 객체의 prototype 프로퍼티에 바인딩된 객체

- 원시값과 래퍼 객체

  - 문자열, 숫자, 불리언 값에 대해 객체처럼 접근하면 생성되는 임시 객체를 **래퍼 객체**라고 함

    ```js
    const str = 'hello';
    
    // 원시 타입인 문자열이 프로퍼티와 메서드를 갖고 있는 객체처럼 동작
    console.log(str.length);	// 5
    console.log(str.toUpperCase());	// HELLO
    console.log(typeof str);	// string
    ```

- 전역 객체

  - 코드가 실행되기 이전 단계에 자바스크립트 엔진에 의해 어떤 객체보다 먼저 생성되는 특수한 객체
  - 어떤 객체에도 속하지 않은 최사위 객체
  - 브라우저 환경에서는 window, Node.js에서는 global이 전역 객체를 가리킴
  - `globalThis`
    - ES11에서 도입
    - 브라우저 환경과 Node.js 환경에서 전역 객체를 가리키던 다양한 식별자를 통일한 식별자



## 22. this

- this 키워드

  - 메서드가 자신이 속한 객체의 프로퍼티를 참조하려면 먼저 **자신이 속한 객체를 가리키는 식별자를 참조할 수 있어야 함**

  - this는 자신이 속한 객체 또는 자신이 생성할 인스턴스를 가리키는 자기 참조 변수

  - this를 통해 자신이 속한 객체 또는 자신이 생성할 인스턴스의 프로퍼티나 메서드를 참조할 수 있음

  - this 바인딩은 함수 호출 방식에 의해 동적으로 결정됨

    - 바인딩이란 식별자와 값을 연결하는 과정을 의미
    - this 바인딩은 this와 this가 가리킬 객체를 바인딩하는 것

    ```js
    console.log(this)	// window
    
    function square(number) {
      // 일반 함수 내부에서 this는 전역 객체 window를 가리킨다.
      console.log(this)
      return number * number;
    }
    
    square(2);	// window
    
    const person = {
      name: 'Lee',
      getName() {
        // 메서드 내부에서 this는 메서드를 호출한 객체를 가르킨다.
        console.log(this);	// {name: 'Lee', getName: f}
        return this.name;
      }
    };
    
    function Person(name) {
      this.name = name;
      // 생성자 함수 내부에서 this는 생성자 함수가 생성할 인스턴스를 가리킨다. 
      console.log(this);
    }
    
    const me = new Person('Lee');	// Person {name: "Lee"}
    ```

- 함수 호출 방식과 this 바인딩

  - 일반 함수 호출

    - 기본적으로 일반 함수 호출 시  this에는 전역 객체가 바인딩

    - 일반 함수로 호출된 모든 함수(중첩 함수, 콜백 함수 포함) 내부의 this에는 전역 객체가 바인딩

    - 메서드 내부의 중첩 함수나 콜백 함수의 this 바인딩을 메서드의 this 바인딩과 일치시키기 위한 방법

      ```js
      var value = 1;
      
      // this 바인딩 that 변수에 할당
      const obj = {
        value: 100,
        foo() {
          // this 바인딩(obj)을 변수 that에 할당
          const that = this;
          
          // 콜백 함수 내에서 this 대신 that을 참조
          setTimeout(function () {
            console.log(that.value);	// 100
          }, 100);
        }
      };
      
      // Function.prototype.bind 메서드 사용
      const obj2 = {
        value: 100,
        foo() {
          // 콜백 함수에 명시적으로 this 할당
          setTimeout(function () {
            console.log(that.value);	// 100
          }.bind(this), 100);
        }
      };
      
      // 화살표 함수 사용
      const obj3 = {
        value: 100,
        foo() {
          setTimeout(() => console.log(this.value), 100);
        }
      };
      ```

  - 메서드 호출

    - 메서드 내부의 this에는 메서드를 호출한 객체가 바인딩

    - 메서드 내부의 this는 메서드를 소유한 객체가 아닌 메서드를 호출한 객체에 바인딩 되므로 주의 필요

      ```js
      function Person(name) {
        this.name = name;
      }
      
      Person.prototype.getName = function () {
        return this.name;
      };
      
      const me = new Person('Lee');
      
      // getName 메서드를 호출한 객체는 me
      console.log(me.getName());	// Lee
      
      Person.prototype.name = 'Kim';
      
      // getName 메서드를 호출한 객체는 Person.prototype
      console.log(Person.protoype.getName());	// Kim
      ```

  - 생성자 함수 호출

    - 생성자 함수 내부의 this에는 생성자 함수가 (미래에) 생성할 인스턴스가 바인딩

      ```js
      function Circle(radius) {
      	// 생성자 함수 내부의 this는 생성자 함수가 생성할 인스턴스를 가리킴
        this.radius = radius;
        this.getDiameter = function () {
          return 2 * this.redius;
        };
      }
      
      const circle1 = new Circle(5);
      const circle2 = new Circle(10);
      
      console.log(circle1.getDiameter());	// 10
      console.log(circle2.getDiameter());	// 20
      
      // new 연산자와 함께 호출하지 않으면 생성자 함수로 동작하지 않음. 즉, 일반적 함수의 호출
      const circle3 = Circle(15);
      
      // 일반 함수로 호출된 Circle에는 반환문이 없으므로 암묵적으로 undifined를 반환
      console.log(circle3);	// undifined
      
      // 일반 함수로 호출된 Circle 내부의 this는 전역 객체를 가리킴
      console.log(radius);	// 15
      ```

  - Function.prototype.apply/call/bind 메서드에 의한 간접 호출

    - Function.prototype.apply/call/bind 메서드에 첫번째 인수로 전달된 객체가 바인딩

    - apply와 call 메서드는 this로 사용할 객체와 인수 리스트를 인수로 전달받아 함수를 호출

      ```js
      function getThisBinding() {
        return this;
      }
      
      // this로 사용할 객체
      const thisArg = { a: 1 };
      
      console.log(getThisBinding());	// window
      
      // getThisBinding 함수를 호출하면서 인수로 전달할 객체를 getThisBinding 함수의 this에 바인딩
      // apply 메서드는 호출할 함수의 인수를 배열로 묶어 전달
      console.log(getThisBinding.apply(thisArg, [1, 2, 3]));	// {a: 1}
      
      // call 메서드는 호출할 함수의 인수를 쉼표로 구분한 리스트 형식으로 전달
      console.log(getThisBinding.call(thisArg, 1, 2, 3));	// {a: 1}
      ```

    - apply와 call 메서드의 본질적인 기능은 함수를 호출하는 것이며, 차이는 인자를 전달하는 방법이 다름

    - bind 메서드는 메서드의  this와 메서드 내부 중첩 함수 또는 콜백 함수의 this가 불일치하는 문제를 해결하기 위해 유용하게 사용됨



## 23. 실행 컨텍스트

- 소스코드의 타입
  - ECMAScript 사양은 소스코드를 4가지 타입으로 구분하여 실행 컨텍스트를 생성
    - 전역 코드
    - 함수 코드
    - eval 코드
    - 모듈 코드
- 실행 컨텍스트의 역할
  - 소스코드를 실행하는 데 필요한 환경을 제공하고 코드의 실행 결과를 실제로 관리하는 영역
  - 식별자(변수, 함수, 클래스 등의 이름)를 등록하고 관리하는 스코프와 코드 실행 순서 관리를 구현한 내부 메커니즘으로, 모든 코드는 실행 컨텍스트를 통해 실행되고 관리됨
  - 식별자와 스코프는 실행 컨텍스트의 **렉시컬 환경**으로 관리하고, 코드 실행 순서는 **실행 컨텍스트 스택**으로 관리
- 실행 컨텍스트 스택
  - 실행 컨텍스트 스택은 코드의 실행 순서를 관리함
  - 실행 컨텍스트 스택의 최상위에 존재하는 실행 컨텍스트는 언제나 현재 실행 중인 코드의 실행 컨텍스트
  - 실행 컨텍스트 스택의 최상위에 존재하는 실행 컨텍스트를 **실행 중인 실행 컨텍스트**라 부름
- 렉시컬 환경
  - 식별자와 식별자에 바인딩 된 값, 상위 스코프에 대한 참조를 기록하는 자료구조로 실행 컨텍스트를 구성하는 컴포넌트
  - 렉시컬 환경은 키와 값을 갖는 객체 형태의 스코프(전역, 함수, 블록 스코프)를 생성하여 식별자를 키로 등록하고 식별자에 바인딩된 값을 관리
  - 렉시컬 환경은 **환경 레코드**와 **외부 렉시컬 환경에 대한 참조** 컴포넌트로 구성 됨



## 24. 클로저

- 렉시컬 스코프 (정적 스코프)

  - 자바스크립트 엔진은 함수를 어디서 호출했는지가 아니라 함수를 어디에 정의했는지에 따라 상위 스코프를 결정
  - 렉시컬 환경의 "외부 렉시컬 환경에 대한 참조"에 저장할 참조값, 즉 상위 스코프에 대한 참조는 함수 정의가 평가되는 시점에 함수가 정의된 환경(위치)에 의해 결정됨

- 함수 객체의 내부 슬롯 [[Environment]]

  - 함수는 자신의 내부 슬롯 [[Enivironment]]에 자신이 정의된 환경, 즉 상위 스코프의 참조를 저장
  - 함수 객체의 내부 슬롯 [[Environment]]에 저장된 현재 실행 중인 컨텍스트의 렉시컬 환경의 참조가 바로 상위 스코프
  - 자신이 호출되었을 때 생성될 함수 렉시컬 환경의 "외부 렉시컬 환경에 대한 참조"에 저장될 참조값
  - 함수 객체는 내부 슬롯 [[Environment]]에 저장한 렉시컬 환경의 참조, 즉 상위 스코프를 자신이 존재하는 한 기억함

- 클로저와 렉시컬 환경

  - 외부 함수보다 중첩 함수가 더 오래 유지되는 경우 중첩 함수는 이미 생명 주기가 종료한 외부 함수의 변수를 참조할 수 있다. 이러한 중첩 함수를 **클로저**라고 부름
  - 클로저는 중첩 함수가 상위 스코프의 식별자를 참조하고 있고 중첩 함수가 외부 함수보다 더 오래 유지되는 경우에 한정하는 것이 일반적
  - 클로저에 의해 참조되는 상위 스코프의 변수를 **자유 변수**라고 부름
  - 클로저는 상위 스코프의 식별자 중에서 기억해야 할 식별자만 기억

- 클로저의 활용

  - 클로저는 상태를 안전하게 변경하고 유지하기 위해 사용

  - 상태가 의도치 않게 변경되지 않도록 상태를 안전하게 은닉하고 특정 함수에게만 상태 변경을 허용하기 위해 사용

    ```js
    // 함수를 반환하는 고차함수
    // 이 함수는 카운트 상태를 유지하기 위한 자유 변수 counter를 기억하는 클로저를 반환
    const counter = (function () {
      // 카운트 상태를 유지하기 위한 자유 변수
      let counter = 0;
      // 함수를 인수로 전달받는 클로저를 반환
      return function (predicate) {
        // 인수로 전달받은 보조 함수에 상태 변경을 위임
        counter = predicate(counter);
        return counter;
      };
    }());
    
    // 보조 함수
    function increase(n) {
      return ++n;
    }
    
    // 보조 함수
    function decrease(n) {
      return --n;
    }
    
    console.log(counter(increase));	// 1
    console.log(counter(increase));	// 2
    console.log(counter(decrease));	// 1
    console.log(counter(decrease));	// 0
    ```

  



## 44. REST API

- REST API

  - REpresentational State Transfer
  - REST의 기본 원칙을 성실히 지킨 서비스 디자인을 'Restful'이라고 표현
  - REST는 HTTP를 기반으로 클라이언트가 서버의 리소스에 접근하는 방식을 규정한 아키텍처
  - REST API는 REST 기반으로 서비스 API를 구현한 것을 의미

- REST API의 구성

  ![스크린샷 2022-07-24 오후 8.07.38](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-07-24 오후 8.07.38.png)

- REST API 설계 원칙

  - URI는 리소스를 표현해야 함

    - URI는 리소스를 표현하는 데 중점을 두어야 함
    - 리소스를 식별할 수 있는 이름은 동사보다는 명사를 사용
    - 이름에 get 같은 행위에 대한 표현이 들어가서는 안 됨

  - 리소스에 대한 행위는 HTTP 요청 메서드로 표현

    - HTTP 요청 메서드는 클라이언트가 서버에게 요청의 종류와 목적(리소스에 대한 행위)을 알리는 방법
    - 주로 5가지 요청 메서드(GET, POST, PUT, PATCH, DELETE 등)를 사용하여 CRUD를 구현
    - 리소스에 대한 행위는 HTTP 요청 메서드를 통해 표현하며 URI에 표현하지 않는다.

    ![스크린샷 2022-07-24 오후 8.11.04](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-07-24 오후 8.11.04.png)



## 47. 에러 처리

- 에러 처리의 필요성

  - 에러가 발생하지 않는 코드를 작성하는 것은 불가능함
  - 발생한 에러에 대해 대처하지 않고 방치하면 프로그램은 강제 종료됨
  - 우리가 작성한 코드는 언제나 에러나 예외적인 상황이 발생할 수 있다는 것을 전제하고 이에 대응하는 코드를 작성하는 것이 중요

  

- try ... catch ... finally 문

  - try ... catch ... finally 문으로 에러를 처리하면 프로그램이 강제 종료되지 않음

  ```ts
  try {
    /// 실행할 코드(에러가 발생할 가능성이 있는 코드)
  } catch (err) {
    // try 코드 블럭에서 에러가 발생하면 이 코드 블록의 코드가 실행
    // err에는 try 코드 블록에서 발생한 Error 객체가 전달
  } finally {
    // 에러 발생과 상관없이 반드시 한 번 실행
  	// 생략 가능
  }
  ```

  

- Error 객체

  - Error 생성자 함수는 에러 객체를 생성

    ```js
    const error = new Error('invalid');
    const error = new ReferenceError('ref error');
    ```

  - Error 생성자 함수가 생성한 에러 객체는 stack 프로퍼티와 message 프로퍼티를 가짐

    - stack 프로퍼티는 에러를 발생시킨 콜스택의 호출 정보를 나타내는 문자열이며 디버깅으로 사용
    - message 프로퍼티는 Error 생성자 함수에 인수로 전달한 에러 메시지

  - 자바스크립트는 Error 생성자 함수를 포함해 7가지의 에러 객체를 생성할 수 있는 Error 생성자 함수를 제공함

    | 생성자 함수    | 인스턴스                                                     |
    | :------------- | :----------------------------------------------------------- |
    | Error          | 일반적 에러 객체                                             |
    | SyntaxError    | 자바스크립트 문법에 맞지 않는 문을 해석할 때 발생하는 에러 객체 |
    | ReferenceError | 참조할 수 없는 식별자를 참조했을 때 발생하는 에러 객체       |
    | TypeError      | 피연산자 또는 인수의 데이터 타입이 유효하지 않을 때 발생하는 에러 객체 |
    | RangeError     | 숫자값의 허용 범위를 벗어났을 때 발생하는 에러 객체          |
    | URIError       | encodeURI 또는 decodeURI 함수에 부적절한 인수를 전달했을 때 발생하는 에러 객체 |
    | EvalError      | eval 함수에서 발생하는 에러 객체                             |



- throw 문

  - Error 생성자 함수로 에러 객체를 생성한다고 에러가 발생하는 것은 아님

  - 에러를 발생시키려면 try 코드 블록에서 throw 문으로 에러 객체를 던져야 함

    ```ts
    throw 표현식;
    ```

  - throw 문의 표현식은 어떤 값이라도 상관없지만 일반적으로 에러 객체를 지정

    - 에러를 던지면 catch문의 에러 변수가 생성되고 던져진 에러 객체가 할당됨

    - 그리고 catch 블록이 실행되기 시작

      ```ts
      try {
        // 에러 객체를 던지면 catch 코드 블록이 실행되기 시작
        throw new Error('something wrong');
      } catch (error) {
        console.log(error);
      }
      ```



- 에러의 전파

  - 에러는 호출자<sup>caller</sup> 방향으로 전파됨

  - 즉, 콜 스택의 아래 방향(실행 중인 실행 컨텍스트가 푸시되기 직전에 푸시된 실행 컨텍스트 방향)으로 전파

    ```ts
    const foo = () => {
      throw Error('foo error');  // 4
    };
    
    const bar = () => {
      foo();  // 3
    };
    
    const baz = () => {
      bar();  // 2
    };
    
    try {
      baz();  // 1
    } catch (err) {
      console.log(err);
    }
    ```

    - 1에서 baz 함수를 호출하면 2에서 bar 함수가 호출되고 3에서 foo 함수가 호출되고 foo 함수는 4에서 에러를 throw 함
    - 이때 foo 함수가 throw한 에러는 다음과 같이 호출자에게 전파되어 전역에서 캐치됨

    ![스크린샷 2022-07-17 오후 6.42.20](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-07-17 오후 6.42.20.png)

  - - throw된 에러를 캐치하지 않으면 호출자 방향으로 전파됨
    - 이 때 throw 된 에러를 캐치하여 적절히 대응한다면 프로그램을 강제 종료시키지 않고 코드의 실행 흐름을 복구할 수 있음
    - throw된 에러를 어디에서도 캐치하지 않으면 프로그램은 강제 종료

  - 비동기 함수인 setTimeout 이나 프로미스 후속 처리 메서드의 콜백 함수는 호출자가 없음

    - setTimeout이나 프로미스 후속 처리 메서드의 콜백 함수는 태스크 큐나 마이크로태스크 큐에 일시 저장되었다가 콜 스택이 비면 이벤트 루프에 의해 콜  스택으로 푸시되어 실행됨
    - 이때 콜 스택에 푸시된 콜백 함수의 실행 컨텍스트는 콜 스택의 가장 하부에 존재하게 됨
    - 따라서 에러를 전파할 호출자가 존재하지 않음



## 48. 모듈

- 모듈의 일반적 의미

  - 모듈 

    - 애플리케이션을 구성하는 개별적 요소로서 재사용 가능한 코드 조각
    - 일반적으로 모듈은 기능을 기준으로 파일 단위로 분리함
    - 모듈이 성립하려면 모듈은 자신만의 **파일 스코프(모듈 스코프)**를 가질 수 있어야 함
    - 자신만의 파일 스코프를 갖는 모듈의 모든 자산은 캡슐화되어 다른 모듈에서 접근할 수 없다.
    - 즉, 모듈은 개별적 존재로서 애플리케이션과 분리되어 존재
    - 코드의 단위를 명확히 분리하여 어플리케이션을 구성할 수 있고, 재사용성이 좋아서 개발 효율성과 유지보수성을 높일 수 있음

  - export

    - 모듈은 공개가 필요한 자산에 한정하여 명시적으로 선택정 공개가 가능

  - import

    - 모듈 사용자 : 공개된 모듈의 자산을 사용하는 모듈
    - 모듈 사용자는 모듈이 공개<sup>export</sup>한 자산 중 일부 또는 전체를 선택해 자신의 스코프 내로 불러들여 재사용할 수 있음

    ![스크린샷 2022-07-23 오후 8.37.28](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-07-23 오후 8.37.28.png)

- 자바스크립트와 모듈
  - 자바스크립트는 모듈이 성립하기 위해 필요한 파일 스코프와 import, export를 지원하지 않음
  - 자바스크립트 파일을 여러 개의 파일로 분리하여 script 태그로 로드해도 분리된 자바스크립트 파일들은 결국 하나의 자바스크립트 파일 내에 있는 것처럼 동작함
  - 즉, 모든 자바스크립트 파일은 하나의 전역을 공유
  - 자바스크립트의 모듈 시스템을 해결하기 위한 방법
    - CommonJS
    - AMD<sup>Asynchronous Module Definition</sup>
    - 브라우저 환경에서 모듈을 사용하기 위해서는 CommonJS 또는 AMD를 구현한 모듈 로더 라이브러리를 사용해야 함
  - Node.js는 모듈 시스템의 사실상 표준인 CommonJS를 채택, 독자적 진화를 거쳐 ECMAScript 표준 사양은 아니지만 모듈 시스템을 지원함



- ES6 모듈(ESM)

  - ES6에서는 클라이언스 사이드 자바스크립트에서도 동작하는 모듈 기능을 추가함(IE를 제외한 대부분의 브라우저에서 지원)

  - 사용법

    - script 태그에 type="module" 어트리뷰트를 추가하면 로드된 자바스크립트 파일은 모듈로서 동작함

    - 일반적인 자바스크립트 파일이 아닌 ESM임을 명확히 하기 위해 ESM의 파일 확장자는 `mjs`를 사용할 것을 권장

      ```ts
      <script type="module" src="app.mjs"></script>
      ```

  - 모듈 스코프

    - ESM은 독자적인 모듈 스코프를 가짐
    - ESM이 아닌 일반적인 자바스크트립트 파일은 script 태그로 분리해서 로드해도 독자적인 모듈 스코프를 갖지 않음

  - export 키워드

    - 모듈 내부에서 선언한 식별자를 외부에 공개하여 다른 모듈들이 재사용할 수 있게 하려면 export 키워드를 사용
    - export 키워드는 선언문 앞에 사용
    - 변수, 함수 클래스 등 모든 식별자를 export 할 수 있음
    - 선언문 앞에 매번 export 키워드를 붙이는 것이 번거롭다면 export할 대상을 하나의 객체로 구성하여 한 번에 export 할 수도 있음

  - import 키워드

    - 다른 모듈에서 공개한 식별자를 자신의 모듈 스코프 내부에 로드하려면 import 키워드를 사용

    - 다른 모듈이 export한 식별자 이름으로 import해야 하며 ESM의 경우 파일 확장자를 생략할 수 없음

    - 모듈이 export한 식별자 이름을 일일이 지정하지 않고 하나의 이름으로 한 번에 import 할 수도 있음

      - 이 때, import 되는 식별자는 as 뒤에 지정한 이름의 객체에 프로퍼티로 할당됨

        ```ts
        import * as lib from './lib.mjs';
        
        console.log(lib.pi);
        console.log(lib.square(10));
        ```

    - 모듈이 export 한 식별자 이름을 변경하여 import 할 수도 있음

      ```ts
      import { pi as PI, square as sq } from './lib.mjs';
      
      console.log(PI);
      console.log(sq(10));
      ```

    - 모듈에서 하나의 값만 export 한다면 default 키워드를 사용할 수 있음

      - default 키워드는 기본적으로 이름 없이 하나의 값을 export 함

      - default 키워드를 사용하는 경우 var, let, const 키워드는 사용할 수 없음

      - default 키워드와 함께 export한 모듈은 {} 없이 임의의 이름으로 import 함

        ```ts
        // lib.mjs
        export default x => x * x;
        
        // lib2.mjs
        export default const foo = () => {};
        // => SyntaxError: Unexpected token 'const'
        // export default () => {};
        
        // app.mjs
        import square from './lib.mjs';
        
        console.log(square(3));
        ```

        

