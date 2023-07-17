# a = 1 
# b= 2
# c =3
# d = [a,b,c]
# import copy

# e = copy.deepcopy(d)
# d[0] = 2

# print(d,e)
T = int(input())
for i in range(1,T+1):
    s = input()
    a = []
    for j in s:
        a,append(j)
    if a == list(reversed(s)):
        print(f'#{i}',1)
    else :
        print(f'#{i}',0)