## 테스트를 하는 이유

- 왜 어플리케이션을 테스트 해야 할까?
  - 더 안정적인 어플리케이션을 위해서
- 테스팅으로 얻는 이점
  - 디버깅 시간을 단축
    - 만약 데이터가 잘못 나왔다면 그것이 UI의 문제인지 DB의 문제인지 전부 테스트를 해봐서 찾아야 함
    - 테스팅 환경이 구축 돼 있다면 자동화 된 유닛 테스팅으로 특정 버그를 쉽게 찾아낼 수 있음
  - 더욱 안정적인 어플리케이션
    - 많은 테스트 코드와 함께 작성된 코드의 어플리케이션이 되기 때문에 훨씬 안정적인 어플리케이션이 됨
  - 재설계 시간의 단축, 추가로 무언가를 더 구현해야 할 때 더 용이하게 할 수 있음



## React Testing Library

- React Testing Library란?

  - https://testing-library.com/docs/react-testing-library/intro/

  - React 구성 요소 작업을 위한 API를 추가하여 DOM Testing Library 위에 구축됨

  - DOM Testing Library란 Dom 노드(Node)를 테스트하기 위한 매우 가벼운 솔루션

  - Create React App으로 생성된 프로젝트는 즉시 React Testing Library를 지원함. 그렇지 않은 경우 다음과 같이 npm을 통 해 추가할 수 있음

    ```bash
    npm install --save-dev @testing-library/react
    ```

  - React Testing Library는 에어비앤비에서 만든 Enzyme을 대처하는 솔루션![스크린샷 2022-09-09 오후 4.15.36](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-09 오후 4.15.36.png)

​			![스크린샷 2022-09-09 오후 4.18.03](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-09 오후 4.18.03.png)



## Dom 이란?

- DOM (Document Object Model)

  - DOM(문서 객체 모델)은 XML, HTML 문서의 각 항목을 계층으로 표현하여 생성, 변형 삭제할 수 있도록 돕는 인터페이스 - 위키피디아

- 웹 페이지 빌드 과정(Critical Rendering Path : CRP)

  - 브라우저가 서버에서 페이지에 대한 HTML 응답을 받고 화면에 표시하기 전에 여러 단계가 있음

  - 웹 브라우저가 HTML 문서를 읽고, 스타일을 입히고, 뷰포트에 표시하는 과정 

    ![스크린샷 2022-09-09 오후 4.29.42](/Users/iseongheon/Desktop/스크린샷 2022-09-09 오후 4.29.42.png)

    ![스크린샷 2022-09-09 오후 4.31.09](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-09 오후 4.31.09.png)

    

![스크린샷 2022-09-09 오후 4.32.56](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-09 오후 4.32.56.png)

- DOM이란?
  - HTML 요소들의 구조화된 표현
  - DOM은 HTML이 브라우저의 렌더링 엔진에 의해 분석되고 분석이 모두 끝나고난 HTMl 파일
  - HTML은 화면에 보이고자 하는 모양과 구조를 문서로 만들어서 단순 텍스트로 구성되어있으며 DOM은 HTML문서의 내용과 구조가 객체 모델로 변화되어 다양한 프로그램에서 사용될 수 있음
  - HTML 문서가 유효하지 않게 작성됐을때는 브라우저가 올바르게 교정해주며, DOM은 자바스크립트에 의해 수정될 수 있음. 하지만 HTML은 수정하지 않음.



## Jest

- Jest

  - Meta에 의해서 만들어진 테스팅 프레임 워크
  - 최소한의 설정으로 동작하며 Test Case를 만들어서 어플리케이션 코드가 잘 돌아가는지 확인해줌
  - 단위(Unit) 테스트를 위해서 이용

- Jest 시작하기

  - 라이브러리 설치

    ```bash
    npm install jest --save-dev
    ```

  - Test 스크립트 변경

  - 테스트 작성할 폴더 및 파일 기본 구조 생성

    ![스크린샷 2022-09-09 오후 5.23.28](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-09 오후 5.23.28.png)

    ![스크린샷 2022-09-09 오후 5.23.37](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-09 오후 5.23.37.png)



