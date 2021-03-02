import styles from "./Hello.module.css"

export default function Hello() {
  function showName() {
    console.log("Mike")
  }
  function showAge(age) {
    console.log(age)
  }
  function showText(e) {
    console.log(e.target.value)
  }

  return (
    <div>
      <p>Hello</p>
      <button onClick={showName}>Show name</button>
      <button onClick={() => {
          showAge(30)
        }}
      >
        Show age
      </button>
      <input type="text" onChange={showText}></input>
      <div className={styles.box}>
      </div>
    </div>
  )
}