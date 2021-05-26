## Type Script

#### TypeScript vs JavaScript

- TypeScript
  - 정적 타입
  - 변수의 타입 -> 컴파일타임에 결정
  - Java, C++
  - 진입 장벽이 높음
  - 코드의 양이 많을 때 생산성이 높음
  - 타입 오류가 컴파일 시 발견
- JavaScript
  - 동적 타입
  - 변수의 타입 -> 런타임에 결정
  - Python, PHP
  - 진입 장벽이 낮음
  - 코드의 양이 적을 때 생산성이 높음
  - 타입 오류가 런타임 시 발견



#### TypeScript

- microsoft에서 개발

- 큰 생태계

- vscode와 좋은 궁합

- 설치

  ```bash
  // 설치
  npx tsc -init
  // 컴파일
  npx tsc
  // 실행
  node example.js
  ```

- Tip

  - Auto Import : command + .
  - 멀티 선택 : command + d / 취소 시 : esc
  - 멀티 커서 : command + option + 화살표



#### Tpye 정의

- 기본 타입

  - number, boolean, string, number[], [string, number], nudefined, null

  - 숫자와 문자의 리터럴도 타입으로 정의 가능 

    ```typescript
    let v1: 10 | 20 | 30;
    let v2: '경찰관' | '소방관';
    ```

  - any 

    - 모든 값을 포함하는 타입 
    - js 코드로 작성된 프로젝트를 ts로 포팅하는 경우에 유용
    - 단, 남발 시 ts를 사용하는 이유가 사라지므로 지양하는 것을 추천

  - void : 아무 것도 반환하지 않음

  - never : 예외 발생, 무한루프 반환 타입 => 거의 사용할 일 없음

- 함수

  ```typescript
  function getText(name: string, ...rest: number[]): string {
      return '';
  }
  ```

- 인터페이스

  - 객체 타입 정의

    - readonly : 읽기만 가능한 속성

      ```tsx
      interface Person {
          readonly name: string;
      }
      ```

      

    - 인덱스 타입 : 속성 이름을 구체적으로 정의하지 않고 값의 타입만 정의

      ```tsx
      interface Person {
          [key: string]: string | number;
      }
      ```

  - 함수 타입 정의

  - 클래스 정의

  - 인터페이스 확장

    ```tsx
    interface Person {
        name: string;
        age: number;
    }
    
    interface Programmer {
        favorite: stering;
    }
    
    interface Korean extends Person, Programmer {
        isLiveInSeoul: boolean;
    }
    ```

  - 교차 타입

    ```tsx
    interface Person {
        name: string;
        age: number;
    }
    
    interface Programmer {
        favorite: stering;
    }
    
    type PP = Person & Programmer
    
    const pp: PP = {
        name: 'a',
        age: 15,
        favorite: 'spring'
    }
    ```

#### 타입 호환성

-  

