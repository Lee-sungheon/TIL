## Django

python을 기반으로 하는 웹 백엔드 프레임워크

- 버전 : pip list (Django 3.1 확인)

- 장고 설치하기

```
pip install django

# 특정 버전으로 받고 싶을 때
pip install django==3.0.5
```



- 장고 시작하기

  ```
  django-admin startproject first_webex
  ```

  - `first_webex` 라는 이름으로 폴더가 생성
    - 여기 안에는 `first_webex` 폴더와 `manage.py` 생성 되어짐
    - `manage.py` : 장고 명령어를 실행하기 위한 파일
      - `python manage.py` : 장고 명령어
    - 가장 밖에 있는 프로젝트 폴더명은 수정 가능하나, setting 파일이 들어있는 폴더명은 건드리지 말자

- 장고 실행하기

  ```
  python manage.py runserver
  ```

- 장고 프로젝트는 Application의 집합체로 동작

  - 실제로 어떠한 역할을 해주는 것이 app
  - 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있음
    - 어플리케이션 : 하나의 역할 및 기능 단위로 쪼개진 형태
      - 회원 관리 / 글 작성, 수정, 글 삭제 / 데이터를 수집 분석 / ......
      - 어플리케이션을 이렇게 나눠야한다 같은 기준은 없음
      - 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 됨

- 에플리케이션 실행

  ```
  python manage.py startapp 앱이름(복수형)
  ```

  - 해당 앱 이름으로 폴더가 생성됨 (앱 폴더)
  - 바로 할 일! (안하면 100% 깨달음)
    - `settings.py`에 내가 생성한 app을 등록
    - installed_apps 가장 윗줄에 등록
    - language_code = 'ko-kr' : 왠만하면 소문자로
    - time_zone = 'Asia/Seoul'

- MTV (MVC 패턴)
  - Model : 장고에서는 Model (DB 관리)
  - View : 장고에서는 Templet (보여지는 페이지 관리)
  - Controller : 장초에서는 View (데이터 처리 및 관리)
  
- 3대장 : 우리가 가장 밀접하게 수정하여야 하는 파일 명
  
  - urls.py
  - views.py
  - templates (html 툴)
  
- 코드의 작성 흐름

  - urls.py -> views.py -> template
  - 어디에서 주소를 설정하는지 (urls)
  - 요청이 들어오면 어떤 파일을 거치게 되는지 (veiws)
  - 어디에 새로운 파일을 만들면 되는지 (template)

- urls.py에서 할 일 
  - path("url 패턴/", 실행이 되어야 하는 views에 있는 함수, 해당 path의 별명)
    - 많이 놓지는 부분 : url 패턴 뒤에 슬래쉬
  
- view.py에서 할 일
  
  - 함수를 정의(첫번째 인자로 request를 받음)
  - return 은 꼭 필요
    - render : 주로 template과 함께 response 할 때 사용되는 함수
  
- template 에서 해야할 일

  * 폴더 명은 반드시 `templates` 인 것을 확인

## 여기 까지가 기본 수정할 파일들 조작 방법



## 여기서 부터는 본격 장고 동작 정의 방법

* Template Variable

  * html 과 같은 template에서 view.py 에서 준비한 변수를 가져다가 쓰는 방법

  * render() 세번째 인자로 `{'key':value}`와 같이 딕셔너리 형태로 넘겨주면 Template에서 key를 이용하여 value를 가져올 수 있다.

  * dictionary 형태로 직접 전달하는 것 보다 `context` 라는 변수를사용해서 넘기는 것이 일반적

    ```python
    context = {'key': value}
    return render(request, 'index.html', context)
    ```

    ```html
    {{ key }} 이렇게 value를 보여줄 수 있다.
    ```

     

* Variable Routing(동적 라우팅)

  * url 주소 일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

  * 왜 사용할까?

    *  hi/justing, hi/john 과 같이 다양한 사람들과 인사를 하는 함수를 작성할 때
  * 동적 라우팅을 쓰지 않으면  urls.py에 일일이 등록해줘야함
    
      * 인원이 많아지거나 누구한테 인사해야할지 모를때 고정적인  방식은 사용하기 어려움
  * 동적 라우팅을 사용하면 뒤에 사람 이름을 변수화 할 수 있다.
        *  `hy/<str:name>` 형식으로 나타낼 수 있음
      * views.py 에서 함수를 정의할 때 인자로 꼭  variable routing 에서 선언한 변수명을 받아야 한다.
      * 변수로 사용할 수 있는  type 의 종류
      * 구글에서 django url dispatcher 로 검색하면 확인 가능
    
  * 주소 요청 : `http://127.0.0.1:8000/hello/문자열`

  * urls.py

    ```
  path('hello/<str(타입):name(저장되는 변수명)>/', views.hello),
    ```

    * int : 숫자 형식으로 받음.
    
  * views.py

    ```
    def hello(request, name(저장되는 변수명)):
    	print(name)
    	context = {
    		'name': name,
    	}
    	return render(request, 'hello.html', context)
    ```

  * template(hello.html)

    ```
    <body>
    이름은 : {{ name }}  # context 의 key 값을 사용하면 value 를 출력한다.
    </body>
    ```

    

