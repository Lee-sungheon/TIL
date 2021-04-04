function solution(gift_cards, wants) {
  function binarySearch (target, dataArray) {
    let low = 0;
    let high = dataArray.length - 1;
    while (low <= high) {
      let mid = Math.floor((high + low) / 2);
      let guess = dataArray[mid];
      if (guess === target && !visitCard[guess] ) {
        return guess;
      } else if (guess > target) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return -1;
  }

  var answer = 0;
  const n = gift_cards.length;
  gift_cards.sort(function(a, b){ return a-b; });
  wants.sort(function(a, b){ return a-b; });

  const visit = [];
  const visitCard = [];
  for (let i=0; i<n; i++){
    visit.push(false);
    visitCard.push(false);
  }
  for (let i=0; i<n; i++){
    if (gift_cards[i] === wants[i]){
      visit[i] = true;
      visitCard[i] = true;
    }
  }
  for (let i=0; i<n; i++){
    if (!visit[i]){
      const result = binarySearch(gift_cards[i], wants)
      if (result >= 0){
        [gift_cards[i], gift_cards[result]] = [gift_cards[result], gift_cards[i]]
        visit[i] = true;
        visitCard[result] = true;
      }
    }
  }
  for (let i=0; i<n; i++){
    if (!visit[i]) {answer++;}
  }
  console.log(answer)
  return answer;
}

solution([4, 5, 3, 2, 1], [2, 4, 4, 5, 1])
solution([5, 4, 5, 4, 5], [1, 2, 3, 5, 4])