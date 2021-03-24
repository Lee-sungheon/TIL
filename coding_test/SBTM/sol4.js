function solution(board) {
  function check(board, value1, value2) {
    for (var i=0 ; i<len ; i++){
      var cnt1 = 0
      var cnt2 = 0
      for (var j=0 ; j<len ; j++){
        if (board[i][j] === value1){
          cnt1++
          if (cnt1 >= 3){
            return true
          }
        } else {
          cnt1 = 0
        }
        if (board[i][j] === value2){
          cnt2++
          if (cnt2 >= 3){
            return true
          }
        } else {
          cnt2 = 0
        }
      }
    }
    for (var i=0 ; i<len ; i++){
      var cnt1 = 0
      var cnt2 = 0
      for (var j=0 ; j<len ; j++){
        if (board[j][i] === value1){
          cnt1++
          if (cnt1 >= 3){
            return true
          }
        } else {
          cnt1 = 0
        }
        if (board[j][i] === value2){
          cnt2++
          if (cnt2 >= 3){
            return true
          }
        } else {
          cnt2 = 0
        }
      }
    }
  }

  var answer = 0;
  const len = board.length;
  const result = []
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  for (var i=0 ; i<len ; i++){
    for (var j=0 ; j<len ; j++){
      for (var del of delta){
        var dx = j + del[0]
        var dy = i + del[1]
        if (dx < 0 || dy < 0 || dx >= len || dy >= len) {
          continue
        }
        [board[i][j], board[dy][dx]] = [board[dy][dx], board[i][j]]
        if (check(board, board[i][j], board[dy][dx]) === true) {
          result.push([[i, j], [dy, dx]])
        }
        [board[i][j], board[dy][dx]] = [board[dy][dx], board[i][j]]
      }
    }
  }

  if (result.length === 0) {
    answer = -1
  } else {
    answer = result.length/2
  }
  for (var i=0 ; i<result.length ; i++) {

  }
  return answer;
}

solution([[1,1,4,3],[3,2,1,4],[3,1,4,2],[2,1,3,3]])
solution([[1,2,1,2],[3,4,3,4],[1,2,1,2],[3,4,3,4]])