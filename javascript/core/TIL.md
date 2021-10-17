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

    - 리액트에서는 함수 선언문이 좋을까? 함수 표현식이 좋을까?

      - 조쉬랑 얘기해보기..?
      - 함수 선언문의 장점?
        - export default function을 한번에 처리할 수 있다..? Temporal Dead Zone 방지..?
      - 함수 표현식의 장점?
        - 클로저 사용..? 호이스팅의 예기치 못한 동작 예방..? 함수의 중복 시, 혼란을 일으키는 원인이 줄어듬..?

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

  -  메서드로서 호출할 때 그 메서드 내부

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
        var obj = {
          outer: function () {
            console.log(this);			// { outer: f }
            var innerFunc1 = function () {
              console.log(this);		// Window { ... }
            };
            innerFunc1();
            
            var self = this;
            var innerFunc2 = function () {
              console.log(self);		// { outer: f }
            };
            innerFunc2();
          }
        };
        obj.outer();
        ```

      - ES6

        - 화살표 함수를 사용
        - 화살표 함수는 실행 컨텍스트를 생성할 때 this 바인딩 과정 자체가 빠지게 됨 -> 상위 스코프의 this를 그대로 활용 가능

        ```js
        var obj = {
          outer: function () {
            console.log(this);			// { outer: f }
            var innerFunc = () => {
              console.log(this);		// { outer: f }
            };
            innerFunc();
          }
        };
        obj.outer();
        ```

        - call, apply 등의 메서드를 활용하는 방법도 있음

  - 콜백 함수 호출 시 그 함수 내부에서의 this

    - 콜백 함수에서 this는 제어권을 가지는 함수(메서드)가 콜백 함수에서 this를 무엇으로 할지에 따라 달라짐

    - 특별히 정의하지 않은 경우에는 기본적으로 함수와 마찬가지로 전역객체를 바라봄

      ```js
      setTimeout(function () { console.log(this); }, 300);
      
      [1, 2, 3, 4, 5].forEach(function (x) {
        console.log(this, x);
      });
      
      document.body.innerHTML += '<button id="a">클릭</button>';
      document.body.querySelector('#a').addEventListener('click', function (e) {
        console.log(this, e);
      });
      
      // (1), (2) : this 는 전역 객체, (3) : this는 querySelector('#a')
      ```

  - 생성자 함수 내부에서의 this

    - 프로그래밍적으로 '생성자'는 구체적인 인스턴스를 만들기 위한 일종의 틀

    - 자바스크립트에서는 new 명령어와 함께 함수를 호출하면 해당 함수가 생성자로서 동작하게 됨

    - 생성자 함수를 호출하면 생성자의 prototype 프로퍼티를 참조하는 `__proto__`라는 프로퍼티가 있는 객체(인스턴스)를 만들고, 미리 준비된 공통 속성 및 개성을 해당 객체(this)에 부여

      ```js
      var Cat = function (name, age) {
        this.bark = '야옹';
        this.name = name;
        this.age = age;
      };
      var choco = new Cat('초코', 7);
      var nabi = Cat('나비', 5);
      console.log(choco, nabi);		// Cat {bark: '야옹', name: '초코', age: 7} undefined
      ```

- 명시적으로 this를 바인딩하는 방법

  - call 메서드

    - `Function.prototype.call(thisArg[, arg1[, arg2[, ...]]])`

    - call 메서드는 메서드의 호출 주체인 함수를 즉시 실행하도록 하는 명령

    - call 메서드를 이용하면 임의의 객체를 this로 지정할 수 있음

      ```js
      var func = function (a, b, c) {
        console.log(this, a, b, c);
      };
      
      func(1, 2, 3);		// Window{ ... } 1 2 3
      func.call({ x: 1 }, 4, 5, 6)	// { x: 1 } 4 5 6
      
      var obj = {
        a: 1,
        method: function (x, y) {
          console.log(this.a, x, y);
        }
      };
      
      obj.method(2, 3);		// 1 2 3
      obj.method.call({ a: 4 }, 5, 6);	// 4 5 6
      ```

  - apply 메서드

    - `Function.prototype.apply(thisArg[, argsArray])`

    - apply 메서드는 call 메서드와 기능적으로 완전히 동일

    - `apply` 는 두 번째 인자를 배열로 받아 그 배열의 요소들을 호출할 함수의 매개변수로 지정

    - `call` 은 첫 번째 인자를 제외한 나머지 모든 인자들을 호출할 함수의 매개변수로 지정

      ```js
      var func = function (a, b, c) {
          console.log(this, a, b, c);
      };
      
      func.apply({x: 1}, [4, 5, 6]);		// { x: 1 } 4 5 6
      
      var obj = {
        a: 1,
        method: function (x, y) {
          console.log(this.a, x, y);
        }
      };
      obj.method.apply({ a: 4 }, [5, 6]);		// 4 5 6
      ```

  - call / apply 메서드의 활용

    - 유사배열객체에 배열 메서드를 적용
    - 생성자 내부에서 다른 생성자를 호출
    - 여러 인수를 묶어 하나의 배열로 전달하고 싶을 때 (apply)

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

      

