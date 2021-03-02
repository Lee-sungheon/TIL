import './App.css';
import Hello from './components/Hello';
import Hello2 from './components/Hello2';
import DayList from './components/DayList';
import Day from './components/Day';
import EmptyPage from './components/EmptyPage';
import styles from "./App.module.css"
import { BrowserRouter, Route, Switch } from "react-router-dom"

function App() { 
  const name = "Tom"
  const naver = {
    name: "네이버",
    url: "https://naver.com"
  }
  return (
    <BrowserRouter>
      <div className="App">
        <h1
          style={{
            color: "white",
            backgroundColor: "green"
          }}
        >
          Hello, {name}.
        </h1>
        <Switch>
          <Route exact path="/">
            {/* <a href={naver.url}>{naver.name}</a>
            <div className={styles.box}>
            </div>
            <Hello />
            <Hello2 age={10} money={200} /> */}
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

export default App;
