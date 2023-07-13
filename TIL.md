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
