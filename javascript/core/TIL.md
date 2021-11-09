# 코어 자바스크립트 정리

### 01. 데이터 타입

- 데이터 타입의 종류 ?

  - 기본형<sup>primitive type</sup> : number, string, boolean, null, undefined, Symbol

    - 심볼 타입

      - ES6에서 추가된 7번째 타입
      - 외부에 노출되지 않으며, 다른 값과 절대 중복되지 않는 유일무이한 값

      ```js
      var key = Symbol('key');
      var obj = {};
      obj[key] = 'value';
      console.log(obj[key]); //value
      ```

    - 값이 담긴 주솟값을 바로 복제

    - 불변성<sup>immutability</sup>

  - 참조형<sup>reference type</sup> : Object, Array, Function, Date, RegExp, Map, Set

    - 값이 담긴 주솟값들로 이루어진 묶음을 가리키는 주솟값을 복제
    - 가변성<sup>mutability</sup>

- 메모리와 데이터

  - 비트
    - 0또는 1로만 표현할 수 있는 하나의 메모리 조각
    - 고유한 식별자를 통해 위치를 확인할 수 있음
  - 바이트
    - 8bit로 구성
    - 시작하는 비트의 식별자로 위치를 파악할 수 있음
    - 모든 데이터는 바이트 단위의 식별자, **메모리 주솟값** 을 통해 서로 구분하고 연결됨

- 식별자와 변수

  - 변수 
    - 변할 수 있는 데이터
  - 식별자
    - 어떤 데이터를 식별하는데 사용하는 이름 -> **변수명**

- 변수 선언과 데이터 할당

  - 변수 선언

    ```js
    var a;
    => 변할 수 있는 데이터를 만들고, 이 데이터의 식별자는 a가 된다
    ```

  - 변수 : 변경 가능한 데이터가 담길 수 있는 공간 또는 그릇

  - 데이터 할당

    ```js
    var a;
    a = 'abc';
    
    var a = 'abc';
    ```

    - 위 두 방법은 같은 동작을 수행
      - a는 임의의 주소에 이름과 값이 할당되고, 이 값은 실제 데이터가 할당 되어 있는 주소를 가리킴
      - a가 가리키는 주소에 'abc'를 데이터로 할당됨
    - 변수 영역에 값을 직접 대입하지 않는 이유?
      - 데이터 변환을 자유롭게 할 수 있고 메모리를 더 효율적으로 관리할 수 있음
      - 가변적인 데이터 변환을 처리하려면 변수와 데이터를 별도의 공간에 나누어 저장하는 것이 최적 
      - 변수 영역과 데이터 영역을 분리하면 중복된 데이터에 대한 처리 효율이 높아짐

- 기본형 데이터와 참조형 데이터

  - 불변값
    - 변수와 상수 : 구분하는 성질은 **변수 영역** 메모리의 '변경 가능성'
    - 불변과 가변 : 구분하는 성질은 **데이터 영역** 메모리의 '변경 가능성'
    - 불변값 
      - 기본형 데이터 : 숫자, 문자열, boolean, null, nudefined, Symbol
      - 변경은 새로 만드는 동작을 통해서만 이루어짐
      - 한 번 만들어진 값은 가비지 컬렉팅을 당하지 않는 한 영원히 변하지 않음
    - Garbage Collector ?
      - https://ko.javascript.info/garbage-collection
  - 가변값
    - 보통의 참조형 데이터 : object, array 등
    - 데이터 영역에 저장된 값은 불변값이지만, 변수에는 다른 값을 얼마든지 대입할 수 있음
    - 참조 카운트 : 어떤 데이터에 대해 자신의 주소를 참조하는 변수의 개수
    - 참조 카운트가 0인 메모리 주소는 가비지 컬렉터의 수거 대상이 됨
  - 변수 복사 비교
    - 자바스크립트의 모든 데이터 타입은 참조형 데이터
    - 기본형 : 주솟값을 복사하는 과정이 한 번만 이루어지기 때문에 복사한 값이 변했을 때도 원본은 유지됨
    - 참조형 : 참조형 데이터 자체를 변경할 경우에는 기본형과 똑같이 기존 데이터는 변하지 않지만, 그 내부의 프로퍼티를 변경하면 원본이 함께 변경됨

- 불변 객체

  - 불변 객체를 만드는 가장 간단한 방법 ? 객체를 복사할 때, 새로운 객체를 만들어 리턴해주기
  - 얕은 복사와 깊은 복사
    - 깊은 복사를 위해서는 **기본형 데이터일 경우에는 그대로 복사**하면 되지만, **참조형 데이터는 다시 그 내부의 프로퍼티들을 복사**해야 함
    - 깊은 복사 방법 
      - 참조형 데이터가 있을 때마다 내부 프로퍼티들을 순회하며 재귀적으로 함수를 호출하는 방법
      - JSON 활용하기
        - But, `메서드`나 `__proto__`, `getter/setter` 등과 같이 JSON으로 변경할 수 없는 프로퍼티들은 무시함
        - `httpRequest`로 받은 데이터를 저장한 객체를 복사할 때 등 순수한 정보만 다룰 때 활용하기 좋음

