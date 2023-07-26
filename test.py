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
# #                     lst_A.append(i)
# #                 else:
# #                     c+=1
# #         b = B
# #         lst_B= []
# #         for i in range(2,B+1):
# #             c = 0 
# #             while c == 0:
# #                 if b%i == 0:
# #                     b = b//i
# #                     lst_B.append(i)
# #                 else:
# #                     c+=1
# #         D = set(lst_A).union(set(lst_B))
# #         d = list(D)
# #         K = 1
# #         for k in d:
# #             K= K*k
# #         print(d)

# # 클래스 정의
# class Person:
#     # 속성(변수)
#     blood_color = 'red'
    
#     # 메서드
#     # __init__ 생성자 메서드 
#     def __init__(self,name):
#         self.name = name
    
#     def singing(self):
#         return f'{self.name}가 노래합니다.'
    
# # 인스턴스 생성
# singer1 = Person('iu')
# singer2 = Person('BTS')

# # 메서드 호출
# print(singer1.singing())
# print(singer2.singing())

# # 속성(변수) 사용
# print(singer1.blood_color)
# print(singer2.blood_color)

# ```
# 메서드 = 행동
# 인스턴스.메서드
# 클래스.메서드

# str.upper('abc')
# 'abc'.upper()
# ```

print(list((1,2,3,4))[::-1])