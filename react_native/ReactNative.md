## React Native

#### React Native

- Facebook에서 만든 오픈소스 프로젝트
- 2015년 3월
- 기존 하이브리드앱에서 겪던 성능문제 없이 JavaScript를 이용하여 ios, android 개발가능

- 장점
  - 쉬운 접근성 (JavaScript)
  - 비용 절감
  - Fast Refresh
- 단점
  - 네이티브 앱과의 성능 차이
  - 디버깅
- Bridge : js와 native 사이에서 통신을 담당해주는 역할



#### 프로젝트 생성

- Expo

  ```bash
  npm install -g expo-cli
  expo login
  expo init my-first-expo
  expo start
  ```



#### 컴포넌트 라이브러리

- https://nativebase.io/

- https://reactnativeelements.com/

  

#### 스타일링

```react
<Text style={[styles.text, { color: 'orange' }]}>Style Code</Text>
<Text style={[styles.text, styles.errorText]}>Error Text</Text>
```

style에서 배열을 활용하면 여러가지 스타일을 중복 적용 가능함



#### 스타일 컴포넌트

````react
import styled from "styled-components/native";

const Container = styled.View`
  flex-direction: row;
  align-items: center;
  background-color: ${({ theme }) => theme.itemBackground};
  border-radius: 10px;
  margin: 3px 0;
  padding: 5px;
`;
````



#### Platform

운영체제마다 다른 코드를 적용시키는 것이 가능

```react
import { StyleSheet, View, Platform, Text } from 'react-native';

const Shadow = () => {
    return (
    	<view style={styles.shadow}>
        	<Text>{Platform.OS === 'ios' ? 'ios' : 'android'} </Text>
        </view>
    )
}

const styles = StyleSheet.create({
    shadow: {
        width: 200,
        height: 200,
        ...Platform.select({
            ios: {
                backgroundColor: 'blue',
                shadowColor: '#000000',
                shadowOffset: {
                    width: 10,
                    height: 10,
                },
                shadowOpacity: 0.5,
                shadowRadius: 10,
            },
            android: {
                backgroundColor: 'green',
                elevations: 20,
            }
        })
    }
});

export default Shadow;
```