- undefined와 null

  - undefined
    - 사용자가 명시적으로 지정할 수도 있지만 값이 존재하지 않을 때 JS 엔진이 자동으로 부여하는 경우도 있음
      1. 값을 대입하지 않은 변수(var)에 접근할 때
      2. 객체 내부의 존재하지 않는 프로퍼티에 접근하려고 할 때
      3. return 문이 없거나 호출되지 않는 함수의 실행 결과
    - '비어있는 요소'와 달리 'undefined를 할당한 요소'는 순회와 관련된 많은 배열 메서드들의 순회 대상에 포함됨
    - 비어있는 요소는 값이 지정되지 않은 인덱스이므로 '존재하지 않는 프로퍼티'에 지나지 않음
    - 직접 undefined를 할당하는 것을 피하는 것을 추천함
  - null
    - 값이 없음을 나타내고자 할 때는 null을 사용하는 것을 권장
      - 이 규칙을 따르는 한 undefined는 '값을 대입하지 않는 변수에 접근하고자 할 때 자바스크립트 엔진이 반환해주는 값'으로서만 존재할 수 있음
    - typeof 를 사용했을 때 object로 나타나는 자바스크립트 자체 버그가 있음
      - https://curryyou.tistory.com/183
    - null 여부를 판단하기 위해서는 일치 연산자(===)를 써야 정확히 판단이 가능



### 02. 실행 컨텍스트

- 실행 컨텍스트 ?

  - 실행할 코드에 제공할 환경 정보들을 모아놓은 객체
    - 동일한 환경에 있는 코드들을 실행할 때 필요한 정보들을 모아 컨텍스트를 구성하고, 콜 스택에 쌓아올렸다가, 가장 위에 쌓여 있는 컨텍스트와 관련 있는 코드들을 실행하는 식으로 전체 코드의 환경과 순서를 보장
    - 하나의 실행 컨텍스트를 구성할 수 있는 방법
      - 전역공간
      - eval() 함수
      - 함수
  - 전역 컨텍스트
    - 최상단의 공간이므로 자바스크립트 코드를 실행하는 순간 전역 컨텍스트가 콜 스택에 담김
    - 일반적 실행 컨텍스트와 차이점은 argumemts의 유무 -> 전역 공간을 둘러싼 외부 스코프는 존재할 수 없기 때문
  - 실행 컨텍스트에 담기는 정보 -> 개발자가 코드를 통해 확인할 수는 없음
    - `VariableEnvironment`
    - `LexicalEnvironment`
    - `ThisBinding`

- `VariableEnvironment`

  - 현재 컨텍스트 내의 식별자들에 대한 정보 + 외부 환경 정보. 선엄 시점의 `LexicalEnvironment` 의 스냅샷으로, 변경 사항은 반영되지 않음
  - 실행 컨텍스트를 생성할 때 `VariableEnvironment` 에 정보를 먼저 담고, 이를 그대로 복사해서 `LexicalEnvironment` 를 만든 다음, 그 이후에는 `LexicalEnvironment` 를 주로 활용
  - `environmentRecord` 와 `outerEnvironmentReference` 로 구성돼 있음

- `LexicalEnvironment`

  - 처음은 `VariableEnvironment` 와 같지만 변경사항이 실시간으로 적용됨

  - `enviromentRecord`

    - 현재 컨텍스트와 관련된 코드의 식별자 정보들이 저장
    - 컨텍스트 내부 전체를 처음부터 끝까지 쭉 훑어나가며 순서대로 수집
    - 이로 인해 코드가 실행되기도 전에 자바스크립트 엔진은 해당 환경에 속한 코드의 변수명들을 모두 알게 됨 -> **호이스팅 개념**이 등장

  - 호이스팅 규칙

    - 변수 정보를 수집하는 과정에서 자바스크립트 엔진은 식별자들을 먼저 수집한 뒤에 실제 코드를 실행함

    - 변수는 선언만 끌어올리나, 함수는 함수 전체를 끌어올리는 차이가 있음

    - 예시를 통해 살펴보기

      ```js
      function a (x) {
        console.log(x);
        var x;
        console.log(x);
        var x = 2;
        console.log(x):
      }
      a(1);
      
      => 실행결과
      // 1, 1, 2
      
      function a () {
        console.log(b);
        var b = 'bbb';
        console.log(b);
        function b () { }
        console.log(b);
      }
      a();
      
      => 실행결과
      // function b, 'bbb', 'bbb'
      ```

  - 함수 선언문과 함수 표현식

    - 함수 선언문

      - function 정의부만 존재하고 별도의 할당 명령이 없음
      - 반드시 함수명이 정의돼 있어야 함 -> 기명 함수 표현식
      - 호이스팅 시 함수 전체를 끌어올림

    - 함수 표현식

      - 정의한 function을 별도의 변수에 할당
      - 함수명이 정의되지 않아도 됨 -> 일반적으로 익명 함수 표현식을 말함
      - 호이스팅 시 변수 선언만 끌어올림

      ```js
      function a () {}
      a();	// ok
      
      var b = function () {}
      b();	// ok
      
      var c = function d () {}
      c();	// ok
      d();	// error
      ```

    - 함수 선언문 vs 함수 표현식?

      - 함수 선언문의 장점?
        - export default function을 한번에 처리할 수 있다
        - Temporal Dead Zone 방지
      - 함수 표현식의 장점?
        - 클로저 사용 가능
        - 호이스팅의 예기치 못한 동작 예방
        - 함수의 중복 시, 혼란을 일으키는 원인이 줄어듬

  - `outerEnviromentRefernce`

    - 스코프 
      - 식별자에 대한 유효범위
      - ES5 까지는 오직 함수에 의해서만 스코프가 생성됨
      - ES6 부터는 let, const, class, stirct mode 에서 함수 선언 등에 대해서만 범위로서 역할을 수행
    - 스코프 체인
      - 식별자의 유효범위를 안에서부터 바깥으로 차례로 검색해나가는 것
      - 이를 가능케 하는 것이 `outerEnvironmentRefernce`
    - `outerEnvironmentRefernce`
      - 현재 호출된 함수가 선언될 당시의 `LexicalEnvironment` 를 참조
      - 연결리스트의 형태를 띰
      - `outerEnvironmentRefernce` 는 오직 자신이 선언된 시점의 `LexicalEnvironment` 만 참조하고 있으므로 가장 가까운 요소부터 차례대로만 접근할 수 있고 다른 순서로 접근하는 것은 불가능
      - 이러한 특성 덕분에 여러 스코프에서 동일한 식별자를 선언한 경우 **무조건 스코프 체인 상에서 가장 먼저 발견된 식별자에게만 접근 가능** 하게 됨

  - 전역 변수와 지역 변수

    - 전역 변수 : 전역 공간에서 선언한 변수
    - 지역 변수 : 함수 내부에서 선언한 변수
    - 코드의 안정성을 위해서는 가급적 전역변수 사용을 최소화해야 함




