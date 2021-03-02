import dummy from "../db/data.json"
import Word from "./Word"
import { useParams } from "react-router-dom"
import { useEffect } from "react"

export default function Day() {
  let day = useParams().day
  day = Number(day)
  const wordList = dummy.words.filter(word => (
    word.day === day
  ))
  
  return <>
  <h2>Day {day}</h2>
  <table>
    <tbody>
      {wordList.map(word => (
        <Word word={word} key={word.id} />
      ))}
    </tbody>
  </table>
  </>
}