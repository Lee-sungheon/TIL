## Clean Code

### 02. 의미 있는 이름

- **의도를 분명히 밝혀라**

  - 의도가 분명한 이름은 매우 중요
  - 좋은 이름을 짓는 시간보다 좋은 이름으로 절약하는 시간이 훨씬 많음
  - 변수, 함수, 클래스 이름은 존재 이유, 수행 기능, 사용 방법을 함축해야함

  ```ts
  // bad
  const d;
  
  function getThem() {
    const list1 = [];
   
    for (const x of theList) {
      if (x[0] === 4) {
        list1.push(x);
      }
    }
    return list1;
  }
  
  // good
  const daySinceCreation;
  
  function getFlaggedCells() {
    const flaggedCells = [];
    for (const cell of gameBoard) {
      if (cell[STATUS_VALUE] === FLAGGED) {
        flaggedCells.push(cell);
      }
    }
    return flaggedCells;
  }
  ```

- 그릇된 정보를 피하라

  - 그릇된 단서를 남기면 코드의 의미를 흐릴 수 있음
  - 흡사한 이름 사용 x
  - 널리 쓰이는 의미가 있는 단어를 다른 의미로 사용 x
  - 유사한 개념은 유사한 표기법 사용
  - 소문자 l, 대문자 O 사용 x

  ```ts
  // bad
  const accountList = { account1: 'john', account2: 'Tom' };
  
  // good
  const accountGroup = { account1: 'john', account2: 'Tom' };
  ```



- **의미 있게 구분하라**

  - 컴파일러나 인터프리터만 통과하려는 코드는 문제를 일으킴

  - 연속된 숫자를 덧붙이기 x
    - a1, a2, a3, ...
    
  - 불용어를 추가한 이름 x
    - productInfo = productData
    - moneyAmount = money
    - theMessage = message
    - accountData = account
    
    

- **발음하기 쉬운 이름을 사용하라**

  - 발음하기 어려운 이름은 토론하기도 어려움

  ```ts
  // bad
  const DtcRcrd102 = {
    genymdhms: new Date(),
    modymdhms: new Date(),
    pszqint = "102"
  };
  
  // good
  const Customer = {
    generationTimestamp: new Date(),
    modificationTimestamp: new Date(),
    recodId: "102"
  };
  ```



- **검색하기 쉬운 이름을 사용하라**

  - 이름 길이는 범위 크기에 비례해야 함 (간단한 메서드에서 로컬 변수만 한 문자를 사용)

  ```ts
  // bad
  for (let i = 0; i < 34; i++) {
    let s = 0;
    s += (t[j]*4/5);
  }
  
  // good
  const realDaysPerIdealDay = 4; 
  const NUMBER_OF_TASKS = 34;
  const WORK_DAYS_PER_WEEK = 5;
  let sum = 0;
  for (let i=0; i < NUMBER_OF_TASKS; i++) {
    realTaskDays = taskEstimate[i] * realDaysPerIdealDay;
    realTaskWeeks = (realTaskDays / WORK_DAYS_PER_WEEK);
    sum += realTaskWeeks;
  }
  ```



- **인코딩을 피하라**

  - 헝가리식 표기법 x
  - 멤버 변수 접두어 x
  - 인터페이스 클래스와 구현 클래스에서는 인코딩이 필요할 수도 있음

  

- **자신의 기억력을 자랑하지 마라**

  - 독자가 코드를 읽으면서 변수 이름을 자신이 아는 이름으로 변환해야 한다면 변수 이름은 바람직하지 못함
  - 루프에서 반복 횟수를 세는 변수 i, j, k는 괜찮음

  

- **클래스 이름**

  - 명사나 명사구가 적합
    - Good: Customer, WikiPage, AddressParser
    - Bad: Manager, Processor, Data, Info / 동사
    
    

- **메서드 이름**

  - 동사나 동사구가 적합
    - postPayment, deletePage, save
  - 접근자, 변경자, 조건자 -> get, set, is (javabean 기준)

  

- **기발한 이름은 피하라**

  - 재미난 이름보다 명료한 이름
  - 의도를 분명하고 솔직하게 표현하기

  

- **한 개념에 한 단어를 사용하라**

  - 추상적인 개념 하나에 단어 하나를 선택해 이를 고수하기
    - 똑같은 메서드를 클래스마다 fetch, retrieve, get으로 제각각 부르면 혼란스러움
  - 일관성 있는 어휘를 사용할 것

  