### 03. this

- this 는 실행 컨텍스트가 생성될 때 함께 결정 => 함수를 호출할 때 결정

- 상황에 따른 this

  - 전역 공간

    - 전역 객체를 가리킴
    - 전역 컨텍스트를 생성하는 주체가 바로 전역 객체기 때문
    - 브라우저에선 `window`, Node에서는 `global`

  - 메서드로서 호출할 때 그 메서드 내부

    - 함수 vs 메서드 ?

      - 메서드 : 객체의 프로퍼티에 할당된 상태에서 객체의 메서드로 호출할 경우

      - 함수 : 위의 경우가 아닌 경우 모두 함수로 동작

        ```js
        var func = function (x) {
          console.log(this, x);
        };
        func(1);	// Window { ... }
        
        var obj = {
          method: func
        };
        obj.method(2);	// { method: f }
        obj['method'](2);	// { method: f }
        ```

    - 메서드 내부에서 this

      - this는 호출한 주체에 대한 정보가 담김

      - 함수를 메서드로 호출하는 경우 주체는 함수명 앞의 객체가 됨

        ```js
        var obj = {
          methodA: function () { console.log(this); },
          inner: {
            methodB: function () { console.log(this); }
          }
        };
        obj.methodA();	// { methodA: f, inner: {...} }
        obj.inner.methodB();	// { methodB: f }
        ```

  - 함수로 호출할 때 그 내부에서의 this

    - 함수 내부에서의 this

      - 함수로서 호출하는 것은 호출 주체를 명시하지 않고 개발자가 코드에 직접 관여해서 실행한 것

      - 호출 주체의 정보를 알 수 없으므로 this는 전역 객체를 가리킴

      - 더글라스 크락포드는 이를 명백한 설계상의 오류라고 말함

        ```js
        var obj1 = {
          outer: function () {
            console.log(this);
            var innerFunc = function () {
              console.log(this);
            };
            innerFunc();
            
            var obj2 = {
              innerMethod: innerFunc
            };
            obj2.innerMethod();
          }
        };
        obj1.outer();
        
        // obj1 / window / obj2 가 this가 됨
        ```

      - this 바인딩은 함수를 실행하는 당시의 주변 환경은 중요하지 않고,  오직 해당 함수를 호출하는 구문 앞에 점 또는 대괄호 표기가 있는지 없는지에 따라 바인딩 됨

    - 메서드 내부 함수에서 this를 우회하는 방법

      - ES5 : 변수를 활용

        ```js
        var obj = {  outer: function () {    console.log(this);			// { outer: f }    var innerFunc1 = function () {      console.log(this);		// Window { ... }    };    innerFunc1();        var self = this;    var innerFunc2 = function () {      console.log(self);		// { outer: f }    };    innerFunc2();  }};obj.outer();
        ```

      - ES6

        - 화살표 함수를 사용
        - 화살표 함수는 실행 컨텍스트를 생성할 때 this 바인딩 과정 자체가 빠지게 됨 -> 상위 스코프의 this를 그대로 활용 가능

        ```js
        var obj = {  outer: function () {    console.log(this);			// { outer: f }    var innerFunc = () => {      console.log(this);		// { outer: f }    };    innerFunc();  }};obj.outer();
        ```

        - call, apply 등의 메서드를 활용하는 방법도 있음

  - 콜백 함수 호출 시 그 함수 내부에서의 this

    - 콜백 함수에서 this는 제어권을 가지는 함수(메서드)가 콜백 함수에서 this를 무엇으로 할지에 따라 달라짐

    - 특별히 정의하지 않은 경우에는 기본적으로 함수와 마찬가지로 전역객체를 바라봄

      ```js
      setTimeout(function () { console.log(this); }, 300);[1, 2, 3, 4, 5].forEach(function (x) {  console.log(this, x);});document.body.innerHTML += '<button id="a">클릭</button>';document.body.querySelector('#a').addEventListener('click', function (e) {  console.log(this, e);});// (1), (2) : this 는 전역 객체, (3) : this는 querySelector('#a')
      ```

  - 생성자 함수 내부에서의 this

    - 프로그래밍적으로 '생성자'는 구체적인 인스턴스를 만들기 위한 일종의 틀

    - 자바스크립트에서는 new 명령어와 함께 함수를 호출하면 해당 함수가 생성자로서 동작하게 됨

    - 생성자 함수를 호출하면 생성자의 prototype 프로퍼티를 참조하는 `__proto__`라는 프로퍼티가 있는 객체(인스턴스)를 만들고, 미리 준비된 공통 속성 및 개성을 해당 객체(this)에 부여

      ```js
      var Cat = function (name, age) {  this.bark = '야옹';  this.name = name;  this.age = age;};var choco = new Cat('초코', 7);var nabi = Cat('나비', 5);console.log(choco, nabi);		// Cat {bark: '야옹', name: '초코', age: 7} undefined
      ```

