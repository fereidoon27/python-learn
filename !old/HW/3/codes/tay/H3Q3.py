n = int(input())
a = input().split(' ')
for i in range(n):
    a[i] = int(a[i])

b = input().split(' ')
for i in range(n):
    b[i] = int(b[i])
result = [[a[i] , i + 1 , b[i]] for i in range (n)]
result.sort()

i = 1
while (i < len(result)):
    # print('i=',i)
    diff1 = abs(result[i-1][0]-result[i][0])
    # print('diff1=',diff1)

    diff2 = abs(result[i-1][2]-result[i][2])
    # print('diff2=',diff2)

    if diff1 > diff2:
        result.remove(result[i])
        # print('removed', i)
        
        # print('i after decrement',i)
    else:
        i += 1
# print(result)
print(len(result))