import { useState } from "react";
import UserName from "./UserName";

export default function Hello2(props) {
  // let name = "Mike"
  console.log(props)
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
