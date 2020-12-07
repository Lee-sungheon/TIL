### Table Name : flights

| name       | data type |
| ---------- | --------- |
| flight_num | text      |
| departure  | text      |
| waypoint   | text      |
| arrival    | text      |
| price      | integer   |

| id   | flight_num | departure | waypoint | arrival | price |
| ---- | ---------- | --------- | -------- | ------- | ----- |
| 1    | RT9122     | Madrid    | Beijing  | Incheon | 200   |
| 2    | XZ0352     | LA        | Moscow   | Incheon | 800   |
| 3    | SQ0972     | London    | Beijing  | Sydney  | 500   |

#### 위 테이블을 바탕으로 아래 문제에 해당하는 SQL query 문을 작성하고 실행하세요.

1. flight 테이블을 생성하세요.

   ```sql
   CREATE TABLE flight (
   	flight_num TEXT NOT NULL,
       departure TEXT NOT NULL,
       waypoint TEXT NOT NULL,
       arrival TEXT NOT NULL,
       price INTEGER NOT NULL
   );
   ```

2. 데이터를 입력하세요.

   ```sql
   INSERT INTO flight VALUES('RT9122', 'Madrid', 'Beiging', 'Incheon', 200),
                            ('XZ0352', 'LA', 'Moscow', 'Incheon', 800),
                            ('SQ0972', 'London', 'Beijing', 'Sydney', 500);
   ```

3. flights 테이블 전체 데이터를 조회하세요.

   ```sql
   SELECT * FROM flight;
   ```

4. 모든 waypoint를 조회하세요

   ```sql
   SELECT waypoint From flight;
   ```

5. 항공권 가격이 600 미만인 항공편들의 id와 flight_num을 조회하세요

   ```sql
   SELECT rowid, flight_num FROM flight WHERE price<600;
   ```

6. 도착지가 Incheon이고 가격이 500 이상인 항공편의 departure를 조회하세요.

   ```sql
   SELECT departure FROM flight WHERE arrival='Incheon' AND price>500;
   ```

7. 항공편 숫자부분이 0으로 시작하고 2로 끝나면서 경유지가 Beijing인 항공편들의 id와 flight_num을 조회하세요.

   ```sql
   SELECT rowid, flight_num FROM flight WHERE flight_num LIKE'__0%2' AND waypoint='Beijing';
   ```

8. 항공편 SQ0972의 경유지를 Tokyo로 수정하세요

   ```sql
   UPDATE flight SET waypoint='Tokyo' WHERE flight_num='SQ0972';
   ```

9. 가격순으로 내림차순 해서 세번째 레코드를 조회하세요.

   ```sql
   SELECT * FROM flight ORDER BY price DESC LIMIT 1 OFFSET 2;
   ```

10. 항공편 RT9122를 테이블에서 삭제하세요.

   ```sql
   DELETE FROM flight WHERE flight_num='RT9122';
   ```

11. flight 테이블을 삭제하세요.

    ```sql
    DROP TABLE flight;
    ```



* 주의! 무단전재나 재배포를 금합니다.