- **말장난을 하지 마라**

  - 한 단어를 두 가지 목적으로 사용하지 말 것

  - 다른 개념에 같은 단어를 사용한다면 말장난에 불과

    - number나 string을 더하는 add 함수
    - 집합에 값하나를 추가하는 함수 ? add가 아닌 insert나 append 사용

    

- **해법 영역에서 가져온 이름을 사용하라**

  - 코드를 읽을 사람도 프로그래머
  - 전산 용어, 알고리즘 이름, 패턴 이름, 수학 용어 등을 사용해도 괜찮음
  - 기술 개념에는 기술 이름이 가장 적합한 선택

  

- **문제 영역에서 가져온 이름을 사용하라**

  - 적절한 프로그래머 용어가 없다면 문제 영역에서 이름을 가져오기
  - 우수한 프로그래머와 설계자라면 해법 영역과 문제 영역을 구분할 줄 알아야 함

  

- **의미 있는 맥락을 추가하라**

  - 이름은 클래스, 함수, 이름 공간에 넣어 맥락을 부여하고, 모든 방법이 실패하면 마지막 수단으로 접두어를 붙임
    - firstName, street, city, stage -> addressFirstName, addressStreet, addressCity, addressStage

  ```ts
  // bad
  function printGuessStatistics(candidate, count) {
    let number = '';
    let verb = '';
    let pluralModifier = '';
    if (count === 0) {
      number = 'no';
      verb = 'are';
      pluralModifier = 's';
    } else if (count === 1) {
      number = '1';
      verb = 'is';
      pluralModifier = '';
    } else {
      number = String(count);
      verb = 'are';
      pluralModifier = 's';
    }
    const guessMessage = `There ${verb} ${number} ${candidate} ${pluralModifier}`;
    console.log(guessMessage);
  }
  
  // good
  const GuessStatisticsMessage = (candidateValue, countValue) => {
    const candidate = candidateValue;
    const count = countValue;
    let number = '';
    let verb = '';
    let pluralModifier = '';
    
    return function make() {
      createPluralDependentMessageParts(count);
      return `There ${verb} ${number} ${candidate} ${pluralModifier}`;
    }
    
    function createPluralDependentMessageParts() {
      if (count === 0) {
        thereAreaNoLetters();
      } else if (count === 1) {
        thereIsOneLetter();
      } else {
        thereAreManyLetters();
      }
    }
    
    function thereAreManyLetters() {
      number = String(count);
      verb = 'are';
      pluralModifier = 's';
    }
    
    function thereIsOneLetter() {
      number = '1';
      verb = 'is';
      pluralModifier = '';
    }
    
    function thereAreNoLetters() {
      number = 'no';
      verb = 'are';
      pluralModifier = 's';
    }
  }
  ```

  

- **불필요한 맥락을 없애라**

  - 일반적으로 짧은 이름이 긴 이름보다 좋음 (단, 의미가 분명한 경우에 한해서)
  - 이름에 불필요한 맥락을 추가하지 않도록 주의
    - accountAddress와 customerAddress는 Address 클래스 인스턴스로는 좋은 이름이나 클래스 이름으로는 적합하지 못함
    - 클래스 이름으로는 Address가 적합



### 03. 함수

- **작게 만들어라**

  - `if / else / while` 문 등에 들어가는 블록은 한 줄이어야 한다

    - 대게 거기서 함수를 호출
    - 블록 안에서 호출하는 함수 이름을 적절히 짓는다면, 코드를 이해하기 쉬워짐

  - 중첩 구조가 생길수록 함수가 커져서는 안됨

    - 함수에서 들여쓰기 수준은 1단이나 2단을 넘어서면 안 됨

    

- **한 가지만 해라**

  - ***함수는 한 가지를 해야 한다. 그 한 가지를 잘해야 한다. 그 한 가지만을 해야 한다.***
  - 지정된 함수 이름 아래에서 추상화 수준이 하나여야 함
  - 함수가 '한 가지'만 하는지 판단하는 방법
    - 단순히 다른 표현이 아니라 의미 있는 이름으로 다른 함수를 추출할 수 있다면 그 함수는 여러 작업을 하는 셈



- **함수 당 추상화 수준은 하나로!**
  - 함수가 '한 가지' 작업만 하려면 함수 내 모든 문장의 추상화 수준이 동일해야 함
  - 위애서 아래로 코드 읽기: **내려가기** 규칙
    - 코드는 위에서 아래로 이야기처럼 읽혀야 좋음
    - 한 함수 다음에는 추상화 수준이 한 단계 낮은 함수가 옴



- **Switch** 문
  - switch 문은 N가지를 처리함
  - 각 switch 문을 저차원 클래스에 숨기고 절대로 반복하지 않도록 설계(?) -> 다형성 이용



