import time

def merge_sort(left, right):
    i = 0
    j = 0
    myList = []
    while i < len(left) and j < len(right):
        t1 = left[i]
        t2 = right[j]
        if t1 < t2:
            myList.append(left[i])
            i += 1
        if t1 > t2:
            myList.append(right[j])
            j += 1
        if t1 == t2:
            myList.append(right[j])
            i += 1
            j += 1
    while i < len(left):
        myList.append(left[i])
        i += 1
    while j < len(right):
        myList.append(right[j])
        j += 1
    return myList

# number = int(input())
number = 500
start_time= time.perf_counter()
a = [1]
i = 0
while (len(a) <= 1.5*number):
    b = [a[i]*3, a[i]*5, a[i]*7]
    a = merge_sort(a, b)
    i += 1
print(a[number-1])
print (len(a))
# print (a)
print("time:", time.perf_counter()-start_time)