- 명시적으로 this를 바인딩하는 방법

  - call 메서드

    - `Function.prototype.call(thisArg[, arg1[, arg2[, ...]]])`

    - call 메서드는 메서드의 호출 주체인 함수를 즉시 실행하도록 하는 명령

    - call 메서드를 이용하면 임의의 객체를 this로 지정할 수 있음

      ```js
      var func = function (a, b, c) {  console.log(this, a, b, c);};func(1, 2, 3);		// Window{ ... } 1 2 3func.call({ x: 1 }, 4, 5, 6)	// { x: 1 } 4 5 6var obj = {  a: 1,  method: function (x, y) {    console.log(this.a, x, y);  }};obj.method(2, 3);		// 1 2 3obj.method.call({ a: 4 }, 5, 6);	// 4 5 6
      ```

  - apply 메서드

    - `Function.prototype.apply(thisArg[, argsArray])`

    - apply 메서드는 call 메서드와 기능적으로 완전히 동일

    - `apply` 는 두 번째 인자를 배열로 받아 그 배열의 요소들을 호출할 함수의 매개변수로 지정

    - `call` 은 첫 번째 인자를 제외한 나머지 모든 인자들을 호출할 함수의 매개변수로 지정

      ```js
      var func = function (a, b, c) {    console.log(this, a, b, c);};func.apply({x: 1}, [4, 5, 6]);		// { x: 1 } 4 5 6var obj = {  a: 1,  method: function (x, y) {    console.log(this.a, x, y);  }};obj.method.apply({ a: 4 }, [5, 6]);		// 4 5 6
      ```

  - call / apply 메서드의 활용

    - 유사배열객체에 배열 메서드를 적용

      - 유사배열객체 : 키가 0 또는 양의 정수인 프로퍼티가 존재하고 length 프로퍼티 값이 0 또는 양의 정수인 객체
      - ES6에서는 유사배열객체 또는 순회 가능한 모든 종류의 데이터 타입을 배열로 전환하는 `Array.from` 메서드를 도입

    - 생성자 내부에서 다른 생성자를 호출

      - 생성자 내부에 닫른 생성자와 공통된 내용이 있을 경우 call 또는 apply를 이용해 다른 생성자를 호출

        ```js
        function Person(name, gender) {  this.name = name;  this.gender = gender;}function Student(name, gender, school) {  Person.call(this, name, gender);  this.school = school;}function Employee(name, gender, company) {  Person.apply(this, [name, gender]);  this.company = company;}
        ```

    - 여러 인수를 묶어 하나의 배열로 전달하고 싶을 때 (apply) -> spread operator로 대체 가능

  - bind 메서드

    - `Function.prototype.bind(thisArg[, arg1[, arg2[, ...]]])`

    - ES5에 추가, call과 비슷하지만 즉시 호출하지는 않고 넘겨받은 this 및 인수들을 바탕으로 새로운 함수를 반환하기만 하는 메서드

    - 함수에 this를 미리 적용하는 것과 부분 적용 함수를 구현하는 두 가지 목적을 지님

      ```js
      var func = function (a, b, c, d) {
        console.log(this, a, b, c, d);
      };
      func(1, 2, 3, 4);											// Window{ ... } 1 2 3 4
      
      var bindFunc1 = func.bind({ x: 1 });
      bindFunc1(5, 6, 7, 8);								// { x: 1 } 5 6 7 8
      
      var bindFunc2 = func.bind({ x: 1 }, 4, 5);
      bindFunc2(6, 7);					// { x: 1 } 4 5 6 7
      bindFunc2(8, 9);					// { x: 1 } 4 5 8 9
      ```

      

### 04. 콜백 함수

- 콜백 함수란?

  - 다른 코드(함수 또는 메서드)에게 인자를 넘겨줌으로써 그 제어권도 함꼐 위임한 함수

- 제어권

  - 호출 시점

    - 콜백 함수의 제어권을 넘겨받은 코드는 콜백 함수 호출 시점에 대한 제어권을 가짐

    ```js
    var count = 0;
    var cbFunc = function () {
      console.log(count);
      if (++count > 4) clearInterval(timer);
    };
    var timer = setInterval(cbFunc, 300);
    ```

    | code                      | 호출 주체  | 제어권      |
    | ------------------------- | ---------- | ----------- |
    | cbFunc();                 | 사용자     | 사용자      |
    | setInterval(cbFunc, 300); | setInteval | setInterval |

  - 인자

    - 콜백 함수의 제어권을 넘겨받은 코드는 콜백 함수를 호출할 때 인자에 어떤 값들을 어떤 순서로 넘길 것인지에 대한 제어권을 가짐

    ```js
    var newArr = [10, 20, 30].map(function (index, currentValue) {
      console.log(index, currentValue);
      return currentValue + 5;
    });
    console.log(newArr);
    
    // 10 0
    // 20 1
    // 30 2
    // [5, 6, 7]
    
    // map 메서드에게 제어권이 있으므로 콜백 함수를 넘길 때는 map 메서드의 규칙에 맞춰 넘기지 않으면 예상치 못한 결과를 불러일으킴
    ```

  - this

    - 콜백 함수도 함수이기 때문에 기본적으로는 this가 전역객체를 참조하지만, 제어권을 넘겨받을 코드에서 콜백 함수에 별도로 this가 될 대상을 지정하는 경우에는 그 대상을 참조하게 됨

      ```js
      setTimeout(function () { console.log(this); }, 300);	// (1) Window { ... }
      
      [1, 2, 3, 4, 5].forEach(function (x) {
        console.log(this);			// (2) Window { ... }
      });	
      
      document.body.innerHTML += '<button id="a">클릭</button>';
      document.body.querySelector('#a').addEventListener('click', function (e) {
        console.log(this, e);					// (3) <button id="a">클릭</button>
      });															// MouseEvent { isTrusted: true, ... }
      ```

      (1) : setTimeout 내부에서 콜백 함수를 호출할 때 call 메서드의 첫번째 인자에 전역객체를 넘김

      (2) : forEach는 별도의 인자를 this로 받지만 해당 코드에선 별도로 this를 넘겨주지 않았으므로 전역객체를 가리킴

      (3) : addEventListener는 내부에서 콜백 함수를 호출할 때 call 메서드의 첫 번째 인자에 addEventListener 메서드의 this를 그대로 넘기도록 정의돼 있음 => 따라서 this는 HTML 엘리먼트를 가르킴

