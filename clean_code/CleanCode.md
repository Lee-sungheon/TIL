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
