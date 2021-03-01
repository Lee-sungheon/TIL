## React JS

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

    

- state

  - 값을 관리해 DOM에 실시간으로 적용해줌

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

- 

