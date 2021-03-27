function solution(customer, K) {
  const answer = [];
  const visit = [];
  for (let index = 0; index < 1000001; index++) {
    visit.push(0)
  }
  for (let index = 0; index < customer.length; index++) {
    if (customer[index][1] === 0) {
      visit[customer[index][0]] += 1
    }
  }
  for (let index = 0; index < customer.length; index++) {
    if (visit[customer[index][0]] > 0 && customer[index][1] === 1) {
      visit[customer[index][0]] -= 1
    }
    else {
      if (customer[index][1] === 0) {
        continue
      }
      if (answer.length === K) {
        break
      }
      answer.push(customer[index][0])
    }
  }
  return answer.sort(function(a, b){ return a-b; });
}

console.log(solution([[1,1],[2,1],[3,1],[2,0],[2,1]], 2))
console.log(solution([[2, 1], [3, 1], [4, 1], [3, 0], [1, 1], [2, 0], [4, 0], [2, 1]], 3))
console.log(solution([[3, 1], [4, 1], [4, 0], [3, 0], [2, 1], [1, 1]], 2))
