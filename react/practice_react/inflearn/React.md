##  리액트란 무엇인가

- 자동으로 업데이트 되는 UI
- UI = render(state)
- render 함수는 순수 함수로 작성
  - 랜덤 함수 사용 (x)
  - 외부 상태 변경 (x)
- state는 불변 변수로 관리
- 가상 돔(virtual dom)



## 바벨

- 자바스크립트 코드를 변환해 주는 컴파일러
- 최신 자바스크립트 문법을 지원하지 않는 환경에서도 최신 문법 사용 가능
- 그 외에도 다양한 용도로 사용
  - 코드에서 주석을 제거하거나 코드를 압축
- 리액트에서는 JSX 문법을 사용하기 위해 바벨을 사용



## 웹팩

- 다양한 기능 제공
  - 파일 내용을 기반으로 파일 이름에 해시값 추가  => 효율적으로 브라우저 캐싱 이용
  - 사용되지 않은 코드 제거
  - 자바스크립트 압축
  - JS에서 CSS, JSON, 텍스트 파일 등을 일반 모듈처럼 불러오기
  - 환경 변수 주입
  
- 웹팩을 사용하는 가장 큰 이유 => 모듈 시스템(ESM, commonJS)를 사용하고 싶어서

  - ESM : javascript를 import 로 사용할 수 있음

- 요즘 브라우저는 ESM을 지원
  - 오래된 브라우저는 지원 x
  - 많은 오픈 소스가 commonJS로 작성됨
  
  

## create-react-app

- 리액트 개발 환경을 직접 구축하려면 많은 지식과 노력이 필요
  - webpack, babel, jest, eslint, polyfill, HMR, CSS 후처리
- 페이스북에서 관리하는 공식 툴

- `npx create-react-app cre-test`

- CLI 명령어

  - start : 개발할 때 사용
    - HTTPS로 시작하고 싶을 때 : `set HTTPS=true&&npm start`
  - build : 배포할 때 사용
    - 빌드를 하게 되면 정적 파일이 생성됨
    - `npx serve -s build`
  - test 
    - `npm test`

  - eject : react-scripts를 사용하지 않고 모든 설정 파일을 추출
    - CRA 를 기반으로 추출하고 싶을 때 사용
    - 꼭 필요한 경우가 아니라면 관리측면에서 추출하지 않는것이 좋음

- polyfill

  - 웹 개발에서 기능을 지원하지 않는 웹 브라우저 상의 기능을 구현하는 코드
  - `caniuse` : 브라우저별 지원 현황을 보여주는 사이트
  - `index.js` 에서 `import 'core-js/features/string/pad-start;`

- 환경변수

  - 배포나 개발환경에 다른 값을 적용할 때 사용
  - 파일 이름 : `.env.변수 이름`
  - 코드 내에서 `process.env.{변수 이름}` or `env.{변수 이름}`으로 사용
  - `process.env.NODE_ENV` : 기본적으로 실행하는 환경변수
    - npm start로 실행하면 development
    - npm test로 실행하면 test
    - npm run build로 실행하면 production



## css 작성 방법

- 일반적 css 파일로 작성하기
  - 같은 이름의 css파일을 만들어 import 하는 방식
  - css 이름이 충돌할 수 있는 문제가 있음
- css-module로 작성
  - 이름충돌 문제를 해결할 수 있음
  - `이름.module.css` 형식으로 생성
    - `import Style from './파일이름.module.css`로 불러고 `${Style.cssname}` 으로 사용
  - `import cn from 'classnames'`
    - `{cn(Style.button, style.big)}` 과 같은 식으로 사용 가능
- Sass로 작성
  - `npm install node-sass`
  - css 파일을 scss로 변경해줘야함
  - `$name`으로 변수형식으로 사용해 다른 sass파일에서 사용 가능
- css-in-js로 작성
  - js파일 안에서 css를 사용 가능
  - js와 css를 다 아는 개발자라면 관리하기 간편



## 단일 페이지 애플리케이션 (SPA)

- SPA가 가능하기 위한 조건
  - 자바스크립트에서 브라우저로 페이지 전환 요청을 보낼 수 있다
    - 단, 브라우저는 서버로 요청을 보내지 않아야 한다
  - 브라우저의 뒤로 가기와 같은 사용자의 페이지 전환 요청을 자바스트립트에서 처리할 수 있다
    - 이때도 브라우저는 서버로 요청을 보내지 않아야 한다
- 위 조건을 만족시켜주는 브라우저 API
  - pushState, replaceState 함수
  - popState 이벤트
- react-router-dom
  - `npm install react-router-dom`
  - `import { BrowserRouter, Route, Link } from 'react-router-dom';`
  - Route로 랜더링을 하면 속성값으로 `match`를 넣어줌
    - `match.url` 로 url 확인 가능



## React 사용 Tip

- `memo`
  
  - `export default React.memo(변수명)` : 변수가 업데이트 되지 않으면 재랜더링 하지 않음
  - 실제 프로젝트 적용 해보기!
  
