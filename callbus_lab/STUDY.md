## STUDY

#### ZARITLAK

- **빌드 후 Notion 캘린더에 일정 추가하기!**



#### Commitlint

- https://www.conventionalcommits.org/en/v1.0.0/#summary
- https://github.com/commitizen/cz-cli
- 커밋 메시지에 대해서 lint를 할 수 있게 해주는 툴
- 커밋 메시지를 규격화해서 작성하면 커밋 메시지를 바탕으로 `CHANGELOG` 나 `Release Notes` 를 자동으로 작성하게 할 수 있음



#### yarn2

- 서버 시작

  ```bash
  yarn workspace @zaritalk/host start
  ```

- [Yarn Berry](https://toss.tech/article/node-modules-and-yarn-berry)



#### AWS

- tinypng => 이미지 압축
- cache control



#### Git

- type 정리
  - `feature` : 새로운 기능 추가
  - `fix` : 버그 수정
  - `docs` : 문서 수정
  - `test` : 테스트 코드 추가
  - `refactor` : 코드 리팩토링
  - `style` : 코드 의미에 영향을 주지 않는 변경사항
  - `chore` : 빌드 부분 혹은 패키지 매니저 수정사항

- 작업하는 도중 브랜치 최신화를 해야할 때?

  1. `dev` 브랜치로 이동

     ```bash
     git checkout host/dev
     ```

  2. 작업중인 내용물을 임시 저장소에 저장

     ```bash
     git stash
     git stash list
     ```

  3. 로컬 저장소 최신화

     ```bash
     git pull
     ```

  4. 작업하는 브랜치로 이동 후 머지 작업

     ```bash
     git checkout ZARI-221
     git merge host/dev
     ```

  5. 작업중인 내용물 pop하기

     ```bash
     git stash pop
     ```

- Git push 방법 (commitlint 양식에 맞춰서)

  1. 파일 추가 => `add .` 말고 `add *` 로 하기 => .파일을 추가하면 다른 유저의 세팅 정보가 바뀔 수 있으므로 따로 추가 권장

     ```bash
     git add *
     ```

  2. 커밋 작업 시작

     ```bash
     yarn commit
     ```

     ![스크린샷 2021-07-07 오후 3.46.10](STUDY.assets/스크린샷 2021-07-07 오후 3.46.10.png)

  3. push 하기

     ```bash
     git push origin ZARI-221
     ```

  4. PR 시, **merge 위치** 바꾸기! (host/dev)

- Git merge 종류

  - merge(일반 머지)

    - 하나의 브랜치와 다른 브랜치의 변경 이력 전체를 합치는 방법

    ```bash
    git checkout master
    git merge my-branch
    ```

    ![스크린샷 2021-07-12 오후 6.00.36](STUDY.assets/스크린샷 2021-07-12 오후 6.00.36.png)

  - Squash and Merge

    - 병합하고자 하는 브랜치의 commit을 하나로 합쳐서 새로운 commit을 만들고 Target 브랜치에 추가됨
    - feature 브랜치의 commit history를 합쳐서 깔끔하게 만들기 위해 사용

    ```bash
    git checkout master
    git merge --squash my-branch
    git commit -m 'your-commit-message'
    ```

  ![스크린샷 2021-07-12 오후 6.01.59](../Desktop/스크린샷 2021-07-12 오후 6.01.59.png)

  - Rebase and Merge

    - 모든 commit들이 합쳐지지 않고 각각 Target 브랜치에 추가
    - 각 commit들은 하나의 parent를 가짐

    ```bash
    git checkout my-branch
    git rebase master
    git checkout master
    git merge my-branch
    ```

    ![스크린샷 2021-07-12 오후 6.05.11](STUDY.assets/스크린샷 2021-07-12 오후 6.05.11.png)

#### WebStorm

- 단축키

  - 새 파일 생성 : `control + return`
  - 파일 이름 변경 : `shift + F6`
  - 터미널창 열기 : `option(alt) + F12`
  - 소스 포맷하기 : `option + command + L`

  - lint 실행(커스텀) : `option+ shift + L`
  - preference 열기 : `command + ,`
  - 한 줄 라인 없애기 : `command + delete`
  - 라인 합치기 : `control + shift + J`
  - 현재줄에서 커서 유지하면서 다음줄 새로 생성하기 : `command + return`
  - 윗줄로 새로운 라인으로 줄바꿈하기 : `command + option(alt) +  return`
  - 한 줄 복사하기 : `command + d`
  - 대소문자 토글하기 : `command + shift + U`
  - 코드 선택적 remove : `command + shift + delete`
  - 코드 라인 소스포맷팅하면서 상하로 옮기기 : `shift + command + 방향키(상하)`
  - 한 줄 주석 처리 : `command + /`
  - 범위 주석 처리 : `command + opt(alt) + /`
  - 최근 복사 목록 : `command + shift + v`
  - 커서 뒤의 코드 모두 지움 : `control + k`
  - 드래그한 블럭과 일치하는 코드 모두 선택 : `command + control + g`
  - 파일 찾기 : `command + shift + O`
  - 심볼 찾기 : `command + opt(alt) + O`
  - 파일간 이동 : `control + tab`
  - 최근 열었던 파일 목록 : `command + E`
  - 프로젝트 안에서 해당 단어가 들어가는 파일 찾기 : `option + F7`
  - 파일 안에서 해당 단어가 들어가 있는 요소 찾기 : `command + F7`





**React-hook-form 공부하기**

