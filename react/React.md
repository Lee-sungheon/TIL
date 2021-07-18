## React JS

- #### React.JS의 장점은?

  - 학습이 간단하다. 컴포넌트만을 사용하기 때문에 복잡하지 않음.
  - 가상 DOM(**Virtual DOM**)을 사용한다.
  - 뛰어난 Garbage Collection, 메모리관리, 성능.
  - UI를 **컴포넌트**화 하여 **매우 간편한** UI 수정 및 재사용.
  - 페이스북 개발자들이 만들어 페이스북에서 꾸준히 업데이트를 함 - 탄탄한 기반❗️
  - 다른 프레임워크나 라이브러리와 **혼용** 가능. 이미 개발이 완료된 서비스에도 적용이 가능.
  - ***서버 & 클라이언트 사이드 렌더링** 모두 지원

- 시작

  ```
  npx create-react-app '이름'
  npm start
  ```

- index.js : vue.js의 index.js 역할

- App.js : vue.js의 App.js 역할

- index.html : vue.js의 index.html 역할

- JSX 

  ```react
  function App() {
    const name = "Tom"
    const naver = {
      name: "네이버",
      url: "https://naver.com"
    }
    return (
      <div className="App">
        <h1
          style={{
            color: "white",
            backgroundColor: "green"
          }}
        >
          Hello, {name}.
        </h1>
        <a href={naver.url}>{naver.name}</a>
      </div>
    );
  }
  
  // return 되는 부분을 JSX라고 하며, HTML 코드와 비슷하게 들어감
  ```

- 컴포넌트

  - src의 component 폴더안에 생성

  - 생성법

    ```react
    const Hello = function() {
      return <p>Hello</p>
    }
    export default Hello
    ```

    ```react
    const Hello = () => {
      return <p>Hello</p>
    }
    export default Hello
    ```

    ```react
    export default function Hello() {
      return <p>Hello</p>
    }
    ```

- CSS

  - Object 형태로 나타냄

  - Camel Case로 작성 

  - 방법

    - Inline (특별한 이유없인 사용 X)

    ```react
    <h1 style={
            {
                color: 'white',
                backgroundColor: 'green',
               	borderRight: '2px',
                opacity: 1
            }
        }>Hello</h1>
    ```

    - index.css -> 전체 프로젝트에 영향

    - App.css -> 앱에 영향

    - css간 overiding 및 중복을 피하려면 module화가 필요!

      ```css
      'Hello.module.css'
      
      .box {
        width: 200px;
        height: 50px;
        background-color: blue;
      } 
      ```

      ```react
      'Hello.js'
      
      import styles from "./Hello.module.css"
      
      export default function Hello() {
        return (
          <div className={styles.box}>
            <p>Hello</p>
          </div>
        )
      }
      ```

- 이벤트

  - Binding : `{}`  이용

  - Modeling  : `onChange`

    ```react
    function showText(e) {
      console.log(e.target.value)
    }
    
    <input type="text" onChange={showText}></input>
    ```

  - Click : `onClick`

    ```react
      function showAge(age) {
        console.log(age)
      }
      <button onClick={() => {
            showAge(30)
        }}
          >
        Show age
      </button>
    ```

    

- state -> 함수와 hook을 사용함 (원래는 클래스와 State를 함꼐 사용했음)

  - `useState` : 값을 관리 및 변경하기 위함, 이 값은 DOM에 실시간으로 적용해줌

    ```react
    import { useState } from "react";
    
    export default function Hello2() {
      // let name = "Mike"
      const [name, setName] = useState('Mike')
    
      function changeName() {
        const newName = name === "Mike" ? "Jane" : "Mike"
        setName(newName)
      }
    
      return (
        <div>
          <h1>state</h1>
          <h2>{name}</h2>
          <button onClick={changeName}>change</button>
        </div>
      )
    }
    ```

  - `useEffect` : 값이 변경되었을 때 함수를 실행시킴

    ```react
    import { useEffect, useState } from "react"
    
    export default function Word({ word }) {
      const [isShow, setIsShow] = useState(false)
      const [isDone, setIsDone] = useState(word.isDone)
    
      function toggleShow() {
        setIsShow(!isShow)
      }
      function toggleDone() {
        setIsDone(!isDone)
      }
    
      useEffect(function() {
        console.log("Change")
      }, [isShow])
    
      return (
        <tr className={isDone ? "off":""}>
          <td>
            <input type="checkbox" checked={isDone}
            onChange={toggleDone}/>
          </td>
          <td>
            <button onClick={toggleShow}>뜻 {
              isShow ? "숨기기": "보기"}</button>
            <button className="btn_del">삭제</button>
          </td>
        </tr>
      )
    }
    ```

  - `Custom Hooks ` : 자신만의 custom hook을 만들 수 있음 - > 재활용에 용이,  `use커스텀명`의 형태

  

