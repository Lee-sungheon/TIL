function LikeButton() {
  const [liked, setLiked] = React.useState(false);
  const text = liked ? '좋아요 취소' : '좋아요';
  // return React.createElement(
  //   'button',
  //   { onClick: () => setLiked(!liked)},
  //   text,
  // );
  return <button onClick={() => setLiked(!liked)}>{text}</button>;
}

// const domContainer1 = document.getElementById('root1');
// ReactDOM.render(React.createElement(LikeButton), domContainer1);
// const domContainer2 = document.getElementById('root2');
// ReactDOM.render(React.createElement(LikeButton), domContainer2);
// const domContainer3 = document.getElementById('root3');
// ReactDOM.render(React.createElement(LikeButton), domContainer3);

// const domContainer1 = document.getElementById('root');
// ReactDOM.render(
//   React.createElement(
//     'div',
//     null,
//     React.createElement(LikeButton),
//     React.createElement(LikeButton),
//     React.createElement(LikeButton),
//   ),
//   domContainer1,
// )
// React.createElement('div', null, 'hello')
// React.createElement('p', null, 'world')


function Container() {
  const [count, setCount] = React.useState(0);
  return (
    <div>
      <LikeButton />
      <div>
        <span>현재 카운트: </span>
        <span style={{ marginRight: 10 }}>{count}</span>
        <button onClick={() => setCount(count + 1)}>증가</button>
        <button onClick={() => setCount(count - 1)}>감소</button>
      </div>
    </div>
  )
}

const domContainer = document.getElementById('root');
ReactDOM.render(React.createElement(Container), domContainer);