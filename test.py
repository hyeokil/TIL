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
# n = t.replace('world', 'py')
# print(n)

x = 0 
while x ==0:
    a = int(input())
    b = []
    if a == -1:
        break
    else:
        for i in range(1,a):
            if a%i == 0:
                b.append(i)
        if sum(b)==a :
            print(f'{a} = 1',end='')
            for j in range(1,len(b)):
                print(f' + {b[j]}',end='')
        else:
            print(f'{a} is NOT perfect.')