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