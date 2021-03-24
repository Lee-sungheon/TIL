function solution(office, k) {
  var answer = 0;
  const len = office.length;
  for (var i=0 ; i<len-k+1 ; i++){
    for (var j=0 ; j<len-k+1 ; j++){
      var num = 0;
      for (var m=i ; m<i+k; m++){
        for (var n=j ; n<j+k; n++) {
          if (office[m][n] == 1) {
            num ++;
          }
        }
      }
      if (answer < num) {
        answer = num
      }
    }
  }
  return answer;
}

solution([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]], 2)