- `<React.Fragment>` : return 값에 <div>를 원하지 않을 때 사용 (축약형 : `<> </>`)

-  `portal ` 
  - modal에서 많이 쓰임
  - 다른 멀리 떨어진 엘리먼트에 랜더링 하고 싶을 때 사용  
  
  ```react
  import ReactDOM from 'react-dom';
  
  export default function App() {
      return (
      {ReactDOM.createPortal(
      	<div>
           	<p>안녕하세요</p>
       	</div>
       )}
  	)
  }
  ```
  
  

## 리액트 훅(hook)

- 컴포넌트에 기능을 추가할 때 사용하는 함수
  - ex) 컴포넌트에 상태값 추가, 자식 요소에 접근
  - 리액트 16.8에 새로 추가됨
    - 그 전에는 클래스 컴포넌트 사용
    - 클래스형 컴포넌트보다 장점이 많으며 리액트 팀에서도 훅에 집중하고 있음
- useState: 상태값 추가
  - 비동기 및 배치로 처리됨
  - setState 시, 객체는 덮어쓰는 방식으로 주소값을 바꿔줘야함
- useEffect: 부수효과 처리
  - 서버 API 호출, 이벤트 핸들러 등록 등
  - `useEffect(() => {}, [])` : `[]`는 의존성 배열
  - 함수에 사용하는 변수는 꼭 의존성 배열에 넣어줘야 함
- 커스텀훅:
  - use'Name'으로 설정해주는 것이 좋음
  - 일반적인 함수 형태로 작성
- 훅 사용 시 지켜야 할 규칠
  - 규칙 1 : 하나의 컴포넌트에서 훅을 호출하는 순서는 항상 같아야 함
    - 훅은 각 훅이 사용된 위치 정보를 기반으로 훅 정보를 관리함
  - 규칙 2 : 훅은 함수형 컴포넌트 또는 훅 안에서만 호출되어야 함

- 내장 훅
  - useRef 
  - useMemo
  - useCallback
  - useReducer
  - useImperativeHandle
  - useLayoutEffect
    - 특별한 이유가 없다면 useEffect를 사용(성능)
    - 동기 방식
    - 리액트가 랜더링을 하고 실제돔에 반영된 후에 함수가 실행됨
  - useDebugValue  



## Context

- 사용법

  ```react
  { createContext, useContext } from 'react'
  const UserContext = createContext('unknown')
  
  ...
  	const [name, setName] = useState('mike')
  	return(
          ...
          <UserContext.Provider value={name}>
              <Name>
          </UserContext.Provider>
          ...
      )
  
  ...
  
  	const user = useContext(UserContent)
  	return (
  		<p>{username}님 안녕하세요</p>
      )
  	
  ```

- 랜더링은 해당 컴포너트만 된다



## Ref

- 사용법

  ```react
  import {useRef} from 'react';
  
  ...
  	const inputRef = useRef();
  	useEffect(() => {
          inputRef.current.focus();
      }, []);
  	
  	return (
      	<div>
          	<input type="text" ref={inputRef} />
              <Box ref={inputRef} />
              <button>저장</button>
          </div>
      )
  ```

- useRef() 를 사용할 때는 컴포넌트 안에서 바로 사용하지 말고 useEffect() 안에서 사용해줘야함

## 컴포넌트 파일 작성법

- 컴포넌트 파일 작성법

  ```react
  MyComponent.propTypes = {
      // ...
  }; // 타입스크립트시 필요 x
  
  export default function MyComponent({ pro1, prop2 }){
      // 함수 이름을 명시해줘야 개발자 도구에서 확인이 가능함
      // 매개변수는 명명된 매개변수 문법으로 작성하는 것을 추천
  }
  
  const COLUMNES = [
      // 변수는 외부에서 만들어서 사용하는 것이 성능상 좋음 (재랜더링을 안함)
  ];
  
  const URL_PRODUCT_LIST = '/api/products'; // 변수 이름은 대문자로
  function getTotalPrice({ price, total }){
      // 변수나 함수는 중요도가 적으니 밑에 몰아서 작성해주는 것이 좋음
  }
  ```

  ```react
  function Profile( { userId }) {
      const [user, setUser] = userState(null);
      useEffect (() => {
          getUserApi(userId).then(data => setUser(data));
      }, [userId]);
      
      //const [user, setUser] = userState(null);
      //useEffect (() => {
      //    getUserApi(userId).then(data => setUser(data));
      //}, [userId]);
      const user = useUser(userId);
  }
  
  // State와 Effect는 기능에 맞춰서 분리해주어야 나중에 custom hook으로 분리하기도 편함
  // 컴포넌트 코드가 복잡해지면 custom hook으로 분리하는 것을 추천
  ```

