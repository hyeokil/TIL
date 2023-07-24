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
      -  1 x 1 = 1
      -  1 x 2 = 2
      -  ...
      -  9 x 8 = 72
      -  9 x 9 = 81    
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
## if a == b == c :
-     가능하다

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


