# 2023 07 13 thursday

## 간단한 git 사용법 정리

- git init : 로컬 저장소 설정(초기화), git의 버전 관리를 시작할 디렉토리에서 진행
- git add sample.txt : 변경 사항이 있는 파일 staging area에 추가
- git commit -m "쓸 이름" : staging area에 있는 파일들을 저장소에 기록, 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
- git status : 로컬 저장소의 파일 상태 확인
- git log : 목록 확인 commit 한것만 가능
- ( git log 이후 끝이 안난다면 esc ; q 순서대로 누르기)
- git log --oneline : 목록 간단 확인

---

- git remote add origin remote_repo_url : 로컬 저장소에 원격 저장소 주소 추가
- git remote -v : 상태확인
- git remote rm origin : 저장소 주소 제거
- git push -u origin master : 원격 저장소에 commit 목록을 업로드
- (push는 집갈때 한번? commit은 자주?, commit 이력이 없으면 push 불가능)
- git pull origin master : 원격 저장소의 변경사항만을 받아옴(업데이트)
- git clone remote_repo_url : 원격 저장소 전체를 복제(다운로드) , clone으로 받은 프로젝트는 이미 git init이 되어있음

---

## python

### 고려해야 할 것

- 대/소문자
- 띄어쓰기
- 스펠링

### 구구단

- for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
  - 결과
    - 1 x 1 = 1
    - 1 x 2 = 2
    - ...
    - 9 x 8 = 72
    - 9 x 9 = 81

#### 단마다 나누기

- for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print('-------------')

### while문 쓰다가 안끝날 때

- ctrl c 누르면 풀린다

# 2023 07 14 friday

## random

- random한 값을 얻고싶을때 사용
- import random
  - selected = random.choice(menu)
  - print(selected)
  - menu 중 한가지가 print 됨

## dictionary

- dict = {'a':12}
- dict.keys() = 'a'
  - 키만 구하기
- dict.values()= 12
  - 값만 구하기

```python
#키값 한줄씩 출력
A = {'a':10,'b':20}
for key,value in A.items():
    print(key,value)

```

- dict['b']= 13
  - {'a':12,'b':13}
  - key와 value 추가
-
- menu = {'롯데리아':'123-3333','중국성':'111-1111','마포식당':'222-2222'}
- list(menu) = ['롯데리아', '중국성', '마포식당']
- selected = random.choice(list(menu))
- print(selected, menu[selected])
  - 중국성 111-1111

## Python 내장 함수

- print('hi')
  - hi
- abs(-3)
  - 3
- len('hi)
  - 2
- str()
- max(list), max(2,3,4)
- sorted() 작은 수 부터 정렬
  - sorted(list,reverse=False)= 오름차순, True = 내림차순
  - 리스트.sort() 는 본체의 리스트를 정렬 후 변환
  - sorted(리스트) 는 본체를 놔두고 정렬한 새로운 리스트를 반환

# 2023 07 15 saturday

## list.index(a)

- list안에 a가 몇번째에 있는지

## list.count(a)

- list 안에 a 가 몇개있는지

# 2023 07 16 sunday

## import sys

    - input = sys.stdin.readline
    - 많은 양의 입력을 받아야할때 input 대신 사용하면 빠르다

## float

- 3.0 같은 소수점이 들어있는 문자열은 int()로 변환이 안됨
- 그럴 때 실수형으로 바꾸기 위해 float() 사용 숫자 끼리 계산가능

## round

- round()
- 반올림 해주는 함수

# 2023 07 17 monday

## 연산자 우선순위

- 지수가 제일 높다(**)

## 얕은복사 깊은복사

- list안에 다른 변수들이 존재할때  list_ = [a,b,c]
- list를 다른 변수에 복사하고      list_new = list
- list안의 변수를 바꿀시 원본 또한 바뀐다고 한다. 혹은 오류..?
- 이때 깊은 복사가 사용되는데
- import copy
  - list_new = copy.deepcopy(list)
  - 위 형태로 사용하면 됨

## 2차원 입력 받기

- arr = [list(map(int, input().split())) for _ in range(세로 길이)]

# 2023 07 17 monday

## f-string 응용

- print(f'{1.6665225346:.4f}')
- 소수점 4번째까지 출력(반올림 적용)
- print 뿐만 아니라 변수에도 적용 가능

```python
v_name = 'aaa'
for i in range(5):
  name = f'{v_name}{i}'
  print(name)
```

# 2023 07 19 wednesday

## 함수

### 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

- 함수를 사용하는 이유
  - 재사용성이 높아지고 코드의 가독성과 유지보수성 향상

### 내장함수

- 파이썬이 기본적으로 제공하는 함수
  - (별도의 import 없이 바로 사용가능)
- ex) print() abs() sum ()

### 함수 정의 호출

- def greet(name):
  - message = 'hello, '+ name
  - return message
- result = greet('Alice')
- print(result)

### 매개변수 (parameter)

- def add_numbers(x,y)
  - result = x+y
  - return result
  - x,y가 매개변수

### 인자 (argument)

- a = 2
- b = 3
- sum_result = add_numbers(a,b)
- print(sum_result)
- a,b가 인자

#### 위치인자, 기본인자, 키워드 인자, 임의의 인자

- 위치 인자 = 변수의 위치에 따라
- 기본 인자 = def greet(name, age=30): age에 기본 값이 할당 돼있음 인자를 전달하면 바뀜
- 키워드 인자 = 키워드를 명시하여 전달
- 임의의 인자 매개변수 앞에 *를 붙여 사용 여러개를 튜플로 처리
  
## 범위

### 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음

- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
  - Local scope : 지역 범위(현재 작업 중인 범위)
  - Enclosed scope : 지역 범위 한 단계 위 범위
  - Global scope : 최상단에 위치한 범위
  - Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

## 재귀 함수

- 함수 내부에서 자기 자신을 호출하는 함수
- ex) 팩토리얼
  - def factorial(n):
    - if n == 0:
      - return 1
    - return n * factorial(n - 1)

## 유용한 내장 함수

### map

- 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

### zip

- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x000001C76DE58700>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]
```

### lambda

- 이름 없이 정의되고 사용되는 익명 함수
  - addition = lambda x, y: x + y

# 2023 07 20 thursday

## 제어문

### 조건문

- 주어진 조건식을 평가하여 조건이 True인 경우에만 코드 블록을 실행하거나 건너뜀

#### if/elif/else

### 반복문

- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
  1. 특정 작업을 반복적으로 수행
  2. 주어진 조건이 참인 동안 반복해서 실행

#### for / while

- while은 반드시 종료 조건이 필요
- break = 반복을 즉시 중지
- continue = 다음 반복으로 건너뜀

## list comprehension

- [i for i in range(10) if i%2 ==1]
- [i if i %2 ==1 else str(i) for i in range(10)]
- elif는 못씀

## 리스트를 생성하는 3가지 방법 비교

### 가장 빠른 것

- for loop
- map
- list comprehension
- 아마도 map..?
- 굳이 list compre 쓸필요 없다

#### 효율성 별차이 없음 (빠른거 때에 따라 다르다)

#### 가독성이 더 중요함

- " 작은 효율성에 대해서는, 말하자면 97% 정도에 대해서는, 잊어버려라. 섣부른 최적화는 모든 악의 근원이다."
- 도널드 커누스

## enumerate(iterable, start=0)

- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
for index, fruit in enumerate(fruits):
  print(f'인덱스 {index}: {fruit}')

인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
```

# 2023 07 21 friday

## json

### import json

- json.loads(json_data)
- 딕셔너리 형태로 변환
  
# 2023 07 23 sunday

## if a == b == c

- 가능하다

# 2023 07 24 monday

### continue

- 반복문에서 아래 문장을 스킵하고 다음 반복문으로 넘어감

## 메서드

- 객체에 속한 함수

### .capitalize

- 'hello'.capitalize()
  - Hello

### 문자열 조회/탐색 및 검증 메서드

- s.find(x)
  - x의 첫 번째 위치를 반환. 없으면 -1 반환
- s.index(x)
  - x의 첫 번째 위치를 반환. 없으면 오류발생
- s.isupper() / s.islower()
  - 모두 대문자인지 / 소문자인지 확인
- s.isalpha()
  - 문자열이 모두 알파벳인지 확인
- s.title()
  - 단어가 대문자로 시작하고 나머지는 소문자가 되도록 함 (공백기준)

- s.replace(world, python)
  - 'hello, world!'
  - 'hello, python!'
  - s.replace(a,b)를 변수에 지정해 두면 새로운 리스트 가됨
    - ss = s.replace(a,b)
- s.strip()
  - 문자열 시작과 끝에 공백 혹은 지정 문자 제거
- s.split()
  - 지정한 문자를 구분자로 문자를 분리하여 문자열의 리스트로 변환
- 구분자.join(s)
  - 구분자를 이용하여 하나의 문자열로 연결
- s.swapcase()
  - 대소문자 바꾸기
  - 대문자는 소문자로 소문자는 대문자로

### chained

- s.swapcase.replace('l','z')
  - s = heLLo
  - HEzzO

### list 값 추가 및 삭제 메서드

- list =[4,5,6]
- list.append([1,2,3])
  - [4,5,6,[1,2,3]]
- list.extend([1,2,3])
  - [4,5,6,1,2,3]
- list.insert(i, x)
  - i에 x삽입
- list.remove(x)
  - 리스트에서 가장 왼쪽의 x를 제거 없으면 ValueError
- list.pop(i)
  - 리스트에서 지정한 인덱스의 항목을 제거 후 반환
  - 작성하지 않을시 마지막 항목 제거
- list.clear()
  - 리스트의 모든 항목 삭제
- list.index(x)
  - x의 가장빠른 인덱스(0,1,2,3 ... 순서) 반환
- list.reverse
  - 리스트를 역순으로 변경 (정렬x)(map 처럼 생겨서 빈칸을 기준으로 나뉘어 있음)
  - join을 사용하여 출력 가능할지도..?
- list.sort()
  - 리스트를 오름차순 정렬
- list.count(x)
  - 리스트에서 x의 개수를 반환

### 슬라이스는 복사본 생성

# 2023 07 25 tuesday

## 세트 메서드

### 순서와 중복이 없는 변경 가능한 자료형

- s.add(x)
  - 세트에 x추가 x가 있으면 아무것도 변하지 않는다.
- s.clear()
  - 세트의 모든 항목을 제거
  - 빈세트는 {}로 표시되지 않는다. set()로 표기됨
- s.remove(x)
  - 세트에서 x를 제거
  - x가 없다면 keyerror 생성
- s.pop()
  - 임의의 요소를 제거
  - 정수는 다시 실행해도 같은 임의의 값이 제거됨
  - 문자열은 다시 실행하면 랜덤의 값이 제거됨
- s.discard(x)
  - 항목 x를 제거 remove와 달리 에러가 없다
- s.update(iterable(list?))
  - 세트에 다른 요소들을 추가 (list의 요소들을 추가)

### 세트는 집합으로 활용 됨

- s1.difference(s2) (s1 - s2)
  - s1에는 있지만 s2에는 없는 것들
- si.intersection(s2) (s1 + s2)
  - 둘다에 둘어있는 것들
- s1.issubset(s2) s1 <= s2
  - s1의 항목이 모두 s2에 있으면 True 반환
- s1.issuperset(s2) s1 >= s2
  - s1에 s2의 모든 항목이 있으면 True 반환
- s1.union(s2) s1 | s2
  - s1 s2 둘다에 들어있는 항목으로 세트를 생성후 반환

## 해시 테이블(Hash Table)

- 데이터를 저장하는 방식
- 키-값 쌍을 연결하여 저장하는 방식
- 정수 타입은 정수 값 자체가 곧 해시 값이 됨
- 문자열은 가변적인 길이를 갖는다.

## 딕셔너리 메서드

### key-value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- d.clear()
  - 딕셔너리 d의 모든 키/값 쌍으로 제거
- d.get(key)
  - 찾고자 하는 키가 없을 때 None이 뜨거나 d.get(key,'unknown')같이 쓰면 none 대신 뜰것을 정할수있음
- d.keys()
  - d의 모든 키 반환
- d.values()
  - d의 모든 값 반환
- d.items()
  - d의 키/값 쌍을 모은 객체 반환
- d.pop(k)
  - d에서 키를 제거하고 값을 반환 (없으면 오류)
  - d.pop(k,v)
  - 없으면 v를 반환
- d.setdefault(k,v)
  - 키와 연결된 값을 반환 키가 d에 없으면 k를 추가하고 v를 반환
- d1.update(d2)
  - d에 있으면 d2값으로 대체 없으면 d2 키/값을 d에 추가

# 2023 07 26 wednesday

## 객체지향 프로그래밍

### 절차지향 프로그래밍

- 데이터와 절차로 구성하는 방식의 프로그래밍 패러다임
- 함수 호출 흐름이 중요
- 복잡성이 증가하면서 위기가 옴

### 객체지향 프로그래밍

- 데이터와 해당데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임
- 객체간 상호작용과 메시지 전달이 중요
- 자식클래스
- 절차 지향과 객체 지향은 대조되는 개념이 아니다

### 클래스

- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공
- 클래스를 기반으로 다른 객체들을 만들어냄

### 객체

- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- 속성과 행동으로 구성된 모든 것
- 하나의 객체는 특정 타입의 인스턴스이다

#### 객체의 특징

- 타입(type) : 어떤 연산자와 조작이 가능한가?
- 속성(attribute) : 어떤 상태를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
- 객체(object) = 속성(attribute) + 기능(method)

### 인스턴스

- 클래스로 만든 객체
- 객체.행동()
- 인스턴스.매서드()

### 클래스 구조

```python
# 클래스 정의
class Person:
  pass

# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute

# 생성자 함수 객체의 초기화를 담당
__init__

```

#### 인스턴스 변수

- self.name = name
- 인스턴스마다 별도로 유지되는 변수
- 인스턴스 마다 독립적인 값을 가짐 인스턴스 생성시 초기화

#### 클래스 변수

- blood_color = 'red'
- 클래스 내부의 변수
- 클래스로 생성된 모든 인스턴스들이 공유하는 변수

#### 인스턴스 메서드

- def singing(self):
  - return ~~
- 각각의 인스턴스에서 호출할 수 있는 메서드
- 인스턴스 변수에 접근, 수정

#### 인스턴스와 클래스 간의 이름 공간

- 클래스를 정의하면 클래스와 해당하는 이름 공간 생성
- 인스턴스 생서, 인스턴스 객체 생성 독립적인 이름 공간 생성
- 인스턴스에서 특정 속성에 접근 하면 인스턴스->클래스 순으로 탐색

#### 독립적인 이름공간을 가지는 이점

- 각 인스턴스는 독립적인 메모리 공간을 가짐
- 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근 불가능
- 객체 지향 프로그래밍의 중요한 특성 중 하나로 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
- 이를 통해 클래스와 인스턴스는 다른 객체들과의 상화작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작 가능
- 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움 됨

### 클래스 변수 활용

- 변경시 클래스.클래스변수 형식으로 변경

### 메서드 종류

#### 인스턴스 메서드

- 클래스로 부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
- 인스턴스의 상태를 조작, 동작 수행
- 반드시 첫 번째 매개변수로 self를 받음

```python
'hello'.upper() # 객체 지향 방식의 메서드로 호출하는 표현
str.upper('hello')
```

- 인스턴스 메서드의 첫번째 매개변수가 반드시 self인 이유

#### 클래스 메서드

- 클래스 변수를 조작하거나 클래스 레벨의 동작 수행
- @classmethod 데코레이터를 사용하여 정의
- 호출시 첫번째 인자로 호출하는 cls가 전달됨

```python
class Myclass:

  @classmethod
  def class_method(cls, arg1, ...):
    pass
```

- 예시
  - Myclass.class_method()

#### 정적 메서드(스태틱 메서드)

- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
- 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

- @staticemethod 데코레이터를 사용하여 정의
- 호출시 필수적으로 작성해야 할 매개변수가 없음
- 즉 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능만을 위한 메서드로 사용

```python
class Myclass:

  @staticemethod
  def static_method(arg1, ...):
    pass
```

### 메서드 정리

- 클래스가 사용할것
  - 클래스 메서드
  - 스태틱 메서드

- 인스턴스가 사용할것
  - 인스턴스 메서드

### 매직 메서드

- 특정 상황에 자동으로 호출되는 메서드
- __가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
  - 스페셜 메서드 혹은 매직 메서드라고 불림
  - __str__ , __len__ 등등

#### 매직 메서드 예시

```python

class Circle:
  def __init__(self,r):
    self.r=r
  def area(self):
    pass
  def __str__(self):
    return f'[원] radius: {self.r}'

c1= Circle(10)
c2= Circle(1)

print(c1) # [원] radius: 10
print(c2) # [원] radius: 1
```

# 2023 07 27 thursday

## classes 상속

### 상속

- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

#### 상속이 필요한 이유

- 코드 재사용
  - 상속을 통해 기존 클래스의 속성과 메서드 재사용 가능
  - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며 중복된 코드를 줄일 수 있음
- 계층 구조
  - 상속을 통해 클래스들 간의 계층 구조를 형성 할수 있다
  - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스 만들수 있다
- 유지 보수의 용이성
  - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지보수 용이
  - 코드의 일관성 유지 수정이 필요한 범위를 최소화 가능

#### 상속 없이 구현 하는 경우

- 학생/교수 정보를 나타내기 어려움
- 메서드 중복 정의

#### super()

```python
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'안녕, {self.name}입니다.')
        
class Professor(Person):
    def __init__(self, name, age, department):
        # Person.__init__(self,name,age)
        super().__init__(name,age)
        self.department = department
        
class Student(Person):
    def __init__(self, name, age, gpa):
        # Person.__init__(self,name,age)
        super().__init__(name,age)
        self.gpa = gpa
        
p1 = Professor('박교수', 49, '컴공')
s1 = Student('김학생', 20, 3.5)

p1.talk()
s1.talk()
```

- 부모 클래스의 메서드를 호출하기 위해 사용되는 내장함수
- super().__init__(name,age)
  - self가 없어도 된다.

#### 다중 상속

- 두 개 이상의 클래스를 상속받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

### 상속 관련 함수와 메서드

#### mro()

- Method Resolution Order
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식클래스 -> 부모클래스로 확장

## error exception

### 버그

- 결함이나 오류를 지칭

### 디버깅

- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
- 프로그램의 오작동 원인을 식별하여 수정하는 작업

#### 디버깅 방법

- print 활용
  - 특정 한수 결과
  - 반복/조건 결과 등 나눠서 생각
  - 코드를 bisection으로 나눠서 생각
- 개발환경에서 제공하는 기능 활용
- python tutor 활용
- 뇌 컴파일, 눈 디버깅....

### 에러

- 프로그램 실행중 발생하는 에외 상황

#### 에러 유형

- 문법 에러
  - 프로그램의 구문이 올바르지 않은 경우
  - 오타, 괄호 및 콜론 누락 등의 문법적 오류

- 예외
  - 프로그램 실행중 감지되는 에러
  
### 예외

- 프로그램 실행 중에 감지되는 에러

#### 내장 예외

- 예외 상황을 나타내는 예외 클래스들
  - 파이썬에 이미 정의되어 있고 특정 예외 상황에 대한 처리를 위해 사용

### 예외 처리

- try-except 구조

```python
try:
  # 예외가 발생할 수 있는 코드
except 예외:
  # 예외 처리 코드
```

# 2023 07 28 friday

## numpy, pandas, matplotlib

# 2023 07 30 sunday

## 시간 복잡도

- 주어진 문제를 해결하기 위한 연산 횟수
- 파이썬 = 1초에 2000만번 ~ 1억번 연산
- 최악일 때를 염두

## 시간 복잡도 활용

### 버블정렬

- O(n**2)

### 병합정렬

- O(nlogn)

### 시간 복잡도 도출 기준

- 상수는 제외 ( O(n)= 3O(n))

# 2023 08 01 tuesday

## 카운팅 정렬

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한 사항
  - 정수나 정수로 표현 가능한 자료만 적용 가능
- 시간 복잡도
  - O(n+k) : n은 리스트 길이, k는 정수의 최대값

### 과정

- Data에서 각 항목들의 발생 횟수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다
- 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정한다.

```python
A[] # 입력 배열 (0 to k)
B[] # 정렬된 배열
C[] # 카운트 배열

C = [0]*(k+1)
for i in range(0,len(A)):
  C[A[i]] += i
for i in range(1,len(C)):
  C[i] += C[i-1]
for i in range(len(B)-1,-1,-1):
  C[A[i]] -= 1
  B[C[A[i]]] = A[i]
```

## 탐욕 알고리즘

- 탐욕 알고리즘은 최적해를 구하는데 사용되는 근시안적 방법
- 여러 경우 중 하나를 결정할때 최적인것을 선택해 나가는 방식을 통해 해답에 도달
- 각 선택의 시점에서의 결정은 지역적으로는 최적이지만 계속 수집하여 해답을 낸다 해도 그것이 최적인 보장은 없다
- 일반적으로 머리에서 떠오르는 생각을 검증 없이 바로 구현하면 그리디 접근이 됨

# 2023 08 02 wednesday

## 배열 : 2차원 배열

```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 3 = N
# 1 2 3
# 4 5 6
# 7 8 9

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 3 = N
# 123
# 456
# 789
```

- 배열 순회

- 행 우선 순회

```python
# n*m의 행렬
# i 행의 좌표
# j 행의 좌표
for i in range(n):
  for j in range(m):
    array[i][j]
```

- 열 우선 순회

```python
# n*m의 행렬
# i 행의 좌표
# j 행의 좌표
for j in range(m):
  for i in range(n):
    array[i][j]
```

- 지그재그 순회

```python
# n*m의 행렬
# i 행의 좌표
# j 행의 좌표
for i in range(n):
  for j in range(m):
    array[i][j+(m-1-2*j)*(i%2)]
```

```python
arr = [[0]*M for _ in range(N)]
arr2 = [[0]*M]*N # 하지말것
arr[0][0] = 1
arr2[0][0] = 1
arr = # 1 0 0 0 , 0 0 0 0
arr2 = # 1 0 0 0 , 1 0 0 0

# 행의 합 중 최대값
max_v = 0
for i in range(N):
  row_total = 0
  for j in range(M):
    row_total += arr[i][j]
  if max_v < row_total:
    max_v = row_total
```

## 델타를 이용한 2차 배열 탐색

- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

```python
arr[N][N] # N*N 배열
di[] [0, 1, 0, -1]
dj[] [1, 0, -1, 0]
for i : 0 -> N-1:
  for j : 0 -> N-1:
    for k in range(4):
      ni <- i + di[k]
      nj <- j + dj[k]
      if 0<= ni< N and 0 <= nj < N: # 유효한 인덱스면
        arr[ni][nj]

```

```python
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
m = 2  # 몇칸이나 더할지 
max_v = 0  # 모든 원소가 0 이상이라면
for i in range(N):  # 모든 원소 arr[i][j]에 대해
    for j in range(N):
        # arr[i][j]중심으로
        s = arr[i][j]
        for k in range(4):
            for p in range(1,m+1):
                ni, nj = i+di[k]*p, j+dj[k]*p
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
            # 여기까지 주변 원소를 포함한 합
            if max_v < s:
                max_v = s
```

## 전치행렬

```python
for i in range(3):
  for j in range(3):
    if i < j :
      arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

```

- 대각선의 합

```python
N= int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total1 = 0  # 대각선
total2 = 0  # 반대 대각선
for i in range(N):
    total1 += arr[i][i]
    total2 += arr[i][N-1-i]
```

# 2023 08 03 thursday

## 부분집합

- 유한 개의 정수로 이루어진 집합이 있을때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 X가 되는 경우가 있는지 알아보는 문제에 사용

- 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 함

- 주어진 집합의 부분집합을 생성하는 방법이 중요

### 부분집합의 수

- 집합의 원소가 n개 일때, 공집합을 포함한 부분집합의 수는 2**n개이다.
- 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다.

```python
def print_subset(bit, arr, n):
    total =0 
    for i in range(n):
        if bit[i]:
            print(arr[i], end = ' ')
            total += arr[i] # 해당 부분 집합의 합
    print(bit, total)

arr = [1,2,3,4]
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit, arr, 4)
        
```

### 비트 연산자

- &
  - 비트 단위로 AND 연산을 한다.
- |
  - 비트 단위로 OR 연산을 한다.
- <<
  - 피연산자의 비트 열을 왼쪽으로 이동시킨다.
- >>
  - 피연산자의 비트 열을 오른쪽으로 이동시킨다.

- 1 << n : 2**n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
- i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 검사 한다.

-

```python
for i in range(1<<N):
  sumV= 0
  fo j in range(N)
```

## 검색(search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

- 목적하는 탐색 키를 가진 항목을 찾는 것
  - 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키

- 검색의 종류
  - 순차 검색(sequential search)
    - 일렬로 되어 있는 자료를 순서대로 검색하는 방법
      - 가장 간단하고 직관적인 검색 방법
      - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
      - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적
    - 2가지 경우
      - 정렬되어 있지 않은 경우
      - 정렬되어 있는 경우
    - 검색 과정
      - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
      - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
      - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
  - 이진 검색(binary search)
    - 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정, 검색을 계속 진행하는 방법
    - 자료가 정렬된 상태여야 함
    - 검색 과정
      - 자료의 중앙에 있는 원소를 고른다.
      - 중앙 원소의 값과 찾고자 하는  
  - 해쉬(hash)

-

```python

def bFind(key):
  l = 0
  r = N-1
  
  while a<=b:
    m = (l+r)//2
    if key == nums[m]:
      return m
    if key > nums[m]:
      l = m+1
    else:
      r = m-1
  return -1

#  key가 nums에 있으면 위치를 return하고 없으면 -1을 return
def sFind(key):
  for idx in range(N):
    if key == nums[idx]:
      return idx
    if key < nums[idx]:
      return -1 
  return -1

  idx = 0
  while idx<N:
    if key ==nums[idx]:
      

```

# 2023 08 04 friday

## 달팽이

```python
N = 5
arr = [[0]*N for _ in range(N)]

d= 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

curR = curC = 0
for value in range(1,N*N+1):
    arr[curR][curC] = value

    newR = curR+dr[d]
    newC = curC+dc[d]
    if newR<0 or newR >=N or newC<0 or newC>=N or arr[newR][newC]!=0:
        d = (d+1)%4

    curR +=dr[d]
    curC +=dc[d]

print(arr)
```

# 2023 08 07 monday

## str() 함수 사용하지않고 거꾸로 출력하기

```python
def itoa(a):
  s =''
  while a>0:
    s += chr(ord('0') + a%10) # 1의자리 숫자의 ASCII값
    a//=10
  return s
```

# 2023 08 08 tuesday

## 패턴 매칭에 사용되는 알고리즘

### 고지식한 패턴 검색 알고리즘

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

### 카프-라빈 알고리즘

### KMP 알고리즘

### 보이어 무어

## 시저 암호문

# 2023 08 09 wednesday

## 스택

