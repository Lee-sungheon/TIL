## TIL - REACT

#### 210427

- React 페이지 새로고침 시 스크롤이 제일 위로 안올라가는 문제

- `window.onbeforeunload`를 사용하여 해결

  ```react
  useEffect(() => {
      window.onbeforeunload = () => {
      	window.scrollTo(0, 0);
  	};
  }, [])
  ```