import math

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head = None

    def search(self, x):
        current = self.head
        while (current != None):
            if (current.data[0] == x):
                current.data[1] += 1
                # print(current.data)
                return current , True
            current = current.next
        newNode = Node([x , 1]) 
        newNode.next = self.head
        self.head = newNode
        # print(newNode.data)
        return newNode , False

def hashfunc(x):
    # return ((math.floor(x) % m) + m) % m
    return int(((a * x) % (2 ** w))) >> (w - r)

n = int(input())
r = math.ceil(math.log2(n))
m = 2 ** r
w = 20
a = 2 ** 19 + 2 ** 17 + 2 ** 13
# m = int(n/4)
T = [LinkedList() for i in range (m)]
zeros = 0
max = 0

A = input().split(' ')
for i in range (n):
    A[i] = int(A[i])

B = input().split(' ')
for i in range (n):
    B[i] = int(B[i])
    if (A[i] == 0 and B[i] == 0):
        zeros += 1
    elif (A[i] != 0):
        x = ((-1)*B[i]) / A[i]
        index = hashfunc(x)
        if(T[index].head):
            t , b = T[index].search(x)
            if (t.data[1] > max):
                max = t.data[1]
        else:
            T[index].head = Node([x , 1])

print(zeros + max)