- props

  - 값을 하위 컴포넌트에 전달

    ```react
    import './App.css';
    import Hello2 from './component/Hello2';
    
    function App() { 
      return (
        <div className="App">
          <Hello2 age={10} money={200}/>
          <Hello2 age={20} />
          <Hello2 age={30} />
        </div>
      );
    }
    
    export default App;
    ```

    ```react
    import { useState } from "react";
    import UserName from "./UserName";
    
    export default function Hello2(props) {
      const [name, setName] = useState('Mike')
      const [age, setAge] = useState(props.age)
    
      function changeName() {
        const newName = name === "Mike" ? "Jane" : "Mike"
        setName(newName)
        setAge(age + 5)
      }
        
      return (
        <div>
          <h1>state</h1>
          <h2>{name}({age}세)</h2>
          <UserName name={name} age={age} />
          <button onClick={changeName}>change</button>
        </div>
      )
    }
    ```

    ```react
    export default function UserName(props){
      return <p>Hello, {props.name} {props.age}</p>
    }
    ```

- for 문

  - map() 및 filter() 를 이용하여 구현

    ```react
    import dummy from "../db/data.json"
    
    export default function Day() {
      const day = 1
      const wordList = dummy.words.filter(word => (
        word.day === day
      ))
    
      return <>
      <table>
        <tbody>
          {wordList.map(word => (
            <tr>
              <td>
                {word.eng}  
              </td>
              <td>
                {word.kor}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      </>
    }
    ```

- 라우터

  - npm 설치 필요

  ```bash
  npm install react-router-dom
  ```

  - `BrouserRouter` 안에 JSX를 넣고 라우팅에 의해 바뀌는 부분은 `Switch` 안에 위치
  - `exact` : 주어진 경로와 정확히 맞아 떨어져야만 설정한 컴포넌트를 보여줌

  ```react
  import { BrowserRouter, Route, Switch } from "react-router-dom"
  
  function App() {
    return (
      <BrowserRouter>
        <div className="App">
          <h1>Hello, {name}</h1> {/* 헤더 자리 */}
          <Switch>
            <Route exact path="/">
              <DayList />
            </Route>
            <Route path="/day/:day">
              <Day />
            </Route>
            {/* 페이지가 잘못된 경로로 접근했을 때 최종 처리 -> 끝에 있어야함 */}
            <Route>
              <EmptyPage />
            </Route>
          </Switch> 
        </div>
      </BrowserRouter>
    );
  }
  ```

  - routing를 해줄 때는 `Link to` 를 사용
  - route 강제 이동 : `histroy.push(‘/인자’)`

  ```react
  import { Link } from "react-router-dom"
  import dummy from "../db/data.json"
  
  export default function DayList() {
    console.log(dummy)
    return <ul className="list_day">
      {dummy.days.map(day => (
        <li key={day.id}>
          <Link to={`/day/${day.day}`}>Day {day.day}</Link>
        </li>
      ))}
    </ul>
  }
  ```

  - 값을 받을 때는 `useParams()` 를 사용하여줌

  ```react
  import dummy from "../db/data.json"
  import { useParams } from "react-router-dom"
  
  export default function Day() {
    let day = useParams().day
    day = Number(day)
    const wordList = dummy.words.filter(word => (
      word.day === day
    ))
  
    return <>
    </>
  }
  ```

  

#### repaint / reflow

`repaint`는 색상이 변경되거나 글자의 내용이 바뀌었을 때 발생되는 연산이다. `reflow`는 하나의 DOM객체의 크기나 위치가 변경되엇 을 때(레이아웃의 변경작업), 다른 DOM객체들의 위치와 크기가 함께 변경하는것을 말한다.



#### React Hook Form

- 공식 페이지
  - https://react-hook-form.com/
- 특징
  - DX(develper Experience)
    - 코드의 양을 줄여줌
    - forms를 만들 때 직관적인 경험을 제공
  - HTML standard
    - 기존 HTML 마크업을 활용
    - 조건 기반 유효성 검사
  - Super Light
    - 패키지 사이즈가 작고 다른 의존관계를 가지지 않은 작은 라이브러리
  - Performance
    - Re-renders를 최소하 하며, 빠른 마운팅을 통한 뛰어난 UX를 제공
  - Adoptable
    - form의 state는 local에서 관리되기 떄문에 다른 의존성 없이 쉽게 적용 가능



