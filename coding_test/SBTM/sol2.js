function solution(n) {
  var arr = [0, 1, 1, 2];
  if (n>3){
    for (var i=4 ; i < n+1 ; i++) {
      var sum_arr = 0;
      for (var j=1 ; j < i ; j++) {
        sum_arr += (arr[j] * arr[i-j]) % 10007;
      }
      arr.push(sum_arr % 10007);
    }
  }
  return arr[n];
}
console.log(solution(2));