- 콜백 함수는 함수

  - 콜백 함수로 어떤 객체의 메서드를 전달하더라도 그 메서드는 메서드가 아닌 함수로서 호출됨

    ```js
    var obj = {
      vals: [1, 2, 3],
      logValues: function(v, i) {
        console.log(this, v, i);
      }
    };
    obj.logValues(1, 2);							// this -> obj
    [4, 5, 6].forEach(obj.logValues);	// this -> window
    ```

  - 어떤 함수의 인자로 객체의 메서드를 전달하더라도 이는 결국 메서드가 아닌 함수

- 콜백 함수 내부의 this에 다른 값 바인딩하기

  - 전통적 방식

    - this를 다른 변수에 담아 콜백 함수로 활용할 함수에서는 this 대신 그 변수를 사용하게 하고, 이를 클로저로 만드는 방식

    ```js
    var obj1 = {
      name: 'obj1',
      func: function () {
        var self = this;
        return function () {
          console.log(self.name);
        };
      }
    };
    setTimeout(obj1.func(), 1000);
    ```

  - this를 사용하지 않는 방식

    - 간결하고 직관적이지만 재활용이 불가능함

    ```js
    var obj1 = {
      name: 'obj1',
      func: function () {
        console.log(obj1.name);
      }
    };
    setTimeout(obj1.func, 1000);
    ```

  - bind 메서드 활용

    - 위의 두방법을 모두 보완하는 방법

    ```js
    var obj1 = {
      name: 'obj1',
      func: function () {
        console.log(obj1.name);
      }
    };
    setTimeout(obj1.func.bind(obj1), 1000);
    
    var obj2 = { name: 'obj2' };
    setTimeout(obj1.func.bind(obj2), 1500);
    ```

- 콜백 지옥과 비동기 제어

  - 콜백 지옥

    - 콜백 함수를 익명 함수로 전달하는 과정이 반복되어 코드의 들여쓰기 수준이 감당하기 힘들 정도로 깊어지는 현상
    - 주로 이벤트 처리나 서버 통신과 같이 비동기적 작업을 수행하기 위해 이런 형태가 자주 등장
    - 가독성이 떨어지고 코드를 수정하기 어려움

  - 비동기 vs 동기

    - 동기
      - 현재 실행 중인 코드가 완료된 후에야 다음 코드를 실행하는 방식
      - CPU의 계산에 의해 즉시 처리가 가능한 대부분의 코드
    - 비동기
      - 현재 실행 중인 코드의 완료 여부와 무관하게 즉시 다음 코드로 넘어가는 방식
      - 별도의 요청(setTimeout), 실행 대기(addEventListener), 보류(XMLHttpRequest) 등과 관련된 코드

  - 콜백 지옥 해결법

    - 기명 함수로 변환

    - Promise

      - ES6에 도입
      - new 연산자와 함께 호출한 Promise의 인자로 넘겨주는 콜백 함수는 호출할 때 바로 실행
      - 콜백 함수의 내부에 resolve 또는 reject 함수를 호출하는 구문이 있을 경우 둘 중 하나가 실행되기 전까지는 다음(then) 또는 오류 구문(catch)으로 넘어가지 않음

      ```js
      const addCoffee = function(name) {
        return function(prevName) {
          return new Promise(function (resolve) {
            setTimeout(function () {
              var newName = prevName ? (prevName + ', ' + name) : name;
              console.log(newName);
              resolve(newName);
            }, 500);
          });
        };
      };
      addCoffee('에스프레소')()
      	.then(addCoffee('아메리카노'))
      	.then(addCoffee('카페모카'))
      	.then(addCoffee('카페라떼'));
      ```

    - Generator

      - ES6 도입
      - `*` 가 붙은 함수
      - Generator 함수를 실행하면 Iterator가 반환되고, Iterator는 next라는 메서드를 가지고 있음
      - next 메서드를 호출하면 Generator 함수 내부에서 가장 먼저 등장하는 yield 에서 함수의 실행을 멈춤

      ```js
      var addCoffee = function (prevName, name) {
        setTimeout(function () {
          coffeeMaker.next(prevName ? prevName + ', ' + name : name);
        }, 500);
      };
      var coffeeGenerator = function* () {
        var espresso = yiled addCoffee('', '에스프레소');
        var americano = yiled addCoffee(espresso, '아메리카노');
        var mocha = yiled addCoffee(americano, '카페모카');
        var latte = yiled addCoffee(mocha, '카페라떼');
      };
      var coffeeMaker = coffeeGenerator();
      coffeeMaker.next();
      ```

    - Async / await

      - ES2017 도입
      - 비동기 작업을 수행하고자 하는 함수 앞에 async를 표기
      - 함수 내부에서 실질적인 비동기 작업이 필요한 위치마다 await를 표기
      - await 뒤의 내용을 Promise로 자동 전환하고, 해당 내용이 resolve 된 이후에야 다음으로 진행 (Promise의 then과 유사)

      ```js
      var addCoffee = function (name) {
        return new Promise(function (resolve) {
          setTimeout(function () {
            resolve(name);
          }, 500);
        });
      };
      var coffeeMaker = async function () {
        var coffeList = '';
        var _addCoffee = async function (name) {
          coffeeList += (coffeeList += (coffeeList ? ',' : '') + await addCoffee(name));
        };
        await _addCoffee('에스프레소');
        await _addCoffee('아메리카노');
        await _addCoffee('카페모카');
        await _addCoffee('카페라떼');
      }
      ```

      


