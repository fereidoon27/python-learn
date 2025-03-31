def swap(array, firstIndex, secondIndex):
	temp = array[firstIndex]
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = temp
s = ''
a = []
c = []
n = int(input())
result = [i for i in range (1, n+1)]

for i in range (n):
    temp = input()
    temp = temp.split(' ')
    a.append(int(temp[0]))
    c.append(int(temp[1]))

for i in range(1,n):
    j = i
    tempC = c[i]
    while (tempC > 0 and j >= 1 and a[j] > a[j-1]):
        tempC -= 1
        swap(a, j, j-1)
        swap(result, j, j-1)
        j -= 1

for i in range(n):
    s += str(result[i]) + ' '

print(s)