- **서술적인 이름을 사용하라!**
  - 함수가 하는 일을 잘 표현할 수 있는 이름
  - 길고 서술적인 이름이 짧고 어려운 이름보다 좋음
  - 이름을 붙일 때는 일관성이 있어야 함



- **함수 인수**
	- 함수에서 이상적인 인수 개수는 0개
	- 3개 이상의 인수는 피하는 편이 좋음
	- 인수는 개념을 이해하기 어렵게 만듬
	- 인수가 많으면 테스트 케이스를 작성하기도 어려움
	- 플래그 인수
  		- 함수로 boolean 형태를 넘기기 X
  		- 함수가 한꺼번에 여러가지를 처리한다고 대놓고 공표하는 셈
  		- 함수를 나눠야 좋음 (좋아요 같은 거는...? 과연 나누는게 좋은 방법론인가...?)
	- 인수가 많다면 독자적인 클래스 변수(혹은 객체)로 선언할 가능성을 짚어보자
	- 동사와 키워드
  		- 함수의 의도나 인수의 순서와 의도를 제대로 표현하려면 좋은 함수 이름이 필수
  		- 단항 함수는 함수와 인수가 동사/명사 쌍을 이뤄야 함 : `writeField(name)`
  		- 함수 이름에 키워드를 추가하는 방법 : `assertExpectedEqualsActual(expected, actual)` -> 인수 순서를 기억할 필요가 없어짐




- **부수 효과를 일으키지 마라!**
  - 함수에서 한 가지를 하겠다고 약속하고 남몰래 다른 짓을 한다
  - 예상치 못하게 클래스 변수를 수정하거나, 함수로 넘어온 인수나 시스템 전역 변수를 수정함
  - 출력 인수를 피해야 함

- **명령과 조회를 분리하라!**
	-  함수는 객체 정보를 반환하거나 객체 상태를 변경하거나 둘 중 하나여야 함
	-  즉, 뭔가를 수행하거나 뭔가에 답하거나 둘 중 하나만 해야 함
	-  둘 다 한다면 혼란을 초래할 수 있음

- **오류 코드보다 예외를 사용하라!**
	- 명령 함수에서 오류 코드를 반환하는 방식은 명령/조회 분리 규칙을 미묘하게 위반함
	- 오류 코드 대신 예외를 사용하면 오류 처리 코드가 원래 코드에서 분리되므로 코드가 깔끔해짐
	- try/catch 블록은 별도 함수로 뽑아내는 편이 좋음 -> 코드 구조에 혼란을 일으키며, 정상 동작과 오류 처리 동작을 뒤섞음
	- 오류 처리도 '한 가지' 작업만 해야 함

- **반복하지 마라!**
	- 중복은 코드 길이가 늘어날 뿐 아니라 알고리즘이 변하면 여러 곳을 손봐야 함
	- 오류가 발생할 가능성도 높음

- **구조적 프로그래밍**
	- 구조적 프로그래밍 원칙 -> 모든 함수와 함수 내 모든 블록에 입구와 출구가 하나만 존재해야 함
	- 즉, 함수는 return 문이 하나여야 함 (break, continue, goto 사용 X)
	- 함수가 작다면 구조적 프로그래밍은 별 이익을 제공하지 못함
	
- **함수를 어떻게 짜죠?**
	- 소프트웨어를 짜는 행위는 여느 글짓기와 비슷함 
	- 처음에는 길고 복잡하고, 들여쓰기 단계도 많고 중복된 루트도 많음
	- 임수 목록도 아주 길고, 이름도 즉흥적이며 코드는 중복됨
	- 그 서투른 코드를 빠짐없이 테스트하는 단위 테스트 케이스를 만듬
	- 그 후 코드를 다듬고, 함수를 만들고, 이름을 바꾸고, 중복을 제거
	- 메서드를 줄이고 순서를 바꾸며 전체 클래스를 쪼갬
	- 코드는 항상 단위 테스트를 통과해야 함



## 04. 주석

- 개요
  - 코드로 의도를 표현하지 못해, 실패를 만회하기 위해 주석을 사용
  - 주석은 오래될수록 코드와 멀어지며 완전히 그릇될 가능성도 커짐
  - 코드는 변화하고 진화하지만, 주석을 유지하고 보수하진 않는다
  - 부정확한 주석은 아예 없는 주석보다 훨씬 더 나쁘다
  - 코드만이 정확한 정보를 제공하는 유일한 출처이므로 주석을 가능한 줄여야한다



- 주석은 나쁜 코드를 보완하지 못한다
  - 코드에 주석을 추가하는 일반적인 이유는 코드 품질이 나쁘기 때문
  - 나쁜 코드를 주석으로 설명하려하지 말고 코드를 정리하자!



