function solution(r, d, xArr, yArr)
{   
    function dfs(a, b){
        if (a+b+2*r > answer){
            answer = a+b+2*r;
        }
        for (let i=0 ; i<xArr.length ; i++){
            if (!visited[i]){
                const endPoint = [[a-d, b], [a-d, b+r], [a, b+r+d], [a+r, b+r+d], [a+r+d, b+r], [a+r+d, b], [a+r, b-d], [a, b-d]];
                for (let end of endPoint){
                    if (end[0] >= xArr[i] && end[0] <= xArr[i]+r && end[1] >= yArr[i] && end[1] <= yArr[i]+r){
                        visited[i] = true;
                        dfs(xArr[i], yArr[i]);
                        break; 
                    }
                }
            }
        }
    }
    var answer = 0;
    const visited = [];
    for (let i=0 ; i<xArr.length ; i++){
        visited.push(false);
    }
    visited[0] = true;
    dfs(0, 0);
    
    return answer;
}

solution(
  4,
  1,
  [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);