* Django Template Language (DTL) (tag와 filter)

  * django template 에서 사용하는 내장 tempate system

  * 조건, 반복, 변수, 치환, 필터 등의 기능을 제공

  * 로직을 사용할 때 표현 형식 : `{% %}`

  * 값을 표현할 때 : `{{ }}`
  
  * 주석으로 나타내고 싶을 때는 : `{# #}` or {% comment %}주석 할 내용 {% endcomment %}
  
  ```
    <!--<h1>{#{ i * 2 }#}</h1>-->
  {% comment %}<h1>{{ i * 2 }}</h1>{% endcomment %}
  ```

  * for 태그
  
    * 반복을 위한 태그
  
    ```
      {% for 임시변수 in iterable 한 객체 %}
    {% endfor %}
      
      {% for menu in iterable menus %}
      	<p>{{ forloop.counter }} {{ menu }}</p>
      {% endfor %}
    ```
  
    * for empty

      ```
    {% for 임시변수 in iterable 한 객체 %}
      	값이 하나라도 있으면 여기가 실행
    {% empty %}
      	출력할 값이 없으면 출력.
      {% endfor %}
      ```
  
  * if 태그
  
  * 조건을 구분하기 위한 태그
  
      ```
      {% if 조건문 %}
      {% elif 조건문 %}
      {% else %}
      {% endif %}
      ```
      
    * 조건 연산자 사용 가능
  
    ```
    <=, >=, ==, !=, >, <, in, not in, is
    ```
  
  * 나머지는 기타 유용한 DTL 문서를 참고
  
* Form

  * HTML form tag 의미

  * 입력 받은 데이터를 어딘가로 전송할 때 사용

    ```
    # action : 보내려는 목표 # method : http method (get / post)
    <form action="" method="GET">
    
    	input : 데이터를 입력 받게 적절히 코딩 하면 됨.
    	<input type="text" name="데이터명">
    	<input type="radio" name="데이터명1">
    	
    	# 오락실 버튼
    	<input type="button">
    	
    	# 미사일 버튼 (데이터를 action으로 전송)
    	<input type="submit">
    			or
    	<button></button>
</form>
    <input type="text"> # form 태그 내부 친구들과 같이 전송되지 않음
    ```
    
  * action : 데이터를 보내려는 목적지 주소
  
    * 목표 url 설정 주의 사항!
    
      ```
      action="/catch/" : localhost:8000/catch/
      => 127.0.0.1:8000/catch?name=asdf
      
      현재 주소 : 127.0.0.1:8000/index
      action="catch/" : 현재주소/catch/
    => 127.0.1:8000/index/catch?name=asdf
      ```
    
  * method : http method (GET, POST)
  
    * GET : 주소에 query string 형식으로 데이터를 전달하는 방식 (정보를 조회할 때 주로 사용)
    * `localhost:8000/catch/?데이터명=데이터값&데이터명1=데이터1값&...`
  
  * `request` 라는 장고 함수를 선언할 때 넣어주었던 인자에 유저가 요청한 값이 들어 있음



## Template 확장 사용하기

- Step 1. base.html을 생성하고 원하는 위치에 templates 폴더 안에 위치 시킨다.
  1. base.html에는 기본 html DOM 트리를 구성한다.
  2. bootstap CDN을 복붙 해준다.
  3. block 을 body 안에 적절한 곳에 위치 시켜준다.
- Step 2. settings.py에 base.html의 경로를 등록
  - TEMPLATES 라는 곳에 있는 DIRS 에 그 경로를 추가해준다.
  - DIRS : [BASE_DIR / 'workshow_sol' / 'templates']  : Django 3.xx 부터 사용
  - DIRS : [os.path.join(BASE_DIR, 'workshop_sol', 'templates')] : Django 2.xx 등록 방식
- Step 3. 확장하고 사용한다.
  1. 가장 첫번째 줄에 `{% extends 'base.html' %}`을 해준다.
  2. 그 다음 block 을 위치 시키고 block 안에 적절히 꾸며 주면 된다.



JSON 파일

파이썬의 딕셔너리와 구조가 똑같다.

{key: value}

단, 차이점은 json 은 binary 형식으로 저장된다.

(쉽게 말하면 문자열로 저장이 된다.

더 쉽게 말하면 10 vs '10')