- proTypes 작성법

  - 설치 : `npm install prop-types`
  - 타입이 중요한 이유 : 큰 규모의 프로젝트를 작성할 때 생산성을 높이기 위해 정적 타입 언어를 사용하는 것이 좋음

  ```react
  import PropTypes from 'prop-types';
  
  User.propTypes = {
      male: PropTypes.bool.isRequired, //isRequired : 필수데이터
      age: PropTypes.number,
      type: PropTypes.oneOf(['gold', 'silver', 'bronze']),
      onChangeName: PropTypes.func, // (name: string) 함수의 매개변수도 주석으로 명시
      onChangeTitle: PropTypes.func.isRequired,
  }
  ```

- 컴포넌트 분류 기준

  - container :  비즈니스 로직과 상태값을 관리하고 있는 경우
  - component : 비즈니스 로직과 상태값은 관리하고 있지 않는 경우



## 렌더링 최적화

- 리액트 렌더링 과정 : component => 가상 돔과 비교 => 실제 돔에 반영
- object의 비교는 불변 변수를 사용하면 단순 비교만으로도 알 수 있음 (덮어 써서 레퍼런스가 변하기 때문)
-  useMemo, useCallback, memo 사용으로 최적화 -> but 처음부터 설계해서 하면 가독성이 떨어지므로 성능이슈가 생겼을 때 그부분만 리팩토링 하는 것을 추천
- type을 바꾸는 상황이라면 if return / else return 보다 조건부 렌더링이나 삼항연산자가 더 최적화
- key 속성 값을 입력하면 리액트는 같은 key 속성을 가진 값들끼리만 비교함



## 리덕스

- 컴포넌트 코드로부터 상태 관리 코드를 분리할 수 있음

- 미들웨어를 활용한 다양한 기능 추가

  - 강력한 미들웨어 라이브러리 (ex. redux-saga)
  - 로컬 스토리지에 데이터 저장하기 및 불러오기

- SSR 시 데이터 전달이 간편하다

- 리액트 콘텍스트보다 효율적인 렌더링 가능

- 구조

  - 액션 -> 미들웨어 -> 리듀서 -> 스토어 -> 뷰 -> 액션

  - 액션 

    - type 속성 값을 가지고 있는 객체
    - `{type: 'type' , ... }`
    - action creater를 만들어줘서 사용하는 것을 권장

  - 미들웨어

    - `const myMiddleware = store => next => action => next(action);`
    - store 와 action은 연결해줌

  - 리듀서

    - 액션이 발생했을 때 새로운 상태값을 만드는 함수

    - 상태값은 불변 상태로 관리해야함

    - immer 

      - 불변 객체를 수정할 때 유용

      ```react
      import produce from 'immer';
      
      function reducer(state = INITIAL_STATE, action ) {
          return produce(state, draft => {
            switch (action.type) {
              case ADD:
                  draft.todos.push(action.todo);
                  break;
              case REMOVE_ALL:
                  draft.todos = [];
                  break;
            }
          });
      }
      ```

    - 사용시 주의 사항

      - 서버 API 호출 하지 말 것
      - random, time 함수같은 랜덤 값을 사용하지 말 것 -> 필요하다면 action 객체에서 생성

    - createReducer

      ```react
      // 기본 형태
      function createReducer(initialState, handlerMap) {
          return function (state = initialState, action) {
              return produce(state, draft => {
                  const handler = handlerMap[action.type];
                  if (handler) {
                      handler(draft, action)
                  }
              })
          }
      }
      
      // 활용
      const reducer = createReducer(INITIAL_STATE, {
          [ADD]: (state, action) => state.todos.push(action.todo),
          [REMOVE_ALL]: state => (state.todos = [])
      });
      ```

      

  - 스토어

    - `createStore`을 사용

    - 상태값을 저장 / 액션 처리가 끝났음을 외부에 알려주는 역할

      ```react
      import React from 'react';
      import { createStore } from 'redux';
      import { createReducer } from './redux-helper'
      
      export default function App() {
          return <div>실전 리액트</div>;
      }
      
      const INITIAL_STATE = { value: 0 };
      const reducer = createReducer(INITIAL_STATE, {
          INCREMENT: state => (state.value += 1),
      });
      const store = createStore(reducer);
      
      let prevState;
      store.subscribe(() => {
          const state = store.getState();
          if (state === prevState) {
              console.log('상태값 같음');
          } else {
              console.log('상태값 변경됨');
          }
          prevState = state;
      });
      
      store.dispatch({ type: 'INCREMENT' });
      store.dispatch({ type: 'OTHER_ACTION' });
      ```

      



## 리덕스에서 비동기 처리

- redux-thunk
  - 비동기 로직이 간단할 때 사용
  - 가장 간단하게 시작할 수 있음
- redux-observable
  - 비동기 코드가 많을 때 사용
  - RxJS 패키지를 기반으로 만들어짐
    - 리액티브 프로그래밍을 공부해야하므로 진입장벽이 가장 높음
- redux-saga
  - 비동기 코드가 많을 때 사용
  - 제너레이터를 적극적으로 활용함
  - 테스트 코드 작성이 쉬움



- debounce -> 실시간 검색창에 사용하면 될듯