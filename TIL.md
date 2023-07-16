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