### 05. 클로저

- 클로저의 의미 및 원리

  - 클로저?

    - 어떤 함수 A에서 선언한 변수 a를 참조하는 내부함수 B를 외부로 전달할 경우 A의 실행 컨텍스트가 종료된 이후에도 변수 a가 사라지지 않는 현상
    - 함수를 선언할 때 만들어지는 유효범위가 사라진 후에도 호출할 수 있는 함수
    - 이미 생명 주기가 끝난 외부 함수의 변수를 참조하는 함수
    - 자신이 생성될 때의 스코프에서 알 수 있었던 변수들 중 언젠가 자신이 실행될 때 사용할 변수들만을 기억하여 유지시키는 함수

  - 클로저가 발생하는 원리?

    - 가비지 컬렉터의 동작 방식 때문에 발생함
    - 가비지 컬렉터는 어떤 값을 참조하는 변수가 하나라도 있다면 그 값은 수집 대상에 포함시키지 않음
    - 클로저의 outerEnvironmentReference가 외부 함수의 LexicalEnvironment를 필요로 하므로 가비지 컬렉터의 수집 대상에 포함되지 않음

  - 클로저가 되는 경우는 다양함

    - return과 함께 외부 함수의 변수를 참조하는 내부 함수

      ```js
      var outer = function () {
        var a = 1;
        var inner = function () {
          return ++a;
        };
        return inner;
      };
      
      var outer2 = outer();
      console.log(outer2());	// 2
      console.log(outer2());	// 3
      ```

    - return 없이 발생하는 경우

      ```js
      // (1) setInterval / setTimeout -> 콜백함수 내부에서 지역변수를 참조
      
      (function () {
        var a = 0;
        var intervalId = null;
        var inner = function () {
          if (++a >= 10) {
            clearInterval(intervalId);
          }
          console.log(a);
        };
        intervalId = setInterval(inner, 1000);
      })();
      
      // (2) setListener -> handler 함수 내부에서 지역변수를 참조
      
      (function () {
        var count = 0;
        var button = document.createElement('button');
        button.innerText = 'click';
        button.addEventListener('click', function () {
          console.log(++count, 'times clicked');
        });
        document.body.appendChild(button);
      })();
      ```

- 클로저와 메모리 관리

  - 클로저는 개발자의 의도대로 GC의 수거대상이 되지않도록 하는 것이므로 '메모리 소모'에 대한 관리법을 잘 파악해서 적용해야함

  - 관리법

    - GC의 참조 카운트를 0으로 만들어주면 됨

    - 식별자에 참조형이 아닌 기본형 데이터(보통 null이나 undefined)를 할당하면 됨

      ```js
      var outer = function () {
        var a = 1;
        var inner = function () {
          return ++a;
        };
        return inner;
      };
      
      outer = null;
      ```