- 코드로 의도를 표현하라!
  - 코드로 대다수 의도를 표현할 수 있다
  - 많은 경우 주석으로 달려는 설명을 함수로 만들어 표현해도 충분하다



- 좋은 주석
  - 정말로 좋은 주석은, 주석을 달지 않을 방법을 찾아낸 주석이다!
  - 법적인 주석
    - 각 소스 첫머리에 들어가는 저작권 정보와 소유권 정보
  - 정보를 제공하는 주석
    - 때로는 기본적인 정보를 주석으로 제공하면 편리함
    - But, 웬만하면 코드로 대체 가능
  - 의도를 설명하는 주석
    - 때때로 주석은 구현을 이해하게 도와주는 선을 넘어 결정에 깔린 의도까지 설명
  - 의미를 명료하게 밝히는 주석
    - 일반적으로 인수나 반환값 자체를 명확하게 만들면 더 좋음
    - 인수나 반환값이 표준 라이브러리나 변경하지 못하는 코드에 속한다면 의미를 명료하게 밝히는 주석이 유용
  - 결과를 경고하는 주석
    - 다른 프로그래머에게 결과를 경고할 목적으로 주석을 사용
  - TODO 주석
    - '앞으로 할 일'을 //TODO 주석으로 남겨두면 편함
    - TODO 주석은 프로그래머가 필요하다 여기지만 당장 구현하기 어려운 업무를 기술
    - 주기적으로 TODO 주석을 점검해 없애도 괜찮은 주석은 없애라고 권함
  - 중요성을 강조하는 주석
    - 자칫 대수롭지 않다고 여겨질 뭔가의 중요성을 강조하기 위해 주석을 사용



- 나쁜 주석
  - 대다수의 주석이 이 범주에 속함
  - 주절거리는 주석
    - 특별한 이유 없이 의무감으로 혹은 혹은 프로세스에서 하라고 하니까 마지못해 주석을 단다면 전적으로 시간낭비
    - 주석을 달기로 결정했다면 충분한 시간을 들여 최선의 주석을 달도록 노력
  - 같은 이야기를 중복하는 주석
    - 코드 내용과 같은 주석
    - 자칫하면 코드보다 주석을 읽는 시간이 더 오래 걸림
  - 오해할 여지가 있는 주석
    - 의도는 좋았으나 프로그래머가 딱 맞을 정도로 엄밀하게는 주석을 달지 못하는 경우도 있음
    - 주석에 담긴 '살짝 잘못된 정보'로 인해 잘못된 코드가 작성될 수 있음
  - 의무적으로 다는 주석
    - 코드를 복잡하게 만들며, 거짓말을 퍼뜨리고, 혼동과 무질서를 초래함
  - 있으나 마나 한 주석
    - 너무 당연한 사실을 언급하며 새로운 정보를 제공하지 못하는 주석
  - 위치를 표시하는 주석
    - 소스 파일에서 특정 위치를 표시하려 주석을 사용
    - 너무 자주 사용하지 않으면 배너는 눈에 띄며 주위를 환기시킬 수도 있음
    - 반드시 필요할 때만, 아주 드물게 사용하는 편이 좋음
  - 닫는 괄호에 다는 주석
    - 중첩이 심하고 장황한 함수라면 의미가 있을지도 모르지만 작고 캡슐화 된 함수에는 좋지 않음
    - 주석 대신 함수를 줄이려고 시도하자
  - 공로를 돌리거나 저자를 표시하는 주석
    - 소스 코드 관리 시스템이 다 기억해준다
  - 주석으로 처리한 코드
    - 주석으로 처리된 코드는 다름 사람이 지우기를 주저함
    - 소스 코드 관리 시스템이 다 기억해준다
  - 전역 정보
    - 주석을 달아야 한다면 근처에 있는 코드만 기술하라
    - 코드 일부에 주석을 달면서 시스템의 전반적인 정보를 기술하지 마라
  - 너무 많은 정보
    - 주석에다 흥미로운 역사나 관련없는 정보를 장황하게 늘어놓지 마라
  - 모호한 관계
    - 주석과 주석이 설명하는 코드는 둘 사이 관계가 명백해야 함
    - 이왕 공들여 주석을 달았다면 적어도 독자가 주석과 코드를 읽어보고 무슨 소린지 알 수 있어야 한다
  - 함수 헤더
    - 짧고 한 가지만 수행하며 이름을 잘 붙인 함수가 주석으로 헤더를 추가한 함수보다 훨씬 좋다