### 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형구조를 갖는다
  - 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다
  - 비선형구조 : 자료 간의 관게가 1대N의 관계를 갖는다. (예 : 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장먼저 꺼낸다, 후입선출(LIFO)이라고 부른다.
  - 예를 들어 스택에 1,2,3순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3,2,1순으로 꺼낼수있다.

### 스택을 프로그램에서 구현하기 위해 필요한 자료구조와 연산

- 자료구조 : 자료를 선형으로 저장할 저장소
  - 배열을 사용할 수 있다
  - 저장소 자체를 스택이라 부르기도 한다.
  - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다

- 연산
  - 삽입 : 저장소에 자료를 저장한다. 보통 push라고 부른다.
  - 삭제 : 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.
  - 스택이 공백인지 아닌지 확인하는 연산. isEmpty
  - 스택의 top에 있는 item(원소)을 반환하는 연산. peek

### 스택의 삽입/삭제 과정

- 별도로 지우는 동작은 필요없다..?

### 스택의 push 알고리즘

- append 메소드를 통해 리스트의 마지막에 데이터를 삽입
  - 오래걸림

```python
def push(item):
  s.append(item)

# 참고

def push(item, size):
  global top
  top += 1
  if top == size:
    print('overflow')
  else:
    stack[top] = item

size = 10
stack = [0]*size
top = -1

push(10,size)
top += 1 # push 20
stack[top] = 20 #
```

### 스택의 pop 알고리즘

```python
def pop():
  if len(s) == 0:
    # underflow
    return
  else:
    return s.pop();

# 참고

def pop():
  global top
  if top == -1 :
    print('underflow')
    return 0
  else:
    top -= 1
    return stack[top+1]

print(pop())

if top > -1:  # pop()
    top -= 1
    pritn(stack[top+1])
```

### 스택 구현

### 스택 구현 고려 사항

- 1차원 배열을 사용하여 구현할 경우 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점이 있다.
- 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다. 동적 연결리스트를 이용하여 구현하는 방법을 의미. 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다.
스택의 동적구현은생략한다.

### 스택의 응용 : 괄호 검사

- 괄호의 종류 : 대괄호('[',']'), 중괄호('{','}'), 소괄호('(',')')
- 조건
  1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
  2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
  3. 괄호 사이에는 포함 관계만 존재한다.
- 잘못된 괄호 사용의 예
  - (a(b)
  - a(b)c)
  - a{b(c[d]e}f)

## 재귀호출

- 자기 자신을 호출하여 순환 수행되는 것
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성
  - 재귀 호출의 예 : factorial
    - n에 대한 factorial : 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
    - 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복

```python
n! = n * (n-1)!
  (n-1)! = (n-1) * (n-2)!
  (n-2)! = (n-2) * (n-3)!
...
  2! = 2 * 1!
  1! = 1
```

# 2023 08 10 thursday

## DP

- Dynamic Programming
- 최적화 문제를 해결하는 알고리즘
- 입력크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 부분 문제들을 해결해 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

### 피보나치 수 DP 적용 알고리즘

```python
def fibo2(n) :
  f = [0]*(n+1)
  f[0] = 0
  f[1] = 1
  for i in range(2,n+1):
    f[1] = f[i-1] +f[i-1]

  return f[n]
```

## DFS(깊이우선탐색)

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함
- 두 가지 방법
  - 깊이 우선 탐색(DFS)
    - 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
    - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
  - 너비 우선 탐색(BFS)

### DFS

1. 시작 정점(v)를 결정하여 방문한다.
2. 정점 v에 인접한 정점 중에서

- 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2.를 반복한다.
- 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복한다.

3. 스택이 공백이 될 때까지 2.를 반복한다

```python
def dfs(n,V,adj_m):
    stack = []              # 스택 생성
    visited = [0] * (V+1)   # visited 생성
    visited[n] = 1          # 시작점 방문 표시
    print(n)                # do[n]
    while True:
        for w in range(1, V):    # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w]==0:
                stack.append(n) # push(v), v = w
                n =w
                print(n)        # do(w)
                visited[n] = 1  # w 방문 표시
                break
        else:
            if stack: # 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop()해서 다시 다른 w를 찾을 n 준비
            else:       # 스택이 비어있으면
                break
    return


V,E = map(int, input().split())
arr = list(map(int,input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1,v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1 
```

# 2023 08 11 friday

- 논리적으로 필요한 것이 무엇인지 써보며 접근하기

# 2023 08 14 monday

## 스택 2

### 계산기1

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
- 문자열 수식 계산의 일반적 방법
  - 중위표기법
    - 연산자를 피연산자의 가운데 표기하는 방법
      - A + B
  - 후위표기법
    - 연산자를 피연산자 뒤에 표기하는 방법
      - AB+

- step1. 중위표기식의 후위표기식 변환 방법1
  - 수식의 각 연산자에 대해서 우선순위에 따라 괄호 를 사용하여 다시 표현한다.
  - 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동시킨다.
  - 괄호를 제거 한다.
    - A*B-C/D
      - ((A*B)-(C/D))
      - ((A B)* (C D)/)-
      - AB*CD/-

- step1. 중위 표기법에서 후위 표기법으로의 변환 알고리즘(스택 이용)2
  1. 입력 받은 중위 표기식에서 토큰을 읽는다.
  2. 토큰이 피연산자이면 토큰을 출력한다.
  3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
  4. 토큰이 오른쪽 괄호 ')'이면 스택 top에 왼쪽 괄호 '(' 가 올때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. 왼쪽 괄호를 pop만 하고 출력하지는 않는다.
  5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
  6. 스택에 남아있는 연산자를 모두 pop하여 출력한다.
  - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.

- step2. 후위 표기법의 수식을 스택을 이용해 계산
  1. 피연산자를 만나면 스택에 push한다.
  2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push한다.
  3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.

```python
  # step1
s = '(6+5*(2-8)/2)'
def step1():
    result = []
    st = []
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    for i in s:
        if i.isdigit():
            result.append(i)
        # elif i == '(':
        elif i == ')':
            while st and st[-1] != '(':
                v = st.pop()
                result.append(v)
            st.pop()        # 왼쪽괄호 ( 버림
        else:
            while st and isp[st[-1]] >= icp[i]:
                v = st.pop()
                result.append(v)
            st.append(i)
    while st:
        v = st.pop()
        result.append(v)
    return result

# step2

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v2 - v1      # 순서 반대
    if op == '*':
        return v1 * v2
    if op == '/':
        return v2 // v1      # 순서 반대

def step2(s):
    st = []
    for i in s:
        if i.isdigit():
            st.append(i)
        else:
            v1 = st.pop()
            v2 = st.pop()
            st.append(cal(int(v1), int(v2), i))      # v1, v2, i를 이용해 계산해줘~ i= 오퍼레이터
    return st.pop()


step1_s = step1()
print(step1_s)      # ['6', '5', '2', '8', '-', '*', '2', '/', '+']
result = step2(step1_s)
print(result)

```
  
### 백트래킹

- 백트래킹 기법은 해를 찾는 도중에 '막히면'(즉,해가 아니면) 되졸아가서 다시 해를 찾아가는 기법이다.
- 백트래킹 기법은 최적화 문제와 결정 문제를 해결할 수 있다.
- 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합 문제 등

- 백트래킹과 깊이우선탐색과의 차이
  - 깊이우선은 모든경로 추적 백트래킹은 불필요한 경로를 조기차단(prunning 가지치기)
  - 깊이우선탐색하기에는 경우의 수가 너무 많음 즉 N! 가지의 경우의 수를 가지면 처리 불가
  - 백트래킹을 사용하면 경우의 수 감소 하지만 이역시 최악의 경우 지수함수 시간을 요함, 처리불가
  
- 유망하지 않으면 가지치기 한다
- 유망성을 점검하고 유망하지 않으면 부모노드로 돌아감
- 해답 가능성이 있으면 유망하다고 봄
- 해당 경로가 해답이 될 수 없으면 유망하지 않다고 봄

- 백트래킹을 이용한 알고리즘은 아래의 절차를 거친다
    1. 상태공간 트리의 깊이 우선 검색을 실시
    2. 각 노드가 유망한지 점검
    3. 만일 그노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 진행

# 2023 08 16 wednesday

## 부분 집합과 순열

```python

def f(i,N):
    if i==N:
        print(A)
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]

A = [1,2,3]
f(0,3)
```

```python
# 백트래킹
def print_re():
    for i in range(n):
        if result[i]:               # == 존재한다면...!1@!@@!@1
            print(arr[i], end=' ')
    print()

def partial(k, cursum):
    if cursum > n:
        return              # 진짜 백트래킹
    if k == n:
        # # print(result)
        # sumV = 0
        # for i in range(n):
        #     if result[i]:
        #         # print(arr[i], end=' ')
        #         sumV += arr[i]
        # # print(sumV)
        if cursum == 10:
            print_re()
        return

    result[k] = 0       # result의 k가 포함이안되었다.
    partial(k + 1, cursum)      # 그냥 그 값 그대로 내려감

    result[k] = 1       # 포함이 됨
    partial(k + 1, cursum + arr[k])     # 그때의 위치값을 더해서 내려감

n = 10
arr = [i for i in range(1, 11)]
result = [-1] * n
partial(0, 0)
```

## 분할 정복 알고리즘

# 2023 08 17 thursday

## 큐

### 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
- 선입선출구조
  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장먼저 삭제된다.

### 큐의 기본 연산

- 삽입 : enQueue
- 삭제 : deQueue

### 큐의 사용을 위해 필요한 주요 연산

- enQueue(item)
- deQueue()
- createQueue()
- isEmpty()
- isFull()
- Qpeek()

```python

def enQ(data):
    global rear
    rear += 1
    Q[rear] = data

def deQ():
  global front
  if front == rear :
    print('Q is empty')
    return -1
  else:
    front += 1
    return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
tmp = Q[front]
print()

while front != rear :# 큐가 비어있지 않을 때
  front += 1
  print(Q[front])


```

### 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 저장된 첫 번째 원소의 인덱스 (마지막 삭제 위치)
  - rear : 마지막 저장된 원소
- 상태 표현
  - 초기 상태 : front = rear = -1
  - 공백 상태 : front == rear
  - 포화 상태 : rear == n-1 (n : 배열의 크기, n-1: 배열의 마지막 인덱스)

### 선형큐 문제점

- 원소의 삽입 삭제를 반복하면 배열의 앞부분에 공간이 있지만 rear= n-1인 상태, 포화상태로 인식하여 더 이상 삽입을 수행 하지 못함
- 해결방법
  - 매연산 마다 저장된 원소들을 배열의 앞부분으로 이동
  - 원소 이동에 많은시간이 소요 되어 큐의 효율성 감소
- 해결방법2
  - 1차원 배열을 사용하되, 논리적으로는 처음과 끝이 연결된 원형형태의 큐를 이룬다고 가정하여 사용

### 원형 큐의 구조

- 초기 상태
  - front = rear = 0
- index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨후, 그다음에 논리적 순환을 이뤄 배열의 처음인 인덱스 0으로 이동
  - 이를 위해 나머지 연산자 mod사용

```python

def enq(data):
  global rear
  rear = (rear+1) % cQsize
  cQ[rear] = data

def deq():
  global front
  front = (front+1)%cQsize
  return cQ[front]

 
cQsize = N
cQ= [0]*cQsize
front = 0
rear = 0
```

### 우선순위 큐

- 우선순위 큐의 특성
  - 우선 순위를 가진항목들을 저장하는 큐
  - FIFO 순서가 아니라 우선순위가 높은 수너대로 먼저 나가게 됨

- 우선순위 큐의 적용분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링

### 큐의 활용 : 버퍼

- 버퍼
  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
  - 버퍼링 : 버퍼를활용하는 방식 또는 버퍼를 채우는 동작 의미

- 버퍼의 자료구조
  - 버퍼는 일반적으로 입출력 및 네트워크와 관련되 기능에서 이용된다.
  - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨

# 2023 08 18 friday

## BFS

- 그래프 탐색 방법
  - 깊이 우선 탐색
  - 너비 우선 탐색
- 너비 우선 탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐 활용

```python

def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
  visited = [0] *(n+1)  # n : 정점의 개수
  Q = []                # 큐생성
  Q.append(v)           # 시작점 v를 큐에 삽입
  visited[v] = 1
  while Q :             # 큐가 비어있지 않은 경우
    t = Q.pop(0)        # 큐의 첫번째 원소 반환
    if not visited[t] : # 방문되지 않은 곳이면
      # visited[t] = True # 방문한 것으로 표시
      visited(t)        # 정점 t에서 할 일
      for i in G[t]:    # t와 연결된 모든 정점에 대해
        if not visited[i]:  # 방문되지 않은 곳이면
          Q.append(i)       # 큐에 넣기  
          visited[i] = visited[t] +1  # n으로 부터 1만큼 이동


def BFS(s, v): # 시작 정점 s, 마지막 정점 v
  visited = [0] *(v+1)      # n : 정점의 개수
  Q = []                    # 큐생성
  Q.append(s)               # 시작점 v를 큐에 삽입
  visited[s] = 1            # 시작점 방문 표시
  while Q :                 # 큐에 정점이 남아있으면 front != rear
    t = Q.pop(0)            # 디큐
    print(t)                # 정점 t에서 할 일
    for w in range(1,v+1):  # 인접한 정점중 인큐 되지 않은 정점 w가 있으면
        if adj_l[t][w]==1 and visited[w]==0: 
          Q.append(i)       # 인큐  , 인큐되었음을 표시
          visited[i] = visited[t] +1  # n으로 부터 1만큼 이동
v,e = map(int, input().split())
arr =list(map(int, input().split()))
# 인접 리스트 --------------------------
adj_l =[[] for _ in range(v+1)]
for i in range(e):
  v1,v2 = arr[i*2], arr[i*2+1]
  adj_l[v1].append(v2)
  adj_l[v2].append(v1)   # 방향이 없으면
# 여기까지 인접 리스트 ------------------
BFS(1,7)

```

# 2023 08 21 monday

## 트리

### 트리의 개념

- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료 구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리모양의 구조
- 노드 - 트리의 원소
- 간선(edge) - 노드를 연결하는 선. 부모노드와 자식 노드를 연결
- 루트 노드(root node) -  트리의 시작 노드
- 형제 노드(sibling node) - 같은 부모 노드의 자식 노드들
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리 - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들
- 차수
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중 가장 큰 값
  - 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드
- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨

### 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다

- 노드 중 최상위 노드를 루트라고 한다.
- 나머지 노드들은 n(>= 0)개의 분리 집합 T1,,,TNㅇ로 분리될 수 있다.

### 이들 T1,,,TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 한다

## 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질수 있는 트리
  - 왼쪽 자식 노드
  - 오른쪽 자식 노드

### 종류

- 포화 이진 트리
  - 모든 레벨에 노드가 포화 상태로 차 있는 이진 트리
- 완전 이진 트리
- 편향 이진 트리
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리

### 이진트리 - 순회

- 순회란 트리의 각 노드를 중복 되지않게 전부 방문 하는것을 말한다.
- 트리는 비선형 구조이기에 선형 구조에서와 같이 선후 연결 관계를 알 수 없다.
- 따라서 특별한 방법 필요

### 순회 방법

- 전위순회
  - 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.
- 중위순회
  - 왼쪽 자식노드, 부모노드,오른쪽 자식노드 순으로 방문
- 후위순외
  - 자식노드를 좌우 순서로 방문한 후, 부모노드를 방문

```python

# ## 연습 문제
'''
v
n = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
'''
n = 13
lst = list(map(int, input().split()))
g = [[] for _ in range(n)]

cleft = [0] * (n + 1)
cright = [0] * (n + 1)
pn = [0] * (n + 1)
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i + 1]
    pn[c] = p
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c
# print(pn)       # [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]       # p[i]번의 부모는 i(0,1,2,,,)
# print(cleft)       # [0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0, 0]
# print(cright)       # [0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0, 0]
# ==============================
## 트리를 만들기
tree = [[0, 0] for _ in range(n + 1)]
# tree = [[0, 0, 0] for _ in range(n + 1)]      # <<  # [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]0,1,2,,,) 이런식으로 만들어보기
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i + 1]
    if tree[p][0] == 0:     # 왼쪽이 비어있으면:
        tree[p][0] = c
    else:
        tree[p][1] = c
    # tree[c][2] = p        # <<  # [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]0,1,2,,,) 이런식으로 만들어보기
# print(tree)     # [[0, 0], [2, 3], [4, 0], [5, 6], [7, 0], [8, 9], [10, 11], [12, 0], [0, 0], [0, 0], [0, 0], [13, 0], [0, 0], [0, 0]]
# =============================
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i + 1]
    g[p].append(c)
# print(g)    # [[], [2, 3], [4], [5, 6], [7], [8, 9], [10, 11], [12], [], [], [], [13], []]


```

```python

def pre_order(root):
    if root:
        print(root)
        pre_order(TREE[root][0])
        pre_order(TREE[root][1])



def print_tree1(root):
    if cl[root]: #왼쪽이 tree이면:
        print_tree(cl[root]) #root의 왼쪽서브트리의 root)
    print(root)

    if cr[root]: #오른쪽이 tree이면:
        print_tree(cr[root]) #root의 오른쪽서브트리의 root)

def print_tree(root):
    if root:
        print_tree(cl[root])
        print(root)
        print_tree(cr[root])


N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
G = [[] for _ in range(N+1)]

cl = [0] * (N+1)
cr = [0] * (N+1)
pn = [0] * (N+1)
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    pn[c] = p
    if cl[p] == 0:
        cl[p] = c
    else:
        cr[p] = c

print_tree(1)

# print(pn)
# print(cl)
# print(cr)

#===============================
TREE = [[0,0,0] for _ in range(N+1)]
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if TREE[p][0] == 0: #왼쪽이 비어 있으면:
        TREE[p][0] = c
    else:
        TREE[p][1] = c

    TREE[c][2] = p
# print(TREE)

#=====================
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    G[p].append(c)

print(G)

def post_order(root):
    
    if len(G[root]) >= 1:
        post_order(G[root][0])
    if len(G[root]) == 2 :
        post_order(G[root][1])
    print(root)

```

# 2023 08 22 tuesday

### 수식 트리의 순회

- 중위 순회
  - A/B*C*D+E
- 후위 순회
  - AB/C*D*E+
- 전위 순회
  - +**/ABCDE

### 이진 탐색 트리

- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖는다

### 이진 탐색 트리 - 연산

- 탐색연산
- 삽입연산
- 삭제연산

### 이진 탐색 트리 - 성능

- 연산시간은 트리의 높이 만큼 시간이 걸린다.
- 평균 O(log n)
- 최악 O(n)

## 힙(heap)

- 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해 만든 자료구조

```python

def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p=1                     # 루트에 옮긴 값을 자식과 비교
    c=p*2                   # 왼쪽 자식
    while c<= last:         # 자식이 하나라도 있으면...
        if c+1 <= last and heap[c] < heap[c+1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1          # 비교 대상이 오른쪽 자식 노드
        if heap[p] < heap[c]:       # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p=c             # 자식을 새로운 부모로
            c =p*2          # 왼쪽 자식 번호를 계산
        else:           # 부모가 더 크면
            break       # 비교 중단

    return tmp

heap = [0]*100
last = 0



#--------------------------------------------------


def insert(item):
    global last

    last += 1
    HEAP[last] = item
    c = last
    p = c // 2
    while c > 1 and HEAP[p] < HEAP[c]:
        # p = c//2
        HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
        c = p
        p = c//2
        # else:
        #     break


def pop():
    global last

    result = HEAP[1]
    HEAP[1] = HEAP[last]
    last -= 1

    p = 1
    c = p*2
    while c<=last:
        if c+1<=last and HEAP[c] < HEAP[c+1]:
            c = c+1
        if HEAP[p] < HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            p = c
            c = p*2
        else:
            break

    return result

HEAP = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] + [0]*100
last = 9
# insert(20)
# print(HEAP)
print(pop())
print(HEAP)
print(pop())
print(HEAP)
print(pop())
print(HEAP)

def insert(item):
    global last

    last += 1
    HEAP[last] = item
    c = last
    while c > 1:
        p = c // 2
        if HEAP[p] < HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            c = p        
        else:
            break
            
def pop():
    global last

    result = HEAP[1]
    HEAP[1] = HEAP[last]
    last -= 1

    p = 1
    while p*2 <= last:
        c = p * 2
        if c+1<=last and HEAP[c] < HEAP[c+1]:
            c = c+1
        if HEAP[p] < HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            p = c
        else:
            break

    return result

HEAP = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] + [0]*100
last = 9
# insert(20)
# print(HEAP)
print(pop())
print(HEAP)
print(pop())
print(HEAP)
print(pop())
print(HEAP)


```

# 2023 08 23 wednesday

## 알고리즘

- 어떤 문제를 해결하기 위한 절차

### 알고리즘의 효율

- 공간적 효율성, 시간적 효율성
  - 연산량 대비 얼마나 적은 메모리 공간을 요하는지
  - 연산량 대비 얼마나 적은 시간을 요하는지
  - 효율성이 낮으면 복잡도가 높다

- 시간 복잡도 분석
  - 환경에 따라 다름

- 복잡도의 점근적 표기
  - O-표기는 복잡도의 점근적 상한을 나타냄

## Python3 표준입출력

### 입력

- Raw 값의 입력 : input()
  - 받은 입력값을 문자열로 취급
- Evaluated된 값 입력 : eval(input())
  - 받은 입력값을 평가된 데이터 형으로 취급

### 출력

- print()
  - 표준 출력 함수. 출력값의 마지막에 개행 문자 포함
- print('text', end='')
  - 출력 시 마지막에 개행문자 제외할 시
- print('%d'%number)
  - Formatting 된 출력

```python
# 10 => 2 진수의 문자열 7 => '111'
def decTobin(decV):
    result = ''
    for shiftBit in range(4):
        t = decV & (1 << shiftBit)
        if t != 0:
            result = '1' + result
        else:
            result = '0' + result
    return result


print(bin(6))
print(decTobin(6))


# '1100' => 12
def BinToDec(Bins):
    result = 0
    for c in Bins:
        result = result * 2 + int(c)

    return result


print(BinToDec('1100'))


def BinToDec(Bins):
    result = 0
    for c in Bins:
        result = result << 1 | int(c)

    return result


print(BinToDec('1101'))


#   00000111 / 00000110
# & 00000001 / 00000001
# ==========================
#   00000001 / 00000000     1/0


def HexToDec(HexS):
    result = 0
    for c in HexS:
        if c.isdecimal():
            t = int(c)
        else:
            t = ord(c) - ord('A') + 10  # 대문자만 들어온다고 가정
        result = result * 16 + t

    return result


print(HexToDec('10A'))


# A => '1010'
def HexToBin(HexC):  # 16진수를 2진수로
    # 16진수 => 10진수
    if HexC.isdecimal():
        decV = int(HexC)
    else:
        tdecV = ord(HexC) - ord('A') + 10  # 대문자만 들어온다고 가정

    result = ''
    for shiftBit in range(4):
        t = decV & (1 << shiftBit)
        if t != 0:
            result = '1' + result
        else:
            result = '0' + result
    return result


def HexToBin2(HexC):
    mappintTable = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1111',
    }
    return mappintTable[HexC]


print(HexToBin2('A'))
```

# 2023 08 24 thursday

## 비트 연산

## 진수

## 실수

# 2023 08 29 tuesday

## 컴퓨팅 사고력

### 논리 vs 직관

- 하드로직  vs 소프트 로직
- 가끔 직관적으로 이해되는 알고리즘이 있지만 조금만 어려워지면 직관으로 완전한 이해를 얻는것은 사실상 불가능

- 명제
  - 참이나 거짓을 알 수 있는 식이나 문장
- 진릿값
  - 참이나 거짓을 표현

### 연산

- 부정 NOT
  - 명제의 진릿값이 반대
  - ~p
- 논리곱 AND
  - p,q 모두 참일 때 참이 되는 명제
  - p^q
- 논리합 OR
  - p,q 모두 거짓일 때만 거짓이 되는 명제
  - pVq
- 베타적 논리합 XOR
  - p,q중 하나만 참일때 참이 되는 명제
- 항진명제 : 진릿값이 항상 참
- 모순명제 : 진릿값이 항상 거짓
- 사건명제 : 항진 명제도 모순 명제도 아닌 명제

- 조건 명제
  - p가 조건, q가 결론으로 제시되는 명제
  - p -> q
- 쌍방 조건 명제
  - p와 q 모두 조건이면서 결론인 명제

- 조건명제의 역,이,대우
  - 역 : q -> p
  - 이 : ~p -> ~q
  - 대우 : ~q -> ~p

### 증명

- 증명은 정확한 명제식으로 표현할 수 있는 것이라야 함
- 보통은 정확한 명제식까지 쓰지는 않으나 근본적으로는 명제식으로 바꿀 수 있음
- 증명에 대한 수많은 오해가 p->q를 쌍방조건명제로 혼동하는 것에서 일어남

# 2023 08 30 wednesday

## 반복과 재귀

- 반복과 재귀는 유사한 작업을 수행할 수 있다.
- 반복은 수행하는 작업이 완료될 때 까지 계속 반복한다.
  - 루프(for, while 구조)
- 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
  - 하나의 큰 문제를 해결할 수 있는 (해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합한다.
  - 재귀 함수로 구현

- 재귀 함수
  - 기본부분 유도부분으로 구성됨

```python

def f(i, N, key, arr):
    if i == N:
        return 0
    elif arr[i] == key:
        return 1
    else:
        return f(i+1, N, key, arr)
N = 5
A = [1,2,3,4,5]
key = 4
print(f(0,N,key, A))

```

- 해결할 문제를 고려해서 반복이나 재귀의 방법을 선택
- 재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스럽다.
  - 추상 자료형(list, tree 등)의 알고리즘은 재귀적 구현이 간단하고 자연스러운 경우가 많다.
- 일반적으로 재귀적 알고리즘은 반복 알고리즘보다 더 많은 메모리와 연산을 필요로 함
- 입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있다.

## 완전 검색 기법

### baby-gin game

### brute-force

- 문제를 해결하기 위한 간단하고 쉬운 접근법
- 대부분의 문제에 적용 가능

- 모든 경우의 수를 생성하고 테스트하기 때문에 수행속도는 느리지만 해답을 찾아낼 확률이 높다
- 완전 검색으로 접근하여 해답을 도출한 후 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는것이 바람직하다

- 완전 검색
  - 특정 조건을 만족하는 경우나 요소를 찾는 문제가 많다.
  - 순열, 조합, 부분집합과 같은 조합적 문제들

### 순열

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현
  - nPr
- nPr은 다음 식이 성립 됨
  - nPr = n*(n-1)*(n-2)...(n-r+1)
- nPn = n!이라고 표기하고 Factorial 이라고 부른다
  - n! = n*(n-1)*(n-2)...2*1
- 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련있다.
  - TSP
- N개의 요소들에 대해서 n!개의 순열들이 존재한다.
  - n>12인 경우, 시간 복잡도 폭발적으로 증가

### 순열 생성 방법

- 사전적 순서
- 최소 변경을 통한 방법
  - 각각의 순열들은 이전의 상태에서 단지 두 개의 요소들 교환을 통해 생성
- 재귀 호출을 통한 순열 생성

```python

def f(i, N):
    if i == N:
        print(p)
        return 0
    else:
        for j in range(N):
            if used[j]==0:
                p[i]=card[j]
                used[j]=1
                f(i+1, N)
                used[j] = 0
card = [1,2,3]
used = [0] *3
p = [0] * 3
f(0,3)


def f(i, N, K):     # i 이전에 고른 개수, N개중에 K개 골라
    global cnt
    if i == K:      # 순열 완성: K개를 모두 고른 경우
        cnt += 1
        print(cnt,p)
        return 0
    else:       # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j]==0:   # 아직 사용되기 전이면
                p[i]=card[j]
                used[j]=1
                f(i+1, N,K) 
                used[j] = 0
card = [1,2,3,4,5]
cnt = 0
N = 5
K=3
used = [0] *N
p = [0] * K
f(0,N,K)     # N개 중에 K개 골라줘
```

## 부분 집합

- 집합에 포함된 원소들을 선택하는 것
- 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분 집합을 찾는 것
  - 예> 배낭 짐싸기
- N 개의 원소를 포함한 집합
  - 자기 자신과 공집합 포함한 모든 부분 집합의 개수는 2^n개
  - 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가

### 바이너리 카운팅을 통한 사전적 순서

- 부분집합을 생성하기 위한 가장 자연스러운 방법
- 바이너리 카운팅은 사전적 순서로 생성하기 위한 가장 간단한 방법

### 바이너리 카운팅

- 원소 수에 해당하는 N개의 비트열을 이용
- n번째 비트 값이 1이면 n번째 원소가 포함되었음을 의미

```python

def partial(k,sumV, zlst,olst):
    if k ==N:
        # print(bits)
        # sumV = 0
        # for i in range(N):
        #     if bits[i] == 1:
        #         sumV += numbers[i]
        #         #print(numbers[i], end = ' ')
        print(zlst,olst)
        return
    bits[k] = 0
    partial(k + 1, sumV, zlst+[numbers[k]], olst)
    bits[k] = 1
    partial(k+1,sumV+numbers[k],zlst,olst+[numbers[k]])

N = 4
numbers = [8,10,20,1]
bits = [-1]*N
result = []
zlst = []
olst = []
partial(0,0,zlst,olst)

```

# 2023 08 31 thursday

## 조합

- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합이라고 부른다
- nCr = n!/(n-r)!r!
- nCr = n-1Cr-1 +n-1Cr = 재귀적 표현
- nC0 = 1

```python

def ncr(n,r):
    if r==0:
        print(tr)
    elif n<r:   # 남은 원소보다 많은 원소를 선택해야하는 경우
        return  # 불가
    else:
        tr[r-1] = a[n-1]        # a[n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r)             # a[n-1]을 포함시키지 않는 경우
N = 5
R = 3
a = [1,2,3,4,5]
tr = [0]*R
ncr(N,R)



def nCr(n, r, s):
    if r==0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)
A = [1,2,3,4,5,6]
N = len(A)
R = 2
comb = [0]*R
nCr(N, R, 0)
```

- 합이 0 이되는 부분집합을 구하는 방법 중 하나

```python

def subset(i,N):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == 0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)


arr = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(arr)
bit = [0]*N
subset(0,N)

```

## 탐욕 알고리즘

- 탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법
- 일반적으로, 머리속에 떠오르는 생각을 검증없이 바로 구현하면 그리디 접근이 된다
- 여러 경우 중 하나를 선택 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
- 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없다.

- 일단 한번 선택된 것은 번복하지 않는다. 이런 특성 때문에 대부분의 탐욕 알고리즘들은 단순하며, 또한 제한적인 문제들에 적용된다.

- 최적화 문제란 가능한 해들중에서 가장 좋은(최대 또는 최소) 해를 찾는 문제이다.

### 탐욕 알고리즘의 동작 과정

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합에 추가한다.
2. 실행 가능성 검사 : 새로운 부분 해 집합이 실행가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는 지를 검사한다.
3. 해 검사 : 새로운 부분 해 집합이 문제의 해가 되는지를 확인 한다. 아직 전체 문제의 해가 완성 되지 않았다면 1의 해 선택부터 다시 시작한다.

### 배낭 짐싸기

- 배낭 짐싸기 문제의 정형적 정의
  - S = 물건들의 집합
  - w = 물건의 무게, p = 물건의 값
  - W = 배낭이 수용가능한 총 무게

  - 문제 정의
    - w <= W 를 만족하면서 p가 최대가 되도록 S에 포함되는 A를 구하는 문제
- 문제 유형
  - 1. 배낭에 담는 물건을 쪼갤 수 없는 경우
    - 완전 검색으로 S의 모든 부분집합을 구한다/
    - W를 초과하는 집합은 버리고 나머지 잡합에서 p가 가장큰것을 선택
    - 물건의 개수가 증가 하면 시간복잡도는 지수적으로 증가
      - 크기가 n인 부분합의 수 2**n
  - 2. 쪼갤수 있는 경우

### 활동 선택 문제

# 2023 09 01 friday

## 정사각형의 방을 푸는 4가지 방법

```python

#ver1

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    max_start = 0
    for p in range(N):
        for q in range(N):
            i, j = p, q
            cnt = 1
            start = arr[i][j]
            while True:
                for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[i][j] +1 == arr[ni][nj]:
                        cnt += 1
                        i, j = ni, nj
                        break
                else:
                    break
            if max_cnt < cnt:
                max_cnt = cnt
                max_start = start
            elif max_cnt == cnt and max_start > start:
                max_start = start
    print(f'#{tc} {max_start} {max_cnt}')

# 2
# 제일 빠름
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    cnt = [0] * (N*N+1)     # 연속으로 1이 커지는 경우를 표시할 배열
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                    cnt[arr[i][j]] = 1
    max_cnt = 0
    max_start = 0
    c = 0
    for k in range(N*N,0,-1 ):
        if cnt[k]:
            c += 1
            if max_cnt<c:
                max_cnt = c
                max_start = k
            elif max_cnt == c:
                max_start = k
        else:   # cnt[k] 가 0이면
            c = 0
    print(f'#{tc}', max_start, max_cnt+1)


# bfs 사용

def bfs(sr,sc,N):
    q = []
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    q.append((sr,sc))
    cnt = 0
    while q:
        i, j = q.pop(0)
        cnt += 1
        if v[i][j] != 0:
            return cnt + v[i][j] -1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and rm[i][j]+1 == rm[ni][nj]:
                q.append((ni,nj))
    return cnt

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    rm = [list(map(int, input().split()))for _ in range(N)]
    v = [[0]*N for i in range(N)]

    maxV = 0
    minV = 1000000
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                v[i][j] = bfs(i,j,N)
                if (maxV < v[i][j]):
                    maxV = v[i][j]
                    minV = rm[i][j]
                elif maxV == v[i][j]:
                    if minV > rm[i][j]:
                        minV = rm[i][j]
    print('#{} {} {}'.format(tc, minV, maxV))


# 재귀

def f(i,j,start,d):
    global ans
    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)): # 튜플 말고 리스트로 하면 시간초과남
        ni,nj=i+di,j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == False and arr[ni][nj] == arr[i][j]+1 :
            visited[i][j] = True
            f(ni,nj,start,d+1)
            visited[i][j] = False
    else:
        if ans[1] < d:
            ans = [start,d]
        elif ans[1] == d and start < ans[0]:
                ans[0] = start
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [0,0]
    visited = [[False] *N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            f(x,y,arr[x][y],1)
    print(f'#{tc}',*ans)

```

# 2023 09 04 monday

## web

- web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

- web site
  - 인터넷에서 여러 개의 web page가 모인것으로, 사용자들에게 정보나 서비스를 제공하는 공간
- web page
  - HTML, CSS 등의 웹 기술을 이용하여 만들어지, website를 구성하는 하나의 요소
  - 구성 요소
    - HTML : 'Structure'
    - CSS : 'Styling'
    - Javascript : 'Behavior'

## 웹 구조화

- HTML
  - HyperText Markup Language
  - 웹 페이지의 의미와 구조를 정의하는 언어
- hypertext
  - 웹 페이지를 다른 페이지로 연결하는 링크
  - 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- markup language
  - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - ex. HTML, Markdown

### HTML 구조

```html

<!DOCTYPE html>
- 해당 문서가 html로 문서라는 것을 나타냄
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
</head>
<body>
    <p>This is my page</p>
</body>
</html>
- 전체 페이지의 콘텐츠를 포함
<title></title>
- 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용

```

### HTML Element(요소)

- 하나의 요소는 여는 태그와 닫느 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫느 태그가 없는 태그도 존재

### HTML Attributes(속성)

- 규칙
  - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
  - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
  - 속성 값은 열고 닫는 따옴표로 감싸야 함
- 목적
  - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS에서 해당 요소를 선택하기 위한 값으로 활용됨

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
</head>
<body>
    <p>This is my page</p>
    <a href="https://www.naver.com/">Naver</a>
    <img src="images/sample.png" alt="sample image">
    <img src="https://random.imagecdn.app/500/150" alt="random image">
    
</body>
</html>



```

### HTML Text structure

- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

### HTML

- 웹 페이지의 의미와 구조를 정의하는 언어
- 예를 들어 h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것

### HTML Text structure 예시

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>main heading</h1>
    <h2>sub heading</h2>
    <p>this is my page</p>
    <p>this is <em>emphasis</em></p>
    <p>Hi my <strong>name is</strong> ait</p>
    <ul>
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ul>
</body>
</html>

```

## 웹 스타일링

### CSS

- 웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 구문

- 선택자
- 선언
- 속성 : 값

```css

h1{                  
  color: red;         
  font-size: 30px;
}

```

- CSS 적용 방법

- 1. 인라인 스타일
  - HTML 요소안에 style 속성 값으로 작성
- 2. 내부 스타일 시트
  - head 태그 안에 style 태그에 작성
- 3. 외부 스타일 시트
  - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
  - 가장 권장

### CSS 선택자

- CSS Selectors 종류
  - 기본 선택자
    - 전체 선택자(*)
      - HTML 모든 요소를 선택
    - 요소 선택자
      - 지정한 모든 태그를 선택
    - 클래스 선택자('.'(dot))
    - 아이디 선택자('#')
      - 주어진 아이디 속성을 가진 요소 선택
      - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
    - 속성 선택자 등
  - 결합자
    - 자손 결합자(""(space))
      - 첫 번째 요소의 직계 자식만 선택
      - 예. p span은 p 안에 있는 모든 span를 선택(하위 레벨 상관 없이)
    - 자식 결합자('>')
      - 첫 번째 요소의 직계 자식만 선택
      - 예. ul > li은 ul 안에 있는 모든 li를 선택(한단계 아래 자식들만)

### 우선순위

- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 적용 되는지 결정하는 것

- CSS : cascading style sheet
  - 웹 페이지의 디자인과 레이아웃을 구성하는 언어
- Cascade
  - 계단식
  - 동일한 우선순위를 같은 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용됨
- 우선순위가 높은 순
  1. importance
      - !important
      - 다른 우선순위 규칙보다 우선하여 적용하는 키워드
      - cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음
  2. inline 스타일
  3. 선택자
      - id > class > 요소
  4. 소스 코드 순서

- 우선순위 연습 코드

```html

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h2 {
      color: darkviolet !important;
    }

    p {
      color: blue;
    }

    .orange {
      color: orange;
    }

    .green {
      color: green;
    }

    #red {
      color: red;
    }
  </style>
</head>

<body>
  <p>1</p>
  <p class="orange">2</p>
  <p class="green orange">3</p>
  <p class="orange green">4</p>
  <p id="red" class="orange">5</p>
  <h2 id="red" class="orange">6</h2>
  <p id="red" class="orange" style="color: brown;">7</p>
  <h2 id="red" class="orange" style="color: brown;">8</h2>
</body>

</html>

```

### 상속

- CSS 상속
  - 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
- 상속 여부
  - 상속되는 속성
    - Text 관련요소 등..
  - 상속되지 않는 속성
    - Box model 관련 요소
    - position 관련 요소 등..
- CSS 상속 여부는 MDN 문서에서 확인하기
  - MDN 각 속성별 문서 하단에서 상속여부 확인 가능

# 2023 09 05 tuesday

## CSS Layout

- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
- Display, Position, Float, Flexbox 등

### CSS Box Model

- 모든 HTML 요쇼를 사각형 박스로 표현하는 개념
- 원이 아니라 네모 박스를 깎은 것
- 박스 요소들로 구조화 된 웹 페이지

#### 구성 요소

- 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되는 개념
- Margin
  - 이 박스와 다른 요소 사이의 공백 가장 바깥쪽 영역
- Border
  - 콘텐츠와 패딩을 감싸는 테두리 영역
- Padding
  - 콘텐츠 주위에 위치하는 공백 영역
- Content
  - 콘텐츠가 표시되는 영역
- width & height 속성
  - 요소의 너비와 높이를 지정
  - 이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함
  - border가 아님 content의 크기를 width값으로 지정

```html

<!-- 1 -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box1 {
      width: 200px;
      padding-left: 25px;
      padding-bottom: 25px;
      border-width: 3px;
      border-color: black;
      border-style: solid;
      margin-left: 25px;
      margin-bottom: 50px;
    }

    .box2 {
      width: 200px;
      border: 3px black dashed;
      /* margin-left: auto;
      margin-right: auto; */
      /* 상하/좌우 */
      margin: 100px auto;
      padding: 25px 50px;
    }
  </style>
</head>

<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
</body>

</html>


<!-- 2 -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* * {
      box-sizing: border-box;
    } */
    .box {
      width: 100px;
      border: 2px solid black;
      padding: 10px;
      margin: 20px;
      background-color: yellow;
    }

    .content-box {
      box-sizing: content-box;
    }

    .border-box {
      box-sizing: border-box;
    }
  </style>
</head>

<body>
  <div class="box content-box">content-box</div>
  <div class="box border-box">border-box</div>
</body>

</html>


```

#### 박스 타입

- Block & Inline
  - block = 상하
    - 항상 새로운 행으로 나뉨
    - width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
    - 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함(너비를 사용가능한 공간의 100%로 채우는 것)
    - 대표적인 block타입 태그
      - h1~6, p, div
  - inline = 좌우
    - 새로운 행으로 나뉘지 않음
    - width와 height 속성을 사용할 수 없음
    - 수직 방향
      - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
    - 수평 방향
      - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
    - 대표적인 inline 타입 태그
      - a, img, span
- Normal flow
  - CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향

#### 기타 display 속성

- inline-block
  - inline과 block 요소 사이의 중간 지점을 제공하는 display 값
  - block 요소의 특징을 가짐
  - 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
- none
  - 요소를 화면에 표시하지 않고, 공간 조차 부여되지 않음

### CSS Layout Position

#### CSS Position

- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

- Position 유형
  - static
    - 기본값
    - 요소를 Normal Flow에 따라 배치
  - relative
    - 요소를 Normal Flow에 따라 배치
    - 자기 자신을 기준으로 이동
    - 요소가 차지하는 공간은 static일 때와 같음
  - absolute
    - 요소를 Normal Flow에서 제거
    - 가장 가까운 relative 부모 요소를 기준으로 이동
    - 문서에서 요소가 차지하는 공간이 없어짐
  - fixed
    - 요소를 Normal Flow에서 제거
    - 현재 화면영역을 기준으로 이동
    - 문서에서 요소가 차지하는 공간이 없어짐
  - sticky
    - 요소를 Normal Flow에 따라 배치
    - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨
    - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
      - 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문

### CSS Layout Flexbox

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
- 공간 배열 & 정렬

# 2023 09 06 wednesday

## Fundamentals of Bootstrap

- Bootstrap
- CSS 프론트엔드 프레임워크(Toolkit)
- 미리만들어진 다양한 디자인 요소들을 제공하여 웹사이트를 빠르고 쉽게 개발할 수 있도록 함

- bootstrap에는 특정한 규칙이 있는 클래스 이름으로 이미 스타일 및 레이아웃이 작성되어 있음

### Typography

- 제목, 본문 텍스트, 목록 등
- display headings
  - 기존 heading보다 더 눈에 띄는 제목이 필요할 경우(더 크고 약간 다른 스타일)
- inline text elements
  - html inline 요소에 대한 스타일
- lists
  - html list 요소에 대한 스타일

### Colors

### Component

- bootstrap에서 제공하는 UI 관련 요소
  - 버튼, 네비게이션 바, 폼, 드롭다운 등

- 대표 component
  - alerts
  - badges
  - buttons
  - cards
  - navbar

- component 이점
  - 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용

## Semantic Web

- 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식
- 이 요소가 시각적으로 어떻게 보여질까? -> 이 요소가 가진 목적과 역할은 무엇일까?

### Semantic in HTML

- 문서의 최상위 제목
  - 단순히 최상위 제목'처럼' 보이게 출력하는 것
    - span style font-size 30px ...
  - 페이지 최상위 제목 의미를 제공하는 semantic 요소 h1, 브라우저에 의해 제목처럼 보이도록 스타일이 지정됨
    - h1

### HTML Semantic Element

- 기본적인 모양과 기능 이외의 의미를 가지는 HTML 요소
- 검색 엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록

#### semantic element

- header
- nav
- main
- article
- section
- aside
- footer

### semantic in CSS

- OOCSS
  - 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

- CSS 방법론
  - CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

- OOCSS 기본 원칙
  - 구조와 스킨을 분리
  - 컨테이너와 콘텐츠를 분리

# 2023 09 07 thursday

## Bootstrap Grid system

- 웹 페이지의 레이아웃을 조정하는데 사용되는 12개의 컬럼으로 구성됨 시스템
- 목적
  - 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

### Grid system 클래스와 기본 구조

- container
  - column들을 담고있는 공간
- column
  - 실제 컨텐츠를 포함하는 부분
- gutter
  - 컬럼과 컬럼 사이의 여백 영역
- 1개의 row안에 12칸의 column 영역이 구성 각 요소는 12칸 중 몇개를 차지할 것인지 지정됨

## Grid system for responsive web

- resposive web design
  - 디바이스 종류나 화면 크기에 상관 없이 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

### Grid system Breakpoints

- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
- 화면 너비에 따라 6개의 분기점 제공

# 2023 09 08 friday

# 2023 09 11 monday

## 일타 싸피

- 당구 게임을 만들어 봤다.
- 삼각함수를 사용해 거리와 쎄타를 구해활용했다.

```python

import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_KIMHYEOKIL'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.






    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    for i in [1,3,5]:
        if balls[i][0] > -1 and  balls[i][1] > -1:
            targetBall_x = balls[i][0]
            targetBall_y = balls[i][1]
            break
  
    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian + 1
    distance = math.sqrt(width**2 + height**2)
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 1
        else:
            angle = 179
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 91
        else:
            angle = 269
    # 1 사분면에 있을때
    # if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
    #     if targetBall_x < 127 and targetBall_y > 63.5 :    
    #         bigwidth = abs(HOLES[4][0] - whiteBall_x)
    #         bigheight = abs(HOLES[4][1] - whiteBall_y)
    #         a = math.sqrt(bigwidth**2 + bigheight**2)
    #         bigradian = math.atan(bigwidth/bigheight) if bigheight > 0 else 0
    #         bigangle = (180 / math.pi * bigradian)
    #         ttohw = abs(HOLES[4][0] - targetBall_x)
    #         ttohh = abs(HOLES[4][1] - targetBall_y)
    #         b = math.sqrt(ttohw**2 + ttohh**2)
    #         ttohradian = math.atan(ttohw/ttohh) if ttohh > 0 else 0
    #         ttohangle = (180 / math.pi * ttohradian)
    #         beta = bigangle - ttohangle
    #         betaradian = math.radians(beta)
    #         tgtohdis = b + 5.73
    #         c = math.sqrt(a**2+tgtohdis**2-2*a*tgtohdis*math.cos(betaradian))
    #         alpha = math.acos((a**2+c**2-tgtohdis**2)/(2*a*c))
    #         angle = bigangle+(180 / math.pi * alpha)
    #     else:
    #         bigwidth = abs(HOLES[5][0] - whiteBall_x)
    #         bigheight = abs(HOLES[5][1] - whiteBall_y)
    #         a = math.sqrt(bigwidth**2 + bigheight**2)
    #         bigradian = math.atan(bigwidth/bigheight) if bigheight > 0 else 0
    #         bigangle = (180 / math.pi * bigradian)
    #         ttohw = abs(HOLES[5][0] - targetBall_x)
    #         ttohh = abs(HOLES[5][1] - targetBall_y)
    #         b = math.sqrt(ttohw**2 + ttohh**2)
    #         ttohradian = math.atan(ttohw/ttohh) if ttohh > 0 else 0
    #         ttohangle = (180 / math.pi * ttohradian)
    #         beta = bigangle - ttohangle
    #         betaradian = math.radians(beta)
    #         tgtohdis = b + 5.73
    #         c = math.sqrt(a**2+tgtohdis**2-2*a*tgtohdis*math.cos(betaradian))
    #         alpha = math.acos((a**2+c**2-tgtohdis**2)/(2*a*c))
    #         angle = bigangle+(180 / math.pi * alpha)
        
    # 2사분면
    
        
    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180
    
    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90
        
    # distance: 두 점(좌표) 사이의 거리를 계산
    # distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = 60
    






    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')

```

# 2023 09 12 tuesday

## Django Intro & Design Pattern

### Django and Framework

- '웹 서비스 개발'에는 무엇이 필요할까?
  - 로그인, 로그아웃, 회원관리, 데이터 베이스, 보안 등... 너무많은 기술들이 필요
  - 하지만 모든 걸 직접 만들 필요가 없음
  - 잘만들어진 것들을 가져와 좋은 화경에서 잘 사용하는 것도 능력인시대
  - 거인의 어깨 위에서 프로그래밍 하기

#### Framework

- 웹 애플리케이션을 빠륵 개발할 수 있도록 도와주는 도구
- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공

- 왜 프레임워크를 사용할까?
  - 기본적인 구조, 도구, 규칙 등을 제공하기 때문에 개발자는 필수적인 해야 하는 핵심 개발에만 집중 할 수 있음
  - 여러 라이브러리를 제공해 개발 속도를 빠르게 할 수 있음 (생산성)
  - 유지 보수와 확장에 용이해 소프트 웨어의 품질을 높임

- django
  - python 기반의 대표적인 웹 프레임 워크

- 클라이언트와 서버
  - 웹의 동작 방식
    - 우리가 컴퓨터 혹은 모바일 기기로 웹 페이지를 보게 될 때까지 무슨 일이 일어날까?
  - 클라이언트
    - 서비스를 요청하는 주체
    - 웹 사용자의 인터넷이 연결된 장치, 웹 브라우저
  - 서버
    - 클라이언트의 요청에 응답하는 주체
    - 웹 페이지, 앱을 저장하는 컴퓨터
  - 우리가 웹 페이지를 보게 되는 과정
    - 웹 브라우저(클라이언트)에서 '구글.com' 입력
    - 인터넷에 연결된 구글 컴퓨터(서버)에 파일 달라고 요청
    - 구글 데이터베이스에서 파일을 찾아 응답
    - 웹 브라우저가 전달받은 파일로 사람이 볼수있게 해석
  - 장고를 사용해 서버 구현

- 프로젝트 및 가상환경
  - 가상환경
    - python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할수 있는 독립적인 실행 환경
  - 가상환경이 필요한 시나리오 1
    - 프로젝트 두개 진행 a,b
    - a에서 requests 버전 1사용
    - b는 2사용
    - 하지만 파이썬에는 패키지 버전 하나만 존재 가능
    - a,b는 다른 버전의 독립적인 개발 환경이 필요
  - 시나리오 2
    - 2개 a,b진행
    - a, water 패키지 사용
    - b, fire 패키지 사용
    - water, fire 패키지 함께 사용시 충돌 발생
    - a,b는 충돌을 피하기 위해 독립적인 개발 환경 필요
  - 패키지 목록이 필요한 시나리오 1
    - 프로젝트를 두명이 개발
    - a가 관련패키지를 설치하고 개발 중 협업을 위해 github에 push
    - b는 clone을 받고 실행하지만 시행 안됨
    - a가 어떤 패키지를 설치 했는지 버전은 어떤것인지 알 수 없다
    - 패키지 목록이 공유 되어야함
  - 장고 프로젝트 생성 루틴 + git
    - 가상환경 venv 생성
      - python -m venv venv
    - 가상환경 활성화
      - source venv/Scripts/activate
    - 장고 설치
      - pip install Django
    - 의존성 파일 생성
      - pip freeze > requirements.txt
    - .gitigmore 파일 생성 (첫 add 전)
    - git 저장소 생성
    - 장고 프로젝트 생성
      - django-admin startproject firstpjt .
      - 여기서 . 은 현재 디렉토리를 의미함
  - 가상환경을 사용하는 이유
    - 의존성 관리
      - 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용 가능
    - 팀 프로젝트 협업
       모든 팀원이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌 방지
  - LTS
    - 프레임 워크나 라이브러리 등의 소프트 웨어에서 장기간 지원 되는 안정적인 버전을 의미할 때 사용
    - 기업이나 대규모 프로젝트에서는 소프트 웨어 업그레이드에 많은 비용과 시간이 필요하기에 안정적이고 장기간 지원되는 버전이 필요

### Django Design Pattern

- 장고 프로젝트
  - 애플리케이션의 집합
  - (DB 설정, URL 연결, 전체 앱 설정 등을 처리)
- 장고 어플리케이션
  - 독립적으로 작동하는 기능 단위 모듈
  - 각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성
- 앱 사용 과정
  - 앱 생성
    - python manage.py startapp articles
    - 앱의 이름은 복수형으로 지정하는것을 권장
  - 앱 등록
    - 반드시 앱생성 후 등록
    - 등록후 생성은 불가능
- 디자인 패턴
  - 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
  - 공통적인 문제를 해결하는데 쓰이는 형식화 된 관행
- MVC 디자인 패턴
  - model, view, controller
  - 애플리케이션을 구조화하는 대표적인 패턴
  - 데이터, 사용자 인터페이스, 비즈니스 로직을 분리
  - 시각적 요소와 뒤에서 실행되는 로직을 서로 영향없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해
- MTV 디자인 패턴
  - model, template, view
  - 장고에서 애플리케이션을 구조화하는 패턴
  - 기존 MVC패턴과 동일하나 명칭을 다르게 정의한 것
- 프로젝트 구조
  - settings.py
    - 프로젝트의 모든 설정을 관리
  - urls.py
    - url과 이에 해당하는 적절한 views를 연결
  - init.py
    - 해당 폴더를 패키지로 인식하도록 설정
  - asgi.py
    - 비동기식 웹 서버와의 연결 관련 설정
  - wsgi.py
    - 웹 서버와의 연결 관련 설정
  - manage.py
    - 장고 프로젝트와 다양한 방법으로 상화작용 하는 커맨드라인 유틸리티
- 앱 구조
  - admin.py
    - 관리자용 페이지 설정
  - models.py
    - db와 관련된 모델 정의
    - mtv 패턴의 m
  - views.py
    - http 요청을 처리하고 해당 요청에 대한 응답을 반환
    - mtv의 v
  - apps.py
    - 앱의 정보가 작성된 곳
  - tests.py
    - 프로젝트 테스트 코드를 작성하는 곳

#### 요청과 응답

# 2023 09 13 wednesday

## Django Template & URLs

### Djang0 Template

- 데이터 표현을 제어하면서, 표현솨 관련된 부분을 담당

- DTL
  - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
- DTL Syntax
  - variable
    - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에서 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot(.)를 사용하여 변수 속성에 접근할 수 있음
  - filters
    - 표시할 변수를 수정할 때 사용
    - chained가 가능하면 일부 필터는 인자를 받기도 함
    - 약 60개의 빌트인 필터 제공
  - tags
    - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 빌트인 태그스 제공
  - comments
    - DTL에서의 주석

#### 템플릿 상속

- 기본 템플릿 구조의 한계
  - 만약 모든 템플릿에 bootstrap을 적용하려면?
  - 모든 템플릿에 bootstrap CDN을 작성해야 할까?
- 템플릿 상속
  - 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
  - 'extend'tag
    - 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
    - 반드시 템플릿 최상단에 작성 필요 (2개 이상 불가)
  - 'block'tag
    - 하위 템플릿에서 재정의 할 수 있는 블록을 정의
    - 하위 템플릿이 작성할 수 있는 공간을 지정

#### HTML form(요청과 응답)

- 데이터를 보내고 가져오기
  - HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기
  - HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 'form'element
  - 사용자로 부터 할당된 데이터를 서버로 전송
  - 웹에서 사용자 정보를 입력하는 여러방식(text, password, checkbox 등)을 제공
- 'action' & 'method'
  - 데이터를 어디(action)로 어떤 방식(method)으로 요청할지
  - action
    - 입력 데이터가 전송될 URL을 지정 (목적지)
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
  - method
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request methods (GET, POST)를 지정

### Django URLs

# 2023 09 14 thursday

## Django Model

- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
- 테이블 구조를 설계하는 청사진

### Model

- 작성한 모델 클래스는 최종적으로 DB에 테이블 구조를 만듦
- django.db.models 모듈의 model이라는 부모클래스를 상속 받음
- Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스
- 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것 (프레임워크의 이점)
- 클래스 변수명
  - 테이블의 각 '필드(열) 이름'
- model Field 클래스
  - 테이블 필드의 데이터타입
- model Field 클래스의 키워드 인자 (필드 옵션)
  - 테이블 필드의 '제약조건' 관련 설정
- 제약 조건
  - 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
  - ex. 숫자만 저장되도록,문자가 100자 까지만 저장되도록 하는 등

### Migrations

- model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법
- model class(설계도 초안) -makemigrations-> migration 파일(최종 설계도) -migrate-> db.sqlite3(DB)
- python manage.py makemigrations
  - model class를 기반으로 최종 설계도(migration) 작성
- python manage.py migrate
  - 최종 설계도를 DB에 전달하여 반영

- 이미 생성된 테이블에 필드를 추가해야 한다면
  - 이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 팔드의 기본값 설정이 필요
    - 1번 현재 대화를 유지하면서 직접 기본 값을 입력 하는 방법
    - 2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
  - 추가하는 필드의 기본 값을 입력해야하는 상황
  - 날짜 데이터이기 때문에 직접 입력하기 보다 Django가 제안하는 기본 값을 사용하는 것을 권장
  - 아무것도 입력하지 않고 엔터를 누르면 장고가 제안하는 기본값으로 설정 됨
  - migrations 과정 종료 후 2번째 migration 파일이 생성됨을 확인
  - 이처럼 장고는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수있도록 함(마치 git commit)

- model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고, 이를 DB에 반영해야 한다.

- model field
  - DB 테이블의 필드(열)을 정의 하며, 해당 필드에 저장 되는 데이터 타입과 제약조건을 정의
- CharField()
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - 필드의 최대 길이를 결정하는 max_length는 필수 인자
- TextField()
  - 글자의 수가 많을 때 사용
- DateTimeField()
  - 날짜와 시간을 넣을 때 사용
  - 선택인자
    - auto_now
      - 데이터가 저장되 때마다 자동으로 현재 날짜 시간을 저장
    - auto_now_add
      - 데이터가 처을 생성될 때만 자동으로 현재 날짜시간을 저장

### Admin site

- Automatic admin interface
  - 장고는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
  - 데이터 확인 및 테스트 등을 진행하는데 매우 유용
- admin 계정 생성
  - email은 선택사항, 입력하지 않고 진행 가능
  - 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
  - python manage.py createsuperuser
- admin에 모델 클래스 등록
  - admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능

# 2023 09 15 friday

## Django ORM

### ORM

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

### QuerySet API

- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

#### Query

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다.
  - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라눈 자료 형태로 변환하여 우리에게 전달

#### QuerySet

- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- django orm을 통해 만들어진 자료형
- 단 데이터베이스가 단일한 객체를 반환할 때는 queryset이 아닌 모델(class)의 인스턴스로 반환됨

- python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것

### QuerySet API 실습

- 장고 app 등록 권장 순서
  1. normal app
  2. third party app
  3. django app

#### Create

- Django shell
  - 장고 환경 안에서 실행되는 python shell
  - 입력하는 queryset api 구문이 장고 프로젝트에 영향을 미침

#### Read

- all()
- get()
- filter()

#### Update

#### Delete

# 2023 09 18 monday

- 알고리즘 설계 기법의 종류
  - 전체를 다 보기 (Brute Force - 완전 탐색)
    - 배열 : 반복문 다 돌리기
    - 그래프 : DFS, BFS
  - 상황마다 좋은 걸 고르자 (Greedy - 탐욕)
    - 규칙을 찾는 것
    - 주의사항 : 항상 좋은 것을 뽑아도, 최종 결과가 제일 좋다 = 보장되지 않는다.
  - 하나의 큰 문제를 작은 문제로 나누어 부분적으로 해결하자(Dynamic Programming)
    - Memorization 기법 사용
    - 점화식(bottom-up), 재귀(top-down)
  - 큰 문제를 작은 문제로 쪼개서 해결하자(Divide and Conquer - 분할 정복)
  - 전체 중, 가능성 없는 것을 빼고 보자(Backtracking - 백트래킹)
    - 가지치기

## 분할 정복 & 백트래킹

- 설계 전략
  - 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다
  - 정복 : 나눈 작은 문제를 각각 해결한다.
  - 통합 : (필요하다면) 해결된 해답을 모은다

- 반복 알고리즘 : O(n)
- 분할 정복 비나 알고리즘 : O(log n)

### 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  - top-down 방식
- 시간 복잡도 : O(n log n)

- 병합 정렬 과정
  - 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
  - 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합

```python

def merge(l_lst, r_lst):
    result = []
    l_pos = r_pos = 0
    while l_pos < len(l_lst) and r_pos < len(r_lst):
        if l_lst[l_pos] < r_lst[r_pos] :
            result.append(l_lst[l_pos])
            l_pos += 1
        else:
            result.append(r_lst[r_pos])
            r_pos += 1
    result += l_lst[l_pos:]
    result += r_lst[r_pos:]
    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    l_lst = merge_sort(arr[:mid])
    r_lst = merge_sort(arr[mid:])
    result = merge(l_lst,r_lst)
    return result

```

### 퀵 정렬

- 주어진 배열을 두개로 분할하고, 각각을 정렬한다.
  - 병합 정렬과 동일

- 다른점1 : 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵정렬은 분할할 때, 기준 아이템 중심으로, 이보다 작은것은 왼편, 큰것은 오른편에 위치 시킨다.
- 다른점2 : 각부분 정렬이 끝난 후, 병합정렬은 '병합'이란 후처리 작업이 필요하나, 퀵정렬은 필요로 하지 않는다.

```python
# ver 1
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# ver 2
def h_par(s,e):
    p = s
    i = s
    j = e
    while i<=j :
        while i<=j and lst[i] <= lst[p]:
            i += 1
        while i<=j and lst[j] >= lst[p]:
            j -= 1
        if i<j :
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[j] = lst[j], lst[p]
    return j

def l_par(s,e):
    p = e
    i =s-1
    for j in range(s,e):
        if lst[j] <= lst[p]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[p] = lst[p], lst[i+1]
    return i+1

def quick_sort(s,e):
    if s>=e:
        return -1
    # pivot = h_par(s,e)
    pivot = l_par(s,e)
    quick_sort(s,pivot-1)
    quick_sort(pivot+1,e)

lst = [2,4,1,5,7,9,2]
N = len(lst)
quick_sort(0,N-1)
print(lst)
```

### 병합 정렬, 퀵 정렬

- 병합 정렬
  - 멀티쓰레드
- 퀵 정렬
  - 매우 큰 입력 데이터에 대해서 좋은 성능을 보인다
- 둘다 직접 구현할 일은 적다, 과거 면접 단골 질문 + 분할 정복 학습에 좋다,
그림 그려보기!

## 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 위해서는 자료가 정렬된 상태여야 한다.

### 검색 과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

```python

arr = [2,4,7,9,11,19,23]

arr.sort()
def binarySearch(target):
    low = 0
    high = len(arr) - 1

    # low > high 라면 데이터를 못찾은 경우
    while low <= high :
        mid = (low+high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target :
            return mid
        # 2. 가운데 값이 정답 보다 작은 경우
        elif arr[mid] < target :
            low = mid +1
        # 3. 가운데 값이 정답 보다 큰 경우
        else:
            high = mid - 1

    return '데이터 없음'

# 재귀

# 함수 한번 호출 때 마다 low, hig 변수가 바뀌어서 사용됨
def binarySearch1(low, high, target):
    # 기저 조건 : 언제까지 재귀호출을 반복할 것인가?
    # low > high 라면 데이터를 못찾음
    if low > high :
        return -1

    mid = (low + high) // 2

    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답 보다 작은 경우
    elif arr[mid] < target:
        return binarySearch1(mid + 1, high, target)
    # 3. 가운데 값이 정답 보다 큰 경우
    elif arr[mid] > target:
        return binarySearch1(low , mid - 1, target)

print(f'9 = {binarySearch1(0, len(arr) - 1, 9)}')

```

# 2023 09 19 tuesday

## 백트래킹

- 여러가지 옵션들이 존재하는 상황에서 한가지를 선택한다.
- 선택이 이루어지면서 새로운 선택지들의 집합이 생성된다.
- 이런 선택을 반복하면서 최종상태에 도달한다.
  - 올바른 선택을 계속하면 목표 상태에 도달한다.

### 당첨 리프 노드 찾기
  
- 루트에서 갈 수 있는 노드를 선택
- 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작
- 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다.
- 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 답이 없다.

### 백트래킹과 DFS의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로 시도의 횟수를 줄임(Prunning 가지치기)
- DFS가 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- DFS를 가하기에는 경우의 수가 너무나 많음 즉 N! 가지의 경우의 수를 가진 문제에 대해 DFS를 가하면 당연히 처리 불가
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능

### 8-Queens 문제

- 퀸 8 개를 체스판 안에 서로를 공격할 수 없도록 배치하는 모든 경우의 수를 구하라

- 후보 해의 수
  - 64C8
  - 64!/8!(64-8)!
  - 약 44억

- 실제 해의 수
  - 이 중에 실제 해는 92개 뿐

- 즉 44억개가 넘는 후보 해의 수 속에서 92개를 최대한 효율적으로 찾아내는 것이 관건

### 백트래킹의 기본 구조

- def
- 재귀를 끝내는 기저 조건
- 가지치기
- 반복문
  - 가지치기
  - 재귀들어가기전
  - 재귀함수 호출
  - 돌아와서 초기화

## 트리

- 사이클이 없는 연결 그래프
  - 사이클
  - 연결 그래프 : 모든 꼭지점이 서로 갈수있다

- 이진 트리
  - 자녀 노드가 둘 이하인 트리
  - 이진 트리 종류
    - 완전 이진 트리
      - 마지막 레벨을 제외한 모든 레벨은 꽉 차있어야 함.
      - 마지막 레벨 노드는 왼쪽부터 채워져야한다.
    - 포화 이진 트리
      - 모든 레벨이 꽉 차있는 것
    - 나머지 이진 트리
  - 순회방법
  - 트리 저장 방법

```python

arr = [1,2, 1,3, 2,4, 3,5, 3,6]

# 이진 트리 만들기
nodes =[[] for _ in range(14)]
for i in range(0,len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)

# 자식이 더 이상 없다는 걸 표시하기 위해 None 을 삽입
for li in nodes :
    for _ in range(len(li),2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None :
        return
    print(nodeNumber, end = ' ')
    preorder(nodes[nodeNumber][0])
    # print(nodeNumber, end= ' ')
    preorder(nodes[nodeNumber][1])
    # print(nodeNumber, end=' ')

preorder(1)

```

## 힙

- 최대 힙
  - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키 값 > 자식 노드의 키 값
  - 루트 노드 : 키값이 가장 큰 노드
- 최소 힙
  - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키 값 < 자식 노드의 키값
  - 루트 노드 : 키값이 가장 작은 노드

```python

def enque(item):
    global hsize

    hsize += 1
    Tree[hsize] = item

    c = hsize
    p = c//2

    while p and Tree[p] < Tree[c]:
        Tree[p], Tree[c] = Tree[c], Tree[p]
        c = p
        p = c//2

def deque():
    global hsize
    result =Tree[1]
    Tree[1] = Tree[hsize]
    hsize -= 1

    p=1
    c=p*2

    while c<=hsize :
        if c+1 <= hsize and Tree[c] < Tree[c+1] :
            c= c+1
        if Tree[p] < Tree[c] :
            Tree[p], Tree[c] = Tree[c], Tree[p]
            p = 1
            c = p*2
        else:
            break
    return result

Tree = [0, 20 , 15, 19,4 ,13, 11]
Tree += [0]*100
hsize= 6
enque(23)
enque(17)
# print(Tree)

print(deque())
print(Tree)


```

# 2023 09 20 wednesday

## 그래프

- 실 세계 문제를 그래프로 추상화해서 해결하는 방법을 학습
  - 그래프 탐색 기법인 BFS와 DFS에 대해서
  - 그래프 알고리즘에 활용되는 상호베타 집합의 자료구조에 대해서
  - 최소 신장트리를 이해, 탐욕기법 이용, 그래프에서 최소 신장트리를 찾는 알고리즘을 학습
  - 두 정점 사이의 최단 경로를 찾는다

- 그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계 표현

- 그래프는 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료구조
  - 5개 정점이 있는 그래프의 최대 간선 수는 5(5-1)/2 , 10개 이다.
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N : N 관계를 가지는 원소들을 표현하기에 용이하다

### 그래프 유형

- 무향 그래프
- 유향 그래프
- 가중치 그래프
- 사이클 없는 방향 그래프
- 완전 그래프
  - 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프
  - 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

### 그래프 경로

- 경로란 간선들을 순서대로 나열한것

- 경로 중 한 정점을 최대한 한번만 지나는 경로를 단순경로 라고한다(0-2-4-6)
- 시작 정점에서 끝나는 경로를 사이클 이라고한다 (1-3-5-1)

### 그래프 표현

- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려
- 인접 행렬
  - 정점*정점 크기의 2차원배열을 이용
  - 메모리를 많이 차지
- 인접 리스트
  - 각 정점에서 해당 정점으로 나가는 간선의 정보를 저장
- 간선의 배열
  - 간선을 배열에 연속적으로 저장

### 그래프 순회 (탐색)

- 그래프 순회는 비선형 구조인 그래프로 표현된 모든 자료(정점)을 빠짐 없이 탐색하는 것을 의미한다.

- DFS
  - 스택
  - 재귀

  ```python
  
  def dfs(now):
    visited[now] = 1    # 방문 표시

    # 인접한 노드들 방문      
    for next in range(5):
      if graph[now][next] == 0:
        continue
      if visited[next]:
        continue
      dfs(next)
  
  ```

- BFS
  - 큐

## 서로소 집합들

- 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다. 교집합이 없다.
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 대표자라 한다.

- 상호배타 집합을 표현하는 방법
  - 연결 리스트
  - 트리

- 상호배타 집합 연산
  - Make-set(x)
  - Find-set(x)
    - 각 요소가 내가 속한 그룹의 대표자를 어떻게 찾을지?
  - Union(x,y)
    - 대표자 저장(같은 그룹으로 묶기)

### 연결 리스트

- 같은 집합의 원소들은 하나의 연결 리스트로 관리한다.
- 연결리스트의 맨앞의 원소를 집합의 대표 원소로 삼는다.
- 각 원소는 집합의 대표원소를 가리키는 링크를 갖는다.

```python

p = [i for i in range(10)]
# find-set
def find_set(x):
    if p[x] == x:
        return x

    #return find_set(p[x])

    # 경로 압축
    p[x] = find_set(p[x])
    return p[x]

# union
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y :
        print('사이클 발생')
        return

    # 2. 이미 다른 집합이라면, 같은 대표자로 수정
    if x < y :
        p[y] = x
    else:
        p[x] = y
union(0,1)

union(2,3)

union(1,3)

# 이미 같은 집합에 속해있는 원소를 한 번 더 union
# 사이클 발생
union(0,2)


# 대표자 검색
print(find_set(2))
print(find_set(3))

# 같은 그룹인지 판별
t_x = 0
t_y = 2


if find_set(t_x) == find_set(t_y):
    print(t_x,t_y,'같은 집합')
else:
    print(t_x,t_y,'다른 집합')

```

# 2023 09 21 thursday

## 최소 비용 신장 트리 (MST)

- 그래프에서 최소 비용 문제
  1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
  2. 두정점 사이의 최소 비용의 경로 찾기

- 신장 트리
  - 모든 정점을 연결
  - 사이클이 존재하지 않는 부분 그래프
    - 간선의 개수 : n-1개
  - 한그래프에서 여러개의 신장 트리가 나올수 있다.
  - n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

- 최소 신장 트리
  - 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

### prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
  1. 임의 정점 하나 선택 후 시작
  2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
  3. 모든 정점이 선택 될때 까지 1.2 반복

- 서로소인 2개의 집합 정보를 유지
  - 트리 정점들 - MST를 만들기 위해 선택된 정점들
  - 비트리 정점들 - 선택 되지 않은 정점들

```python

def prim(s):
    # 연결된 노드의 번호를 저장
    U = []
    D = [10000]*N
    P = [-1]*N
    D[s] = 0
    for _ in range(N):
        # D에 있는 것중에 최선을 고른다(제일 작은값)
        minV = 10000
        for i in range(N):
            if i in U:
                continue
            if D[i] < minV :
                minV = D[i]
                curN = i

        # curN 결정
        U.append(curN)

        # curN 와 연결되어있는 노드들의 값을 최선으로 변경
        for i in range(N):
            if i in U or G[curN][i] == 0:
                continue
            if D[i] > G[curN][i] :
                D[i] = G[curN][i]
                P[i] = curN
    print(U)
    print(D)
    print(P)

N, E = map(int, input().split())
G = [[0]*N for _ in range(N)]
for i in range(E):
    v1,v2, w = map(int,input().split())
    G[v1][v2] = w
    G[v2][v1] = w
prim(0)

```

### KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
  1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
  2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가 시킴, 사이클이 전재하면 다음으로 가중치가 낮은 간선 선택
  3. n-1개의 간선이 선택될 때 까지 2를 반복

## 최단경로

- 최단 경로 정의
  - 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단경로
  - 다익스트라 알고리즘
    - 음의 가중치를 허용하지 않음
  - 벨만 포드 알고리즘
    - 음의 가중치를 허용하지 않음

- 모든 정점들에 대한 최단 경로
  - 플로이드 워샬 알고리즘

### 다익스트라 알고리즘

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.
- 시작 정점(s) 에서 끝정점(t) 까지의 최단 경로에 정점 x가 존재한다.
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성된다.
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다

```python

def dijk(s):
    U = []
    D = [10000]*N
    D[s] = 0
    for _ in range(N):
        # D에 있는 것중에 최선을 고른다(제일 작은값)
        minV = 10000
        for i in range(N):
            if i in U:
                continue
            if D[i] < minV :
                minV = D[i]
                curN = i

        # curN 결정
        U.append(curN)

        # curN 와 연결되어있는 노드들의 값을 최선으로 변경
        for i in range(N):
            if G[curN][i] == 0:
                continue
            if D[i] > G[curN][i] + D[curN] :
                D[i] = G[curN][i] + D[curN]

    print(U)
    print(D)



N,E = map(int, input().split())
G = [[0]*N for _ in range(N)]
for i in range(E):
    v1,v2, w = map(int, input().split())
    G[v1][v2] = w

dijk(0)

```

# 2023 09 25 monday

## Django ORM with view

### Read

- 전체 게시글 조회
- 단일 게시글 조회

### Create

- Create 로직을 구현하기 위해 필요한 view 함수의 개수
  - 사용자 입력 데이터를 받을 페이지를 렌더린
    - new
  - 사용자가 입력한 데이터를 받아 DB에 저장
    - create
  
### HTTP request methods

- HTTP
  - 네트워크상에서 데이터를 주고 받기 위한 약속
- HTTP request methods
  - 데이터에 어떤 요청을 원하는지를 나타내는 것
  - GET & POST
    - GET
      - 특정 리소스를 조회하는 요청
      - GET으로 데이터를 전달하면 Query String 형식으로 보내짐
    - POST
      - 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 요청
      - POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐
- HTTP response status code
  - 특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하기로 약속한 것
  - 404 Forbidden
    - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
    - CSRF
      - 사이트간 요청 위조
    - CSRF Token 적용
      - DTL의 csrf_token 태그를 사용해 사용자에게 토큰 값을 부여

- redirect
  - 게시글 작성 후 완료를 알리는 페이지를 응답하는 것
  - 사용자가 GET 요청을 한번 더 보내도록 해야한다.
  - 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수

### Delete

### Update

# 2023 09 26 tuesday

## Django Form

- HTML 'form'
  - 지금까지 사용자로부터 데이터를 받기위해 활용한 방법 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
  - 유효한 데이터인지 확인 필요

- 사용자 입력데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화 할 수있는 기능을 제공

### 유효성 검사

- 수집한 데이터가 정확하고 유효한지 확인하는 과정

- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

### Form Class

### Widgets

- HTML 'input' element의 표현을 담당

### Django ModelForm

- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때
  - ex. 로그인

- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때
  - ex. 게시글, 회원가입
  - Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
  - Form + Model

- Meta class
  - ModelForm의 정보를 작성하는 곳
  - fields , exclude 속성
  - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음

- 정리
  - 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구
  - HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

## Handling HTTP requests

### view 함수 구조 변화

- new & create view 함수간 공통점과 차이점
  - 공통점
    - 데이터 생성을 구현하기 위함
  - 차이점
    - new는 GET method 요청만을, create는 POST method 요청만을 처리

# 2023 09 27 wednesday

## Static files

- 정적 파일
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS파일 등)
- 웹 서버의 기본 동작은 특정 위치에 있는 자원을 요청받아서 응답을 처리하고 제공하는 것

- 이는 자원에 접근 가능한 주소가 있다 라는 의미
- 웹서버는 요청받은 URL로 서버에 존재하는 정적 자원을 제공함
- 정적파일을 제공하기 위한 경로가 있어야함

- 기본경로에서 제공하기
- 추가 경로에서 제공하기

### static_url

- 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL 실제 파일이나 디렉토리가 아니며, URL로만 존재

## Media files

- 사용자가 웹에서 업로드하는 정적 파일

### Imagefield()

- 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로'가 문자열로 DB에 저장

### MEDIA_URL

- media_root에서 제공되는 미디어 파일에 대한 주소를 생성

- 성능 및 DB 최적화
  - 직접 파일을 저장하면 DB 크기가 급격하게 증가
  - 성능 저하
  - 파일 자체는 파일 시스템에 별도로 저장
  - DB에는 그 파일에 대한 문자열 경로만

- 유지 보수 관점
  - 만약 db에 직접 파일을 저장해버리면 파일을 변경하거나 업데이트 할때 db를 직접 조작해야 함
  - 그런데 db에 경로만 저장되어있다면 파일시스템에서만 파일을 수정하면 됨

# 2023 10 04 wednesday

## Django Authentication System 1

### Cookie & Session

- 우리가 서버로부터 받은 페이지를 둘러볼 때 우리는 서버와 서로 연결되어 있는 상태가 아니다

- HTTP
  - HTML 문서와 같은 리소스들은 가져올 수 있도록 해주는 규약 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
  - 비연결 지향
    - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 무상태
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
    - 상태가 없다는 것
      - 장바구니에 담은 상품을 유지 불가
      - 로그인 상태 유지 불가
      - 등등..
- 쿠키
  - 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
  - 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식
  - 같은 서버에 다른 페이지로 재요청시마다 받고 저장해 놓았던 쿠키를 함께 전송

- 쿠키 사용 원리
  - 브라우저는 쿠키를 KEY-VALUE의 데이터 형식으로 저장
  - 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
    - 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
      - 이를이용해 사용자의 로그인 상태를 유지할 수 있음
      - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억시켜 주기 때문

- 쿠키 사용 목적
  - 세션 관리
  - 개인화
  - 트래킹

- 세션
  - 서버측에서 생성되어 클라이언트와 서버 간의 상태를 유지 상태정보를 저장하는 데이터 저장 방식

### Authentication System

- Authentication
  - 사용자가 자신이 누구인지 확인하는 것

### Custom User model

- custom user model로 대체하기
  - 장고가 기본적으로 제공하는 user model은 내장된 auth 앱의 user 클래스를 사용

- 기존 user 모델은 직접 수정할 수 가없어 커스텀으로 대체

- 프로젝트 중간에 AUTH_USER_MODEL을 변경 할 수 없음
  - 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행

- 프로젝트를 시작하며 반드시 User 모델을 대체해야한다
  - 충분하더라도 커스텀을 강력히 권장
  - 필요한경우 맞춤으로 설정 가능하기 때문
  - 단 유저 모델 대체는 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 마쳐야 한다.

### Login

- 세션을 create하는 과정

- AuthenticationForm()
  - 로그인 인증에 사용할 데이터를 입력 받는 빌트인 폼

- get_user()
  - AuthenticationForm의 인스턴스 메서드
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

### Logout

- logout(request)
  - 현재 요청에 대한 세션데이타를 DB에서 삭제
  - 클라이언트의 쿠키에서도 세션 id를 삭제

### Template with Authentication data

- 템플릿에서 인증 관련 데이터를 출력하는 방법

- context processors
  - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
  - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
  - 즉, 장고에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것

# 2023 10 05 thursday

## Django Authentication System 2

### 회원가입

- user 객체를 create 하는 과정
- UserCreationForm()
  - 회원가입시 사용자 입력 데이터를 받을 빌트인 모델폼
  - 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스 - 에러남
- get_user_model()
  - 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 함수

### 회원탈퇴

- user 객체를 delete 하는 과정

### 회원정보수정

- user 객체를 update 하는 과정
- UserChangeForm()
  - 회원정보 수정 시 사용자 입력 데이터를 받을 빌트인 모델폼
  - 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야함
  - CustomUserChangeForm에서 접근 가능한 필드를 조정

# 2023 10 10 tuesday

## SQL 1

### Database

- 체계적인 데이터 모음

- 데이터
  - 저장이나 처리에 효율적인 형태로 변환된 정보
  - 전세계 모든 데이터의 약 90%는 2015년 이후에 생성된것

- 데이터를 저장하고 잘 관리하여 활용할 수 있는 기술이 중요해짐

- 기존의 데이터 저장 방식
  - 파일
    - 어디서나 쉽게 사용가능
    - 구조적인 관리의 어려움
  - 스프레드 시트
    - 테이블의 열과 행을 사용해 구조적으로 관리 가능
    - 한계
      - 크기
      - 보안
      - 정확성

### Relational Database

- 데이터 베이스의 역할
  - 데이터를 저장하고 조작
- 관계형 데이터베이스
  - 데이터간에 관계가 있는 데이터 항목들의 모음
  - 테이블, 행, 열의 정보를 구조화하는 방식
  - 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공

- Table (Rekation)
  - 데이터를 기록하는 곳
- Field (Column, Attribute)
  - 각 필드에는 고유한 데이터 타입이 지정됨
- Record (Row, Tuple)
  - 각 레코드에는 구체적인 데이터 값이 지정됨
- Database (Schema)
  - 테이블의 집합
- Primary Key (기본 키)
  - 각 레코드의 고유한 값
- Foreign Key (외래 키)
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는데 사용

### SQL

- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

- SQL 키워드는 대소문자 구분하지 않음 (하지만 대문자 작성 권장)
- 각 SQL Statements의 끝에는 세미콜론이 필요

- DDL
  - 데이터의 기본 구조 및 형식 변경
- DQL
  - 데이터 검색
- DML
  - 데이터 조작
- DCL
  - 데이터 및 작업에 대한 사용자 권한 제어

- Query
  - 데이터베이스로부터 정보를 요청하는 것

- SELECT syntax
  - SELECT select_list FROM table_name;

```sql

-- 01. Querying data
SELECT LastName 
FROM employees;

SELECT LastName, FirstName 
FROM employees;

SELECT * 
FROM employees;

SELECT FirstName AS '이름' 
FROM employees;

SELECT Name, Milliseconds/60000 '재생 시간(분)'
FROM tracks;

-- 02. Sorting data
SELECT FirstName
FROM employees
ORDER BY FirstName ASC;

SELECT FirstName
FROM employees
ORDER BY FirstName DESC;

SELECT Country,City
FROM customers
ORDER By Country DESC, City ASC;

SELECT Name,Milliseconds/6 0000 '재생 시간(분)'
FROM tracks
ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
SELECT ReportsTo 
FROM employees
ORDER BY ReportsTo;

-- 03. Filtering data
SELECT DISTINCT Country
FROM customers
ORDER BY Country;

SELECT LastName, FirstName, City
FROM customers
WHERE City = 'Prague';

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE
 Company IS NULL
 AND Country = 'USA';

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE
 Company IS NULL
 OR Country = 'USA';

SELECT Name,Bytes
FROM tracks
WHERE
 Bytes BETWEEN 100000 AND 500000;

SELECT Name,Bytes
FROM tracks
WHERE
 Bytes BETWEEN 100000 AND 500000
ORDER BY Bytes;

SELECT LastName, FirstName, Country
FROM customers
WHERE
 Country IN 
 ('Canada', 'Germany', 'France');

SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE '%son';

SELECT LastName, FirstName
FROM customers
WHERE FirstName LIKE '___a';

SELECT TrackId, Name,Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 7;

SELECT TrackId, Name,Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 3, 4;


-- 04. Grouping data
SELECT Country, COUNT(*)
FROM customers
GROUP BY Country;

SELECT Composer, AVG(Bytes)
FROM tracks
GROUP BY Composer
ORDER BY AVG(Bytes) DESC;


-- 에러
SELECT Composer,
 AVG(Milliseconds/60000) AS avgOFMinute
FROM tracks
WHERE avgOFMinute < 10
GROUP BY Composer;


-- 에러 해결
SELECT Composer,
 AVG(Milliseconds/60000) AS avgOFMinute
FROM tracks
GROUP BY Composer
HAVING avgOFMinute < 10;
```

### Single Table Queries

# 2023 10 11 wednesday

## Many to one relationships 1

- 한테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- comment-article
  - 0개 이상의 댓글은 1개의 게시글에 작성 될 수 있다.
  - comment(N)-article(1)

- ForeignKey()
  - N:1 관계 설정 모델 필드

- 역참조
  - N:1 관계에서 1 에서 N 을 참조하거나 조회하는 것
  - 예시
    - article.comment_set.all()
- related manager
  - N:1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저
  - objects 매니저를 통해 queryset api를 사용했던것 처럼
  - related 매니저를 통해 queryset api를 사용

### 댓글 create 구현

- forms.py

```python

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

```

- urls.py

```python

path('<int:pk>/comments/', views.comments_create, name='comments_create'),

```

- views.py

```python

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 특정 게시글의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request,pk):
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    # CommentForm으로 사용자로 부터 데이터를 입력 받음
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

```

- detail.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url "articles:update" article.pk %}">UPDATE</a>
  <form action="{% url "articles:delete" article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
  <hr>
  <form action="{% url "articles:comments_create" article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url "articles:index" %}">[back]</a>