- 클로저 활용 사례

  - 콜백 함수 내부에서 외부 데이터를 사용하고자 할 때

    ```js
    var fruits = ['apple', 'banana', 'peach'];
    var $ul = document.createElement('ul');
    
    fruits.forEach(function (fruit) {
      var $li = document.createElemnt('li');
      $li.innerText = fruit;
      $li.addEventListener('click', function () {
        alert('your choice is ' + fruit);
      });
      $ul.appendChild($li);
    });
    document.body.appendChild($ul);
    ```

    콜백 함수 내부에서 외부 데이터인 `fruit`를 사용하고 있음 -> 콜백 함수에 들어가는 함수가 공통 함수라면 다음과 같이 바뀔 수 있음

    ```js
    var fruits = ['apple', 'banana', 'peach'];
    var $ul = document.createElement('ul');
    
    var alertFruit = function (fruit) {
      alert('your choice is ' + fruit);
    };
    
    fruits.forEach(function (fruit) {
      var $li = document.createElemnt('li');
      $li.innerText = fruit;
      $li.addEventListener('click', alertFruit.bind(null, fruit));
      $ul.appendChild($li);
    });
    document.body.appendChild($ul);
    ```

    이 방법은 this가 원래의  this와 달라진다는 단점이 있음

    ```js
    var fruits = ['apple', 'banana', 'peach'];
    var $ul = document.createElement('ul');
    
    var alertFruitBuilder = function (fruit) {
      return function () {
        alert('your choice is ' + fruit);
      };
    };
    
    fruits.forEach(function (fruit) {
      var $li = document.createElemnt('li');
      $li.innerText = fruit;
      $li.addEventListener('click', alertFruitBuilder(fruit));
      $ul.appendChild($li);
    });
    document.body.appendChild($ul);
    ```

    고차함수를 이용한 방법으로 클로저를 적극 활용 => 함수형 프로그래밍에서 자주 쓰이는 방식

  

  - 접근 권한 제어(정보 은닉)

    - 정보은닉은 어떤 모듈의 내부 로직에 대해 외부로의 노출을 최소화해서 모듈간의 결합도를 낮추고 유연성을 높이고자 하는 현대 프로그래밍 언어의 중요한 개념 중 하나
    - 자바스크립트는 변수 자체에 접근 권한을 직접 보여하도록 설계 돼 있지 않음
    - 클로저를 이용한다면 `public`한 값과 `private`한 값을 구분하는 것이 가능

    ```js
    var createCar = function () {
      var fuel = Math.ceil(Math.random() * 10 + 10);
      var power = Math.ceil(Math.random() * 3 + 2);
      var moved = 0;
      
      var publicMembers = {
        get moved () {
          return moved;
        },
        run: function () {
          var km = Math.ceil(Math.random() * 6);
          var wastedFuel = km / power;
          if (fuel < wasteFuel) {
            console.log('이동불가');
            return;
          }
          fuel -= wasteFuel;
          moved += km;
          console.log(km + 'km 이동 (총 ' + movied + 'km). 남은 연료: ' + fuel);
        }
      };
      
      Object.freeze(publicMembers);
      return publicMembers;
    };
    ```

    - 접근권한 제어 방법

      1. 함수에서 지역변수 및 내부함수 등을 생성

      2. 외부에 접근권한을 주고자 하는 대상들로 구성된 참조형 데이터(대상이 여럿일 때는 객체 또는 배열, 하나일 때는 함수)를 return 함

         -> return한 변수들은 공개 멤버가 되고, 그렇지 않은 변수들은 비공개 멤버가 됨

  - 부분 적용 함수

    - n개의 인자를 받는 함수에 미리 m개의 인자만 넘겨 기억시켰다가, 나중에 (n-m)개의 인자를 넘기면 비로소 원래 함수의 실행 결과를 얻을 수 있게끔 하는 함수
    - `this` 를 바인딩해야한다는 점을 제외하면 `bind` 메서드의 실행 결과가 바로 부분 적용 함수가 됨

    ```js
    var partial3 = function () {
      var originalPartialArgs = arguments;
      var func = originalPartialArgs[0];
      if (typeof func !== 'function') {
        throw new Error('첫 번째 인자가 함수가 아닙니다.');
      }
      
      return function() {
        var partialArgs = Array.prototype.slice.call(originalPartialArgs, 1);
        var restArgs = Array.prototype.slice.call(arguments);
        for (var i = 0; i < partialArgs.length; i++) {
          if (partialArgs[i] === Symbol.for('EMPTY_SPACE')) {
            partialArgs[i] = restArgs.shift();
          }
        }
        return func.apply(this, partialArgs.concat(restArgs));
      };
    };
    
    var add = function () {
      var result = 0;
      for (var i = 0; i < arguments.length; i++) {
        result += arguments[i];
      }
      return result;
    };
    
    var _ = Symbol.for('EMPTY_SPACE');
    var addPartial = partial3(add, 1, 2, _, 4, 5, _, _, 8, 9);
    console.log(addPartial(3, 6, 7, 10));		// 55
    
    var dog = {
      name: '강아지',
      greet: partial3(function(prefix, suffix) {
        return prefix + this.name + suffix;
      }, '왈왈, ')
    };
    
    dog.greet('배고파요!');
    ```

    

  - 커링 함수

    - 여러 개의 인자를 받는 함수를 하나의 인자만 받는 함수로 나눠서 순차적으로 호출될 수 있게 체인 형태로 구성한 함수

    - 중간 과정상의 함수를 실행한 결과는 그 다음 인자를 받기 위해 대기만 할 뿐으로, 마지막 인자가 전달되기 전까지는 원본 함수가 실행되지 않음

    - 인자가 많아질수록 가독성 떨어짐

    - 각 단계에서 받은 인자들은 모두 마지막 단계까지 참조되다가, 마지막 호출로 실행 컨테스트가 종료된 후 한꺼번에 GC의 수거 대상이 됨

    - 함수형 프로그래밍에서는 지연실행<sup>lazy execution</sup> 이라고 부름

    - 원하는 지점까지 지연시켰다가 실행하는 것이 요긴항 상황이라면 커링을 쓰기에 적절

      ```js
      var getInformation = function (baseUrl) {
        return function (path) {
          return function (id) {
            return fetch(baseUrl + path + '/' + id);
          };
        };
      };
      
      // ES6
      var getInformation = baseUrl => path => id => fetch(baseUrl + path + '/' + id);
      
      var imageUrl = 'http://imageAddress.com/';
      
      var getImage = getInformation(imageUrl);
      var getEmoticon = getImage('emoticon');
      var getIcon = getImage('icon');
      
      var emoticon1 = getEmoticon(100);
      var emoticon2 = getEmoticon(102);
      var Icon1 = getIcon(205);
      var Icon2 = getIcon(234);
      ```



### 06. 프로토타입

- 프로토타입
  - 자바스크립트는 프로토타입 기반 언어

  - 클래스 기반 언어에서는 '상속'을 사용하지만, 프로토타입 기반 언어에서는 어떤 객체를 원형으로 삼고 이를 복제(참조)함으로써 상속과 비슷한 효과를 얻음

  - 프로토타입 흐름
    - 어떤 생성자 함수(Constructor)를 `new` 연산자와 함께 호출
    - `Constructor` 에서 정의된 내용을 바탕으로 새로운 인스턴스가 생성
    - 이때 `instance` 에는 `__proto__` 라는 프로퍼티가 자동으로 부여
    - 이 프로퍼티는 `Contructor` 의 `prototype` 이라는 프로퍼티를 참조
    
  - `__proto__` 는 생략 가능한 프로퍼티

    ```js
    var Person = function (name) {
      this._name = name;
    };
    Person.prototype.getName = function () {
      return this._name;
    };
    
    var suzi = new Person('Suzi');
    suzi.__proto__._name = 'SUZI__proto__';
    suzi.__proto__.getName();	// SUZI_proto__
    
    var suzi = new Person('Suzi', 28);
    suzi.getName();		// Suzi;
    var iu = new Person('Jieun', 28);
    iu.getName();
    ```

    - `__proto__` 를 생략하지 않으면 this는 `__proto` 를 가리키지만, 이를 생략하면 instance를 가리킴
    - `__proto__` 는 생략가능하므로 생성자 함수의 prototype에 어떤 메서드나 프로퍼티가 있다면 인스턴스에 마치 자신의 것처럼 해당 메서드나 프로퍼티에 접근할 수 있음
    - `Array` 의 인스턴스의 `__proto__` 은 `Array.prototype` 을 참조하여 prototye에 있는 메소드를 자신의 것처럼 호출할 수 있으나, `Array` 의 프로퍼티 내부에 있지 않은 `from, isArray` 등의 메서드들은 인스턴스가 직접 호출할 수 없음

  - constructor 프로퍼티

    - 생성자 함수의 `prototype` 객체 내부에는 `constructor` 라는 프로퍼티가 있음 (인스턴스도 마찬가지)

    - 원래의 생성자 함수(자기 자신)을 참조함

    - 인스턴스로부터 그 원형이 무엇인지 알 수 있는 수단이 됨

      ```js
      var arr = [1, 2];
      Array.prototype.constructor === Array	// true
      arr.__proto__.constructor === Array		// true
      arr.constructor === Array							// true
      
      var arr2 = new arr.constructor(3, 4);
      console.log(arr2);		// [3, 4]
      ```

    - 읽기 전용 속성이 부여된 예외적인 경우(기본형 리터럴 변수 - number, string, boolean)를 제외하고는 값을 바꿀 수 있음

    - `constructor`을 변경하더라도 참조하는 대상이 변경될 뿐 이미 만들어진 인스턴스의 원형이 바뀐다거나 데이터 타입이 변하는 것은 아님

      ```js
      // 모두 동일한 대상을 가리킴
      [Constructor]
      [instance].__proto__.constructor
      [instance].constructor
      Object.getPrototypeOf([instance]).constructor
      [Constructor].prototype.constructor
      ```

      ```js
      // 모두 동일한 객체에 접근할 수 있음
      [Constructor].prototype
      [instance].__proto__
      [instance]
      Object.getPrototypeOf([instance])
      ```

