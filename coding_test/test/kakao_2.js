function solution(needs, r) {
  function combination(source, target, n, r, count) {
    if(r === 0)final.push(target);
    else if(n === 0 || n < r) return;
    else {
        target.push(source[count]);
        combination(source, Object.assign([], target), n - 1, r - 1, count + 1);
        target.pop();
        combination(source, Object.assign([], target), n - 1, r, count + 1);
      }
  }

  var answer = 0;
  const n = needs.length;
  const partN = needs[0].length;
  const newNeeds = []
  const source = []
  for (let i=0 ; i<n ; i++){
    const tmp = [];
    for (let j=0 ; j<partN ; j++){
      if (needs[i][j] === 1){
        tmp.push(j);
      }
    }
    newNeeds.push(tmp);
  }
  for (let i=0 ; i<partN; i++){
    source.push(i);
  }
  const final = [];
  combination(source, [], partN, r, 0);

  for (let item of final){
    let cnt = 0;
    for (let need of newNeeds){
      let isBreak = false;
      for (let i=0 ; i<need.length ; i++){
        if (item.indexOf(need[i]) === -1){
          isBreak = true;
          break
        }
      }
      if (!isBreak) {
        cnt +=1
      }
    }
    if (answer < cnt){ answer = cnt; }
  }
  return answer;
}

console.log(solution([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ], 2))