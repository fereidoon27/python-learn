n = int(input())
# a = input().split(' ')
# a = list(map (int , a))
# b = input().split(' ')
# b = list(map (int , b))

a = input().split(' ')
for i in range (n):
    a[i] = int(a[i])

print (a)