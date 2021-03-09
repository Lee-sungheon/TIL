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