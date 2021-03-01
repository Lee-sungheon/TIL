import './App.css';
import Hello from './component/Hello';
import Hello2 from './component/Hello2';
import DayList from './component/DayList';
import Day from './component/Day';
import styles from "./App.module.css"

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
      <div className={styles.box}>
      </div>
      <Hello />
      <Hello2 age={10} money={200} />
      <Hello2 age={20} />
      <Hello2 age={30} />
      <DayList />
      <Day />
    </div>
  );
}

export default App;
