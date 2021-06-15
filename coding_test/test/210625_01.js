function solution(n, capacity, files) {
  function dfs(start, drive, cnt, files, visit) {
    const sum = cnt.reduce((sum, cal_val) => {
      return sum + cal_val;
    }, 0);
    if (sum > answer) {
      answer = sum;
    }
    if (start >= files.length) {
      return;
    }
    for (let j = start; j < files.length; j++) {
      if (!visit[j]) {
        for (let i = 0; i < n; i++) {
          if (drive[i] - files[j] >= 0) {
            drive[i] -= files[j];
            cnt[i] += 1;
            visit[j] = true;
            dfs(start + 1, drive, cnt, files, visit);
            visit[j] = false;
            cnt[i] -= 1;
            drive[i] += files[j];
            dfs(start + 1, drive, cnt, files, visit);
          }
        }
      }
    }
    return;
  }

  var answer = -1;
  const drive = [];
  const cnt = [];
  const visit = [];
  for (let i = 0; i < n; i++) {
    drive.push(capacity);
    cnt.push(0);
  }
  for (let i = 0; i < files.length; i++) {
    visit.push(false);
  }
  dfs(0, drive, cnt, files, visit);
  return answer;
}

console.log(solution(1, 5, [1, 4, 5]));
console.log(solution(1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]));
// console.log(solution(10, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]));