</body>
</html>


```

### 댓글 delete 구현

- urls.py

```python

 path('<int:article_pk>/comments/<int:comment_pk>/delete/',
         views.comments_delete,
         name= 'comments_delete'),

```

- views.py

```python

def comments_delete(request, article_pk, comment_pk):
    # 댓글 조회
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

```

- detail.html

```html

 <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST" >
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>

```

# 2023 10 12 thursday

## Data Modeling

- 데이터베이스 시스템을 시각적으로 표현하는 프로세스
- 데이터 유형, 데이터 간의 관계 및 분석 등을 통해 비즈니스 요구사항을 만들어 낼 수 있도록 도움
- ERD
  - 다이어 그램을 사용하여 데이터베이스의 엔터티간 관계를 나타내는 방법
- 데이터 모델링의 중요성
  - 데이터베이스 소프트웨어 개발 오류감소
  - 데이터베이스 설계 및 생성 속도와 효율성 촉진
  - 조직 전체에서 데이터 문서화 및 시스템 설계의 일관성 조성
  - 데이터 엔지니어와 비즈니스 팀 간의 커뮤니케이션 촉진

# 2023 10 13 friday

## 웹 크롤링

- 파이썬으로 웹 페이지에 있는 정보를 가져오는 방법
  - 누군가 업로드해 둔 데이터 다운 받기(ex. 캐글)
  - 누군가 만들어 둔 API Server를 활용하여 정보를 받아오기
  - 사람이 검색하는 것처럼 파이썬이 자동으로 검색 후 결과를 수집하는 방법
    - 크롤링

- 여러 웹 페이지를 돌아다니며 원하는 정보를 모으는 기술

- 원하는 정보를 추출하는 스크래핑과 여러 웹 페이지를 자동으로 탐색하는 크롤링의 개념을 합쳐 웹 크롤링이라고 부름

- 즉, 웹사이트들을 돌아다니며 필요한 데이터를 추출하여 활용할 수 있도록 자동화 된 프로세스

- 웹 크롤링 프로세스
  - 웹 페이지 다운로드
  - 페이지 파싱
  - 링크 추출 및 다른 페이지 탐색
  - 데이터 추출 및 저장

# 2023 10 16 monday

## Many to many relationships 1

- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 N:1 관계를 갖음

### N:1의 한계 상황

- 1번 환자가 두의사에게 모두 진료를 받고자한다면 환자 테이블에 1번환자 데이터가 중복으로 입력됨

### 중계모델 생성

- 예약정보를 담는 모델 생성

- django에서는 ManyToManyField로 중계모델을 자동으로 생성

- 만약 예약 정보에 증상,예약일 등 추가 정보가 포함되어야 한다면

```python

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'