- 프로토타입 체인

  - 메서드 오버라이드

    - 인스턴스가 동일한 이름의 프로퍼티 또는 메서드를 가지면 오버라이딩이 됨

    - `__proto__` 를 이용해 원본에 우회적으로 접근이 가능함

      ```js
      var Person = function (name) {
        this.name = name;
      };
      Person.prototype.getName = function () {
        return this.name;
      };
      
      var iu = new Person('지금');
      iu.getName = function () {
        return '바로 ' + this.name; 
      };
      console.log(iu.getName());		// 바로 지금
      
      console.log(iu.__proto__.getName.call(iu));		// 지금
      ```

  - 프로토타입 체인

    - 어떤 데이터의 `__proto__` 프로퍼티 내부에서 다시 `__proto__` 프로퍼티가 연쇄적으로 이어진 것을 **프로토타입 체인**이라고 함

    - 프로토타입 체인을 따라가며 검색하는 것을 **프로토타입 체이닝**이라고 함

    - 어떤 메서드를 호출하면 자바스크립트 엔진은 데이터 자신의 프로퍼티들을 검색해서 원하는 메서드가 있으면 그 메서드를 실행하고, 없으면 `__proto__`를 검색해서 있으면 그 메서드를 실행하는 식으로 진행

      ```js
      var arr = [1, 2];
      Array.prototype.toString.call(arr);		// 1, 2
      Object.prototype.toString.call(arr);	// [object Array]
      arr.toString();												// 1, 2
      
      arr.toString = function () {
        return this.join('_');
      };
      arr.toString();												// 1_2
      ```

      - arr 변수는 배열이므로 `Array.toString` -> `Array.prototype.toString` -> `Object.prototype.toString` 의 순서로 프로토타입 체이닝을 실행
  
  - 객체 전용 메서드의 예외 사항
  
    - 어떤 생성자 함수든 `prototype` 은 반드시 객체이기 때문에 `Object.prototype` 이 언제나 프로토타입 체인의 최상단에 존재하기 됨
  
    - 따라서, 객체에서만 사용할 메서드는 다른 데이터 타입처럼 프로토타입 객체 안에 정의할 수가 없음 -> 다른 데이터 타입도 해당 메서드를 사용할 수 있기 때문
  
    - 객체 전용 메서드는 `Object` 에 스태틱 메서드로 부여할 수 밖에 없음
  
    - 생성자 함수인 `Object` 와 인스턴스인 객체 리터럴 사이에는 `this` 를 통한 연결이 불가능하기 때문에 `this`의 사용을 포기하고 대상 인스턴스를 인자로 직접 주입해야하는 방식으로 구현
  
    - `Object.prototype` 에는 어떤 데이터에서도 활용할 수 있는 범용적인 메서드들만 있음 (`toString, hasOwnProperty, valueOf, isPrototypeOf` 등)
  
    - `Object.create(null)` 를 이용하면 `__proto__` 가 없는 객체를 생성함 -> 기본 기능에는 제약이 있지만 성능상 이점을 가짐
  
      ```js
      var _proto = Object.create(null);
      _proto.getValue = function(key) {
        return this[key];
      };
      var obj = Object.create(_proto);
      obj.a = 1;
      console.log(obj.getValue('a'));	// 1
      console.dir(obj);								// __proto 에 getValue 만 있음
      ```
  
  - 다중 프로토타입 체인
  
    - 자바스크립트의 기본 내장 데이터 타입들은 모두 프로토타입 체인이 1단계(객체)이거나 2단계(나머지)로 끝나느 경우만 있음
  
    - 사용자가 생성자 함수의 `prototype` 이 연결하고자 하는 상위 생성자 함수의 인스턴스를 바라보게 해주면 다중 프로토타입 체인이 가능해짐
  
      ```js
      var Grade = function () {
        var args = Array.prototype.slice.call(arguments);
        for (var i = 0; i < args.length; i++) {
          this[i] = args[i];
        }
        this.length = args.length;
      };
      var g = new Grade(100, 80);
      
      Grade.prototype = [];
      
      g.pop();		// Grade(1) [100]
      g.push(90);	// Grade(2) [100, 90]
      
      ==> 안되는데,,,???
      ```
  
      
