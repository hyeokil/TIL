# a = 1 
# b= 2
# c =3
# d = [a,b,c]
# import copy

# e = copy.deepcopy(d)
# d[0] = 2

# print(d,e)
#print(f'{1.6665525346:.4f}')

# from datetime import datetime

# now = datetime.now()
# print(now.date())

# def a(lst):
#     lst.append(10)
#     print(lst)
#     return

# s = ['a','b']
# a(s)
# print(s)

# A = {'a':10,'b':20}
# for key,value in A.items():
#     print(key,value)

# t ='Hello, ,world!'
# # n = t.replace('world', 'py')
# # print(n)

# x = 0 
# while x ==0:
#     a = int(input())
#     b = []
#     if a == -1:
#         break
#     else:
#         for i in range(1,a):
#             if a%i == 0:
#                 b.append(i)
#         if sum(b)==a :
#             print(f'{a} = 1',end='')
#             for j in range(1,len(b)):
#                 print(f' + {b[j]}',end='')
#         else:
# #             print(f'{a} is NOT perfect.')

# # T = int(input())
# # for j in range(T):
# #     A,B= map(int,input().split())
# #     if A == 1 or B ==1 :
# #         print(A*B)
# #     else:
# #         a = A
# #         lst_A= []
# #         for i in range(2,A+1):
# #             c = 0 
# #             while c == 0:
# #                 if a%i == 0:
# #                     a = a//i
# # #                     lst_A.append(i)
# # #                 else:
# # #                     c+=1
# # #         b = B
# # #         lst_B= []
# # #         for i in range(2,B+1):
# # #             c = 0 
# # #             while c == 0:
# # #                 if b%i == 0:
# # #                     b = b//i
# # #                     lst_B.append(i)
# # #                 else:
# # #                     c+=1
# # #         D = set(lst_A).union(set(lst_B))
# # #         d = list(D)
# # #         K = 1
# # #         for k in d:
# # #             K= K*k
# # #         print(d)

# # # 클래스 정의
# # class Person:
# #     # 속성(변수)
# #     blood_color = 'red'
    
# #     # 메서드
# #     # __init__ 생성자 메서드 
# #     def __init__(self,name):
# #         self.name = name
    
# #     def singing(self):
# #         return f'{self.name}가 노래합니다.'
    
# # # 인스턴스 생성
# # singer1 = Person('iu')
# # singer2 = Person('BTS')

# # # 메서드 호출
# # print(singer1.singing())
# # print(singer2.singing())

# # # 속성(변수) 사용
# # print(singer1.blood_color)
# # print(singer2.blood_color)

# # ```
# # 메서드 = 행동
# # 인스턴스.메서드
# # 클래스.메서드

# # str.upper('abc')
# # 'abc'.upper()
# # ```

# # print(list((1,2,3,4))[::-1])

# # T = int(input())
# # for i in range(1,T+1):
# #     N = int(input())
# #     lst = list(map(int,input().split()))
# #     lst_ = []
# #     score = 0
# #     for j in range(len(lst)):
# #         if j != len(lst)-1:
# #             if lst[j] > lst[j+1]:
# #                 if len(lst_)!=0:
# #                     for k in lst_:
# #                         score += (lst[j]-k)
# #             else:
# #                 lst_.append(lst[j])
# #     print(f'#{i}',score)  

# class Person:
#     def __init__(self,name):
#         self.name = name
    
        
#     def greeting(self):
#         return f'안녕, {self.name}'
        

# class Mom(Person):
#     gene = 'XX'
    
#     def __init__(self,name):
#         super().__init__(name)
        
#     def swim(self):
#         return '엄마가 수영'
    
# class Dad(Person):
#     gene = 'XY'
    
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
        
#     def walk(self):
#         return '아빠가 걷기'
    
# class FirstChild(Dad,Mom):
    
#     def __init__(self,name, age):
#         # super().__init__(name)
#         Dad.__init__(self,name,age)
        
#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
        
        

# baby1 = FirstChild('아가')
# print(baby1.cry())
# print(baby1.swim())
# print(baby1.walk())
# print(baby1.gene)

# print(FirstChild.mro())

# a = {'a':1,'b':2}
# # print(len(list(a)))
# a = [1,1,3,5,6,1]
# print(a.index(max(a)))

# a = [1,5,3,6,2,1]
# # len
# cnt=0
# for i in a:
#     cnt += 1
# # sum
# s = 0
# for i in a:
#     s+=i
    
# #min
# c_min = 10000000000
# for i in a:
#     if i < c_min:
#         c_min = i

# #max
# c_min = 10000000000
# for i in a:
#     if i < c_min:
#         c_min = i

# a = [
#     [1,2,3],
#     [3,4,5]
# ]
# for c in a[0]:
#     print(c)


# import copy

# T = int(input())
# for i in range(1,T+1):
#     N = int(input())
#     lst = list(map(int,input().split()))
#     lst_ = copy.deepcopy(lst)
#     lst_m = []
#     score = 0
#     for j in lst:
#         if j == max(lst_):
#             lst_m.append(j)
#             for k in lst_[:
            
    
#     print(f'#{i}',score)  

# T = int(input())
# for i in range(1,T+1):
#     N = int(input())
#     lst = list(map(int,input().split()))
#     score = 0
#     while lst[0]!=max(lst) :
#         for j in range(len(lst)):
#             if lst[j] == max(lst):
#                 for k in lst[:j+1]:
#                     score += (lst[j]-k)
#                     lst.remove(k)
#             break
    
#     print(f'#{i}',score) 

# T = int(input())
# for i in range(1,T+1):
#     N = int(input())
#     lst = list(map(int , input().split()))
#     score = 0
#     while len(lst) != 0:
#         c_max = max(lst)
#         now = lst.index(c_max)
#         l_n = lst[:now]
#         lst = lst[now+1:]
#         for j in range(len(l_n)):
#             score += (c_max-l_n[j])
#     print(f"#{i}",score) 

res=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
T = int(input())
for m in range(1,T+1):
    n=int(input())
    c=[n-1]*3
    for i in range(n-2,0,-1):
        for j in range(2):
            c.append(i)
    lst=[[0]*(n) for _ in range(n)]
    lst[0][0]=1
    x,y=0,0
    idx=0
    val=2
    for i in c:
        for j in range(i):
            lst[x+dx[idx]][y+dy[idx]]=val
            x+=dx[idx]
            y+=dy[idx]
            val+=1
        idx+=1
        if idx==4:
            idx=0
    print(f'#{m}')
    for i in range(n):
        print(*lst[i],sep=" ")