
size = int(input())
right = input()
mangool = input('')

right = right.split(' ')
mangool = mangool.split(' ')

# size = 9
# right = [1, 9]
# mangool = ['a', 'a', 'a', 'b', 'b', 'b','b', 'b', 'b']



mangool2=[]
for i in range(0, size-1):
    if mangool[i] == mangool[i+1]:
        mangool2.append(1)
    else:
        mangool2.append(0)

second =int(right[1])
first =int(right[0])

sum = 0
for i in range(first+1,second-1):
    if mangool2[i] == 1:
        sum += 1
print(sum+1)


