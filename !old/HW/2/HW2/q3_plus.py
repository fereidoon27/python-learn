# nt = list (map (int, input().split(' ') ) )
# a = list (map (int, input().split(' ') ) )
# t_list =[]
# for i in range (nt[1]):
#     t_list.append(list (map (int, input().split(' ') ) ))

# n ,t = nt [0] , nt [1]

nt = input()
nt = nt.split(' ')
n = int(nt[0])
t = int(nt[1])

a = input()
a = a.split(' ')
for i in range(n):
    a[i] = int(a[i])
t_list = []

for i in range(t):
    temp = input()
    temp = temp.split(' ')
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    t_list.append(temp)

# print (n, t)
# print(a)
# print(t_list)

# nt = [7, 3] 
# n = 7
# t = 3
# a = [1, 2, 1, 1, 2, 2, 1] 
# t_list = [[3, 4], [6, 4], [1, 1]]

sorted_a=[]
  
for i in range(n):
      sorted_a.append([a[i],i])

sorted_a.sort()

def f(x, left, right, z):
    global mid

    if (left <= right):
        mid = left + ( (right - left) // 2)

        if (sorted_a[mid][0] > a[z]):
            right = mid - 1
            f(x, left, right, z)
        if (sorted_a[mid][0] < a[z]):
            left = mid + 1
            f(x, left, right, z)
        if (sorted_a[mid][0] == a[z]):
            if (sorted_a[mid][1] < z):
                left = mid + 1
                f(x, left, right, z)
            if (sorted_a[mid][1] > z):
                right = mid - 1
                f(x, left, right, z)
            if (sorted_a[mid][1] == z):
                return mid + 1
                
for i in range (t):
    k = f(sorted_a, 0, n - 1, t_list[i][0]-1)
    kk = f(sorted_a, 0, n - 1, t_list[i][1]-1)
    string1 = str(k) + ' ' +str(kk)
    print (string1)

    # print(f(t_list[i][0]), f(t_list[i][1]))
