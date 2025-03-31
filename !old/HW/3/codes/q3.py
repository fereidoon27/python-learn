# n = 3
# a = [2, 1, 3]
# b = [4, 5, 9]

# n = 5
# a = [5, 1, 6, 2, 3]
# b = [9, 3, 1, 4, 4]

n = int(input())
a = input().split(' ')
a = list(map (int , a))

b = input().split(' ')
b = list(map (int , b))

scarry = []
for i in range (n) :
    scarry.append ([a[i] , i + 1 , b[i]]) 
scarry.sort()

i = 1
for k in range (0 , 100000) :
    if i >= len(scarry) :
        break 
    else :
        m1 , m2 = scarry[i][0] , scarry[i-1][0]
        n1 , n2 = scarry[i][2] , scarry[i-1][2]
        d1 , d2 = abs(m2-m1) , abs(n2-n1)
        if d1 > d2:
            scarry.remove(scarry[i])
        else:
            i += 1
l = len(scarry)
print(l)


