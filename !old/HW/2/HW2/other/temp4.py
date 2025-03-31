nt = input()
nt = nt.split(' ')
n = int(nt[0])
t = int(nt[1])

inArray = input()
inArray = inArray.split(' ')
for i in range(n):
    inArray[i] = int(inArray[i])
tArray = []

for i in range(t):
    temp = input()
    temp = temp.split(' ')
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    tArray.append(temp)

sortedList=[]
  
for i in range(n):
      sortedList.append([inArray[i],i])
sortedList.sort()

def f(x):
    left = 0
    right = n - 1
    while (left <= right):
        mid = int(left + (right - left) / 2)
        if (sortedList[mid][0] > inArray[x-1]):
            right = mid - 1
        if (sortedList[mid][0] < inArray[x-1]):
            left = mid + 1
        if (sortedList[mid][0] == inArray[x-1]):
            if (sortedList[mid][1] < x-1):
                left = mid + 1
            if (sortedList[mid][1] > x-1):
                right = mid - 1
            if (sortedList[mid][1] == x-1):
                return mid + 1
                
for i in range (t):
    print(str(f(tArray[i][0])) + ' ' + str(f(tArray[i][1])))