주어진 정보를 활용하여 작성된 SQL 문과 대응하는 ORM 문을 작성하고 실행해보자.

#### Table Name : users

| name       | data type   |
| ---------- | ----------- |
| id         | integer(pk) |
| first_name | text        |
| last_name  | text        |
| age        | integer     |
| country    | text        |
| phone      | text        |
| balance    | integer     |

---

1. user 테이블 전체 데이터를 조회하시오.

```sql
SELECT * FROM users_user;
```

```python
User.objects.all()
```

2. id가 19인 사람의 age를 조회하시오.
   - pk = (id__exact)

```sql
SELECT age FROM users_user
WHERE id = 19;
```

```python
User.objects.get(id=19).age -> 전체 레코드 받아온 후 값 접근
User.objects.filter(id=19).values('age') -> 쿼리셋
```

3. 모든 사람의 age를 조회하시오.

```sql
SELECT age FROM users_user;
```

```python
User.objects.all().values('age')
```

4. age가 40 이하인 사림들의 id와 balance를 조회하시오.

```sql
SELECT id, balance FROM users_user
WHERE age <= 40;
```

```python
User.objects.filter(age__lte=40).values('id', 'balance')
```

5. last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오.

```sql
SELECT first_name FROM users_user
WHERE last_name = '김' AND balance >= 500;
```

```python
User.objects.filter(last_name='김', balance_gte=500).values('first_name')
```

6. first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오.

```sql
SELECT balance FROM users_user
WHERE first_name LIKE '%수' AND country = '경기도';
```

```python
User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
```

7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오.

```sql
SELECT COUNT(*) FROM users_user
WHERE balance >= 2000 OR age <= 40;
```

```python
User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()
```

8. phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오.

```SQL
SELECT COUNT(*) FROM users_user
WHERE phone LIKE '010%';
```

```python
User.objects.filter(phone__startswith='010').count()
```

9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오.

```sql
UPDATE users_user SET country = '경기도'
WHERE first_name = '옥자' AND last_name = '김';

SELECT country FROM users_user
WHERE first_name = '옥자' AND last_name = '김';
```

```python
# 여러 명
users = User.objects.filter(first_name='옥자', last_name='김')
for user in users:
    user.country = '경기도'
    user.save()
    
User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')

# 한 명
user = User.objects.filter(first_name='옥자', last_name='김')[0].country='경기도'
user.save()
```

10. 이름이 ‘백진호’인 사람을 삭제하시오.

```sql
DELETE FROM users_user
WHERE first_name = '진호' AND last_name = '백';
```

```python
User.objects.filter(first_name='진호', last_name='백').delete()
```

11. balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오.

```sql
SELECT first_name, last_name, balance FROM users_user
ORDER BY balance DESC LIMIT 4;
```

```python
User.objects.order_by('-balance').values('fisrt_name', 'last_name', 'balance')[:4]
```

12. phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오.

```sql
SELECT * FROM users_user
WHERE age < 30 AND phone LIKE '%123%';
```

```python
User.objects.filter(phone__contains='123', age__lt=30)
```

13. phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오.

```sql
SELECT DISTINCT country FROM users_user
WHERE phone LIKE '010%';
```

```python
User.objects.filter(phone__startwith='010').values('country').distinct()
```

14. 모든 인원의 평균 age를 구하시오.

```sql
SELECT AVG(age) FROM users_user;
```

```python
User.objects.aggregate(Avg('age'))
```

15. 박씨의 평균 balance를 구하시오.

```sql
SELECT AVG(balance) FROM users_user
WHERE last_name = '박';
```

```python
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```

16. 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오.

```sql
SELECT MAX(balance) FROM users_user
WHERE country = '경상북도';
```

```python
User.objects.filter(country='경상북도').aggregate(Max('balance'))
User.objects.filter(country='경상북도').order_by('-balance').values('balance')[0]
User.objects.filter(country='경상북도').order_by('-balance').values('balance').first()
```

17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

```sql
SELECT first_name FROM users_user
WHERE country = '제주특별자치도' 
ORDER BY balance DESC LIMIT 1;
```

```python
User.objects.filter(country='제주특별자치도').annotate(Max('balance')).values('first_name')[0]
User.objects.filter(country='제주특별자치도').order_by('balance').values('first_name')[0]
```



* **주의! 무단전재나 재배포는 금합니다.**

