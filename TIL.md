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