```

- 역참조시 사용하눈 manager name을 변경

```python

class Patient(models.Model):
    # ManyToManyField - related_name 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()


```

# 2023 10 17 tuesday

## Many to many relationships 2

### 팔로우 기능 구현

- models.py

```python

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

```

- urls.py

```python

path('<int:user_pk>/follow/', views.follow, name='follow'),

```

- views.py

```python

def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    
    if me != you:
        # 내가 상대방의 팔로워 목록에 있다면
        if me in you.followers.all():
            # 팔로우 취소
            you.followers.remove(me)
            # me.followings.remove(you)
        else:
            you.followers.add(me)
            # me.followings.add(you)
    return redirect('accounts:profile', you.username)


```

- profile.html

```html

<div>
    <div>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url "accounts:follow" person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <input type="submit" value="Unfollow">
          {% else %}
            <input type="submit" value="Follow">
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>

```

# 2023 10 18 wednesday

## Django REST framwork 1

### REST API

- REST라는 설계 디자인 약속을 지켜 구현한 API

- API
  - 애플리케이션과 프로그래밍으로 소통하는 방법
  - 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

- Web API
  - 웹 서버 또는 웹 브라우저를 위한 API
  - 현대 웹 개발은 하나부터 열까지 직접 개발하기보다 여러 Open API 들을 활용하는 추세
  - 대표적인 Third Party Open API
    - Youtube API
    - Google Map API
    - Naver Papago API
    - Kakao Map API

- REST
  - API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론 "약속(규칙X)"

- RESTful API
  - REST 원리를따르는 시스템을 RESTful 하다고 부름
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

#### RESR에서 자원을 정의하고 주소를 지정하는 방법

- 자원의 식별
  - URL
    - 웹에서 주어진 리소스의 주소
    - 네트워크 상에 리소스가 어디있는지를 알려주기 위한 약속
  - URI
    - 인터넷에서 리소스를 식별하는 문자열
    - 가장 일반적인 URI는 웹 주소로 알려진 URL

- 자원의 행위
  - HTTP Methods
  - HTTP Request Mehods
    - 리소스에 대한 행위를 정의
    - HTTP verbs 라고도 함
    - GET, POST, PUT, DELETE 등등..
- 자원의 표현
  - JSON 데이터
  - 궁극적으로 표현되는 데이터 결과물

### DRF

- Django REST framework
- 장고에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

- Serialization
  - 직렬화
  - 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

### DRF with Single Model

- serializers.py

```python

from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


```

- urls.py

```python

from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]

```

- views.py

```python

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


```

# 2023 10 19 thursdayday

## Django REST framwork 2

### DRF with N:1 Relation

- urls.py

```python

from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]

```

- views

```python

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


```

### 역참조 데이터 구성

- serializers.py

```python

from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

```

### API 문서화

- OpenAPI Specification
  - RESTful API를 설명하고 시각화하는 표준화 방법

# 2023 10 23 monday

## Introductrion of javascript

- 웹의 탄생
- 웹 브라우저의 대중화
- javascript의 탄생
- 파편화

### ECMAScript

- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야하는 규칙, 세부사항 등을 제공
- 자바 스크립트는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
- ECMAScript의 명세를 기반으로 웹 브라우저나 Node.js와 같은 환경에서 실행됨

## JavaScript and DOM

- 웹 브라우저에서의 JavaScript
  - 웹 페이지의 동적인 기능을 구현

### DOM

- 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
- 모두 document 객체의 자식으로 구성됨

- 핵심
  - 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API

```html

<!-- 선택, 출력 -->

<body>
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  <script>
    console.log(document.querySelector('.heading'))
    console.log(document.querySelector('.content'))
    console.log(document.querySelectorAll('.content'))
    console.log(document.querySelectorAll('ul > li'))
  </script>
</body>



<!-- style 적용 -->

<body>
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  <script>
    // 속성 조작
    // 1. 클래스 속성 조작
    const h1Tag = document.querySelector('.heading')
    console.log(h1Tag)

    console.log(h1Tag.classList)
    h1Tag.classList.add('red')
    
    console.log(h1Tag.classList)
    h1Tag.classList.remove('red')

    h1Tag.classList.toggle('red')

    // 2. 일반 속성 조작
    const aTag = document.querySelector('a')
    console.log(aTag)

    aTag.setAttribute('href', 'https://www.naver.com/')
    console.log(aTag.getAttribute('href'))

    aTag.removeAttribute('href')
    console.log(aTag.getAttribute('href'))
  </script>
</body>



<!-- 텍스트 수정 -->

  <script>
    // h1 요소 선택
    const h1Tag = document.querySelector('.heading')
    console.log(h1Tag)
    console.log(h1Tag.textContent)

    // h1 요소의 콘텐츠를 수정
    h1Tag.textContent = '싸피'
    console.log(h1Tag.textContent)
  </script>



<!-- js만으로 구성해보기 -->

<body>
  <div></div>
  <script>
    // 부모 요소 선택
    const divTag = document.querySelector('div')

    // 1.요소 생성
    const h1Tag =  document.createElement('h1')
    console.log(h1Tag)

    // 2. 값 추가(속성, 클래스 속성, 콘텐츠...)
    h1Tag.textContent = '제목입니다'
    console.log(h1Tag)

    // 3. 완성한 요소를 문서에 추가
    divTag.appendChild(h1Tag)

    // 4. 요소 삭제
    divTag.removeChild(h1Tag)
  </script>
</body>



<!-- js로 css구현 -->

<body>
  <p>Lorem, ipsum dolor.</p>
  <script>
    const pTag = document.querySelector('p')
    console.log(pTag)
    console.log(pTag.style)
    pTag.style.color = 'crimson'
    pTag.style.fontSize = '3rem'
    pTag.style.border = '1px solid black'

  </script>
</body>

```

# 2023 10 24 tuesday

## Basic syntax of JavaScript

- ECMAScript 2015 이후의 명제를 따름

### 변수

- 반드시 문자, 달러($), 또는 밑줄(_)로 시작
- 대소문자 구분
- 예약어 사용 불가
  - for, if, function 등
- 카멜 케이스
  - 변수, 객체, 함수에 사용
- 파스칼 케이스
  - 클래스, 생성자에 사용
- 대문자 스네이크 케이스
  - 상수에 사용

- 변수 선언 키워드
  - let
    - 재할당 가능
    - 재선언 불가능
  - const
    - 재할당 불가능
    - 재선언 불가능
  - var

- 블록 스코프
  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

- 기본적으로 const 사용 권장
- 재할당이 필요한 변수는 let으로 변경해서 사용

```html

<body>
  <script>
    // let
    let number = 10
    // 재할당
    number = 20
    console.log(number)
    // 재선언
    let number = 20

    // const
    const number = 10
    number = 20
    console.log(number) // Uncaught TypeError: Assignment to constant variable.

    const number = 20 // Uncaught SyntaxError: Identifier 'number' has already been declared


    // 블록 스코프
    let x = 1
    if (x === 1) {
      let x = 2
      console.log(x) // 2
    }
    console.log(x) // 1

    // 템플릿 리터럴
    const age = 100
    const message = `홍길동은 ${age}세입니다.`
    console.log(message)

  </script>
</body>

```

### 데이터 타입

- 원시 자료형
  - 변수에 값이 직접 저장 되는 자료형
  - (불변, 값이 복사)
- 참조 자료형
  - 객체의 주소가 저장 되는 자료형
  - (가변, 주소가 복사)

### 연산자

```html

<body>
  <script>
    // 전위 연산자
    // 피연산자에 1을 더한 값을 반환
    // a에 4를 할당한 후 4를 반환
    let a = 3
    const b = ++a
    console.log(a, b) // 4 4

    // 후위 연산자
    // 피연산자에 1을 더하기 전의 값을 반환
    // 3을 먼저 반환한 후 x에 4를 할당
    let x = 3
    const y = x++
    console.log(x, y) // 4 3

  </script>
</body>

```

### 조건문

```html

<body>
  <script>
    const name = 'customer'

    if (name === 'admin') {
      console.log('관리자님 환영해요')
    } else if (name === 'customer') {
      console.log('고객님 환영해요')
    } else {
      console.log(`반갑습니다. ${name}님`)
    }
  </script>
</body>

```

### 반복문

```html

<body>
  <script>
    // while
    let i = 0

    while (i < 6) {
      console.log(i)
      i += 1
    }


    // for
    for (let i = 0; i < 6; i++) {
      console.log(i)
    }


    // for...in
    const object = {
      a: 'apple',
      b: 'banana'
    }

    for (const property in object) {
      console.log(property)
      console.log(object[property])
    }


    // for...of
    const numbers = [0, 1, 2, 3]

    for (const number of numbers) {
      console.log(number) // 0, 1, 2, 3
    }

    const myStr = 'apple'

    for (const str of myStr) {
      console.log(str) // a, p, p, l, e
    }


    // for...in 과 for...of 의 차이
    const arr = ['a', 'b', 'c']

    for (const i in arr) {
      console.log(i) // 0, 1, 2
    }

    for (const i of arr) {
      console.log(i) // a, b, c
    }

  </script>
</body>


<body>
  <script>
    // for...in

    // Array
    const arr = ['a', 'b', 'c']
    for (const elem in arr) {
      console.log(elem) // 0 1 2
    }

    // Object
    const capitals = {
      korea: '서울',
      japan: '도쿄',
      china: '베이징',
    }
    for (const capital in capitals) {
      console.log(capital) // korea japan china
    }

    // for...of

    // Array
    const arr = ['a', 'b', 'c']
    for (const elem of arr) {
      console.log(elem) // a b c
    }

    // Object
    const capitals = {
      korea: '서울',
      japan: '도쿄',
      china: '베이징',
    }
    for (const capital of capitals) {
      console.log(capital) // TypeError: capitals is not iterable
    }
  </script>
</body>
```

# 2023 10 25 wednesday

## JavaScript Reference data types

### 함수 

- 참조 자료형에 속하며 모든 함수는 Function object

```html

<script>
// 함수 선언식
function add(num1, num2) {
  return num1 + num2
}

console.log(add(3, 9))

// 함수 표현식
const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(3, 9))

```

- 매개변수

```html

<script>
// 기본 함수 매개변수
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

console.log(greeting())


// 나머지 매개변수 (가변 인자)
const myFunc = function (num1, num2, ...restArgs) {
  return [num1, num2, restArgs]
}

console.log(myFunc(1, 2, 3, 4, 5))
console.log(myFunc(1, 2))


// 매개변수와 인자의 개수 불일치 허용
// 매개변수 개수 > 인자 개수
const threeArgs = function (num1, num2, num3) {
  return [num1, num2, num3]
}

console.log(threeArgs()) // [undefined,undefined,undefined]
console.log(threeArgs(1)) // [1,undefined,undefined]
console.log(threeArgs(2, 3))


// 매개변수 개수 < 인자 개수
const noArgs = function () {
  return 0
}

console.log(noArgs(1, 2, 3))  // 0

const twoArgs = function (num1, num2) {
  return [num1, num2]
}

console.log(twoArgs(1, 2, 3)) // [1, 2]

```

- 전개 구문 = ...
  - 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것 (확장, 전개)
  - 함수와의 사용

```html

  <script>
    // 1. 함수 호출 시 인자 확장
    function myFunc(x, y, z) {
      return x + y + z
    }

    let numbers = [1, 2, 3]

    console.log(myFunc(...numbers)) // 6


    // 2. 나머지 매개변수
    function myFunc2(x, y, ...restArgs) {
      return [x, y, restArgs]
    }

    console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
    console.log(myFunc2(1, 2)) // [1, 2, []]
  </script>

```

- 화살표 함수 표현식
  - 함수 표현식의 간결한 표현법

```html

<script>
    const arrow1 = function (name) {
      return `hello, ${name}`
    }

    // 1. function 키워드 삭제 후 화살표 작성
    const arrow2 = (name) => { return `hello, ${name}` }

    // 2. 인자가 1개일 경우에만 () 생략 가능
    const arrow3 = name => { return `hello, ${name}` }

    // 3. 함수 본문이 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
    const arrow4 = name => `hello, ${name}`
  </script>

```

### 객체

- object
  - 키로 구분된 데이터 집합을 저장하는 자료형

- 구조
  - 중괄호를 이용해 작성
  - 중괄호 안에는 key:value 쌍으로 구성된 속성을 여러개 작성가능
  - 대괄호로 객체 요소 접근 가능 

```html

<script>
    const user = {
      name: 'Alice',
      'key with space': true,
      greeting: function () {
        return 'hello'
      }
    }

    // 조회
    console.log(user.name) // Alice
    console.log(user['key with space']) // true

    // 추가
    user.address = 'korea'
    console.log(user) // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}

    // 수정
    user.name = 'Bella'
    console.log(user.name) // Bella

    // 삭제
    delete user.name
    console.log(user) // {key with space: true, address: 'korea', greeting: ƒ}

    // in 연산자
    console.log('greeting' in user) // true
    console.log('country' in user) // false

    // 메서드 호출
    console.log(user.greeting()) // hello
  </script>

```

- this 
  - 함수나 메서드를 호출한 객체를 가리키는 키워드
  - 호출하는 방법에 따라 가리키는 대상이 다름
  - 단순 호출 - 전역 객체
  - 메서드 호출 - 메서드를 호출한 객체
  - 함수 호출시에 값이 결정 ( 동적 할당 )

```html

<script>
    // 1.1 단순 호출
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // window

    // 1.2 메서드 호출
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }
    console.log(myObj.myFunc()) // myObj

    // 2. Nested
    // 2.1 일반 함수
    const myObj2 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.numbers.forEach(function (number) {
          console.log(this) // window
        })
      }
    }
    console.log(myObj2.myFunc())

    // 2.2 화살표 함수
    const myObj3 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.numbers.forEach((number) => {
          console.log(this) // myObj3
        })
      }
    }
    console.log(myObj3.myFunc())

  </script>

```

- 추가 객체 문법

```html

<script>
    // 단축 속성
    const name = 'Alice'
    const age = 30

    const user = {
      name: name,
      age: age,
    }

    // 단축 메서드
    const myObj1 = {
      myFunc: function () {
        return 'Hello'
      }
    }

    const myObj2 = {
      myFunc() {
        return 'Hello'
      }
    }

    // 계산된 프로퍼티
    const product = prompt('물건 이름을 입력해주세요')
    const prefix = 'my'
    const suffix = 'property'

    const bag = {
      [product]: 5,
      [prefix + suffix]: 'value',
    }

    console.log(bag) // {연필: 5, myproperty: 'value'}


    // 구조 분해 할당
    const userInfo = {
      firstName: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    // const firstName = userInfo.name
    // const userId = userInfo.userId
    // const email = userInfo.email

    // const { firstName } = userInfo
    // const { firstName, userId } = userInfo
    const { firstName, userId, email } = userInfo

    // Alice alice123 alice123@gmail.com
    console.log(firstName, userId, email)

    // 구조 분해 할당 활용 - 함수 매개변수
    function printInfo({ name, age, city }) {
      console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
    }

    const person = {
      name: 'Bob',
      age: 35,
      city: 'London',
    }

    // 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
    printInfo(person) // '이름: Bob, 나이: 35, 도시: London'

    // with 전개 구문
    const obj = { b: 2, c: 3, d: 4 }
    const newObj = { a: 1, ...obj, e: 5 }
    console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}

    // 유용한 객체 메서드
    const profile = {
      name: 'Alice',
      age: 30,
    }

    console.log(Object.keys(profile)) // ['name', 'age']
    console.log(Object.values(profile)) // ['Alice', 30]

  </script>

```

- optional chaining 
  - 존재하지 않아도 괜찮은 대상(ex. 중첩객체)에만 사용해야 함
  - 왼쪽 평가 대상이 없어도 괜찮은 경우에만 선택적으로 사용
  - 앞에 변수는 반드시 선언되어 있어야 함
  - obj?.prop
    - obj가 존재하면 obj.prop을 반환 else undefined반환
  - obj?.[prop]
    - obj가 존재하면 obj[prop]을 반환 else undefined반환
  - obj?.method()
    - obj가 존재하면 obj.method()를 호출 else undefined반환

```html

<script>
    const user = {
      name: 'Alice',
      greeting: function () {
        return 'hello'
      }
    }

    console.log(user.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
    console.log(user.address?.street) // undefined

    console.log(user.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
    console.log(user.nonMethod?.()) // undefined

    console.log(user.address && user.address.street) // undefined

    console.log(myObj?.address) // Uncaught ReferenceError: myObj is not defined

    // 위 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
    // user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문

    // Bad
    user?.address?.street

    // Good
    user.address?.street
  </script>

```
  
- JSON

```html

<script>
    const jsObject = {
      coffee: 'Americano',
      iceCream: 'Cookie and cream',
    }

    // Object -> JSON
    const objToJson = JSON.stringify(jsObject)
    console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
    console.log(typeof objToJson)  // string

    // JSON -> Object
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
    console.log(typeof jsonToObj)  // object

  </script>

```

- new 연산자 

```html

<script>
    function Member(name, age, sId) {
      this.name = name
      this.age = age
      this.sId = sId
    }

    const member3 = new Member('Bella', 21, 20226543)

    console.log(member3) // Member { name: 'Bella', age: 21, sId: 20226543 }
    console.log(member3.name) // Bella
  </script>

```

### 배열

- object
  - 키로 구분된 데이터 집합을 저장하는 자료형 
  - -> 이제는 순서가 있는 collection이 필요

- Array
  - 순서가 있는 데이터 집합을 저장하는 자료구조
  - 대괄호 이용
  - length 속성으로 길이 알수있음

```html

<script>
    const names = ['Alice', 'Bella', 'Cathy',]

    console.log(names[0]) // Alice
    console.log(names[1]) // Bella
    console.log(names[2]) // Cathy

    console.log(names.length) // 3

    // 수정
    names[1] = 'Dan'
    console.log(names)
  </script>

<script>
    const names = ['Alice', 'Bella', 'Cathy',]

    // pop
    console.log(names.pop()) // Cathy
    console.log(names) // ['Alice', 'Bella']

    // push
    names.push('Dan')
    console.log(names) // ['Alice', 'Bella', 'Dan']

    // shift
    console.log(names.shift()) // Alice
    console.log(names) // ['Bella', 'Dan']

    // unshift
    names.unshift('Eric')
    console.log(names) // ['Eric', 'Bella', 'Dan']

  </script>
```


- Array Helper Methods
  - 배열을 순회하며 특정 로직을 수행하는 메서드
  - 메서드 호출시 인자로 함수를 받는 것이 특징
  - forEach()
    - 인자로 주어진 함수를 배열 요소 각각에 대해 실행

  ```html
  
  <script>
    const names = ['Alice', 'Bella', 'Cathy',]

    // 일반 함수
    names.forEach(function (item, index, array) {
      console.log(`${item} / ${index} / ${array}`)
    })

    // 화살표 함수
    names.forEach((item, index, array) => {
      console.log(`${item} / ${index} / ${array}`)
    })
  </script>
  
  <script>
    const names = ['Alice', 'Bella', 'Cathy',]

    // for loop
    for (let idx = 0; idx < names.length; idx++) {
      console.log(idx, names[idx])
    }

    // for...of
    for (const name of names) {
      console.log(name)
    }

    // forEach 권장
    names.forEach((name, idx) => {
      console.log(idx, name)
    })
  </script>
  ```

  - map
    - 베열 내의 모든 요소 각각에 대해 함수를 호출하고, 호출 결과를 모아 새로운 배열을 반환

  ```html
  
  <script>
    // 1
    const names = ['Alice', 'Bella', 'Cathy',]

    const result1 = names.map(function (name) {
      return name.length
    })

    const result2 = names.map((name) => {
      return name.length
    })

    console.log(result1) // [5, 5, 5]
    console.log(result2) // [5, 5, 5]


    // 2
    const numbers = [1, 2, 3,]

    const doubleNumber = numbers.map((number) => {
      return number * 2
    })

    console.log(doubleNumber) // [2, 4, 6]
  </script>
  
  ```

- 콜백함수
  - 다른 함수에 인자로 전달되는 함수

  ```html
  
  <script>
    // 1
    const numbers1 = [1, 2, 3,]
    numbers.forEach(function (num) {
      console.log(num ** 2)
    })

    // 2
    const numbers2 = [1, 2, 3,]
    const callBackFunction = function (num) {
      console.log(num ** 2)
    }

    numbers.forEach(callBackFunction)

  </script>
  
  ```


# 2023 10 26 thursday

## Controlling event 

### event

- 컴퓨터를 눌러 텍스트를 입력하는 것
- 전화벨이 울려 전화가 왔음을 알리는 것
- 손을 흔들어 인사하는 것
- 전화기의 버튼을 눌러서 통화를 시작하는 것

- 웹에서의 이벤트
  - 버튼을 클릭했을 때 팝업 창이 출력되는것
  - 마우스 커서의 위치에 따라 드래그 앤 드롭하는것
  - 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
  - 일상에서의 이벤트처럼 웹에서도 이벤트를 통해 특정 동작을 수행한다

- 모든 DOM요소는 이런 이벤트 만들어냄 

- event object
  - DOM에서 이벤트가 발생했을 때 생성되는 객체 
  - 이벤트의 종류
    - mouse, input, keyboard, touch ...ect

- DOM 요소는 이벤트를 받고 받은 이벤트를 처리할수있다

```html

<body>
  <button id="btn">버튼</button>

  <script>
    // 1. 버튼 선택
    const btn = document.querySelector('#btn')

    // 2. 콜백함수 작성
    const clickCallbackFunc = function (event) {
      console.log(event)
      console.log(event.target)
      console.log(event.currentTarget)
      console.log(this)
    }

    // 3. 버튼에 이벤트 핸들러를 부착
    btn.addEventListener('click', clickCallbackFunc)
  </script>
</body>

```

### event handler 활용

- event handler 
  - 이벤트가 발생했을 때 실행되는 함수 
  - 사용자의 행동에 어떻게 반응할지를 자바스크립트 코드로 표현한 것

- 버블링
  - 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모요소의 핸들러가 동작하는 현상
  - 가장 최상단의 조상 요소를 만날 때까지 이 과정이 반복되면서 요소각각에 할당된 핸들러가 동장
  - 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물속 거품과 닮았기 때문

```html

<body>
  <form id="form">
    form
    <div id="div">
      div
      <p id="p">p</p>
    </div>
  </form>

  <script>
    const formElement = document.querySelector('#form')
    const divElement = document.querySelector('#div')
    const pElement = document.querySelector('#p')

    const clickHandler1 = function (event) {
      console.log('form이 클릭되었습니다.')
    }
    const clickHandler2 = function (event) {
      console.log('div가 클릭되었습니다.')
    }
    const clickHandler3 = function (event) {
      console.log('p가 클릭되었습니다.')
    }

    formElement.addEventListener('click', clickHandler1)
    divElement.addEventListener('click', clickHandler2)
    pElement.addEventListener('click', clickHandler3)
  </script>
</body>

<body>
  <div id="outerouter">
    outerouter
    <div id="outer">
      outer
      <div id="inner">inner</div>
    </div>
  </div>

  <script>
    const outerOuterElement = document.querySelector('#outerouter')

    const clickHandler = function (event) {
      console.log('currentTarget:', event.currentTarget.id)
      console.log('target:', event.target.id)
    }

    outerOuterElement.addEventListener('click', clickHandler)
  </script>
</body>

```

- click event

```html

<body>
  <button id="btn">버튼</button>
  <p>클릭횟수 : <span id="counter">0</span></p>

  <script>
    // 1. 초기값 할당
    let counterNumber = 0

    // 2. 버튼 요소 선택
    const btn = document.querySelector('#btn')

    // 3. 콜백 함수 (버튼에 클릭 이벤트가 발생할때마다 실행할 코드)
    const clickHandler = function () {
      // 3.1 초기값 += 1
      counterNumber += 1

      // 3.2 span 요소를 선택
      const spanTag = document.querySelector('#counter')

      // 3.3 span 요소의 컨텐츠를 1 증가한 초기값으로 설정
      spanTag.textContent = counterNumber
    }

    // 4. 버튼에 이벤트 핸들러 부착 (클릭 이벤트)
    btn.addEventListener('click', clickHandler)
  </script>
</body>

```

- input evet

```html

<body>
  <input type="text" id="text-input">
  <p></p>

  <script>
    // 1. input 요소 선택
    const inputTag = document.querySelector('#text-input')

    // 2. p 요소 선택
    const pTag = document.querySelector('p')

    // 3. 콜백 함수 (input 요소에 input 이벤트가 발생할때마다 실행할 코드)
    // 3.1 작성하는 데이터가 어디에 누적되고 있는지 찾기
    const inputHandler = function (event) {
      // console.log(event)
      // console.log(event.currentTarget)
      console.log(event.currentTarget.value)
      console.log(this.value)
      
      // 3.2 p요소의 컨텐츠에 작성하는 데이터를 추가
      pTag.textContent = event.currentTarget.value
    }

    // 4. input 요소에 이벤트 핸들러 부착 (input 이벤트)
    inputTag.addEventListener('input', inputHandler)
  </script>
</body>

```

- click input event

```html

<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">

  <script>
    // input 구현
    const inputTag = document.querySelector('#text-input')
    const h1Tag = document.querySelector('h1')

    const inputHandler = function (event) {
      h1Tag.textContent = event.currentTarget.value
    }

    inputTag.addEventListener('input', inputHandler)

    // click 구현
    const btn = document.querySelector('#btn')
    
    const clickHandler = function (event) {
      // console.log(event)
      // h1Tag.classList.add('blue')

      // toggle
      h1Tag.classList.toggle('blue')
    }

    btn.addEventListener('click', clickHandler)

  </script>
</body>

```

- todo 

```html

<body>
  <input type="text" class="input-text">
  <button id="btn">+</button>
  <ul></ul>

  <script>
    // 1. 필요한 요소 선택
    const inputTag = document.querySelector('.input-text')
    const btn = document.querySelector('#btn')
    const ulTag = document.querySelector('ul')


    const addTodo = function (event) {
      // 2.1 사용자 입력 데이터 저장
      const inputData = inputTag.value

      // 3. 사용자 입력데이터가 빈 데이터인지 확인
      if (inputData.trim()) {
        // 2.2 데이터를 저장할 li 요소를 생성
        const liTag = document.createElement('li')
        // console.log(liTag)
  
        // 2.3 li 요소 컨텐츠에 데이터 입력
        liTag.textContent = inputData
        // console.log(liTag)
  
        // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
        ulTag.appendChild(liTag)
        
        // 2.5 todo 추가 후 input의 입력 데이터는 초기화
        inputTag.value = ''
      } else {
        alert('투두를 입력하세요!!!')
      }
    }

    // 2. 버튼에 이벤트 핸들러를 부착
    btn.addEventListener('click', addTodo)


  </script>
</body>

```

- lottery

```html

<body>
  <h1>로또 추천 번호</h1>
  <button id="btn">행운 번호 받기</button>
  <div></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    // 1. 필요한 요소 선택
    const btn = document.querySelector('#btn')
    const divTag = document.querySelector('div')

    // 2. 로또 번호를 생성 + 태그를 만들고 출력까지하는 (콜백함수)
    const getLottery = function (event) {
      // 2.1 1부터 45까지의 값이 필요
      const numbers = _.range(1, 46)
      // console.log(numbers)

      // 2.2 45개의 요소가 있는 배열에서 6개 번호 추출
      const sixNumbers = _.sampleSize(numbers, 6)
      console.log(sixNumbers)

      // 2.5 6개의 li 요소를 담을 ul 요소 생성
      const ulTag = document.createElement('ul')

      // 2.3 추출한 번호 배열을 "반복"하면서 li 요소를 생성
      sixNumbers.forEach(function (number) {
        // 2.4 번호를 담을 li 요소 생성 후 입력
        const liTag = document.createElement('li')
        liTag.textContent = number
        // console.log(liTag)
        // 2.6 만들어진 li를 ul 요소에 추가
        ulTag.appendChild(liTag)
        console.log(ulTag)
      })
      // 2.7 완성한 ul 요소를 div 요소에 추가
      divTag.appendChild(ulTag)
    }

    // 3. 버튼 요소에 이벤트 핸들러를 부착
    btn.addEventListener('click', getLottery)
  </script>
</body>

```

- prevent event

```html

<body>
  <h1>중요한 내용</h1>

  <form id="my-form">
    <input type="text" name="username">
    <button type="submit">Submit</button>
  </form>

  <script>
    // 1
    const h1Tag = document.querySelector('h1')

    h1Tag.addEventListener('copy', function (event) {
      console.log(event)
      event.preventDefault()
      alert('복사 할 수 없습니다.')
    })

    // 2
    const formTag = document.querySelector('#my-form')

    const handleSubmit = function (event) {
      event.preventDefault()
    }

    formTag.addEventListener('submit', handleSubmit)

  </script>
</body>

```

# 2023 10 30 monday

## Asynchronous JavaScript

### 비동기

- Synchronous (동기)
  - 프로그램의 실행 흐름이 순차적으로 진행
  - 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식
  - 주문 후 커피가 나올 때 까지 기다려야함
  - 메인 작업이 모두 수행되어야 마지막 작업이 수행됨
  - 함수의 작업이 완료될 때까지 기다렸다가 값을 반환해야 계속 진행할 수 있음(동기 함수)

- Asynchronous (비동기)
  - 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기자리지 않고 다음 작업이 실행되는 방식
  - 작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행할 수 있음
  - 주문 후 진동 벨이 울리면 커피를 가져옴
  - 병렬적 수행
  - 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리


### JavaScript와 비동기

- Single Thread 언어, JavaScript
  - Thread : 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
  - JavaScript는 한번에 여러 일을 수행할 수 없다.
  - 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음

- java script Runtime
  - 자바스크립트가 동작할 수 있는 환경
  - 자바스크립트가 비동기 처리를 할 수 있도록 도와주는 환경이 필요
  - 브라우저, Node 같은 환경에서 처리
  - 브라우저에서 자바스크립트 비동기 처리 관련 요소
    - javascript engine의 call stack
    - Web API
    - Task Queue
    - Event Loop
  - 비동기 처리 동작 방식 
    - 모든 작업은 call stack(LIFO)로 들어간 후 처리 됨
    - 오래걸리는 작업은 Web API로 보내 별도로 처리
    - Web API에서 처리가 끝난 작업들은 바로 call stack으로 가지않고 task queue(FIFO)에 순서대로 들어감
    - Event Loop가 Call Stack이 비어있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 먼저 처리되어 들어온) 작업을 Call Stack으로 보낸다

### AJAX

- 자바스크립트의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술

- XMLHttpRequest 객체
  - 서버와 상호작용할 때 사용하며 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음

- Axios
  - 자바스크립트에서 사용되는 HTTP 클라이언트 라이브러리

### Callback과 Promise

# 2023 10 31 tuesday

## Ajax with Django

- Ajax
  - 자바스크립트의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술

### Ajax와 서버

- 이벤트 발생 -> XHR 객체 생성 및 요청 -> Ajax 요청 처리 -> 응답 데이터 생성 -> JSON 데이터 응답 -> 응답 데이터를 활용해 DOM 조작

### Ajax with follow

- views.py

```python

@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user

    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context = {
            'is_followed': is_followed,
            'followings_count': you.followings.count(),
            'followers_count': you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)

```

- profile.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>{{ person.username }}님의 프로필</h1>

  <div>
    <div>
      팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span> / 
      팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
    </div>
    {% if request.user != person and request.user.is_authenticated %}
      <div>
        <form id="follow-form" data-user-id="{{ person.pk }}">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <input type="submit" value="Unfollow">
          {% else %}
            <input type="submit" value="Follow">
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>

  <hr>

  <h2>작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <p>{{ article.title }}</p>
  {% endfor %}

  <hr>

  <h2>작성한 댓글</h2>
  {% for comment in person.comment_set.all %}
    <p>{{ comment.content }}</p>
  {% endfor %}

  <hr>

  <h2>좋아요를 누른 게시글</h2>
  {% for article in person.like_articles.all %}
    <p>{{ article.title }}</p>
  {% endfor %}

  <hr>

  <a href="{% url "articles:index" %}">[back]</a>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1. form 요소 선택
    const formTag = document.querySelector('#follow-form')
    // 6. csrftoken value 값 선택
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    
    // 2. form 요소에 이벤트 리스터 부착
    formTag.addEventListener('submit', function (event) {
      // 3. submit 이벤트 기본 동작 취소
      event.preventDefault()
      // 5. form 요소에 지정한 data 속성 접근하기
      const userId = formTag.dataset.userId

      // 4. axios로 비동기적으로 팔로우/언팔로우를 요청
      axios({
        url: `/accounts/${userId}/follow/`,
        method: 'post',
        headers: {'X-CSRFToken': csrftoken},
      })
        .then((response) => {
          console.log(response.data)
          // 7. Django에서 보낸 follow 여부를 알 수 있는 변수를 저장
          const isFollowed = response.data.is_followed
          // 8. 팔로우 버튼 선택
          const followBtn = document.querySelector('#follow-form > input[type=submit]:nth-child(2)')
          // 9. 팔로우 버튼 토글
          if (isFollowed === true) {
            followBtn.value = 'Unfollow'
          } else {
            followBtn.value = 'Follow'
          }

          // 10. 팔로워 / 팔로잉 수 조작
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCountTag = document.querySelector('#followers-count')
          
          followingsCountTag.textContent = response.data.followings_count
          followersCountTag.textContent = response.data.followers_count
        })
        .catch((error) => {
          console.log(error)
        })
    })
  </script>
</body>
</html>

```

### Ajax with likes

- views.py

```python

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)

```

- index.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>INDEX</h1>
  {% if request.user.is_authenticated %}
    <h3>{{ user.username }}님 안녕하세요!</h3>
    <a href="{% url "accounts:profile" user.username %}">내 프로필</a>
    <form action="{% url "accounts:logout" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="LOGOUT">
    </form>
    <form action="{% url "accounts:delete" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <a href="{% url "accounts:update" %}">회원정보수정</a>
  {% else %}
    <a href="{% url "accounts:login" %}">LOGIN</a>
    <a href="{% url "accounts:signup" %}">SIGNUP</a>
  {% endif %}

  <hr>
  
  <a href="{% url 'articles:create' %}">CREATE</a>
  <hr>
  {% for article in articles %}
    <p>
      작성자 : 
      <a href="{% url "accounts:profile" article.user.username %}">{{ article.user }}</a>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      <p>글 제목 : {{ article.title }}</p>
    </a>
    <p>글 내용 : {{ article.content }}</p>
    <form class="likes-forms" data-article-id="{{ article.pk }}">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
      {% else %}
        <input type="submit" value="좋아요" id="like-{{ article.pk }}">
      {% endif %}
    </form>
    <hr>
  {% endfor %}

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const formTags = document.querySelectorAll('.likes-forms')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    formTags.forEach((formTag) => {
      formTag.addEventListener('submit', function (event) {
        event.preventDefault()

        const articleId = formTag.dataset.articleId

        axios({
          url: `/articles/${articleId}/likes/`,
          method: 'post',
          headers: {'X-CSRFToken': csrftoken},
        })
          .then((response) => {
            // console.log(response.data.is_liked)
            const isLiked = response.data.is_liked
            const likeBtn = document.querySelector(`#like-${articleId}`)

            if (isLiked === true) {
              likeBtn.value = '좋아요 취소'
            } else {
              likeBtn.value = '좋아요'
            }
          })
          .catch((error) => {
            console.log(error)
          })
      })
    })
  </script>
</body>
</html>


```

# 2023 11 01 tuesday

## Introduction of Vue

### Front-end Development

- 웹사이트와 웹 애플리케이션의 사용자 인터페이스와 사용자 경험을 만들고 디자인하는 것
- HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발

- Client-side frameworks
  - 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임워크
  - 필요한 이유
    - 웹에서 하는 일이 많아짐 -> 다루는 데이터가 많아짐
    - 단순히 무언가를 읽는 곳 -> 무언가를 하는 곳
    - 동적인 대화형 애플리케이션을 더 쉽게 구축가능
    - 애플리케이션의 기본 데이터를 안정적으로 추적, 업데이트하는 도구가 필요
    - 애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 업데이트해야 한다는 것

- SPA 
  - 페이지 한 개로 구성된 웹 애플리케이션

- client-side Rendering 장점
  - 빠른 속도
  - 사용자 경험
  - 프론트와 백의 명확한 분리

- client-side Rendering 단점
  - 초기 구동속도가 느림
  - SEO(검색 엔진 최적화) 문제

### Vue

- Vue 학습 이유
  - 쉬운 학습 곡선, 간편한 문법
  - 반응성 시스템
  - 모듈화, 유연한 구조
  - 거대하고 활발한 커뮤니티 -> 풍부한 문서, 튜토리얼

```html

<body>
  <div id="app">
    <h1>{{ greeting }}</h1>
    <button @click="count++">{{ count }}</button>
    <p>{{ count }}</p>
    <h3>{{ count }}</h3>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const greeting = ref('Hello')
        return {
          count,
          greeting
        }
      }
    })

    app.mount('#app')
  </script>