## Jest 파일 구조 & 사용법

- describe : 여러 관련 테스트를 그룹화하는 블록을 만듬
- it (= test) : 개별 테스트를 수행하는 곳. 각 테스트를 작은 문장처럼 설명
- expect : 값을 테스트할 때마다 사용하는 함수. 혼자서는 거의 사용되지 않으며 matcher와 함께 사용됨
- matcher : 다른 방법으로 값을 테스트하도록 'matcher'를 사용 



## React Testing Library 주요 API

- render 함수
  - DOM에 컴포넌트를 랜더링하는 함수 인자로 랜더링할 React 컴포넌트가 들어감
  - Return은 RTL에서 제공하는 쿼리 함수와 기타 유틸리티 함수를 담고 있는 객체를 리턴(Destructuring 문법으로 원하는 쿼리 함수만 얻어올 수 있다.)  => 소스 코드가 복잡해지면 비추천
  - screen 객체를 사용하기 : 사용해야 할 쿼리가 많아질수록 코드가 복잡해질 수 있음



## 쿼리 함수

- 쿼리함수

  - 쿼리는 페이지에서 요소를 찾기 위해 테스트 라이브러리가 제공하는 방법
  - 여러 유형의 쿼리("get", "find", "query") 있음
  - 이들 간의 차이점은 요소가 발견되지 않으면 쿼리에서 오류가 발생하는지 또는 Promise를 반환하고 다시 시도하는지 여부

- get, fine, query 차이점

  - getBy
    - 쿼리에 일치하는 노드를 반환
    - 일치하는 요소가 없거나 둘 이상의 일치가 발견되면 설명 오류를 발생
    - 둘 이상의 요소가 예상되는 경우 대신 getAllBy 사용
  - queryBy
    - 쿼리에 대해 일치하는 노드를 반환하고 일치하는 요소가 없으면 null을 반환 (테스트 실패 X)
    - 둘 이상의 일치 항목이 발견되면 오류를 발생
    - 확인된 경우 대신 queryAllBy 사용
  - findBy
    - 주어진 쿼리와 일치하는 요소가 발견되면 Promise를 반환
    - 요소가 발견되지 않거나 기본 제한 시간인 1000ms 후에 둘 이상의 요소가 발견되면 약속이 거부됨
    - 둘 이상의 요소를 찾아야 하는 경우 findAllBy 사용
    - getBy + waitFor = findBy
  - waitFor
    - 일정 시간 동안 기다려야 할 때 waitFor을 사용하여 기대가 통과할 때까지 기다릴 수 있음

  ​	![스크린샷 2022-09-18 오전 2.07.57](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-09-18 오전 2.07.57.png)



## TDD

- TDD(Test Driven Development)

  - 실제 코드를 작성하기 전에 테스트 코드를 먼저 작성함

  - 테스트 코드를 작성 후 크 테스트 코드를 Pass 할 수 있는 실제 코드를 작성함

    ![스크린샷 2022-10-10 오후 4.18.58](/Users/iseongheon/Library/Application Support/typora-user-images/스크린샷 2022-10-10 오후 4.18.58.png)

  - TDD를 하면 좋은 점

    - TDD를 함으로 인해 많은 기능을 테스트하기에 소스 코드에 안정감이 부여된다
    - 실제 개발하면서 많은 시간이 소요되는 부분은 디버깅 부분이기에 TDD를 사용하면 디버깅 시간이 줄어들고 실제 개발 시간도 줄어듬
    - 소스 코드 하나하나를 더욱 신중하게 짤 수 있기 때문에 깨끗한 코드가 나올 확률이 높음




## Query 사용 우선 순위

- https://testing-library.com/docs/queries/about/#priority
- useEvent > fireEvent
  - userEvent는 fireEvent 를 사용해서 만들어짐
  - userEvent의 내부 코드를 보면 fireEvent를 사용하면서 엘리먼트의 타입에 따라서 Label을 클릭했을 때, checkbox, radio 을 클릭했을 때 그 엘리먼트 타입에 맞는 더욱 적절한 반응을 보여줌