</body>

<body>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const message = ref('hello vue!')
        console.log(message)
        console.log(message.value)
        return {
          message
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

- event listener

```html

<body>
  <div id="app">
    <button v-on:click="increment">{{ count }}</button>
    <button @click="increment">{{ count }}</button>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const increment = function () {
          count.value++
        }
        return {
          count,
          increment
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

- ref vs variable

```html

<body>
  <div id="app">
    <p>반응성 변수: {{ reactiveValue }}</p>
    <p>일반 변수: {{ normalValue }}</p>
    <button @click="increment">값 업데이트</button>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const reactiveValue = ref(0)
        let normalValue = 0
        const increment = function () {
          reactiveValue.value++
          normalValue++
          console.log(normalValue)
        }
        return {
          reactiveValue,
          normalValue,
          increment
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

# 2023 11 02 thursday

## Basic Syntax

### Template Syntax

- DOM을 기본구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용

- 종류
  - Text Interpolation
    - 데이터 바인딩의 가장 기본적인 형태
  - Raw HTML
  - Attribute Bindings
  - JavaScript Expressions

```html

<body>
  <div id="app">
    <!-- Inline Handlers -->
    <button v-on:click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @click="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <button @click="greeting('hello')">Say hello</button>
    <button @click="greeting('bye')">Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <button @click="warning('경고입니다.', $event)">Submit</button>

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">
      <input type="submit">
    </form>
    <a @click.stop.prevent="onLink">Link</a>

    <!-- key modifiers -->
    <input type="text" @keyup.enter="onSubmit">
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const name = ref('Alice')
        const myFunc = function (event) {
          console.log(event)
          console.log(event.currentTarget)
          console.log(`hello, ${name.value}`)
        }
        const greeting = function (message) {
          console.log(message)
        }
        const warning = function (message, event) {
          console.log(message)
          console.log(event)
        }
        const onSubmit = function (event) {
          console.log(event)
        }
        return {
          count,
          name,
          myFunc,
          greeting,
          warning,
          onSubmit
        }
      }
    })

    app.mount('#app')
  </script>
</body>


<body>
  <div id="app">
    <img v-bind:src="imageSrc" alt="#">
    <a v-bind:href="myUrl">Link</a>

    <img :src="imageSrc" alt="#">
    <a :href="myUrl">Link</a>

    <p :[dynamicattr]="dynamicValue">.....</p>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const imageSrc = ref('https://picsum.photos/200/')
        const myUrl = ref('https://www.google.co.kr/')
        const dynamicattr = ref('title')
        const dynamicValue = ref('Hello')
        return {
          imageSrc,
          myUrl,
          dynamicattr,
          dynamicValue
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

### Dynamically data binding

- html-classes

```html

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .active {
      color: crimson;
    }

    .text-primary {
      color: blue;
    }
  </style>
</head>

<body>
  <div id="app">
    <!-- Binding to Objects -->
    <div :class="{ active: isActive }">Text</div>
    <div class="static" :class="{ active: isActive, 'text-primary': hasInfo }">Text</div>
    <div class="static" :class="classObj">Text</div>

    <!-- Binding to Arrays -->
    <div :class="[activeClass, infoClass]">Text</div>
    <div :class="[{ active: isActive }, infoClass]">Text</div>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const isActive = ref(true)
        const hasInfo = ref(true)
        const classObj = ref({
          active: isActive, 
          'text-primary': hasInfo
        })
        const activeClass = ref('active')
        const infoClass = ref('text-primary')
        return {
          isActive,
          hasInfo,
          classObj,
          activeClass,
          infoClass
        }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>

```

- inline-styles


```html

<body>
  <div id="app">
    <!-- Binding to Objects -->
    <div :style="{ color: activeColor, fontSize: fontSize + 'px'}">Text</div>
    <div :style="{ 'font-size': fontSize + 'px'}">Text</div>
    <div :style="styleObj">Text</div>

    <!-- Binding to Arrays -->
    <div :style="[styleObj, styleObj2]">Text</div>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const activeColor = ref('crimson')
        const fontSize = ref(50)
        const styleObj = ref({
          color: activeColor, 
          fontSize: fontSize.value + 'px'
        })
        const styleObj2 = ref({
          color: 'blue',
          border: '1px solid black'
        })
        return {
          activeColor,
          fontSize,
          styleObj,
          styleObj2
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

### Event Handling

```html

<body>
  <div id="app">
    <!-- Inline Handlers -->
    <button v-on:click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @click="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <button @click="greeting('hello')">Say hello</button>
    <button @click="greeting('bye')">Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <button @click="warning('경고입니다.', $event)">Submit</button>

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">
      <input type="submit">
    </form>
    <a @click.stop.prevent="onLink">Link</a>

    <!-- key modifiers -->
    <input type="text" @keyup.enter="onSubmit">
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const name = ref('Alice')
        const myFunc = function (event) {
          console.log(event)
          console.log(event.currentTarget)
          console.log(`hello, ${name.value}`)
        }
        const greeting = function (message) {
          console.log(message)
        }
        const warning = function (message, event) {
          console.log(message)
          console.log(event)
        }
        const onSubmit = function (event) {
          console.log(event)
        }
        return {
          count,
          name,
          myFunc,
          greeting,
          warning,
          onSubmit
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

### Form Input Bindings

```html

<body>
  <div id="app">
    <p>{{ inputText1 }}</p>
    <input type="text" @input="onInput" :value="inputText1">

    <p>{{ inputText2 }}</p>
    <input type="text" v-model="inputText2">
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const inputText1 = ref('')
        const inputText2 = ref('')
        const onInput = function (event) {
          inputText1.value = event.currentTarget.value
        }
        return {
          inputText1,
          onInput,
          inputText2
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

- v-model

```html

<body>
  <div id="app">
    <!-- single checkbox -->
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">{{ checked }}</label>

    <!-- multiple checkbox -->
    <div>Checked names: {{ checkedNames }}</div>

    <input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
    <label for="alice">Alice</label>

    <input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
    <label for="bella">Bella</label>

    <!-- single select -->
    <div>Selected: {{ selected }}</div>

    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>Alice</option>
      <option>Bella</option>
      <option>Cathy</option>
    </select>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const checked = ref(false)
        const checkedNames = ref([])
        const selected = ref('')
        return {
          checked,
          checkedNames,
          selected
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

# 2023 11 06 monday

## Basic Syntax 2

### Computed Property

```html

<body>
  <div id="app">
    <h2>남은 할 일</h2>
    <p>{{ restOfTodos }}</p>
    <p>{{ getRestOfTodos() }}</p>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref, computed } = Vue

    const app = createApp({
      setup() {
        const todos = ref([
          { text: 'Vue 실습' },
          { text: '자격증 공부' },
          { text: 'TIL 작성' }
        ])

        const restOfTodos = computed(() => {
          return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
        })

        const getRestOfTodos = function () {
          return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
        }

        return {
          todos,
          restOfTodos,
          getRestOfTodos,
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

### Conditional Rendering

```html

<body>
  <div id="app">
    <!-- if else -->
    <p v-if="isSeen">true일때 보여요</p>
    <p v-else>false일때 보여요</p>
    <button @click="isSeen = !isSeen">토글</button>

    <!-- else if -->
    <div v-if="name === 'Alice'">Alice입니다</div>
    <div v-else-if="name === 'Bella'">Bella입니다</div>
    <div v-else-if="name === 'Cathy'">Cathy입니다</div>
    <div v-else>아무도 아닙니다.</div>

    <!-- v-if on <template> -->
    <template v-if="name === 'Cathy'">
      <div>Cathy입니다</div>
      <div>나이는 30살입니다</div>
    </template>

    <!-- v-show -->
    <div v-show="isShow">v-show</div>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const isSeen = ref(true)
        const name = ref('Cathy')
        const isShow = ref(false)
        return {
          isSeen,
          name,
          isShow
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

### List Rendering

```html

<body>
  <div id="app">
    <div v-for="(item, index) in myArr">
      {{ index }} // {{ item.name }}
    </div>
    
    <div v-for="(value, key, index) in myObj">
      {{ index }} / {{ key }} / {{ value }}
    </div>

    <!-- v-for on <template> -->
    <ul>
      <template v-for="item in myArr">
        <li>{{ item.name }}</li>
        <li>{{ item.age }}</li>
        <hr>
      </template>
    </ul>

    <!-- nested v-for -->
    <ul v-for="item in myInfo">
      <li v-for="friend in item.friends">
        {{ item.name }} - {{ friend }}
      </li>
    </ul>

  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const myArr = ref([
          { name: 'Alice', age: 20 },
          { name: 'Bella', age: 21 }
        ])
        const myObj = ref({
          name: 'Cathy',
          age: 30
        })

        // nested v-for
        const myInfo = ref([
          { name: 'Alice', age: 20, friends: ['Bella', 'Cathy', 'Dan'] },
          { name: 'Bella', age: 21, friends: ['Alice', 'Cathy'] }
        ])

        return {
          myArr,
          myObj,
          myInfo
        }
      }
    })

    app.mount('#app')
  </script>
</body>


<body>
  <div id="app">
    <!-- Maintaining State with key -->
    <div v-for="item in items" :key="item.id">
      <!-- content -->
      {{ item }}
    </div>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        let id = 0

        const items = ref([
          { id: id++, name: 'Alice' },
          { id: id++, name: 'Bella' },
        ])

        return {
          items,
        }
      }
    })

    app.mount('#app')
  </script>
</body>

<body>
  <div id="app">
    <!-- [Bad] v-for with v-if -->
    <!-- <ul>
      <li v-for="todo in todos" v-if="!todo.isComplete" :key=""todo.id>
        {{ todo.name }}
      </li>
    </ul> -->

    <!-- [Good] v-for with v-if & computed-->
    <ul>
      <li v-for="todo in completeTodos" :key="todo.id">
        {{ todo.name }}
      </li>
    </ul>

    <!-- [Good] v-for with v-if & template-->
    <ul>
      <template v-for="todo in todos" :key="todo.id">
        <li v-if="!todo.isComplete">
          {{ todo.name }}
        </li>
      </template>
    </ul>


  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref, computed } = Vue

    const app = createApp({
      setup() {
        let id = 0

        const todos = ref([
          { id: id++, name: '복습', isComplete: true },
          { id: id++, name: '예습', isComplete: false },
          { id: id++, name: '저녁식사', isComplete: true },
          { id: id++, name: '노래방', isComplete: false }
        ])

        const completeTodos = computed(() => {
          return todos.value.filter((todo) => !todo.isComplete)
        })

        return {
          todos,
          completeTodos
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```

### Watchers

```html

<body>
  <div id="app">
    <!-- 1 -->
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- 2 -->
    <input v-model="message">
    <p>Message length: {{ messageLength }}</p>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref, watch } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const message = ref('')
        const messageLength = ref(0)

        const countWatch = watch(count, (newValue, oldValue) => {
          console.log(`newValue: ${newValue}, old Value: ${oldValue}`)
        })

        const messageWatch = watch(message, (newValue, oldValue) => {
          messageLength.value = newValue.length
        })

        return {
          count,
          message,
          messageLength
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

### Lifecycle Hooks

```html

<body>
  <div id="app">
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>
    <p>{{ message }}</p>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref, onMounted, onUpdated } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const message = ref(null)

        onMounted(() => {
          console.log('mounted')
        })

        onUpdated(() => {
          message.value = 'updated~!'
        })

        return {
          count,
          message
        }
      },
    })

    app.mount('#app')

  </script>
</body>


<body>
  <div id="app">
    <button @click="getCatImage">냥냥펀치</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref, onMounted } = Vue
    const URL = 'https://api.thecatapi.com/v1/images/search'

    const app = createApp({
      setup() {
        const getCatImage = function () {
          axios({
            method: 'get',
            url: URL,
          })
            .then((response) => {
              imgUrl = response.data[0].url
              return imgUrl
            })
            .then((imgData) => {
              imgElem = document.createElement('img')
              imgElem.setAttribute('src', imgData)
              document.body.appendChild(imgElem)
            })
            .catch((error) => {
              console.log('실패했다옹')
            })
        }

        onMounted(() => {
          getCatImage()
        })

        return {
          getCatImage
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```

### Vue Style Guide

- A - 필수
- B - 강력추천
- C - 추천
- D - 주의해서 사용

# 2023 11 07 tuesday

## Single-File Components

- component 
  - 재사용 가능한 코드 블록
  - 특징
    - UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
    - 그러면 자연스럽게 앱은 중첩된 Component의 트리로 구성됨

### Single-File Components

- 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식

```html

<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('hello world!')
</script>

<style scoped>
.greeting {
  color: crimson;
}
</style>

```

### SFC build tool (vite)

- Node.js의 영향
  - 기존에 브라우저 안에서만 동작할 수 있었던 javascript를 브라우저가 아닌 서버 측에서도 실행할 수 있게 함
    - 프론트엔드와 백엔드에서 동일한 언어로 개발할 수 있게 됨
  - NPM을 활용해 수많은 오픈 소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함

### Vue Component

- App.vue

```html

<template>
  <h1>App.vue</h1>
  <MyComponent />
</template>

<script setup>
// import MyComponent from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent.vue'

</script>

<style scoped>

</style>

```

- MyComponent.vue

```html

<template>
  <div>
    <h2>MyComponent</h2>
    <MyComponentItem />
    <MyComponentItem />
    <MyComponentItem />
  </div>
</template>

<script setup>
import MyComponentItem from '@/components/MyComponentItem.vue'

</script>

<style scoped>

</style>


```

- MyComponentItem.vue

```html

<template>
  <p>MyComponentITEM</p>
</template>

<script setup>

</script>

<style scoped>

</style>

```

# 2023 11 08 wednesday

## Component State Flow

### Passing Props

- Props
  - 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
  - 특징
    - 부모 속성이 업데이트 되면 자식으로 흐르지만 그 반대는 안됨
    - 즉 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
    - 또한 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨
    - 부모 컴포넌트에서만 변경하고 이를 내려받는 자식 컴포넌트는 자연스럽게 갱신

- One-Way Data Flow
  - 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성

- 단방향인 이유
  - 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함

### Component Events

- App.vue

```html

<template>
  <div>
    <Parent />
  </div>
</template>

<script setup>
import Parent from '@/components/Parent.vue'

</script>

<style scoped>

</style>

```

- Parent.vue

```html

<template>
  <div>
    <ParentChild 
      my-msg="ssafy" 
      :dynamic-props="name" 
      @some-event="someCallback"
      @emit-args="getNumbers"
      @update-name="updateName"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

const name = ref('Alice')

const someCallback = function () {
  console.log('ParentChild가 발신한 emit 이벤트를 수신했습니다.')
}

const getNumbers = function (...args) {
  console.log(args)
}

const updateName = function () {
  name.value = 'Bella'
}
</script>

<style scoped>

</style>

```

- ParentChild.vue

```html

<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild 
      :my-msg="myMsg" 
      @update-name="updateName"
    />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';

// 1. props - 문자열 배열 선언 방식
// defineProps(['myMsg'])

// 2. props - 객체 선언 방식
// defineProps({
//   myMsg: String,
//   dynamicProps: String,
// })

// props 데이터를 script에서 사용하려면
// const props = defineProps({
//                 myMsg: String,
//                 dynamicProps: String,
//               })

// console.log(props)
// console.log(props.myMsg)

// 3. props - 객체 선언 방식의 활용
// defineProps({
//   myMsg: {
//     type: String,
//     required: true,
//     // validator(value) {
//     //   return ['success', 'warning', 'danger'].includes(value)
//     // }
//     validator(value) {
//       const validValues = ['success', 'warning', 'danger']
//       if (!validValues.includes(value)) {
//         console.error('에러입니다!!')
//         return false
//       }
//       return true
//     }
//   }
// })

// emit - 문자열 배열 선언 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}

</script>

<style scoped>

</style>

```

- ParentGrandChild.vue

```html

<template>
  <div>
    <p>{{ myMsg }}</p>
    <button @click="updateName">이름 변경!</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String,
})

const emit = defineEmits(['updateName'])

const updateName = function () {
  emit('updateName')
}

</script>

<style scoped>

</style>

```


# 2023 11 09 thursday

## Router

### Routing

- 네트워크에서 경로를 선택하는 프로세스 
- 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술
- 만약 routiong이 없다면 
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감
    - 링크를 공유할 시 첫 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

### Vue Router

- Vue 공식 라우터

### Navigation Guard

- 종류
  - Globally
    - 애플리케이션 전역에서 동작
    - index.js에서 정의
  - Per-route
    - 특정 route에서만 동작
    - index.js의 각 routes에 정의
  - In-component
    - 특정 컴포넌트 내에서만 동작
    - 컴포넌트 Script에 정의

- index.js

```js

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'


const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인되어 있습니다.')
          return { name: 'home' }
        }
      }
    }
  ]
})

// router.beforeEach((to, from) => {
//   console.log(to)
//   console.log(from)
// })

// router.beforeEach((to, from) => {
//   const isAuthenticated = false
  
//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login' }
//   }
// })

export default router

```

- userview.vue

```html

<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
    <h2>{{ userId }}번 유저의 페이지입니다.</h2>
    <button @click="goHome">홈으로!</button>
    <button @click="goAnotherUser">100번 유저 페이지로!</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네이게이션
const router = useRouter()

const goHome = function () {
  // router.push({ name: 'home' })
  router.replace({ name: 'home' })
}

// In-component Guard
// 1. onBeforeRouteLeave
onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

// 2. onBeforeRouteUpdate
const goAnotherUser = function () {
  router.push({ name: 'user', params: {id: 100} })
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})

</script>

<style scoped>

</style>

```

# 2023 11 13 monday

## State Management

- Vue 컴포넌트는 이미 반응형 상태를 관리하고 있음 
- 상태 === 데이터

- 컴포넌트 구조의 단순화
  - 상태 
  - 뷰
  - 기능
  - 단방향 데이터 흐름의 간단한 표현

- 상태 관리의 단순성이 무너지는 시점
  - 여러 컴포넌트가 상태를 공유할 때
  - 서로 다른 뷰의 기능이 동일한 상태를 변경시켜야 하는 경우

- 해결책
  - 각 컴포넌트의 공유 상태를 추출하여, 전역에서 참조할 수 있는 저장소에서 관리
  - 컴포넌트 트리는 하나의 큰 '뷰'가 되고 모든 컴포넌트는 트리 계층 구조에 관계없이 상태에 접근하거나 기능을 사용할 수 있음
  - Vue의 공식 상태 관리 라이브러리 === 'Pinia'

### State management library (Pinia)

- main.js

```js

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)

app.mount('#app')

```

- stores/counter.js

```js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    { id: id++, text: 'todo 1', isDone: false },
    { id: id++, text: 'todo 2', isDone: false },
  ])

  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function (todoId) {
    // todos 배열에서 몇번째 인덱스가 삭제되었는지 검색
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // 찾은 인덱스 값을 통해 배열에서 요소를 제거 후 원본 배열 업데이트
    todos.value.splice(index, 1)
  }

  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo) =>{
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodosCount = computed(() =>{
    return todos.value.filter((todo) => todo.isDone).length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist: true })

```

- components/TodoForm.vue

```html

<template>
  <div>
    <form @submit.prevent="createTodo()">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const todoText = ref('')
const store = useCounterStore()

const createTodo = function () {
  store.addTodo(todoText.value)
  todoText.value = ''
}

</script>

<style scoped>

</style>

```

- components/TodoList.vue

```html

<template>
  <div>
    <TodoListItem 
      v-for="todo in store.todos"
      :key="todo.id"
      :todo-data="todo"
    />
  </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>

</style>

```

- components/TodoListItem.vue

```html

<template>
  <div>
    <span 
      @click="store.updateTodo(todoData.id)"
      :class="{ 'is-done': todoData.isDone}"
    >
      {{ todoData.text }}
    </span>
    <button @click="store.deleteTodo(todoData.id)">X</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

defineProps({
  todoData: Object
})

const store = useCounterStore()

</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}

</style>

```

- App.vue

```html

<template>
  <div>
    <h1>Todo PJT</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'

import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>
</style>

```

# 2023 11 14 tuesday

## Vue with DRF 1

- index.js

```js

import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
// import SignUpView from '@/views/SignUpView.vue'
// import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    // {
    //   path: '/signup',
    //   name: 'SignUpView',
    //   component: SignUpView
    // },
    // {
    //   path: '/login',
    //   name: 'LogInView',
    //   component: LogInView
    // }
  ]
})

export default router

```

- counter.js

```js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { articles, API_URL, getArticles }
}, { persist: true })

```

- ArticleView.vue

```html

<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>

```

- CreateView.vue

```html

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>

```

- DetailView.vue

```html

<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>

```

- ArticleList.vue

```html
<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
console.log(store.articles)
</script>
```

- ArticleListItem.vue

```html

<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>

```

- App.vue

```html

<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>

```

# 2023 11 15 wednesday

## Vue with DRF 2

### DRF Authentication

- settrings.py

```python

# 추가
INSTALLED_APPS = [
  'rest_framework.authtoken',
  'dj_rest_auth',
  'django.contrib.sites',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'dj_rest_auth.registration',
]

SITE_ID = 1

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

```

- signals.py(accounts)

```python

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

```

- views.py(articles)

```python

# post
serializer.save(user=request.user)

```

### Authentication with Vue

- index.js

```python

import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router

```

- counter.js

```python

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin, logOut }
}, { persist: true })

```

# 2023 12 07 thursday

## Java Chapter 01

```java

package ch01;

public class HelloWorld {

	public static void main(String[] args) {
		System.out.println("Hello, World");
		
	}

}

```

```java

package ch03;

public class BinaryTest {

	public static void main(String[] args) {

		int num = 10;
		int bNum = 0b1010;
		int oNum = 012;
		int xNum = 0XA;
		
		System.out.println(num);
		System.out.println(bNum);
		System.out.println(oNum);
		System.out.println(xNum);
		
		int cNum = 0b01000001;
		System.out.println((char)cNum);
	}

}

```

```java

package ch04;

public class VariableTest {

	public static void main(String[] args) {

		int age;
		age = 10;
		int level = 1000;
		System.out.println(age);
		System.out.println(level);
	}

}

```

```java

package ch05;

public class IntVariableTest {

	public static void main(String[] args) {
		byte bs = 127;
		
		System.out.println(bs);
		
		long iVal = 12345678900L;
		System.out.println(iVal);
		
		
		
	}

}

```

```java

package ch06;

public class DoubleTest {

	public static void main(String[] args) {
		
		double dnum = 3.14;
		float fnum = 3.14F;
		
		System.out.println(dnum);
		System.out.println(fnum);
		
		double mynum = 1;
		for ( int i=0; i<10000; i++) {
			mynum += 0.1;
		}
		
		System.out.println(mynum);
	}

}

```

```java

package ch07;

public class CharacterTest {

	public static void main(String[] args) {
		
		char ch1 = 'A';
		System.out.println(ch1);
		System.out.println((int)ch1);
		
		char ch2 = 66;
		System.out.println(ch2);
		
		char ch3 = '한';
		char ch4 = '\uAC00';
		System.out.println(ch3);
		System.out.println(ch4);
		
		
		
		
	}

}

```

```java

package ch08;

public class BooleanTest {

	public static void main(String[] args) {
		
		boolean isMarried = false;
		System.out.println(isMarried);
		
	}

}

```

```java

package ch08;

public class LocalVariableType {

	public static void main(String[] args) {
		
		var i = 10;
		var j = 10.0;
		var str = "hello";
		
		System.out.println(i);
		System.out.println(j);
		System.out.println(str);
		
		str = "test";
		System.out.println(str);
		
	}

}

```

```java

package ch09;

public class ConstantTest {

	public static void main(String[] args) {
		
		final int MAX_NUM;
		final int MIN_NUM = 10;
		MAX_NUM = 1000;
		System.out.println(MIN_NUM);
		System.out.println(MAX_NUM);
	}

}

```


# 2024 01 03 wednesday

## 애자일
- 공통프로젝트에서 하는 것은 애자일 방법을 따라서 개발을 해본다는 것 
- 개발과 함께 즉시 피드백을 받아서 유동적으로 개발하는 방법

# 2024 01 05 friday

## JAVA 인터페이스
- 모든 메서드가 추상 메서드로 선언됨 public abstract
- 모든 변수는 상수로 선언됨 public static final

## 코드리뷰 받을 때
- 코드!=나
- 나에 대한 평가가 아니라 그저 코드에 대한 리뷰
- 리뷰해주는건 당연한 것은 아니다!
- 리뷰어에 대한 감사

## 코드리뷰
1. 빠르게 리뷰하기
    
    - P1 : 이번에 반드시 반영되어야 하는 중대한 코드 수정 의견(Request Changes)
    
       - 버그 가능성이 있거나 잘못된 구현인 경우, 만약 반영되지 않는다면 이에 대한 반대 의견도 낼 수 있어야 한다.
    
    - P2 : 적극적으로 이야기했으면 하는 의견(Request Changes)
    
       - 잠재적인 이슈나 확장성을 고려해야 하는 경우. 토론하며 의견 조율할 수 있다.
    
    - P3 : 가능하다면 반영해주었으면 하는 의견(Request Changes)
    
       -  지금 구현보다 더 나은 방향이 있는 경우. 이번 반영이 얼벼다면 다음 작업에서도 고려해볼 수 있도록 한다.
    
    - P4 : 다음에 반영해도 되는 의견 (Approve)
    
       - 반영이 되지 않거나 반대 의견을 적극적으로 할 필요 없다.
    
    - P5 : 사소한 의견(Approve)
    
       - 무시해도 됨. 혹은 관련 나누고 싶은 점 나눌 수 있다.
    
    
2. nit 줄이기
    - 사소하고 작은 문제로 주로 스타일 가이드 준수, 가독성 개선 등을 의미
    - 전체적으로는 중요하지 않지만 품질 햐상에 도움이 될 수 있는 부분에서 사용
3. 변경 사이즈 줄이기

## 크롬 익스텐션
- WorkerB for Pull requests

# 2024 01 10 wednesday

# Agaile 개발론

1. 애자일개발이란?
  
2. 등장배경
  
3. 장단점
  
4. 애자일 프레임워크
  

## 정의

- 사전적 의미 : 신속한, 날렵한, 기민한
  
- sw 방법론 : 짧은 주기의 개발 단위를 반복하며 프로젝트를 완성
  
- how? : 스프린트(sprint)단위로 디자인-> 개발 -> 테스트 반복
  

## 특징

- 고객과 개발자의 지속적인 소통으로 변화하는 요구 사항 신속하게 반영 가능
  
- 개인 보다는 팀의 목적 우선시, 고객의 의견을 가장 높은 가치로
  
- 팀원들의 주기적인 회의 및 시현을 통해 잠재적인 보그 수정, 미흡한 기능 추가
  
- 고객으로부터 즉각적인 피드백을 통한 수정, 보완 가능
  
- 팀원들과의 주도적이며 자발적인 개발 문화로 프로그램의 전체적 품질 향상
  

=> 게임, 배달 앱, 대부분의 앱 프로그램 등

- 서비스의 요구사항 빈번히 수정되고 반복적인 업데이트 필요한 프로젝트

## 폭포수(워터풀) 개발론

- 가장 오래된 sw 개발론
  
  - 각 작업이 마치 폭포수가 내려가듯이 작업 절차 진행
    
  - 한 단계가 마무리되기 전 다음 단계로 진행 안됨
    
  - 속도 느리고 유연하지 못함
    
  - 요구 사항이 바뀌거나 수정하려면 다시 맨 처음부터 수정해야 하는 불편함
    

=> B2B(Business to Business)

- 은행권 업무, POS 프로그램, 키오스크
  
- 프로세스가 비교적 정확, 요구사항 변동 적음
  

## 장단점

- 장점
  
  - 프로젝트 계획에 걸리는 시간 최소화
    
  - 반복적인 테스트로 잠정적인 버그 쉽고 빠르게 개선 가능
    
  - 계획 변경, 기능 추가에 유연
    
  - 고객의 요구 사항에 대한 즉각적인 피드백에 유연, 프로토타입 모델 빠르게 출시 가능
    
  - 비교적 빠르게 제품 출시 가능
    
- 단점
  
  - 반복적인 유지 보수 작업 많음
    
  - 요구 사항 및 계획이 크게 변경될 경우 모델 자체가 무너질 수 있음
    
  - 공통 작업의 리소스 투입이 많음
    
  - 개발속도는 빠르나 번아웃 현상 쉽게 올 수 있음
    
  - 확정되지 않은 계획으로 인해 개발 진행에 대한 정확한 이해 부족 발생 가능
    

## 애자일 프레임 워크

- MVP(Minimum Viable Product) : 최소 기능 제품
  
  - 고객이 우너하는 제품의 최소한을 정의
    
    - 최소 비용, 핵심 기능 만을 담은 제품
      
    - 시간과 비용 절감 측면에서 효율적
      
    - 사업 리스크 최소화
      
- 스프린트(Sprint)
  
  - 팀의 일정량의 작업을 완료하기 위해 정해진 짧은 기간
    
  - 스프린트 계획 회의 - 스프린트 기간 동안 해야할 일들을 정리하고 달성하기 위한 방법 회의
    
- 스크럼(Scrum)
  
  - 정해진 스프린트 내에 실제 행해져야 하는 개발 업부
    
  - 제품 백로그 작성 : 고객, 프로젝트 이해관계자 의견 취합, 업무 우선 순위 매기는 작업
    
  - 스프린트 백로그 작성 : 스프린트 내에 각 팀원들이 해야할 업무의 리스트 만드는 작업
    
  - 데일리 스크럼 : 매일 진행한 업무를 보고하고 공유
    
  - 개발 및 테스트 : 실제 맡은 영역 개발, 테스트
    
  - 스프린트 리뷰 및 회고 : 장 단점 분석, 더 나은 방향으로 개선
    
- 테스트 주도적 개발
  
  - 실제 필요한 기능만 만들고 그 기능이 제대로 동작하는지 코드 기반 테스트
    
  - 잘 동작 => 코드 리팩토링 및 모듈화
    
- 데브옵스
  
  - 개발 + 운영
    
  - 새로운 소프트웨어 기능 개선, 버그 수정시 바로 배포함 => 빠른 피드백 가능
    
  - 지속적 통합 및 연속 배포(CI/CD) 구축

  # 2024 01 11 thursday

  ## TIP

- 너무 새로운 것에 집착하지 말자. 기존 프로젝트를 부분적으로 고쳐 개선하는 것도 좋은 프로젝트!
- 회의 시에는 항상 회의 시간을 정해두고 하자. 무조건 진행하는 회의는 에너지 낭비
- 기술에 너무 매몰되지 말자.
- 공통 모든 명세서를 훑어보고 다양한 기술 중 우리팀에 맞는 기술 선택
- ! 프로젝트의 메인 기능을 명확하게 도출할 것.

## 프로젝트 당위성

- 행복 회로에 갇혀 다른 유저들이 사이트를 왜 써야 하는지에 대해 고민하지 않음
  
- 최초 유저를 끌어들이는 방법 또는 다양한 유저가 관심있어할 기능에 대한 고민 필요
  
- 포괄적인 기능을 가지고 있는 것들은 개발하기 어려움 (블로그)
  
- 명확한 주제가 있는 프로젝트를 하는 것이 규모와 일정을 맞추기 쉬움
  

## 세부 기획

- 메인 아이디어, 시스템화 되려면 필요한 기능에 대해 고민
  
- 시스템 프로세스에 전체적으로 필요한 부분(쇼핑몰 : 조회 > 장바구니 > 결제 > 배송조회)
  
- 대부분 시스템에 들어가는 공통영역(회원가입, 유저관리, 게시판, 관리자 페이지)
  
- 아이디어 -> 세부기획을 보고 누구나 이해할 수 있어야 함
  
- 작성된 내용을 보고 질문이 오지 않게 작성(질의응답 => 문서 업데이트)
  
- 할 수 있는 한 자세하기~
  
- 기능명세/화면설계/DB설계에서 작성된 내용이 동일한지가 가장 중요

# 2024 01 12 friday

# 아키텍처의 정의와 설계 방법

- 아키텍처의 필요성에 대한 인지
  
- 목적에 맞는 아키텍처 문서작성 방법의 이해
  

## 정의

- 아키텍처 : 건물이나 다른 구조물을 계획하고 건설하는 **과정과 그 결과물**
  
- SW아키텍처
  
  - 소프트웨어 구성요소드 사이에서 유기적 관계를 표현하고
    
  - 소프트웨어의 설계와 업그레이드를 통제하는 **지침과 원칙**이다.
    

## 어떻게 사용되는가?

- 초기 설계 과정의 결정 사항
  
  - 구현에 대한 제약사항 검토 및 시스템에 대한 구조 결정
    
- 커뮤니케이션의 기준점
  
  - 서비스나 시스템의 이해 당사자들 간의 공통분모
    
- 재사용 가능한 레퍼런스
  
  - 아키텍처를 결정짓게 한, 유사한 요구사항 및 설계 경험의 재사용
    

> 구현 방법에 대한 고도화 전략 수립 및 검토
> 
> Sequence 등 상세 구현 방법 결정 및 도식화의 근거자료
> 
> 팀내 의사결정 내용 Synchronized
> 
> 레퍼런스 축척

## 아키텍처 설계

- 학사관리시스템
  
  > 결정요인 도출
  > 
  > - 이해관계자 선별 : 시스템과 연관되는 사람이나, 다른 시스템   
  >   
  >   - 학생, 교수, 교직원, 외부시스템(인사관리, 학사관리 시스템)
  > - 기능요구사항
  >   
  >   - 학사 관리 기능, 수업 관리 기능, 수강 관리 기능, 사용자 관리 기능
  > - 비기능요구사항
  >   
  >   - 강의 신청 기간에 원활한 진행, 언제어디서나 접근 가능, 모바일 접속 가능, 권한을 통한 정보보안, 데이터 손실 방지
  
- 품질속성시나리오 & 비기능요구사항
  
  - 스파이크 성 트래픽에 대한 처리, public 환경, 하이브리드 앱
    

## 정리

- 아키텍처 그리기 순서
  
  - 비기능요구사항 도출 > 품질속성 시나리오 작성 > 아키텍처 패턴 결정 > 아키텍처 도식화
    
  
  1. 품질속성을 정확히 정의
    
  2. 품질속성 별로 전략 도출
    
  3. 도출된 전략을 잘 보여줄 수 있게 도식화
    
  4. 아키텍처 검증(평가)

  # 2024 01 16 tuesday

  ### 깃의 사용 이유

*   소스코드 관리
*   협업 개발

### 깃 기본 설정

*   깃 커밋 정보
    *   소스코드 변경 내용과 함께 작성자의 이름과 이메일도 포함
    *   문제 상황이나 코드 리뷰시 중요한 정보
    *   특히 여러 명의 개발자가 동시에 작업해야 하는 상황에서는 더욱 중요
*   정확한 이름과 이메일 사용gt 중요

### git config

*   GIT 사용 환경 설정 도구(명령어)
    *   GIT을 사용하기 위해서는 git config 명령을 통해 이름과 이메일 주소 설정 필수
    *   커밋 정보에 포함되어 누가 커밋을 했는지 알 수 있도록 해 줌

### GIT 커밋 메세지 컨벤션

*   GIT 커밋 메시지
    
    *   다른 개발자의 작업 내역이나 변경사항을 파악하는데 이용
    *   변경 이력 추적 및 문제 해결에 도움
*   Conventional Commits
    
    *   가벼운 컨벤션으로 명확한 커밋 히스토리를 생성하기 위한 간단한 규칙 제공
    *   커밋 메시지에 신규 기능 추가, 문제 수정, 커다란 변화가 있음을 기술함
    
    [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
    
*   커밋 메시지 구조 (제목, 본문, 꼬리말)
    
        <type>[optional scope]: <description>
        
        [optional body]
        
        [optional footer(s)]
        
    
    *   타입
        *   fix와 feat 이외의 타입 허용
        *   앵귤러 컨벤션 : build, chore, ci, docs, style, refactor, perf, test 등
    *   설명
        *   작업한 내용을 최대한 함축하여 대략 50자 이내로 작성
    *   본문 (선택사항)
        *   기본적으로는 선택사항이지만 **가급적 작성**
        *   자유로운 형식으로 필요시 여러 단락으로도 작성 가능
        *   무엇을 변경했는지 보다는 **왜 수정 했는지**를 설명
    *   꼬리말
        *   필요시 작성
        *   연관되어 있는 JIRA 이슈 번호 등을 작성
*   커밋 메시지를 통해 코드 리뷰어에게 정보 제공
    
    *   Gerrit을 통한 코드 리뷰시 커밋 단위로 코드 리뷰
    *   빠른 리뷰를 위해서는 리뷰어에게 정보 제공 필요
    *   커밋 메시지 본문을 통해 정보 제공

### GIT 브랜치 전략

*   Git 브랜치
    
    *   독립적인 개발 공간 제공
    *   쉽고 빠르게 브랜치를 생성하고 이동 가능
    *   아이디어를 쉽게 시험해 볼 수 있음
*   브랜치 전략
    
    *   쉽고 편리한 브랜치, 계획없이 만들다 보면 남용될 수 있음
    *   브랜치를 효율적으로 사용하는 방법에 대한 다양한 브랜치 전략 제시
    *   가장 대표적인 브랜치 전략은 gitflow
    *   최근에는 배포 주기가 빨라지면서 다른 전략도 모색함(Github flow, Gtlab flow 등) → Gitflow 보다 단순한 형태로 배포가 매우 잦은 환경에 적합함.
    
*   Gitflow 전략
    
    *   master, develop, feature, release, hotfix 5가지 브랜치로 관리
    *   브랜치 마다 목적이 명확
    *   브랜치별 생명 주기에 따른 처리 주의

### Git 히스토리 중요성

*   Git History
    *   Git은 SW 변경 사항을 커밋 단위로 기록하기 때문에 커밋 이력의 모음이 있다
    *   Git 그래프나 로그로 확인한다.
*   Git 히스토리가 중요한 이유
    *   레거시 코드 유지 보수에 중요
    *   버그 발생 시점 파악 및 문제 해결 실마리 제공
*   버그 발생 시점 파악 및 문제 해결 실마리 제공
    *   과거 커밋 시점으로 돌아가서 동작 확인
    *   git checkout 명령어 이용

### 유용한 기능 - git stash

*   갑자기 끼어드는 작업
    
    *   A 기능 작업 중인데, 갑자기 B 기능 작업 해달라고 한다면
    *   새 작업 위해 새로운 브랜치를 생성하거나 기존 작업 중인 브랜치로 이동 필요
    *   생각보다 자주 발생
*   브랜치 이동 안되는 상황
    
    *   수정중인 파일이 있을 경우 브랜치 이동 불가
    *   커밋 하거나 수정 전 상태로 리셋 필요
*   git stash
    
    *   현재 작업중인 내용을 모두 stash 공간에 차곡차곡 쌓아 줌
    
        $ git stash save # 현재 작업 상태 백업
        ---
        새로운 작업 진행
        ---
        $ git stash pop # 이전 작업 상태 복구

# 2024 01 17 wednesday

## WEB

:)

- 브라우저만 있다면 어디서든 접속 가능
  
- 웹페이지가 업데이트된 후 배포 속도가 빠르다
  
- 플랫폼 환경에 제약 없음
  

:(

- 속도 느림
  
- UI 사용성이 앱보다는 좋지 않음
  
- 연결하기 위해서는 URL 입력해야함
  

## 모바일

:)

- 앱 마켓 사용 가능 (다양한 수익 창출 가능)
  
- 알림, 주소록, 카메라, GPS 등의 스마트폰 기능 사용할 수 있음
  
- 서비스 실행이 편함(아이콘 클릭으로 서비스 시작 가능)
  
- 스마트폰에 최적화, 속도 빠름
  
- UI사용성이 스마트폰에 최적화
  

:(

- 마켓에 등록하기 위해 개발자 등록을 해야함.
  
- 사용자가 앱을 다운 받아야하는 불편함
  
- IOS, AOS 모두 개발해야함
  
- 앱이 수정되면 마켓에 새로 배포해야함(배포까지 시간 오래 걸림)
  
- 사용자가 사용하는 디바이스 OS에 따라 버전을 관리해야 한다.
  

## 예시(카카오톡)

- 사용자가 서비스에 자주 접속해야 한다.(접속 간편해야 함)
  
- 메시지가 왔을 경우 수신지가 빠르게 확인할 수 있어야 한다(알람 기능)
  
- UI 매우 중요(최적화 중요)
  
- 간편한 인앱 결제 기능 필요(이모티콘, 기프티콘 구매 등)
  

## 개발의 현실

- 새롭게 개발하려는 프로젝트에 딱 맞는 인원을 배치하기 어렵다
  
- 정해진 시간 안에 프로젝트를 완성해야 하기 때문에 모든 기능을 넣기 어렵다
  
- 정해진 자원과 한정된 기간 내에 최대한 완성도 높이는 것이 프로젝트
  

## 타협 방법

- 공통의 목표를 정하자
  
- 우리가 구현하고자 하는 핵심기능이 무엇인지 명확하게 정의하고 개발자를 배치하자
  
- 우리팀의 역량을 객관화하자
  
- 서비스를 구현하는 것 뿐만 아니라 서비스를 구현할 수 있는 준비를 하는 것 또한 개발자의 역할

# PRJ_SSAFY 개발환경
2024.01.17 양희재 실습코치님
# 프로젝트 과정

프로젝트 과정은 기획, 설계, 개발, 테스트, 오픈/운영의 순으로 이루어지며 추가로 프로젝트 회고와 함께 마무리된다.

## 기획

기획 과정에서는 주제 확정과 서비스 설계 전 필요한 요소를 정의하는 과정을 거친다.

### 개발 컨벤션

- 팀 마다 꼭 정해야 하는 기준
    - 마치 한 명이 진행한 것처럼
- 깃 컨벤션/ 지라 컨벤션 모두 협의
- 팀원들과 설정 후 페이지 생성 기록
- 켄벤션을 통해
    - 의미 있는 코드, 유지보수가 용이한 코드, 일관된 코드

### 기술 스택 선정

- 단순 나열 x
- 버전까지 상세히 작성
    - 모든 팀원이 동일한 환경에서 작업해야 함

### 기능 명세서

- 프로젝트의 볼륨을 알 수 있는 가장 좋은 도구
- 최대한 상세하게 작성
    - 팀원 간 인식 차이 확인, 의견 통일

## 설계

설계 과정에서는 기획 과정을 기반으로 코드 작성에 대한 자료를 작성하는 과정을 거친다.

### 디자인 시스템

- 서비스에 적용된 디자인 스타일의 규칙이나 가이드라인
- 파비콘
- 서비스 로고 → 서비스 컨셉에 많은 영향을 끼침
- 컬러 팔레트, 글꼴 등

### 와이어프레임

- 선(Wire)으로 틀(Frame)을 잡는다.

### 프로토타입

### 스토리보드

- 화면 설계도
- 다이어그램과 함께 작성하여 프로젝트의 전체적인 흐름과 페이지별 세부 기능에 대해서 한 눈에 알 수 있도록 정리

### ERD

- 데이터베이스 구조 정리

### API Docs

- URL, Request, Response, Error code/message

### 아키텍처

- 구성 요소 간의 관계 및 시스템 외부 환경과의 관계 등을 설명하는 설계도
- 서비스의 동작 원리
- 지속적인 피드백을 통해서 아키텍처 업그레이드

## 개발

### 진행 상황에 대한 공유

- 중요한 데이터는 따로 저장
- 노션 적극 이용
- 스크럼 / 회고를 통해서 팀 현황 확인

## 테스트

### 버그리포트

- 오류 내용 및 재현 방법 기재
- 해결 시 해결 방법 기재
- 포트폴리오 / 자기소개서 사용 가능

## 오픈/운영

- 오류 수집
- 피드백 수집
- 차이 업데이트 문서
- 유지보수
    - Google Analytucs
    - 부하테스트 등

## 프로젝트 회고

시간이 지나면 프로젝트는 점점 더 잊혀진다.. 그때그때 정리하자!

프로젝트 회고에 대한 내용에는 다음 내용이 포함될 수 있다.

- 프로젝트/교육명, 프로젝트 목표, 주요 내용, 키워드, 활동 기간, 기술스택
- 내가 기여한 부분, 긍정적인 결과, 극복한 문제 상황, 부족했던 부분, 배운점
- 추가 증빙자료 등

# SSAFY 개발 환경

### Mattermost

깃이나 지라 자동화 봇을 적용하여 확장된 서비스 이용 가능 → 구글링해서 방법 찾기

팀 헤더 설정을 통해 바로가기 생성 가능!

![마크다운 형태로 쓸 수 있음](https://prod-files-secure.s3.us-west-2.amazonaws.com/3dd3db3b-df8c-4041-bb45-ab33a34e39c8/21b82af5-b49c-4679-acf1-9ee73610629b/Untitled.png)

마크다운 형태로 쓸 수 있음

- 팀 회고나 공지, 봇, 로그 기록 등의 용도로 mm을 사용할 수 있음
- 필수 확인이 필요한 사람 언급해 메세지를 놓치는 일이 없도록 하자
- 또한 확인 후에는 항상 이모지를 남기자!

### GitLab

Readme를 잘 쓰자!

wiki: 자세한 PRJ 내용 기록용으로 쓸 수 있음

### Gerrit

코드리뷰 툴

- 코드리뷰란? 본인이 만들지 않은 코드에 대해서 리뷰를 통해 전체 코드를 관리

Gerrit 구조

- 로커에서 코드의 변경사항을 Gerrit에 리뷰 요청
- 해당 변경사항 검토 후 점수 및 리뷰 의견을 매김(-2~+2)
- 다음 조건을 충족할 시, 승인자는 변경 사항을 승인하여 Gerrit 내부의 Git 저장소에 반영할 수 있음
    - -2 받은 코드가 하나도 없을 것
    - +2 받은 코드가 하나는 있어야 함
- 변경 사항 반영 시 자동으로 git 에 반영

Gerrit 기대 효과

- 코드 일관성
- 협업 강화
- Merge 전 안전성 보장
- 코드 품질 향상

## Jira

- 로드맵에서 에픽 생성
- 백로그에서 이슈 생성
- 이슈에 에픽 연결 및 스토리 포인트 설정
- 스프린트에 이슈 이동
- 스프린트 시작
- 이슈 해결
- 스프린트 종료

백로그

- 프로젝트에서 해야하는 일(요구 사항)을 보여줌

스프린트

- 스크럼 보드의 개발 주기 단위
- SSAFY에서는 1주일 단위가 기본

이슈

- 오류, 버그, 새로운 기능, 작업 요청, 질문이나 의견 등 개발에 관한 모든 것
- ISSUE 종류
    - EPIC
    - STORY
    - TASK
    - SUB-TASK
    - BUG

## Jenkins

- 오픈 소스 지속적 통합 및 배포(CI/CD) 도구

# 2024 01 19 friday

# Code Review

## Code Review

- 개발자가 작성한 코드를 다른 개발자들이 검토하고 피드백하는 과정
  
- 배움을 주고 받으며 좋은 sw 개발자가 될 수 있는 실천법
  
- 기대효과
  
  1. 코드 품질 개선
    
  2. 코드 작성 능력 향상
    
  3. 협업 능력 향상
    

## SSAFY 에서의 코드 리뷰

- 팀원들 간의 코드리뷰를 통한 개발/소통 능력 향상
  
- 현업에서의 코드리뷰 문화를 사전 경험
  

## Code Review 의 필요성

- 코딩 컨벤션(Codeing Convention)
  
  - 읽고 관리하기 쉬운 코드를 작성하기 위한 일종의 코딩 스타일 규약
- 대표적인 컨벤션 요소
  
  - 명확한 네이밍 규칙
    
  - 들여쓰기와 포맷팅 규칙
    
  - 주석 작성 규칙
    
  - 함수와 메소드 규칙
    
- 좋은 코드 <-> 나쁜 코드
  
  - 성능이 좋은 코드 <-> 성능이 나쁜 코드
    
  - 의미가 명확하고 가독성이 좋은 코드 <-> 의미가 모호한 코드
    
  - 중복되는 내용이 제거된 코드 <-> 중복되는 코드
    
- 클린코드의 필요성
  
  - SW의 진정한 비용 \~= 유지보수(전체의 80% 이상)
    
  - 한번 작성한 코드는 10번 이상 읽음
    
  - 90% 이상의 시간을 코드를 이해하는데 사용
    

## Code Review의 목적

- 코드 품질 향상 및 표준화
  
  - 코드 리뷰를 통해 코드 품질을 높이고 일관된 컨벤션을 유지
- 안정성 강화
  
  - 다양한 시각으로 코드를 검토하며, 버그를 발견하고 프로그램의 안정성 향상
- 팀 전체 역량 강화(개발/협업/소통 등)
  
  - 팀원 간 지식을 공유하며, 팀 전체 개발 역량 및 협업을 강화

## Code Review의 절차

- 구성
  
  - 저자 : 코드의 작성자로 작업한 코드 내역을 리뷰어들에게 리뷰를 요청
    
  - 리뷰어 : 저자로부터 받은 변경 내역을 확인하고, 의견을 제시(팀원)
    
  - 승인자 : 리뷰가 완료되고 코드 변경 사항을 승인하는 역할
    
- 진행 순서
  
  - 0 준비단계 : 저자가 코드를 리뷰어들이 쉽게 이해할 수 있도록 준비
    
  - 1 리뷰요청 : 저자가 리뷰어들에게 리뷰 요청을 보냄
    
  - 2 리뷰진행 : 리뷰어들이 코드 변경 사항을 검토하고 피드백 작성
    
  - 3 리뷰 승인 : 최종 버전으로 승인 여부 결정
    
  - 4 최종 병합 : 승인이 된 코드는 팀 레포지토리에 병합
    

## Code Review의 어려움

- 코드 비판에 대한 두려움
  
- 개발 일정 지연 우려
  
- 의사 소통 중 생기는 마찰
  
- 전문성 부족으로 인한 부담
  

## Code Review 권장사항

1. 개선 필요 이유를 충분히 설명
  
2. 단순 해법보다 스스로의 고민과 학습을 통한 개선 방법 안내
  
3. 코드 컨벤션 기반 클린코드 유지 및 일관적 구현 안내
  
4. 숙제 검사가 아닌 학습 과정으로서의 리뷰
  
5. 리뷰를 위한 리뷰를 지양하고 칭찬을 활용
  
6. 친절, 배려 기반 명확한 피드백
  

# Gerrit Guide

## Gerrit?

- 코드 리뷰 기능과 Git 서버저장소 관리 기능을 제공하는 웹 기반 코드 리뷰 시스템
  
- Github, Gitlab 등에서는 PR(Pull Request), MR(Merge Request) 단계에서 merge 단위로 리뷰가 가능하나 Gerrit은 코드 리뷰에 목적을 둔 솔루션으로 각 commit 단위로 리뷰를 진행할 수 있는 것이 특징이다
  
  - 집중된 리뷰
    
  - 빠른 피드백
    
  - 분산된 리뷰 부담 감소
    

## SSAFY Gerrit

- SSAFY에서 제공하는 gerrit은 팀 프로젝트용 EC2에 사전 구축된 상태
  
- 백업
  
  - 명렁어로 폴더를 압축한 후 home 폴더에 생성된 압축 파일을 SCP, SFTP등으로 내려 받을 수 있음
    
  - 유사시를 대비해 주기적인 백업을 권장
    
  - replication 설정으로 소스 코드는 gitlab에 저장되더라도 코드 리뷰의 history는 gerrit을 복구해야만 확인 가능
    
  - 백업
    
    ```
    sudo systemctl stop gerrit
    cd/ opt && sudo tar -czvf ~/gerrit-backup.tar.gz gerrit
    sudo systemctl start gerrit
    ```
    
  - 복구
    
    ```
    sudo systemctl stop gerrit
    sudo mv /opt/gerrit /opt/gerrit-old
    sudo tar -xzvf gerrit-backup.tar.gz -C /opt/
    sudo systemctl start gerrit
    ```

    # 2024 01 25 thursday

    React 기초 및 응용 개발 실습
===================

2024.01.18

박세영 컨설턴트

그린랩스 개발본부/본부장, CJ 올리브네트웍스 대안통운IT서비스팀/PL, 유진그룹 물류부문 정보전략팀, 세종대학교 정보산업학 석사

**학습목표** : 처음 다루는 사람도 기본적인것을 다룰 수 있도록

Why ~ How
---------

### why?

*   새로운 언어 라는 막연함
*   눈에 안 들어오는 코드의 난해함 (Vue에 비해)

CRA : Create React App
----------------------

*   babel (컴파일러) ← 브라우저별로 서로 다른 자바스크립트를 이해할 수 있도록 통합해주는 역할
*   webpack (빌드 시켜주는 파일 팩) → 사용을 위해 javascript 실행기인 node가 필요하다.

### 설치 및 시작

*   Node.js 설치 → NPM사용을 위해서 사용함. 최신버전 추천함.
    
*   CRA 설치 → 설치 희망 path로 이동 후 npx명령어로 설치
    
        # npm 5.2 이상인 경우
        npx create-react-app appname
        
        # npm 6 이상인 경우
        npm init react-app appname
        
    
*   서버 실행
    
        # appname 폴더로 이동한 후
        npm start
        
    
*   index.html, index.js, App.js 등의 파일이 만들어진것을 확인할 수 있음
    

useState
--------

### 테이블 생성 & 데이터 적용

[React로 사고하기 – React](https://ko.legacy.reactjs.org/docs/thinking-in-react.html#step-2-build-a-static-version-in-react)

*   React 문법 : 대부분의 Object 표현 방식

    // App.js
    import logo from './logo.svg';
    import './App.css';
    
    function App() {
    	let title = ['name', 'major'];
    	let name = ['a', 'b'];
    	let major = ['industrial engineering', 'computer engineering'];
    
    	return (
    		// 여기에 div, table 등 작성!
    	)
    }
    

### \[객체, 대체값\]

*   useState 사용 위해

component
---------

React를 사용할 때는 컴포넌트를 class 또는 함수로 정의할 수 있습니다.

[React.Component – React](https://ko.legacy.reactjs.org/docs/react-component.html)

    // 함수형 컴포넌트
    import React from 'react';
    
    function MyComponent(props) {
    	return <div>Hello, {props.name}</div>;
    }
    
    export default MyComponent; //다른 JS파일에서 불러올 수 있도록 내보내주기
    
    //----------
    // 클래스형 컴포넌트
    import React from 'react';
    
    class MyComponent extends React.Component {
    	constructor(props) { // 생성함수
    		super(props);
    	}
    	
    	componentDidMount() { // 상속받은 생명주기 함수
    	}
    	
    	render() { // 상속받은 화면 출력 함수, 클래스형 컴포넌트는 render() 필수
    		return <div>Hello, {this.props.name}</div>;
    	}
    }
    
    export default MyComponent; //다른 JS파일에서 불러올 수 있도록 내보내주기
    

DataGrid
--------

[DataGrid API - MUI X](https://mui.com/x/api/data-grid/data-grid/)

⇒ 스프레드시트와 유사하게 표기하는 등 다양한 형태로 활용할 수 있음.

### MUI

→ 업계 표준처럼 사용하기도 함! 레퍼참고에 좋은 사이트

SSAFY 코드 리뷰와 Gerrit 사용 안내
=========================

2024.01.19

이준철 프로

Code Review
-----------

### 1\. Code Review란?

*   코드 리뷰
    *   개발자가 작성한 코드를 다른 개발자들이 검토하고 피드백하는 과정
    *   배움을 주고 받으며 좋은 SW 개발자가 될 수 있는 실천법
    *   **기대효과**
        1.  코드 품질 개선
        2.  코드 작성 능력 향상
        3.  협업 능력 향상
*   싸피에서의 코드 리뷰
    *   팀원들 간의 코드리뷰를 통한 개발/소통 능력 향상
    *   현업에서의 코드리뷰 문화를 사전 경험

### 2\. Code Review의 필요성

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e4a72e00-c2d8-4118-887b-37e2b5f8b0de/46b1e765-5bae-43f2-a4c7-6c0c36312a8e/Untitled.png)

팀 내 **일관된 스타일**과 **가독성**을 높이기 위해 필요하다.

*   코딩 컨벤션 (Coding Conventions)
    
    *   읽고 관리하기 쉬운 코드를 작성하기 위한 일종의 코딩 스타일 규약
*   대표적인 컨벤션 요소
    
    *   명확한 네이밍 규칙
    *   들여쓰기와 포멧팅 규칙
    *   주석 작성 규칙
    *   함수와 메소드 규칙
*   코드 포메터 (Code Formatter)
    
    *   VSCode Extention - Prettier
*   Oracle SQL Code Convention
    
    [Oracle SQL and PL/SQL Optimization for Developers — Oracle SQL & PL/SQL Optimization for Developers 3.1.0 documentation](https://oracle.readthedocs.io/en/latest/)
    
*   Clean Code ↔ Dirty Code
    
    *   성능이 좋은 코드 ↔ 성능이 나쁜 코드
    *   의미가 명확하고 가독성이 좋은 코드 ↔ 의미가 모호한 코드
    *   중복되는 내용이 제거된 코드 ↔ 중복되는 코드
*   클린코드의 필요성
    
    *   SW의 진정한 비용 ~= 유지보수 (전체의 80% 이상)
    *   한번 작성한 코드는 10번 이상 읽음
    *   90% 이상의 시간을 코드를 이해하는 데 사용함.

[Clean Code 클린 코드 - 예스24](https://www.yes24.com/Product/Goods/11681152)

⇒ 유지보수를 염두해두면서 프로젝트 하기

*   Microsoft 개발자의 75%는 매일 코드리뷰 진행!

### 3\. Code Review의 목적과 절차

*   목적
    *   코드 품질 향상 및 표준화 (일관된 컨벤션 유지)
    *   안정성 강화 (버그 일찍 발견하여 프로그램 안정성 향상)
    *   팀 전체 역량 강화 (개발,, 협업, 소통 등)
    *   상호 책임감과 관심 증대, 내 코드에 대한 부담 낮춤
*   절차
    *   구성
        *   저자 - 코드의 작성자로 작업한 코드 내역을 리뷰어들에게 리뷰 요청
        *   리뷰어 - 저자로부터 받은 변경 내역을 확인하고, 의견을 제시 (팀원)
        *   승인자 - 리뷰가 완료되고 코드 변경 사항을 승인 하는 역할
    *   진행 순서
        1.  준비 단계 - 저자가 코드를 리뷰어들이 쉽게 이해할 수 있도록 준비
        2.  리뷰 요청 - 저자가 리뷰어들에게 리뷰 요청을 보냄
        3.  리뷰 진행 - 리뷰어들이 코드 변경 사항을 검토하고 피드백 작성
        4.  리뷰 승인 - 최종 버전으로 승인 여부 결정
        5.  최종 병합 - 승인이 된 코드는 팀 레포지토리에 병합

### 4\. Code Review의 어려움

*   코드 비판에 대한 두려움
*   개발 일정 지연 우려
*   의사 소통 중 생기는 마찰
*   전문성 부족으로 인한 부담

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e4a72e00-c2d8-4118-887b-37e2b5f8b0de/8479c0fc-c9cb-49de-a659-f71bcaf03238/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e4a72e00-c2d8-4118-887b-37e2b5f8b0de/641037f3-e035-464c-b600-078fb371a475/Untitled.png)

### 5\. Code Review의 권장사항

1.  개선 필요 이유를 충분히 설명
2.  단순 해법보다 스스로의 고민과 학습을 통한 개선 방법 안내
3.  코드 컨벤션 기반 클린코드 유지 및 일관적 구현 안내
4.  숙제 검사가 아닌 학습 과정으로서의 리뷰
5.  리뷰를 위한 리뷰를 지양하고 칭찬을 활용
6.  친절, 배려 기반 명확한 피드백

Gerrit
------

네이버 등에서도 사용!

### 1\. Gerrit이란?

*   코드 리뷰 기능과 Git 서버저장소 관리 기능을 제공하는 웹 기반 코드 리뷰 시스템
*   Github, Gitlab 등에서는 PR(Pull Request), MR(Merge Request) 단계에서 merge 단위로 리뷰가 가능하나, Gerrit은 코드 리뷰에 목적을 둔 솔루션으로, 각 commit 단위로 리뷰를 진행할 수 있는 것이 특징

⇒ 집중된 리뷰, 빠른 피드백, 분산된 리뷰 부담 감소

### 2\. Gerrit의 구조

8989포트를 통해 접근 가능함

*   저자 Developer
    1.  push for review
*   리뷰어 Reviewers
    1.  review
*   승인자 Submitter
    1.  ( vote +2가 하나 이상이고, -2가 없을 때) submit

1.  repository 반영
2.  repository 자동 동기화

### 3\. SSAFY에서의 Gerrit

팀 프로젝트용 EC2에 사전 구축된 상태! 몇몇 설정만 가이드에 따라서 직접 하기

*   백업
    *   명령어로 폴더를 압축한 후 home 폴더에 생성된 압축 파일을 SCP, SFTP 등으로 내려 받을 수 있음
    *   유사시를 대비해 주기적 백업 권장
    *   replication 설정으로 소스 코드는 gitlab에 저장되더라도 코드 리뷰의 history는 gerrit을 복구해야만 확인 가능

    // backup
    sudo systemctl stop gerrit
    cd/ opt && sudo tar -cgvf !/gerrit-backup.tar.gz gerrit
    sudo systemctl start gerrit
    
    // 복구
    sudo systemctl stop gerrit
    sudo mv /opt/gerrit/opt/gerrit-old
    sudo tar-xzvf gerrit-backup.tar.gz -C/opt/
    sudo systemctl start gerrit

# 프로젝트 설계 리뷰 (사례별)

2024.01.24

최인국 컨설턴트
** email 구분이 확실하신거 봐서 경상도출신이신 것 같다.

목표 : 설계 시 생각해봐야 할 다양한 측면 (정답은 없지만 고려해보기!!!)

- 사례 1 - 데이터 타입
    
    - UINT 최대 값 42억 ← 전 세계 인터넷 인구의 74%정도, but int보다 느림
    - B Tree
    
    → 데이터 타입은 작을수록 빠르다
    
    → 사용 범위를 충분히 고려 후, 가능한 작은 크기로 결정
    
    → PK의 타입은 특히 중요함. (가급적 정수형, AUTO_INCREMENT 설정해야하기 때문)
    
    →퀴리 시 PK 우선 사용하기
    
    - email, username(id)가 PK이면 찾는데 많은 시간이 걸린다. 그리고 보안상으로도 좋지 않음
    
    ⇒ rest API 사용 시, pk로 검색하도록 하는것이 빠름!!
    

- 사례 2 - 비정규화
    
    게시글 - 댓글 (1:N)
    
    - 댓글 수 ← 댓글 count하면 알 수 있음 (없어도 무방)
    - 그럼에도 불구하고 게시글 table에 넣는다면 댓글수가 많을 때 시간이 걸리기 때문
    
    ⇒ 비정규화의 목적 : 시간 단축
    
    ```sql
    SELECT BOARD.*, COUNT(comment.id) AS comment_count FROM board
    
    LEFT OUTER JOIN comment ON board.board_id = comment.board_id
    
    GROUP BY board.board_id
    
    ORDER BY board.id desc
    
    LIMIT 10
    ```
    
    - 비정규화 하게 되면 댓글 2개인데 1개로 표시되는 경우도 생김
    - ^^ comment INSERT 된 후,  board 테이블 update하지 않으면 값이 바뀌지 않기 때문!
    
    ---
    
    - DATA가 많아지면, JOIN이 많아져 느려질 거라고 예상
    - 비정규화는 공짜가 아님! **기술 부채**임
    - 성능 높이는 대신 문제가 발생할 여지를 남김 → **유지 보수 비용 증가 + QA팀에 시달림**
    - **미리 비정규화 자제** → 운영하다가 느려지면 판단 (HW 업그레이드 등의 선택지가 있음!)
    - SELECT COUNT(*)는 느리지 않음 (캐시 있으면 더 빨라짐)
    - ! **SW 개발은 최소비용이 원칙**임을 유의하자


    ### 240202 AIoT의 현재와 미래(고성현 컨설턴트)

- 유비쿼터스
    - 언제 어디에나 존재한다는 뜻의 라틴어
    - 사용자가 컴퓨터나 네트워크를 의식하지 않고 장소에 상관없이 자유롭게 네트워크에 접속할 수 있는 환경
    - 어떤 기기나 사물에 컴퓨터를 집어넣어 커뮤니케이션이 가능하도록 해주는 정보기술 패러다임을 뜻함
    - 사물 인터넷(IoT)의 기술적 토대 역할

- 사물인터넷(IoT)
    - 각종 사물에 센서와 통신 기술을 내장하여 무선 통신을 통해 각종 사물을 연결하는 기술
    - 기존 유비쿼터스 센서 네트워크(Ubiqutuous Sensor Network, USN)와 사물과 사물간 연결을 일컫는 사물통신(Machine to Machine, M2M)에서 발전.

- AIoT가 필요하게 된 원인
    - IoT 디바이스의 증가로 처리할 데이터의 수가 폭발적으로 증가하여 지연과 정체가 발생
    - 실시간 의사 결정이 요구될 경우 큰 문제가 야기됨

- AIoT란?
    - Artificial Intelligence of Things
        - AI + IoT = AIoT
    - IoT를 통해 수집된 데이터를 인공지능 알고리즘이 분석하여 스스로 판단을 내리는 융합 기술

- IoT와 AIoT의 비교
    - 사물에서 센싱한 데이터의 수집과 데이터 처리 과정에서는 동일한 기능을 수행
    - IoT는 정의된 프로그램과 알고리즘 기반으로 정해진 명령을 수행
    - AIoT는 학습과 추론에 의한 지능형 동작을 수행한다는 것에 차이가 있음

- AIoT의 특징
    - 초연결성(Hyperconnectivity)
    - 초지능성(Hyperintelligence)
    - 초융합성(Hyperconvergence)
    - 일상 모든 것을 디지털화하고 지능적으로 연결

- 엣지 컴퓨팅 / 엣지 AI
    - 데이터를 생성하는 지점, 즉 로컬 기기나 센서에서 데이터를 처리하고 분석하는 기술
        - 부하를 막아줄 수 있다. (분산처리 가능) ⇒ 처리 쉬워짐.
    - 엣지 컴퓨팅과 AI가 결합하여 로컬에서 데이터를 처리하고 인공지능 알고리즘을 실행하는 시스템/솔루션을 엣지 AI라고 함

- 디지털 트윈
    - 컴퓨터에현실 속 사물의 쌍둥이를 만들고, 현실에서 발생할 수 있는 상황을 컴퓨터로 시뮬레이션함으로서 결과를 미리 예측하는 기술
    - 현실 시스템만으로 해결할 수 없는 현실 문제를 해결하거나 서비스를 최적화하기 위한 것

- AIoT의 미래 전략
    - 사람 개입이 최소화된 실시간 자율 대응 서비스
    - 지능 사물을 중재·조정해 임무를 수행하는 사물 중심의 자율형 IoT 플랫폼
    - 디바이스 간 자율 연결을 제공하고 응용 도메인에 최적화된 IoT 네트워크
    - 다양한 센서를 이용해 수집한 데이터를 스스로 학습·추론하고 상호 협업하여 임무를 수행하는 자율형 디바이스 ⇒ **온디바이스 AI**

- CES2024 AIoT 활용 제품
    - AIoT 로봇 집사 ‘볼리(Ballie)’ - 삼성전자
    - 사용자의 특정 근육 기능을 센서가 감지하고, 의수에 내장된 AI가 ‘미러링 과정’을 거쳐 학습해 착용자가 마음먹은 대로 움직이도록 돕는 AI 의수 ‘바이오닉암’ - 지멘스
    - 장애물과 주행로, 번호판, 차량 크기 및 무게 등을 감지한 뒤 빈자리를 찾아서 ‘알아서’ 주차해주는 로봇 ‘파키’ - 만도

- AIoT 서비스·제품 기업 편람(www.kiot.or.kr 제공)


### 240206  공통 프로젝트 배포하기(이상현 컨설턴트)

*   NGINX
    *   High perfomance load balancer, web server, API gateway & reverse proxy
    *   비동기 방식이기 때문에 매우 높은 성능
    *   정적인 파일(주로 프론트엔드 파일)을 서비스할때 뛰어난 성능(vs 톰캣)
    *   load balancer나 API gateway 용도로도 사용 가능
    *   DOS 공격 방어도 가능하다
    *   NGINX 얼마나 많이 쓰나 ⇒ 502 Bad Gateway 화면
*   배포 구조
    *   프론트엔드와 백엔드의 분기
        *   / 로 들어오는 요청을 프론트엔드의 라우터로
        *   /api 로 들어오는 요청은 백엔드로 보낸다
        *   webserver로서의 역할
        *   API gateway로서의 역할
*   Nginx validator
    *   [https://ngins.viraptor.info/](https://ngins.viraptor.info/)
    *   어디가 잘못됐는지 알 수 있다.
*   CORS
    *   Cross Origin Resource Sharing
    *   도메인, 포트, 프로토콜이 다를 때 발생한다
    *   nginx의 설정을 기억해보자!
    *   [](https://domain-a.xn--com-5k0o)[https://domain-a.com](https://domain-a.com) 의 프론트엔드 JavaScript 코드가 XMLHttpRequest를 사용하여 [https://domain-b.com/data.json](https://domain-b.com/data.json) 을 요청하는 경우
*   우리는 왜 도커를 쓰는가
    *   빠르게 필요한 서버를 증설할 수 있다.
    *   기존에는 VM을 증설하는 방식을 사용했음
    *   VM이 부팅되는 1분이면 서비스 전체가 중지되기에 충분한 시간
    *   운영체제를 부팅해야 하는 기존의 방식보다 빠름
    *   이미지를 만들어두면 찍어내기만 하면 되는 배포의 편의성(w / k8s) (Java 버전을 잘못 깔았어요. node가 이 버전이 아닌데?)
*   어디까지 도커화 해야할까?
    *   프론트엔드 / 백엔드는 필수적
    *   배포의 효율성 / 편의성 생각하기
    *   DB/Jenkins/nginx는 선택적
    *   DB를 이미지화해서 새로 배포할 일이 많이 있을까? 옮긴다면 데이터는?
    *   빌드 서버를 병렬적으로 추가 증설하는 경우는?
*   보안 이슈
    *   Docker container를 실행하게 되면 iptable에 포트를 여는 설정을 하고 실행하게 된다.
    *   UFW에 안 열었는데요?
        *   UFW로 열지 않더라도 iptable에 열려 있다면 외부로 향하는 포트는 열려 있게 된다.
    *   3306같은 위험한 포트를 여는 것에 유의하기.
*   임의의 포트를 쓰면 안 되는 이유?
    *   ISP(skt, kt, lg u+)에 따라 닫혀 있는 포트가 존재
    *   어느 곳에서는 되고, 어느 곳에서는 안 되는 서비스라면?
        *   고객은 포트가 막혔을 것이라는 생각을 하지 못하고 그냥 이탈한다.
*   Gitlab ⇒ Jenkins
    *   개발자가 gitlab의 특정 브랜치(develop or master)에 머지를 하면 이벤트가 트리거되어 jenkins에서 빌드를 시작한다.
    *   빌드가 완료되면 도커 이미지가 제작되어 배포된다.
    *   동일한 도커 이미지로 제작, 배포되기 때문에 동일성이 보장된다.
*   TLS
    *   회원가입 시에 비밀버호 등의 개인 정보가 전송되고, 수시로 유출되어서는 안되는 정보들이 오가기 때문에 암호화가 필요하다.
    *   매번 데이터를 암호화해서 전송하기 어렵기 때문에 TLS(Transport Layer Security)를 사용한다.
    *   이론적으로는 TLS를 활용한 통신은 안전하다고 볼 수 있다.
    *   WebRTC를 위해서는 SSL 인증서 설치가 필요.
*   CertBot
    *   https 확산을 위해서 시작된 비영리 푸로젝트
    *   상용 프로그램을 제작할 때는 보통 신뢰할 수 있는 ROOT 인증서 발급자로부터 SSL 인증서를 구매하여 사용한다.
    *   SSAFY 프로젝트의 경우에는 Cert Bot를 이용해서 무료 인증서를 발급받아서 사용하면 좋다.
    *   Cert Bot는 nginx에 자동으로 설정을 추가해 준다.
*   사용자 계정 만들기
    *   각 프로그램들을 실행할 때는 프로그램에 맞는 권한을 가진 사용자계정을 만들어 실행한다.
    *   ubuntu 계정이나 심지어 root 계정으로 실행하는 경우에는 해커의 공격 명령이 그 계정의 권한으로 실행되기 때문에 매우 위험하다.
    *   사용자 계정으로 실행하는 경우 해커의 공격을 받더라도 피해를 최소화할 수 있다.


### 240208 SSAFY 프로젝트와 생성형 AI 서비스(강시몬 컨설턴트)

- 다양한 생성형 AI
    - 챗GPT, bard bing 등
- 분류
    - 요청 To 결과
        - Text to Text
        - Text to Image
        - Image to Text
        - Image To Image
        - Text To Sound, Text To Music 등
    - 서비스 방식
        - API 방식
        - Open Source방식(직접 설치)
        - 그 외
- 챗GPT
    - 구분
        - Text To Text, Image to Text, Text to Image
        - API 제공(유료)
    - 개요
        - OpenAI사가 개발한 대형 언어 모델(LLM) 챗봇
        - 사용자의 질문에 따라 답변을 제공하는 서비스
        - ChatGPT 3.5는 무료, 4.0은 매월 20$ 구독
        - API 사용인 경우 월 구독요금과 별도로 과금
        - 환각 현상(Hallucination) 주의
            - 오류 등 잘못된 데이터를 학습한 결과
            - 주어진 단어를 기반으로 다음에 위치할 단어를 확률적으로 예측하는 생성형 AI 기술의 특성상 불가피하게 나타나는 것
    - 프로젝트에서 활용 사례
        - 단어 학습을 위한 예문 작성, 퀴즈 생성, 동화 생성, 장르에 따른 이야기 생성, 안내문 작성, 빠른 답변 지원, 타로풀이 생성, 목표 생성, 사용자의 독서평을 토대로 일기 작성, 상담내용 요약, 연습용 대사 작성
- Bard
    - 구분
        - Text To Text, Image To Text
        - API 제공은 아직
    - 개요
        - Google에서 개발한 대규모 언어 모델
        - GPT 아키텍처를 기반으로 구축
        - 고품질의 시, 기타 창의적인 글쓰기 형식의 자연어 생성을 위해 특별히 설계
            - 운율 및 시적 은유 감지기가 포함
        - 아직 실험버전으로 계속 업데이트가 이루어지고 있음 - 아직 무료
    - Github에 Bard API를 제공하는 여러 리포지토리가 존재하나, 공식 제공은 아님
    - 제미니어로 전면 리브랜딩한다는 기사가 나왔으나 아직은 모름.
- Stable Diffusion XL
    - 구분
        - Text To Image
        - Image To Image
        - Open Source(API는 유료로 제공하고 있음)
    - 개요
        - Stability AI에서 오픈소스 라이선스로 배포한 인공지능 모델
        - 다른 Image 생성 모델애 비해 컴퓨터 사용 리소스를 대폭 줄였음. 싸트북에서도 돌려볼만 함
        - Open Source로 공개되어 이를 기반으로 하는 AI 이미지 서비스 기능이 계속 나오고 있음
        - Text To Image뿐 아니라 원본 이미지를 입력하고 Prompt를 통해 변화된 이미지를 얻을 수 있음
        - Positive Prompt도 중요하지만 Negative Prompt를 잘 지정해 주어야 좋은 퀄리티의 결과물을 얻을 수 있음
        - 이미지 특정 부분을 지정해서 수정하는 기능도 제공(inpainting 기능)
        - Outpainting 기능도 제공
    - 프로젝트에서의 활용 실례
        - 사용자 주문 케이크 미리보기 이미지 생성, 앨범 커버 생성, 강아지 사진을 만화 형태로 변경하여 NFT로 활용
- DALL-E 3
    - 구분
        - Text To Image
        - Image To Image
        - API 제공
    - 개요
        - OpenAI에서 제작한 생성형 이미지
        - 사실적인 이미지, 오일페인팅, 디지털아트 등 다양한 스타일의 이미지를 생성
        - https://labs.openai.com/ 에서 생성된 이미지의 Prompt를 볼수 있음
        - ChatGPT API와 마찬가지로 유료로 제공됨.
        - Stable Diffusion과 마찬가지로 이미지 수정, inpainting, outpainting 기능 모두 제공됨
    - 3에서 추가된 기능
        - 한글 Prompt 기능
        - 수정 및 보완 - 생성된 이미지 중 특정 부분에 대한 수정요청 가능
        - Text 문구 추가
        - 비율 지정 - 이미지의 가로 세로 비율은 원하는 대로 지정
    - Prompt 예시
        - masterpiece = 걸작(실사 표현시 자주 쓰임), 좋은 품질의 이미지 생성 요구시
        - best quality = 최고의 퀄리티
        - realistic = 사실적인
        - ultra high res = 정말 실체와 같은 고해상도(res = Resolution의 약자)
        - dslr = DSLR로 찍은듯한
        - cinematic lighting: 디테일한 조명
        - tyndall effect: 틴들 효과
        - photorealistic: 사진처럼 리얼한
        - 4K, 8K, uhd
        - upper body = 상반신 위주 출력
        - dynamic angle = 다양한 각도
    - Negative Prompt 예시
        - nsfw(Not safe for work) 야하고 노출 심한 이미지
        - lowres 저해상도
        - bad hands 이상한 손이 안 나오게 하는 단어
        - missing fingers = bad hands처럼 손가락의 모양과 수 오류가 많음
        - fewer fingers - 손가락 수가 적은
        - strange fingers - 이상한 손가락
        - extra digit = missing fingers와 비슷한 개념, 너무 많은 손가락 제외 시
        - fewer digits = 너무 적은 손가락 제외 시
        - worst quality - 저퀄리티가 아니게 출력하기 위해
        - cropped - 이미지 안 잘리게 하기 위해
        - watermark - 워터마크 제외
        - bad anatomy - 해부학에 맞지 않는
    - Photoshop Generative Fill
        - Inpainting, Outpainting 기능
    - Deep Art Effects
        - 구분
            - Image To Image
            - API 제공(무료 Test Plan 제공)
        - 개요
            - 사진이나 이미지를 다른 미술 작품의 스타일로 바꿔주는 서비스
            - API뿐 아니라 설치용 프로그램 제공(PC, Android, IOS)
- 그 외 다양한 Image 생성 AI 서비스
    - Midjourney
        - Discord봇 명령어를 사용하여 이미지 생성(유료)
        - Prompt를 기반으로 이미지 생성
        - 이미지 생성 후 새로운 변형을 요청하여 세밀하게 조정된 이미지를 재생성
        - 현재 웹 인터페이스도 개발중
    - pokeit(포킷)
        - 오늘 컨설턴트님이 사용하심
        - 한국 스타트업의 생성형 AI
        - 장르, 스타일, 테마, 복장 등 옵션을 선택하여 이미지 생성
        - 한글로 되어 있어 사용 편함.
        - 무료, 유료 사용 가능
- Music(Sound) 생성 AI 서비스
    - AudioCraft(Audiogen, Musicgen)
        - Text To Music, Melody+Text to Autoregressive generate Model
        - Meta에서 제공하는 Open Source Audio, Music 생성 AI(당연히 무료)
        - 텍스트 설명이나 멜로디에서 힌트를 얻어 고품질 음악을 생성
        - https://audiocraft.metademolab.com
    - Stable Audio
        - Text To Music(Sound)
        - StabilityAI사에서 제작한 생성 AI
        - 무료(상업적 이용은 유료)
        - https://stableaudio.com/
- 생성형 AI 사용 우수 프로젝트
    - 8기 자율 서울 1반 A101팀(환상일기)
    - 8기 자율 부울경 2반 E205팀(ZippyZiggy)
    - 9기 자율 서울 1반 A105팀(도담바람)

### 240213 소프트웨어 테스트의 7가지 원칙 (김성준 컨설턴트)

*   소프트웨어 테스팅
    
    *   사람이 만들어 놓은 소프트웨어를 테스트하는 작업
    *   하드웨어 테스트와는 접근이 달라야 함

|하드웨어 테스트|소프트웨어 테스트 |
| :---: |:---: |
| 기계가 만들어 놓은 것을 테스트 | 사람이 만들어 놓은 것을 테스트 |
| 수정사항 발생시 수정이 매우 어려움 | 수정사항 발생시 수정이 쉬움 |
| 제작 과정에서 요구사항 변경이 어려움 | 제작과정에서 요구사항 변경이 빈번함 |
| 오류 발견이 상대적으로 쉬움 | 오류 발견이 상대적으로 어려움 |
    
- SW테스팅 7가지 원칙
    1. 테스팅은 결함이 존재함을 밝히는 활동이다.
        - 테스팅을 통해 결함이 없어졌다고 해도 완벽한 소프트웨어라고 말할 수 없다. 릴리즈 이후에도 오류 발생에 대비가 필요.
    2. 완벽한 테스팅은 불가능하다
        - 모든 테스트 케이스를 완벽하게 수행하는 것은 비용관점에서 매우 어렵습니다. 효율적으로 테스트할 수 있는 전략이 필요합니다.
    3. 개발 초기에 테스트하라
        - 통합, 릴리즈 직후에 진행되는 디버깅은 범위가 커져 매우 어렵습니다. 통합 이전에 범위가 작을 때 테스트 및 디버깅을 한다면 이런 수고를 미연에 방지할 수 있습니다.
    4. 결함은 집중된다
        - 결함은 사람, 환경, 모듈 등 여러가지 원인으로 발생할 수 있습니다. 그 원인을 중심으로 결함은 몰려 발생하는 성향이 있습니다.
    5. 살충제 패러독스(=살충제 내성)
        - 동일한 테스트 케이스를 오래 쓰면 개발자들은 내성이 생겨버립니다. 환경, 시간에 맞게 변경하는 작업이 필요합니다.
    6. 테스팅은 정황 의존적이다
        - 상황에 따라 동일한 대상도 테스트 범위가 달라집니다. 정황에 대한 파악 작업이 중요합니다.
    7. 오류 부재의 궤변
        - Verification과 Validation은 다르다
            - Verification: 분석 체크
            - Validation: 고객 요구

###  240215 공통 프로젝트 발표회 팁(이태희 컨설턴트)
- 세줄 요약
    - 모든걸 보여주려고 하면 어렵습니다. 우리 프로젝트의 핵심 가치를 잘 전달해 주세요.
    - 발표 내용을 외우는 것은 당연합니다. 읽지 말고 프로젝트를 전달해주세요.
    - 오프라인, 온라인 별로 특장점이 있습니다. 발표 환경을 최대한 활용해 주세요.
- 팀의 최종 산출물 보고
    - 6주간 프로젝트 과정 ⇒ 팀 구성, 아이디어 도출, 설계, 개발..
    - 발표 시간은 최대 15분
    - 어떻게 이 과정을 잘 전달할 수 있을까?
- 잘하는 발표는 어떻게 할까? = 3요소를 고려해야
    - Where
        - 대화를 어디에서 하는가?
        - 격식? 단 둘이 있는 장소? 사람이 많은 곳? 운동장?
        - 같은 이야기를 전달하더라도 장소에 따라서 내용이 다르게 느껴질 수 있다.
    - Who(가장 중요!!!)
        - 대화를 누구랑 하는가
        - 개인(편안한, 처음보는, 친해져가는 사이가 나쁜), 단체(친구들, 가족, 그룹, 직장상사) ?
        - 음식 맛이 별로에요라는 이야기를 쉐프한테 할 때랑 엄마한테 할 때랑 반응이 다르다
        - 같은 이야기를 전달하더라도 상대에 따라 반응이 다르다.
    - How
        - 어떻게 전달하고 싶은가?
            - 단순 대화, 자료를 활용한 보고용 대화, 인맥을 활용한 이벤트성 대화
            - 같은 이야기를 전달하더라도 방향에 따라서 내용이 다르게 느껴질 수 있다.
- 우리에게 가장 부족한 것
    - 초 - 중 - 고 - 대 교육과정을 거친 보고성 발표의 최종
    - 단순히 내가 원하는 것을 이야기하고 전달하기보다는 상대가 원하는 것이 무엇인가를 고민해봐야 한다
    - 상대가 원하는 형태로 내가 전달하고자 하는 것을 준비해야 한다.(빌드업)
- 발표는 누가 보는가?
    - 이해 관계자(stakeholder)
        - 평가자: 컨설턴트, 우리반 다른 교육생, 사무국, 연구팀, 부서장, 임원 등등
        - 우리가 만든 프로젝트를 잘 설명하고, 보여주어 평가자들에게 높은 점수를 얻어야 한다.
        - 6주간의 개발을 보고하는 형태의 발표를 준비하는 것이 아니라, 프로젝트를 소개하는 발표를 준비해야 한다.
- 하지 말아야 할 것
    - (A-Z)까지 프로젝트의 모든 것을 보여주기
        - 특히 로그인, 회원가입 같은 정말 기본적인 기능(CRUD)
    - 활용한 기술에 대한 디테일하고 자세한 설명
        - 스프링 시큐리티를 넣어서 어쩌고 저쩌고..
        - 기술적인 것을 전달하는 자리는 면접자리이지 프로젝트 발표 자리가 아니다!
    - 6주간 이 프로젝트를 만들기 위해 노력한 우리의 고생에 대한 넋두리
        - 전국에 있는 싸피 2학기생은 다 힘들었습니다..
- 면접은 무엇이 중심일까
    - 너는 누구랑 일하고 싶니?
    - 그럼 면접관, 개발팀 등은 어떻게 일하는 사람을 원할까?
    - 내가 같이 일하고 싶은 롤 모델을 생각해 보고, 어떻게 나를 표현해야 롤 모델처럼 보여질지 고민하자.
- 싸피 발표는 그래서 어떻게 준비해야 하는가?
    - 부울경 정소정 코치님
        - 발표 장표 구성은 통상적으로 기획 의도/배경 ⇒ 프로젝트 소개 ⇒ ucc 및 시연 ⇒ 서비스 특장점 ⇒ 기대효과 및 향후계획이 일반적이나, 팀의 사정에 따라 다르게 잡을 수 있다.
        - 청중의 집중을 잡기 위한 8초!
        - 장표 구성 팁
            - 기획 의도 및 배경
                - 왜 만들었을까?
                    - 우리는 쓸모 있는 걸 만들었어요.
                - 근거는 필수
                    - 필요성, 재미요소, 트렌드 등 어필 포인트 + 근거자료 준비
            - 장표 구성 시 유의사항
                - 리딩메시지는 간결하면서도 명확하게 작성하기
                - 슬라이드는 복잡하게 구성하지 않기
                - 한 장의 슬라이드에는 주장 한 가지, 이를 설명하는 근거 2~3가지
                - 서체의 종류, 크기를 청중 입장에서 확인하기.
            - 시연 시 주의사항
                - 사용자의 입장에서 이해하기 쉬운 흐름의 시나리오
                - 텍스트 입력이 필요하다면, 미리 준비
                - 테스트 흔적 지우기 / 데이터 준비
                - 카메라, 마이크 등을 이용한다면 사전에 테스트하고 적절히 셋팅
                - 혹시 모를 상황에 대비하여 시연을 대신할 영상 준비
            - 시연에 필요한 Tool
                - Webex
                - 삼성 플로우 (모바일과 연결 시 편리)
                    - 싸피 플립과 함께 사용해도 인식 잘 됨
                - 디스코드
                - OBS
                    - 이 두 가지는 여러 화면을 동시에 송출해야 할 때 편리하다. 화면전환도 쉬움
    - 서울캠 강준영 코치님
        - 발표를 잘 하기 위한 팁(특히 내향형에게)
            - 발표 잘하는 사람들 특징
                - 대본 x
                - 적절한 시각자료 활용
                - 여유로움
            - 연습을 어떻게(대본x)
                1. 발표처럼 말하고 대본을 적어 두기
                2. 적은 내용을 소리내어 읽으며 문장 수정
                3. 이 과정을 계속 반복
                    - 외우는건 비효울적이고 키워드를 찾게 되며 흐름을 파악할 수 있게 된다.
            - 여유로움
                - 세 방향으로 시선처리하기
            - 그 밖의 꿀팁
                - 실수를 할까 겁이 나서 너무 떨린다?
                    - 겁이 나는 것은 당연하다.
                    - 발생할 수 있는 여러 상황(돌발 상황) 미리 생각해보기
                    - 예시
                        - 대본이 생각나지 않아요.. 
                        ⇒ 특정 페이지에서 발표 시작하기
                        - 연습할 땐 됐는데 시연이 안 됩니다 
                        ⇒ 시연영상을 미리 준비
                        - 질문을 받았을 때 답변을 못할까봐 걱정이 됩니다..
                        ⇒ 예상 질문 리스트 만들기 (다른 팀과 발표자료 공유하면서 만드는 것도 좋다.)
            - 연습한 자신을 믿으세요. 
            앞이 안 보여도 생각이 안 나도 입은 연습한 대로 움직입니다.
    - 대전캠퍼스 최하영 코치님
        - 발표를 통해 해결해야 하는 세 가지 의문
            1. 그래서 저게 뭔데? 그래서 어떤 걸 하려는 건데?
            2. 그래서, 뭐가 중요한 건데?
                - 모든 것을 보여주려 하지 말자! 핵심만 보여주자.
            3. 저게 정말 되는거 맞아? (시연)
                - 어떻게 효과적으로 보여줄 수 있을까?
                - 중요 기능 중심으로 자연스럽게 다른 기능 노출시킬 수도 있고 시연을 통해 발표 분위기 자체를 바꿀 수도 있다.
        - 우수 사례 분석 - 최하영 코치님 피유
            - 슬로건
                - 서비스를 한 줄로 설명
                - 시작: 이어질 내용에 대한 기대
                - 마무리: 발표 내용에 대한 정리
            - 도입부
                - 청중의 상태 - 지쳐 있음
                하루종일 프로젝트 발표를 들었음
                특히 ssafy는 이미 청중이 피곤함
                ⇒ 따라서 청중의 집중 유도가 필요
                그래서 질문을 통해 청중과 소통함
                유머를 통해 분위기를 환기시킴
                - 기술에 대한 간단한 설명 + 기술을 사용한 효과
                ⇒ 기술은 기능을 구현하기 위해 사용한 것
            - 제스처
                - 숫자, 포인팅, 내용
            - 억양과 강세
                - 강조가 필요한 부분은 강세로 집중!
                - 지루한 발표가 되지 않도록 주의!
            - 시선과 동선
                - 움직임으로 시선을 모으고, 시선으로 소통
                ⇒ 소통하고 있다고 느낄 때 경청이 시작된다!
            - 메신저
                - 비언어적 표현
                    - 넓은 무대 활용, 제스처 시선
                - 준언어적 표현
                    - 억양, 발음, 강세

# On-Device AI의 개념과 활용
## 1. On-Device AI란 무엇일까?
- 인공지능 모델 학습(training)과 추론(inference)을 할 때는 클라우드 서버의 고성능 GPU 혹은 TPU를 사용한다.
- 대규모 데이터 센터에서 작동하는 거대언어모델로 ChatGPT가 있다. 하지만 네트워크가 없다면 동작이 안 된다는 문제가 있다. 
- `휴대폰 혹은 내 device 단에서 AI를 작동시킬 수는 없을까? ` ➡ On-device AI의 등장
- On-Device AI: 중앙의 cloud 서버가 아닌 edge 단의 device에서 인터넷 연결없이 자체적으로 AI training/inference을 수행하는 기술
- edge라는 건 뭘까? cloud서버가 중앙에 있다면, 사용자와 가장 가까운 (말단에 있는) device를 edge라고 한다.

### 📌그렇다면 On-Device AI를 왜 하는가? (On-Device AI의 장점)
- 데이터 프라이버시
  - 클라우드: 내 정보가 server side에 저장되는 불안감이 있다. 
  - On-Device AI: 기기 내부에서 사용자의 데이터를 직접적으로 이용하여 AI 모델을 실행하기 때문에 **사용자 데이터를 전송할 필요가 없다**. 
- 네트워크
  - 클라우드: AI 추론을 할 때 server로 데이터를 보내고 받아오니까 delay가 있을 수 있다. 
  - On-device AI: 사용자 데이터 전송에 따른 **네트워크 오버헤드를 줄일 수 있다**. 네트워크 연결 없이도 AI가 동작한다.
- 클라우드 운영
 - On-device AI: **클라우드 운영 비용을 절감**할 수 있고, **이산화탄소 배출량을 감소**할 수 있다. 

### 📌On-device AI와 AIOT의 차이점
- 둘은 완전히 다른 개념이다. 
- On-device AI: 디바이스에서 직접 AI 훈련과 추론을 수행한다
- AIot는 device에서 얻은 정보를 인터넷을 통해 cloud 서버로 전달하여 추론을 수행한다. 즉, **클라우드에서 연산을 해서** device에 전달하는 것이다. 

## 2. On-device AI 기술 기반 제품들
(1) 갤럭시 S24
(2) TESLA 차량의 자율주행
- 테슬라 차량에는 FSD 하드웨어가 들어가 있다. 이 컴퓨터에는 gpu도 들어있는데 training은 고성능 GPU를 사용해서 하고, inference는 device 안에 탑재된 저전력의 NPU를 사용한다. ➡ On-device
- 자율주행 기능이 있는 자동차들은 device 자체에서 연산을 하는 on-device로 완성이 되어 있다. 현대 자동차의 자율주행차도 마찬가지다.

## 3. On-device AI 기술을 싸피 팀 프로젝트에 녹여낼 수는 없을까?
(1) 오픈소스 On-device AI 프레임워크 활용하기
- NNStreamer
- NNtrainer: 디바이스 자체에서 inference 뿐만 아니라 training을 할 수 있도록 하는 프레임워크.
(2) 삼성의 One
- [One 깃허브](https://github.com/Samsung/ONE)
- NNStreamer와 NN Trainer는 C로 되어 있고, One은 C++로 되어 있다. (C와 C++는 하드웨어 성능을 끌어올릴 수 있는 언어)
- C와 C++로 모든 코딩을 전부 하는 게 아니라 속도가 필요한 부분은 C와 C++ 이걸로 개발하고, 다른 부분은 Java로 코딩할 수 있다. **JNI**를 활용하면 된다! **JNI (Java Native Interface)는 Java 프로그램이 네이티브 코드(C 또는 C++)와 상호 작용할 수 있도록 하는 프레임워크**이다. 이를 통해 Java에서 네이티브 코드를 호출하거나, 반대로 네이티브 코드에서 Java 코드를 호출할 수 있다. JNI를 사용하면 안드로이드 애플리케이션에서 Java로 작성된 고수준 기능과 C++로 작성된 성능 최적화 기능을 효과적으로 결합할 수 있다. 즉, 안드로이드에서 UI나 다른 편의 기능을 Java/Kotlin으로 개발하고, 중요한 AI 연산 작업은 C++로 개발하여 성능을 최적화할 수 있다. 또한 Android NDK 컴포넌트를 활용하여 C나 C++로 작성된 코드를 통합함으로써 전체적인 애플리케이션의 성능을 향상시킬 수 있다.
(3) ML on android with MediaPipe and TF lite
- [MediaPipe](https://developers.google.com/mediapipe/solutions/examples)을 이용해서 가볍게 모델을 만들고 적용할 수 있다. 완성이 되어 있는 모델이어서 라이브러리로 사용하면 된다!
(4) Google Coral Edge TPU
- [Coral + Teachable machine + Raspberry Pi 프로젝트](https://youtu.be/ydzJPeeMiMI?si=TjujTgfQYKSFGdC2)
- Coral은 연산을 가속화해주는 작은 칩이다. 그런데 모든 연산을 가속해주지는 않는다. CNN 계열 모델만 가속이 가능하고, RNN과 Transformer는 불가능하다.


## 4. 정리
- 인공지능은 Training과 inference 과정이 있고, 상황에 따라 Cloud 서버와 Edge Device에서 기능을 수행한다.
- Inference를 Cloud서버 없이 Edge Device에서 수행하는 AI 를 On-Device AI 라고 한다.
- On-Device AI 는 데이터 프라이버시, 네트워크 오버헤드 제거, 클라우드 비용절감의 3가지 장점을 갖고 있다.
- On-Device AI 를 적극적으로 제품을 생산하는 회사로 삼성전자, 애플, 테슬라, 현대자동차 등이 있다.
- 활용 방안: NNStreamer, NNTrainer, ONE, MediaPipe, Coral Edge TPU, Teachable Machine
- SSAFY 교육 과정에서의 팀프로젝트로 On-Device AI 기술을 경험해보자.

## 240313 데이터 과학과 머신 러닝(이승윤 컨설턴트)

*   사례 - 데이터 과학
    *   아마존의 예측배송(anticipatory shipment)
    *   카카오페이의 이상거래 탐지
    *   대선후보 캠프의 맞춤형 선거전략 수립
*   데이터 과학
    *   데이터의 분석과 활용이 개인과 조직의 새로운 힘이 되고 경쟁력이 되는 시대입니다. 데이터 사이언스는 데이터 수집, 큐레이션, 통계 분석과 기계학습 등의 다양한 기술과 지식을 활용하여 복잡한 데이터로부터 인사이트를 얻거나 지능화된 시스템을 구현하기 위한 모든 업무를 총칭합니다. (출처: 솔트룩스)
*   로드맵
    *   [https://roadmap.sh/ai-data-scientist](https://roadmap.sh/ai-data-scientist)
    *   수학, 통계학, 계량경제학, 코딩 등 → ML → DL → MLOps
*   진행 과정
    *   목표 설정
        *   어떤 데이터와 리소스가 필요하고, 어떻게 이익을 내며, 일정, 최종 산출물 정의
    *   데이터 획득
        *   사용할 데이터 존재여부(내부, 외부), 품질 정도, 접근 가능여부 파악 후 raw 데이터 확보
    *   데이터 준비
        *   데이터 정제(오류, 이상치, 결측치 등등) 및 가공(변환, 조합)
    *   데이터 탐색
        *   EDA, 데이터에 대한 깊은 이해 및 해석(변수들의 상호작용, 데이터 분포), 시각화, 단순 모델링
    *   데이터 모델링 및 구축
        *   도메인 지식, 통찰력으로 답을 찾는 과정, 모델 구축(변수선택 > 실행 > 진단을 반복)
    *   발표 및 자동화
        *   경영진 발표, 연구 보고서, 업무 수행 과정 자동화
    *   출처: 파이썬으로 배우는 데이터 과학 및 입문과 실습(위키북스)
    *   개발자 버전의 진행 과정(Python 기준)
    *   수집
        *   request BeautifulSoup, Selenium, OpenAPI, CSV, Excel, txt..
    *   처리
        *   Database, SQLAlchemy, Pandas
    *   분석
        *   Pandas, Polars, Numpy, Scipy, statsmodels, 시각화
    *   적용
        *   Scikit-learn, TF, PyTorch, FastAI
    *   스크래핑 시 규칙(robot.txt, 저작권 정보)과 예의(과도한 요청 자제)를 지키자.
*   머신러닝
    *   기계가 일일이 코드로 명시하지 않은 동작을 데이터로부터 학습하여 실행할 수 있도록 하는 알고리즘을 개발하는 연구 분야
*   전통적인 프로그래밍 vs 머신러닝
    *   전통적인 프로그래밍
        *   컴퓨터에 데이터와 규칙들을 넣어줘서 출력해줌
    *   머신러닝
        *   컴퓨터에 데이터와 출력값을 넣으면 컴퓨터가 규칙들을 찾아주는 것
*   머신러닝 주요 개념
    *   모델
        *   특정 알고리즘이 데이터의 특징을 학습한 것
    *   비용함수(손실함수)
        *   실제 값과 모델이 예측한 값 사이의 차이
    *   최적화
        *   비용함수를 최소화하기 위해 모델을 조정하는 과정
    *   샘플/특성(feature)/타겟
        *   행/열/정답
    *   파라미터
        *   모델이 학습한 데이터의 특징, 방정식의 계수, 모델의 내부 변수
    *   하이퍼파라미터
        *   모델의 학습 과정을 제어하는 외부 변수
    *   설명 가능성
        *   Interpretability/Explainability
    *   분류
        *   크게 인공지능>머신러닝>딥러닝
        *   인공지능
            *   사고나 학습 등을 인간이 가진 지적 능력을 컴퓨터를 통해 구현하는 기술
        *   머신러닝
            *   컴퓨터가 스스로 학습하여 인공지능의 성능을 향상시키는 기술 방법
        *   딥러닝
            *   인간의 뉴런과 비슷한 인공신경망 방식으로 정보를 처리
        *   머신러닝 분류
            *   지도학습
                *   회귀분석
                *   분류
            *   비지도학습
                *   군집화
                *   차원 축소
            *   강화학습
                *   준지도학습 등이 있음.
        *   학습 방식에 따른 분류
            *   배치 학습 vs 온라인 학습
            *   사례 기반 vs 모델 기반
            *   표층 학습 vs 심층 학습
    *   머신러닝의 과정
        *   목표 설정, 문제와 데이터 이해
        *   전처리(모델 입력에 알맞은 형태로 변환)
            *   특성 공학(Feature Engineering)
            *   정규화, 표준화, 인코딩, 벡터화
        *   데이터 세트 분할(훈련, 검증, 테스트)
        *   훈련 / 평가: 절대평가, 상대평가, 교차검증(Cross Validation)
        *   하이퍼파라미터 튜닝: GridSearch, RandomizedSearch
        *   배포와 실행, 모니터링
    *   문제
        *   데이터 문제
            *   부족한 데이터(샘플, 특성)
            *   특성: 무관한, 너무 많은(차원의 저주). 상관관계 높은
            *   대표성과 균형(샘플링 편향)
        *   모델 문제
            *   과대적합 vs 과소적합
            *   설명 가능성 → XAI
            *   성능(학습, 예측)
        *   사회/윤리적 문제: 편향과 차별, 사생활, 빅브라더
    *   머신 러닝 알고리즘
        *   선형 회귀
        *   SVM(지도, 분류/회귀)
            *   두 그룹을 나누는 경계선(면)을 찾자: 초평면
            *   가장 먼 직선거리 경계선(면)으로 최적화 하자 → Maximum margin
            *   손실함수 = Hinge Loss
            *   선형으로 구분이 안 되면? → 차원을 높여보자(Kemel)
            *   특징
                *   시간 복잡도 높은 편
                    *   n^2 ~ n^3, 메모리 효율은 높음
                *   수치형 자료만 + 스케일에 민감(전처리 필요성 높음)
                *   설명 가능성 낮음, 신경망(딥러닝)과 연관 높음
        *   Decision Tree(지도, 분류/회귀)
            *   특성에서 분류(분할) 기준을 찾아보자
            *   어떻게 분류할까? → 가장 효율적으로 나눌 수 있게
                *   그거 NP래요 → 근사하자
            *   손실함수: 불순도를 최대한 낮출 수 있게(Gini, 엔트로피)
            *   특징
                *   훈련 데이터에 민감, 과적합 되기 쉬움 → 규제, 교차검증, 앙상블
                *   결측치, 스케일에 둔감(전처리 필요성 낮음)
                *   범주형, 이산형 데이터도 처리
                *   설명 가능성 높음. 특성 중요도 제공. 여러 앙상블 알고리즘의 배경.
        *   K-Means(비지도, 클러스터링)
            *   거리에 따라 군집을 모음
            *   K개로 모음
            *   얼마나 잘 모였는지 이너셔(inertia), 실루엣을 사용함
            *   용도: 세분화(Segemtn), 압축(양자화), 이상치 탐지
            *   특징
                *   이상치, 스케일과 편항(샘플 수)에 민감
                *   랜덤한 성격(비결정적)
            *   다른 클러스터링 모델: (H)DBSCAN, 계층형, GMM, AutoEncoder
        *   PCA(비지도, 차원축소)
            *   특징(characteristic)을 보존하면서 특성(차원)을 줄이기
            *   분산의 방향을 특징으로 삼아 진행
            *   용도: 시각화, 모델 최적화, 특성 추출, 압축
            *   특징
                *   설명 가능성 낮음
                *   전역적인 특징을 잘 보존
                *   선형성 가정. 이상치, 스케일에 민감(전처리)
                *   속도 빠른 편
            *   다른 차원축소 모델: UMAP, t-SNE, AutoEncoder


## 데이터셋 모음 대공개

* 오늘 방송에 나온 데이터셋 모음집 입니다.
* 프로젝트에 필요한 데이터가 있을지 한번 찾아보세요!
* [여기](https://docs.google.com/spreadsheets/d/1A5z_YPNJuyvbJWaVqhnNdg3_BLbclClQbDCAjvvDX8I/edit?usp=sharing)
* 좋은 데이터셋 찾으면 공유해봅시다~~

## 240327 TDD를 통한 코드 품질 향상(김성준 컨설턴트)
*   테스트 가능한 코드의 특징
    *   Parameterize
    *   Separate Logic and Effect
*   추천 도서: [내 코드가 그렇게 이상한가요?](https://search.shopping.naver.com/book/catalog/40347874630?cat_id=50010920&frm=PBOKPRO&query=%EB%82%B4+%EC%BD%94%EB%93%9C%EA%B0%80+%EA%B7%B8%EB%A0%87%EA%B2%8C+%EC%9D%B4%EC%83%81%ED%95%9C%EA%B0%80%EC%9A%94%3F&NaPm=ct%3Dlu91muaw%7Cci%3D261aec2d5502bec3537f88babfb86b67dccee81e%7Ctr%3Dboknx%7Csn%3D95694%7Chk%3Dcbbb7884f71f1581b2cd7af74e52eccbdf1b9468)
*   아예 테스트 코드부터 먼저 만들고 거기에 맞춰 기능을 코딩하자
    *   개발 먼저 하는 방식
        *   시스템에서 time을 읽어 → 12와 비교 후 → AM, PM을 리턴
        *   테스트가 번거롭다
    *   테스트 먼저 하는 방식
        *   10:00 입력하면 AM이 리턴 → 15:20 입력하면 PM이 리턴
        *   case 1: 오전 시간이 10:00인 경우 am이 출력
        *   case 2: 오후 시간이 15:20인 경우 pm이 출력
*   테스트코드 작성 시 도움되는 것들
    *   mockMVC 사용 시 postman을 사용하지 않고도 api 테스트 가능
*   TDD의 장, 단점
    *   장점
        *   의식하지 않고 높은 테스트 커버리지 달성
        *   테스트에 대한 고민이 줄어듦(결정과 피드백의 사이가 좁아짐)
    *   단점
        *   테스트 케이스의 퀄리티에 따라 효과가 차이가 난다
        *   발상의 전환에 시간이 걸린다

## 240329 스마트 컨트랙트(고성현 컨설턴트)
- 정의
    - 계약에 필요한 요소를 코드를 통해 스스로 실행되게 하는 전산화된 거래 약속(Nick Szabo, 1994)
    - 온라인 상에서 중개자 없이 계약 집행이 가능(탈 중앙화)
    - 계약 당사자가 사전에 협의한 내용을 미리 프로그래밍해서 전자계약서 문서 안에 넣어두고, 해당 조건이 충족되면 블록체인 네트워크에서 자동적으로 계약을 집행하는 기능
- 특징
    - 탈중앙화
        - 중개자 개입 없이 계약 가능
    - 자동화
        - 코드 실행의 자동화 가능
    - 확장성
        - 프로그래밍 언어로 작성되어 확장할 수 있는 유연성을 가짐
    - 투명성(개방성)
        - 누구나 참여하고 확인 가능
    - 불변성
        - 배포하면 변경할 수 없음
    - 무신뢰
        - 서로에 대한 정보나 신뢰 없이 상호작용 할 수 있음
- 스마트 컨트랙트가 필요한 곳
    - 투명하게 거래내역 공개가 필요하며 위변조를 어렵게 할 필요성이 있는 곳
    - 중개인이 많이 필요하거나 비용이 커서 중개인 관련 비용 절감의 이익이 큰 곳
    - 거래 수수료 자체가 너무 비싸서 해당 비용에 대한 감소에 대한 니즈가 클 경우
- 라이프 사이클
    - Solidity Code → Compile(ABI Bytecode) → [Deploy(Address) → Insert(Functions, Events)]
    - [ 부터 ] 까지의 부분이 블록체인 네트워크
- 이더리움구조
    - 이더리움 계정 비교
        - 외부 소유 계정(EOA)
            - 개인 키를 가진 사람이 제어하는 계정
            - 계정을 만드는 데는 비용이 들지 않음
            - 외부 소유 계정 간의 ETH 전송, CA 호출 등 다양한 활동 가능
            - 암호화 키 쌍으로 구성: 계정 활동을 제어하는 공개 키와 개인 키
        - 계약 계정(CA)
            - 컨트랙트 코드에 의해 제어되는 계정
            - 네트워크 스토리지를 사용하기 때문에 계정 생성시 비용이 발생
            - 거래 수신에 대한 응답으로만 거래를 보낼 수 있음(스스로 동작할 수 없음)
            - 새 계약 생성 등의 작업을 실행할 수 있는 코드를 트리거할 수 있음
            - 계약 계정에는 개인 키가 없고, 대신 스마트 계약 코드의 논리에 의해 제어
- 이더리움 가상 머신(EVM)
    - Ethereum의 스마트 컨트랙트를 위한 런타임 환경
    - 스마트 컨트랙트의 배호와 Solidity 코드 실행을 처리
    - 완벽한 고립성
    - EVM에서 구동되는 코드는 네트워크, 파일 시스템, 다른 프로세스 접근 권한은 없음
    - PC: 스마트 컨트랙트 수행 시점 기록
    - 스택(Stack): 연산을 위한 데이터를 저장하고 연산을 수행하는 휘발성 공간. EVM은 스택 기반의 구조를 가지고 있으며, EVM의 모든 연산은 스택에서 이루어짐
    - 메모리(Memory): 트랜잭션 실행 중에만 유지되는 휘발성 데이터 저장소
    - 가상 ROM(Virtual ROM): 스마트 컨트랙트의 바이트코드 저장(비휘발성)
    - World State: 다른 스마트 컨트랙트 스토리지, 블록정보
    - 스토리지(Storage): 컨트랙트의 상태를 영구히 저장하는 비휘발성 저장소
- 스마트 컨트랙트 동작(등록자)
    - 구현하고자 하는 내용을 Solidity 등으로 구현
    - Solidity 코드를 컴파일하여 배포할 수 있는 Bytecode, ABI를 생성
    - 트랜잭션에 Bytecode, ABI를 담고, 해당 트랜잭션이 담긴 블록을 블록체인 네트워크에 기록
- 스마트 컨트랙트 동작(사용자)
    - 사용자는 배포된 스마트 컨트랙트 코드에 정의된 함수를 호출하는 Bytecode를 생성하고, 트랜잭션에 담아 블록체인 네트워크에 전달
    - 마이너는 유저로부터 받은 Bytecode를 배포한 스마트 컨트랙트 코드에 따라 EVM 위에서 실행
    - Gas Fee가 계산되면서 블록에 추가되고, 실행 결과가 유효한 경우 실행 결과가 State(블록체인 네트워크)에 반영
- ABI(Application Binary Interface)
    - 고수준 언어와 저수준 언어의 소통을 도와주는 인터페이스
    - 컨트랙트 함수와 매개변수들을 JSON 형식으로 나타낸 리스트
    - 컨트랙트의 객체를 만들 수 있고 컨트랙트 함수를 호출할 수 있음
- 스마트 컨트랙트 개발 환경
    - Geth
    - 가나슈(Ganache)
    - 트러플(Truffle)
    - 메타마스크(Metamask)
    - Infura
- Dapp 아키텍처
    - 스마트 컨트랙트와 프론트엔드 사용자 인터페이스를 결합한 분산 네트워크에 구축된 애플리케이션
- 스마트 컨트랙트 분석
    - 이더 스캔 사용
        - 솔리 아디티 코드(프로그래밍 소스코드), ABI(어떤 함수를 사용할 수 있는지 등이 기재되어 있음)
        - 해당 소스를 복사하여 개발 환경에서 테스트해볼 수 있음
        - 현재 사용중인 컨트랙트를 유저가 직접 사용해 볼 수 있음
        - 오너가 누군지, 백서에 기재된 대로 전체 발행량 설정이 되었는지를 확인할 수 있음
        - 오픈 AI API를 활용하여 스마트 컨트랙트의 소스 코드를 해석할 수 있음
- 기술적 한계
    - 오라클 문제
        - 스마트 컨트랙트의 경우 계약 조건이 충족되면 자동으로 계약 내용이 실행되므로 블록체인 외부에서 발생하는 이벤트나 조건에 대한 정보를 수집할 수 없으므로 외부에서 데이터를 입력해 주어야 하는데, 블록체인 외부에서 내부로 들어오는 데이터의 차이에 따라 발생하는 문제를 오라클 문제라고 함
        - 해결 방법
            - 투표를 통한 데이터 검증
            - 데이터 중앙값 선택
            - 신뢰할 수 있는 중간자
- 하이퍼레저 패브릭 특징
    - 엔터프라이즈 환경에서 사용하도록 설계된 오픈 소스 분산 원장 기술(DLT) 플랫폼
        - 공개형이 아닌 허가형 블록체인(폐쇄형/기업형 블록체인)
        - 모듈형 구조를 가져서 다양한 네트워크 구성이 가능
        - 암호화폐 기반이 아님
        - 일반 프로그래밍 언어를 사용(Java, Go 및 Node.js 등)
        - 멀티 블록체인 지원
        - 거래를 병렬적으로 처리해 성능(Performance)이 좋음
    - 체인코드(스마트 컨트랙트와 같은 의미)로 패키징되어 블록체인 네트워크에 배포됨
    - 실행 순서 검증이라고 하는 트랜잭션을 위한 새로운 아키텍처 도입
- 하이퍼레저 패브릭 흐름
    - 트랜잭션의 흐름을 세 단계로 분리하여 주문 실행 모델이 직면한 탄력성, 유연성, 확장성, 성능 및 기밀성 문제를 해결
        - 거래를 실행하고 그 정확성을 확인하여 승인
        - (플러그형) 합의 프로토콜을 통해 거래를 주문
        - 원장에 커밋하기 전에 애플리케이션별 보증 정책에 따라 트랜잭션을 검증
- 코다 R3
    - 세계 최대 블록체인 컨소시엄으로 자체 개발한 블록체인 플랫폼을 기반으로 금융뷴야에 블록체인 기술 적용을 주도하고 있음
    - 암호화폐 또는 기본 제공 토큰을 가지지 않으며 승인된 참가자만 전체 네트워크가 아닌 데이터에 액세스 할 수 있도록 허용

    
## 240320 한국어 데이터 전처리(최호근 컨설턴트)
- 요약
    - 한국어 전처리하는데 어떤 방법들이 있는지, 예외가 발생하는 이유에 대한 이해가 있어야 분석의 정확도를 높일 수 있다.
- 자연어 처리(NLP)란 무엇인가?
    - 사람이 이해하는 자연어를 컴퓨터가 이해할 수 있는 값으로 변환하는 과정
    - 컴퓨터가 이해하는 값을 사람이 이해할 수 있도록 다시 바꾸는 과정까지 포함
- 한국어 자연어 처리가 어려운 이유
    - 모호성(Ambuiguity)
- 언어의 종류
    - 교착어
        - 어간과 어미가 명백하게 분리됨.
        - 하나의 형태소는 하나의 문법적인 기능을 함.
        - 한국어, 일본어, 터키어, 핀란드어, 헝가리어..
    - 고립어
        - 문법적인 형태를 나타내는 어미가 거의 없고 어순과 위치만으로 문법적인 형태를 나타냄
        - 중국어, 태국어, 미얀마어, 티벳어
    - 굴절어
        - 단어의 활용 형태가 단어 자체의 변형으로 나타나는 언어로 어간과 접사가 쉽게 분리되지 않음
        - 어휘 자체에 격, 품사 등을 나타내는 요소가 포함됨
        - 인도어, 유럽어, 러시아어
    - 영어는?
        - 단어적으로 보면 굴절어 요소가 남아 있지만 문장으로 보면 고립어
- 한국어 자연어 처리가 어려운 이유
    - 띄어쓰기가 지켜지지 않는다
    - 한국어는 교착어이다
        - ‘그’라는 단어 하나에도 ‘그가’, ‘그를’, ‘그와’, ‘그는’ 과 같이 다양한 조사가 ‘그’라는 글자 뒤에 띄어쓰기 없이 바로 붙게 됨.
        - 같은 단어임에도 서로 다른 조사가 붙어서 다른 단어로 인식이 되면 자연어 처리가 힘들고 번거로워지는 경우가 많음. 어간에 접사가 붙어, 단어를 이루고 의미와 문법적 기능이 정해짐
    - 같은 정보를 다르게 표현하기(Paraphrase)
        - 문장의 표현 방식이 다양, 비슷한 단어들이 존재
- 한국어 전처리는 왜 필요한가?
    - 한글로 된 데이터를 크롤링 또는 오픈 데이터를 가져다 쓰려고 할 때 띄어쓰기 맞춤법 등이 틀린 것들도 많다(한글의 맞춤법을 잘 지키지 않는 SNS 피드 데이터 등)
    - 사소한 차이는 임베딩 데이터로 보면 큰 차이일 수 있다.
    - 정제하지 않은 데이터와 정제된 데이터는 분석 결과에서 많은 차이를 보인다.
    - 비표준어, 맞춤법 무시, 특수문자, 이모지 등이 섞여 있음(커여워 등)
    - 부정의 부정, 모호한 표현, 채널의 분리 필요
- 워드 임베딩
    - 단어를 벡터로 표현하는 방법으로 단어를 밀집 표현으로 변환
    - 밀집 벡터를 워드 임베딩 과정을 통해 나온 결과라고 하여 임베딩 벡터(embedding vector)라고도 함
    - 워드 임베딩 방법론으로 LSA, Word2Vec, FastText, Glove 등이 있음
- 전처리 방법
    - Basic, Tokenize, Spell check, Pos Tag, Stemming, Stopwords, Replacing and Correcting words
    - Basic
        - 기초적인 전처리
        - html tag 제거(크롤링한 html 원문 데이터인 경우)
        - 숫자, 영어, 특수문자 등 필요하지 않은 언어 제거
        - Lowercasting
        - “@%*=()/+ 와 같은 punctuation(문장부호) 제거
        - Emoji 및 BMP(유니코드에서 Basic Multilingual Plane(기본 다국어 평면)) 제거
    - Tokenize
        - 자연어 처리에서는 텍스트를 토큰 단위로 나눈다. 특히 한국어에서는 띄어쓰기는 문맥과 의미를 구분하는데 큰 영향
        - 애초에 모든 공백을 없앤 후, 문맥에 따라 띄어쓴 문장을 만드는 것이 좋은 방법
        - ex) 너무 기대를 안했나봐(원문) → 너무기대를안했나봐(공백 없애기) → 너무 기대를 안 했나 봐(토큰 단위 구부)
        - 띄어쓰기 방식
            - 경계인식 방식
                - 머신러닝을 이용한 문장 경계인식(다중 클래스 분류 모델, 다중 손실을 이용한 공동 학습모델)
            - 영역 인식 방식
                - 띄어쓰는 지점 주변 토큰의 영향을 고르게 받음
                - 문장 분리의 경우 형태로 분석으로 종결어미를 구분, 문장의 CRF(Conditional Random Field) 결과로 판단하는 방법 등
                - 한국어 문장분리 파이썬 라이브러리 kss, kiwi, koala, Baseline
                - 정확도는 약간의 편차들이 있음
                - 정확도는 중요하나 대량 데이터 처리시 속도도 고려해야 함
    - Pos Tag(품사 태깅)
        - 품사를 붙이는 행위를 PoS(Part of Speech, 품사) Tagging이라고 한다.
        - 형태소 분석은 의미있는 가장 작은 단위의 말(형태소)을 분석한다라는 뜻
        - Pos Tagging 즉 품사 태깅 행위를 현업에서는 구부없이 동의어로 상당히 자주 사용함
        - 형태소 분석은 말 그대로 형태소를 분석하는 모든 행위(어근, 접두사/접미사 등 속성 구조 파악까지)를 하지만 품사 태깅은 형태소의 품사를 붙이는 역할까지만 함
        - konlpy의 형태소 분석기(komoran, hannanum, kkma, okt, mecab) 및 Khaiii 등 여러가지 분석기가 나와 있으며 컨텐츠에 따른 정확도를 확인하여 선택
        - 영어눈 NLTK(Natural Language Toolkit)는 자연어 처리 및 문서 분석용 파이썬 패키지 많이 사용
        - 품사가 제대로 태깅되어야 양질의 분석이 가능하다.
        - 최근의 ELMo와 BERT 같은 Contextualized Word Embedding 방법에서는 단어 주변의 문맥 정보를 전체적으로 사용하기 때문에, 주요 품사만 사용하는 방법은 효과가 안 좋을 수 있다.
    - Stemming(어간 추출)
        - 주어진 단어에서 핵심 의미를 담고 있는 부분을 찾는 과정
        - 단어를 의미를 담고 있는 어간(stem)과 문법적 역할을 하는 접사(affix)를 분리하는 방식으로 동작
        - 동사를 원형으로 복원한다. (입니다 → 이다로 바꾸어 줌)
    - Lemmatisation(표제어)
        - 주어진 단어의 사전적 어원(기본 사전형 단어를 찾는 과정)
        - caring → care | am, are, is → be
    - Stopwords(불용어 처리)
        - 갖고 있는 데이터에서 유의미한 단어 토큰만을 선별하기 위해서 큰 의미가 없는 단어 토큰을 제거하는 작업
    - 한국어 전처리 패키지
        - PyKoSpacing: 띄어쓰기 교정
        - Py-Hanspell: 네이버 한글 맞춤법 검사기
        - SOYNLP: 품사 태깅, 단어 토큰화를 지원하는 단어 토크나이저
        - Customized KoNLPy: 영어는 띄어쓰기만 해도 단어가 잘 분리되나 한국어는 경우가 다르다. 형태소 분석기를 사용할 때 이러한 상황을 극복하기 위해 하나의 해결책으로써 형태소 분석기에 사용자 사전을 추가
        - 특정 도메인 업종, 특수 명칭 등을 사용하는 텍스트 분석에 유용
    - 실무에서 한국어 전처리
        - 기존에 나와 있는 라이브러리를 100% 활용하지는 않음
        - 내부에서 사용하는 용어, 동의어, 불용어 사전을 함께 운용해서 반영함
        - 신조어도 주기적으로 반영
        - AI 기반 확률적 전처리 방법에는 예외가 종종 발생하여 대량의 데이터 처리 시 발생하는 처리 속도 문제도 있음.


  ## 240416 알아 두면 쓸모 있는 데이터베이스 객체 1 (강시몬 컨설턴트)
- Relation DBMS
    - MySQL, MariaDB, Oracle(유료) PostgreSQL, Microsoft SQL Server(유료)
    - 최근에는 HeidiSQL이나 DBeaver 같은 프로그램을 많이 씀.
        - 다른 DBMS에서 쓰던 설정 그대로 가져다 쓸 수 있음
- 실습 시나리오
    - 현 상태: MySQL 기본 설치, root 사용자로 외부에서 접근 가능
    - 회원 정보는 한글사용자, 영문사용자로 나눠서 관리
    - 회원정보 변경시 LOG 테이블에 변경 내역 저장
    - 회원정보 조회시 회원이 작성한 글 수를 함께 보여줘야 함
    - 작성한 글 조회시 항상 작성자 아이디, 이름 함께 보여줘야 함
- Schema? Database?
    - 인스턴스: DBMS가 동작할 때의 단위, OS 입장에서는 ‘프로세스’
    - Database: 물리적으로 구분된 데이터베이스(스키마의 집합)
        - 다른 데이터베이스에 접근할 수 없음
    - Schema: 데이터베이스의 구조와 제약 조건을 정의한 것
        - 접근 제한 등 권한 관리가 가능
 - MySQL은 인스턴스 - 스키마 - 테이블 순으로, 오라클은 인스턴스 - 데이터베이스 - 스키마 - 테이블 순으로 구조화되어있음
- 데이터베이스 생성(MySQL)
    - `CREATE SCHEMA SSAFY DEFAULT CHARACTER SET UTF8;` 혹은 `CREATE DATABASE FREE DEFAULT CHARACTER SET UTF8;`
- 테이블
    - 데이터를 담고 있는 객체
    - 행(Row)과 열(Column)로 구성된 2차원 행태(표)의 객체
    - DBMS의 모든 데이터는 테이블로 관리
    - `'USER_EMAIL' VARCHAR(200) DEFAULT NULL COMMENT '사용자 이메일'` 처럼 `COMMENT`를 꼼꼼하게 달라고 추천함.
        - erd를 굳이 열어보지 않게끔 할 수 있어서 추천 :)
    - 비밀번호는 `VARCHAR(64)`로 설정했는데 해싱의 편의를 위함.
- Constraint
    - 제약조건
    - 데이터의 **무결성**을 지키기 위해 제한된 조건(성능과는 상관이 없음)
    - NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, DEFAULT 등
    - `CREATE TABLE 테이블이름 ( 필드이름 필드타입, ..., [CONSTRAINT 제약조건이름] PRIMARY KEY ... )` 이런 식으로 작업하는데 대괄호는 생략 가능
- Sequence
    - 시퀀스는 자동 순번을 반환하는 데이터베이스 객체
    - MySQL에서는 지원하지 않음(Oracle, Postgresql, MS-SQL 등에서 지원)
    - `SEQ_USER.nextval`, `SEQ_USER.currval`, `SEQ_USER.setval` 등으로 사용
    - `INCREMENT BY  증감숫자`, `START WITH 시작숫자`, `NOMINVALUE | MINVALUE` ⇒ 최소값, `NOMAXVALUE | MAXVALUE` ⇒ 최대값, `NOCYCLE | CYCLE`, `NOCACHE | CACHE`
- 함수(Function)
    - 우리가 알고 있는 바로 그 함수
    - Return 값 필수(void가 없다!)
    - Return 값은 하나
    - `CREATE FUNCTION '함수명' (파라미터) RETURNS 반환할 데이터타입 BEGIN 수행할 쿼리 RETURN 반환할 값  END`
    - **DELIMITER**
        - 구분자
        - 정상적인 로직들을 만들기 위해 필요함.
        - Delimiter 명령어 뒤에 구문 문자로 사용하고자 하는 문자를 넣어주면 된다.
    - 기본 함수
        - `sha2`, `min`, `max` 등

# 프로젝트 회고 By 김민정 컨설턴트님

## 회고

- 프로젝트 기간 동안 진행한 태스크에 대해 돌아보면서 문제점/잘한점 찾기
- 좋은 점 기억, 아쉬웠던 점 되돌아보면서 개선

## 회고 목적

- 과거 돌아보고, 이제 무성ㅅ을 해야할까 생각하는 것이 핵심
- Action Item을 생각해서 점점 나은 방향으로 가는 것

### 1. 맺음

맺음으로 추진력 얻는다

- 해온 프로젝트 돌아볼 수 있도록 마침표 찍는데 도움
- 마침표 찍으므로써, 회고는 다시 시작하고 복기할 수 있는 기회 제공
- 맺음을 새롭게 시작할 수 있는 돟력 제공, 지난 것에 대한 평가 가능하게

### 2. 나의 상태 확인

목표를 세울 때, 지금의 나를 확인해야 자신의 성장을 파악하기 쉬움

- 목표하는 것이 무엇인지 재확인
- 우리가 한 일들이 목표 부합하는지 확인
- 앞으로 어떤 일을 해야 목표를 달성할 수 있는지 확인

### 3. 행동 명확성

Action item을 만들고, 실제 수행 여부 다음 회고에서 확인

- 우리가 어떻게 업무 해야하는 지
- 어떤 행동을 통해 개선할 수 있을지
- 지속적으로 행하지 못했던 것은 무엇이 있는지

### Action Item은 어떻게 관리

- 무엇: 회고에서 합의된 **해야 할 일**들을 정리
- 누가: 진행해야 하는 **담당자**를 지정
- 언제까지: **마감 기한** 지정

→ 주기적으로 **진행사항 추적** (진행중/완료/지연)

## 바람직한 회고의 방식

회고는 서로 불만을 이야기 하는 자리가 아닌 이슈나, 불편한 점과 비효율점을 팀원들과 공유하고 해결하기 위한 방안 고민하는 시간되어야 함

### 1. 사람이 아닌 이슈에 집중

문제점을 이야기할 때는 사람보다 이슈에 초점을 맞춰 설명하기

### 2. 포장할 필요는 없음

- 문제점을 이야기할 때 상대방을 배려하기 위해 잘 포장해서 표현하면 문제를 정확하게 설명하지 못하는 경우가 발생
- 문제가 있다면, 사실 기반으로 정확하게 팩트를 공유하는게 효율적

### 3. 적극적으로 참여

- 팀 구성원이 많은 경우 특정인 위주로 회고 진행되는 경우가 종종 있음
- 회고는 함께하는 팀원이 모두 참여하는게 큰 의미가 있으므로 모든 구성원들이 참여할 수 있도록 진행자가 유도 (진행자 바꿔보기)

### 4. 실천이 중요

- 열심히 회고하고 결정된 사항을 실천하려는 노력이 필요
- 실천이 어려운 점을 다음 회고에서 논의하고 실천할 수 있는 방법 고민

## 회고의 방법론

- KPT: 3가지 관점(Keep, Problem, Try)으로 분류하여 진행하는 것이 핵심
- 짧은 시간에 **모든 구성원**의 생각을 공유하고 실행 가능한 **Action Item** 도출

### KPT 회고

- Keep
    - 좋았던 점을 기반으로 앞으로 프로젝트 진행할 때 계속 유지해야 할 사항
    - 잘하고 있는 우리의 태도나 액션이 무엇인지 고민
    - 예시
        - 컨벤션을 상세화해서 가독성을 높인 것
        - 자신과 다른 의견도 잘 들어줌
        - 트러블 슈팅한 것을 노션에 상세히 정리한 것
        - 서로 생각하는 그림이 같은지 계속확인하는 과정이 좋았음
        - 데일리 스크럼에서 자신의 이슈 상황을 투명하게 공유하고 문제 해결에 초점을 둔 계획을 수립함,
        - 서로의 코드를 리뷰해줬던 과정, 하드코딩 대신 로직을 모듈화해서 재사용성 높인 것
- Problem
    - 아쉬웠던 점을 아픙로 프로젝트를 진행할 때 개선해야 할 문제 저으이
    - 각각의 사건이나 이벤트에 집중하는 것이 아니라 “과정”을 나누는 것을 강조
    - 예시
        - 시간의 부족으로 같은 프로젝트 안에서 자신의 영역 외에는 잘 모르고 지나친 것
        - 기능 구현을 위해 튜토리얼에 찾은 코드를 복붙만 해서 이해도가 낮아 문제 해결 능력 부족
        - 상호 소통이 필요한 개발 부분이 문서화가 아닌 말로만 이루어지고 있음
        - 스크럼 시 Agenda를 명확하게 정하지 않아 회의가 산으로 가는 경우가 있음
        - Commit 메시지를 모호하게 잓겅해서 히스토리 파악 난해
        - 마감일의 부재는 미루는 습관을 만듦
        - 각 팀원들의 진척도 파악이 어려워 프로젝트 관리가 잘되지 않음
- Try
    - 회고 이후의 Action Item을 구체화하는 것이 핵심
    - 이번 회고가 끝난 직후, 팀의 역량을 실행 가능한 것으로 할 것
    - 예시
        - 각 기능별 개발일정을 계확하고 관리하기
        - 최고 기능 단위로 Commit하고, Commit 메시지 직관적으로 작성
        - 그날 그날의 트러블 슈팅 기록
        - 회의의 안건과 긑나는 시간을 명확히 정하고 회의 내용을 요약 정리 후 끝내기
        - 개발 전 코딩 컨벤션 정하기
        - 이슈를 세분화해서 할당하고, 진행 상황 공유
        - 기능 구현에서 어려운 부분이 있으면 빠른 시간 내에 도움 요청하기

### 회고 마무리할 때

- 결정된 사항 다 같이 확인하고, 합의하는 시간 꼭 갖기
- 결정된 Action Item은 담당자와 구체적인 실행 방안 및 기한 함께 기록
- 해당 내용을 포함한 회의록을 참석자 모두에게 공유
- Actio Item에 주기적인 Remind 잊지 않기

## 회고의 핵심

나와 팀의 지속적인 성장!

## 240329 스마트 컨트랙트(고성현 컨설턴트)
- 정의
    - 계약에 필요한 요소를 코드를 통해 스스로 실행되게 하는 전산화된 거래 약속(Nick Szabo, 1994)
    - 온라인 상에서 중개자 없이 계약 집행이 가능(탈 중앙화)
    - 계약 당사자가 사전에 협의한 내용을 미리 프로그래밍해서 전자계약서 문서 안에 넣어두고, 해당 조건이 충족되면 블록체인 네트워크에서 자동적으로 계약을 집행하는 기능
- 특징
    - 탈중앙화
        - 중개자 개입 없이 계약 가능
    - 자동화
        - 코드 실행의 자동화 가능
    - 확장성
        - 프로그래밍 언어로 작성되어 확장할 수 있는 유연성을 가짐
    - 투명성(개방성)
        - 누구나 참여하고 확인 가능
    - 불변성
        - 배포하면 변경할 수 없음
    - 무신뢰
        - 서로에 대한 정보나 신뢰 없이 상호작용 할 수 있음
- 스마트 컨트랙트가 필요한 곳
    - 투명하게 거래내역 공개가 필요하며 위변조를 어렵게 할 필요성이 있는 곳
    - 중개인이 많이 필요하거나 비용이 커서 중개인 관련 비용 절감의 이익이 큰 곳
    - 거래 수수료 자체가 너무 비싸서 해당 비용에 대한 감소에 대한 니즈가 클 경우
- 라이프 사이클
    - Solidity Code → Compile(ABI Bytecode) → [Deploy(Address) → Insert(Functions, Events)]
    - [ 부터 ] 까지의 부분이 블록체인 네트워크
- 이더리움구조
    - 이더리움 계정 비교
        - 외부 소유 계정(EOA)
            - 개인 키를 가진 사람이 제어하는 계정
            - 계정을 만드는 데는 비용이 들지 않음
            - 외부 소유 계정 간의 ETH 전송, CA 호출 등 다양한 활동 가능
            - 암호화 키 쌍으로 구성: 계정 활동을 제어하는 공개 키와 개인 키
        - 계약 계정(CA)
            - 컨트랙트 코드에 의해 제어되는 계정
            - 네트워크 스토리지를 사용하기 때문에 계정 생성시 비용이 발생
            - 거래 수신에 대한 응답으로만 거래를 보낼 수 있음(스스로 동작할 수 없음)
            - 새 계약 생성 등의 작업을 실행할 수 있는 코드를 트리거할 수 있음
            - 계약 계정에는 개인 키가 없고, 대신 스마트 계약 코드의 논리에 의해 제어
- 이더리움 가상 머신(EVM)
    - Ethereum의 스마트 컨트랙트를 위한 런타임 환경
    - 스마트 컨트랙트의 배호와 Solidity 코드 실행을 처리
    - 완벽한 고립성
    - EVM에서 구동되는 코드는 네트워크, 파일 시스템, 다른 프로세스 접근 권한은 없음
    - PC: 스마트 컨트랙트 수행 시점 기록
    - 스택(Stack): 연산을 위한 데이터를 저장하고 연산을 수행하는 휘발성 공간. EVM은 스택 기반의 구조를 가지고 있으며, EVM의 모든 연산은 스택에서 이루어짐
    - 메모리(Memory): 트랜잭션 실행 중에만 유지되는 휘발성 데이터 저장소
    - 가상 ROM(Virtual ROM): 스마트 컨트랙트의 바이트코드 저장(비휘발성)
    - World State: 다른 스마트 컨트랙트 스토리지, 블록정보
    - 스토리지(Storage): 컨트랙트의 상태를 영구히 저장하는 비휘발성 저장소
- 스마트 컨트랙트 동작(등록자)
    - 구현하고자 하는 내용을 Solidity 등으로 구현
    - Solidity 코드를 컴파일하여 배포할 수 있는 Bytecode, ABI를 생성
    - 트랜잭션에 Bytecode, ABI를 담고, 해당 트랜잭션이 담긴 블록을 블록체인 네트워크에 기록
- 스마트 컨트랙트 동작(사용자)
    - 사용자는 배포된 스마트 컨트랙트 코드에 정의된 함수를 호출하는 Bytecode를 생성하고, 트랜잭션에 담아 블록체인 네트워크에 전달
    - 마이너는 유저로부터 받은 Bytecode를 배포한 스마트 컨트랙트 코드에 따라 EVM 위에서 실행
    - Gas Fee가 계산되면서 블록에 추가되고, 실행 결과가 유효한 경우 실행 결과가 State(블록체인 네트워크)에 반영
- ABI(Application Binary Interface)
    - 고수준 언어와 저수준 언어의 소통을 도와주는 인터페이스
    - 컨트랙트 함수와 매개변수들을 JSON 형식으로 나타낸 리스트
    - 컨트랙트의 객체를 만들 수 있고 컨트랙트 함수를 호출할 수 있음
- 스마트 컨트랙트 개발 환경
    - Geth
    - 가나슈(Ganache)
    - 트러플(Truffle)
    - 메타마스크(Metamask)
    - Infura
- Dapp 아키텍처
    - 스마트 컨트랙트와 프론트엔드 사용자 인터페이스를 결합한 분산 네트워크에 구축된 애플리케이션
- 스마트 컨트랙트 분석
    - 이더 스캔 사용
        - 솔리 아디티 코드(프로그래밍 소스코드), ABI(어떤 함수를 사용할 수 있는지 등이 기재되어 있음)
        - 해당 소스를 복사하여 개발 환경에서 테스트해볼 수 있음
        - 현재 사용중인 컨트랙트를 유저가 직접 사용해 볼 수 있음
        - 오너가 누군지, 백서에 기재된 대로 전체 발행량 설정이 되었는지를 확인할 수 있음
        - 오픈 AI API를 활용하여 스마트 컨트랙트의 소스 코드를 해석할 수 있음
- 기술적 한계
    - 오라클 문제
        - 스마트 컨트랙트의 경우 계약 조건이 충족되면 자동으로 계약 내용이 실행되므로 블록체인 외부에서 발생하는 이벤트나 조건에 대한 정보를 수집할 수 없으므로 외부에서 데이터를 입력해 주어야 하는데, 블록체인 외부에서 내부로 들어오는 데이터의 차이에 따라 발생하는 문제를 오라클 문제라고 함
        - 해결 방법
            - 투표를 통한 데이터 검증
            - 데이터 중앙값 선택
            - 신뢰할 수 있는 중간자
- 하이퍼레저 패브릭 특징
    - 엔터프라이즈 환경에서 사용하도록 설계된 오픈 소스 분산 원장 기술(DLT) 플랫폼
        - 공개형이 아닌 허가형 블록체인(폐쇄형/기업형 블록체인)
        - 모듈형 구조를 가져서 다양한 네트워크 구성이 가능
        - 암호화폐 기반이 아님
        - 일반 프로그래밍 언어를 사용(Java, Go 및 Node.js 등)
        - 멀티 블록체인 지원
        - 거래를 병렬적으로 처리해 성능(Performance)이 좋음
    - 체인코드(스마트 컨트랙트와 같은 의미)로 패키징되어 블록체인 네트워크에 배포됨
    - 실행 순서 검증이라고 하는 트랜잭션을 위한 새로운 아키텍처 도입
- 하이퍼레저 패브릭 흐름
    - 트랜잭션의 흐름을 세 단계로 분리하여 주문 실행 모델이 직면한 탄력성, 유연성, 확장성, 성능 및 기밀성 문제를 해결
        - 거래를 실행하고 그 정확성을 확인하여 승인
        - (플러그형) 합의 프로토콜을 통해 거래를 주문
        - 원장에 커밋하기 전에 애플리케이션별 보증 정책에 따라 트랜잭션을 검증
- 코다 R3
    - 세계 최대 블록체인 컨소시엄으로 자체 개발한 블록체인 플랫폼을 기반으로 금융뷴야에 블록체인 기술 적용을 주도하고 있음
    - 암호화폐 또는 기본 제공 토큰을 가지지 않으며 승인된 참가자만 전체 네트워크가 아닌 데이터에 액세스 할 수 있도록 허용


## 240424 서비스 성능 및 안정성 향상을 위한 Message Queue 도입(한기철 컨설턴트)

### 메시지 큐 정의 및 이용 현황

- 정의
    - 메시지
        - 애플리케이션에서 다른 애플리케이션이 이용할 수 있도록 생성하는 데이터 패킷
    - 메시지를 전송되는 순서대로, 이용하는 애플리케이션에서 해당 메시지를 처리할 수 있는 상태가 되기까지 저장하는 것
- 활용도
    - 2022 Forbes Global 2000, 상위 100대 기업 중 90%
    - 2022 Forbes Global 2000, 상위 10대 헬스케어 기업 중 70%
    - 2022 Forbes Global 2000, 상위 10대 석유 가스 기업 중 80%
- 특징
    - 메시지 버퍼 역할을 하며 비동기적으로 전송
    - 서비스(서버)간 느슨한 결합 가능
    - 메시지의 **무손실**을 보장
    - 이기종간 메시징에도 적합
- 사용하는 이유
    - HTTP를 호출하기에는 HTTP는 꽤나 무거운 메시지 구조를 가짐(AMQP 대비 5배 이상의 크기)
    - 짧은 메시지를 빈번하게 전송한다면 명백한 낭비
- 대표적인 서비스
    - `RabbitMQ`
        - 기본 활용만으로도 많은 장점
        - 단순 사용 경험보다는 어떠한 환경에서 어떤 이유로 적용했는지에 대한 가설을 세워본 경험이 중요
        - 손쉽게 작업을 처리하는 별도 서비스의 scale-out이 가능
        - 이런 흐름을 직접 구축하려면 생각보다 고려해야 할 것들이 많음
        - 다양한 클라이언트 라이브러리 제공
        - 메시지 디스크 저장 설정 가능(옵션 설정 기능 있음)
        - 메시지 무손실(영속성) 보장
        - 고가용성을 위한 클러스터 설정 가능
        - 접근성 좋은 Web UI 제공

### 좋은 웹 API가 가져야 할 것들

- 성능, 안정(신뢰)성, 보안

### 동기 vs 비동기

- 일반적으로 코드는 순차적으로 실행
- 특정 명령어들의 모음을 별도의 작업 흐름으로 생성하여 명령 제어권을 바로 이어받을 수 있게 만든 방식이 비동기 처리 방식
- 비동기 처리 방법
    - 사용중인 프레임워크에서 처리하는 방식
        - async - `Django`, `Springboot`

### 사례 - 영상 자동 보정 웹 서비스 구현

- 상황
    - 웹 서버 한 대, WAS 한 대로 구축
    - WAS는 JAVA 언어로 구현, 자동 보정 라이브러리 역시 JAVA
    - 최대 50MB 파일 업로드
    - 50MB 파일 기준 보정 작업에 대략 10초 소요
    - **동시 요청 50개**를 수용해야 함, 그러나 현재 동시에 10개밖에 수용할 수 없음.
- 해결 방안
    - 1번 서비스가 실행되는 동일 WAS를 5대로 확장하면 해결
- 상황
    - WAS는 JAVA 언어로 구현, 자동 보정 모듈은 C++
    - OS는 각각 linux와 windows
    - 최대 50MB 업로드
    - 50MB 파일 기준 보정 작업에 대략 5초 소요
    - 한 대의 머신에서 최대 20개 파일 동시 작업 가능
    - 동시 요청 50개를 수용해야 함
    

### 사례 - 무인 주차 정산 시스템 구현

- 카카오 모빌리티
    - 입차시 카메라로 차량번호 인식
    - 요금 할인 대상 차량 여부 확인(REST API)
    - 출차시 주차 요금 자동 정산
- 행정안전부
    - 경차, 저공해 차량 여부 체크
    - 장애인, 유공자 여부 체크

```java
// 예시 코드

입차(차량번호) {
	입차ID = 입차기록생성(차량번호);
	장애인여부_RESTAPI(차량번호);
	유공자여부_RESTAPI(차량번호);
	경차여부_RESTAPI(차량번호);
	저공해여부_RESTAPI(차량번호);
	입차기록업데이트(입차ID, 할인정보);
	
	return "view"
}
```

- 그런데 실패했다. 왜?
    - REST API  평균 응답시간 4초.
    - 비동기 처리가 필요함
- 예상되는 문제점들
    - WAS 재실행, 서버 이상 등 이슈가 발생하면 예상되는 문제?
    - 실 서비스라고 가정했을 경우 이상하다고 생각되는 점은?
    - 이를 해결하기 위해 메시지 큐를 도입

### 프로젝트 하면서 고려하면 좋을 것들

- 서비스를 분리하고 관계를 맺으려 한다면 먼저 메시지 큐 활용법보다 **적합한 사용 시나리오**를 찾기 위해 노력해 보자
- 비동기 처리를 통한 성능 향상과 서비스(서버)간 느슨한 결합이 가져다주는 장점을 경험해 보자
- MSA를 고려하고 있다면 적극적/긍정적으로 고려해 보자