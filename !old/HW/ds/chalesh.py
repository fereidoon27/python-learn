####test1
# n , q , a = 5 , 3 , [1, 4, 0, 1, 3]
# req1 , req2 , req3 = ['a', 1, 4, 2,] , ['b', 0, 4, 1,] , ['c', 1, 5, 2]

NQ = list(map(int , input().split(' ')))
n , q = NQ
a = list(map(int , input().split(' ')))

import heapq
from heapq import heappop
 

# Function to find the k'th smallest element in a list using min-heap
def find_kth_smallest(input, k):
 
    # base case
    if not input or len(input) < k:
        exit(-1)
 
    # transform the input list into a min-heap
    heapq.heapify(input)
 
    # pop from min-heap exactly `k-1` times
    while k > 1:
        heappop(input)
        k = k - 1
 
    # return the root of min-heap
    return input[0]

# sorted_a = sorted(a)

# for i in ([req1 , req2 , req3]):
for i in range (q):
    # temp = i
    temp = input().split(' ')
    req = temp[0]
    l = int(temp[1])
    r = int(temp[2])
    y = int(temp[3])
    # req.extend(list(map(int , temp[1:])))

    if req == 'a':
        count = 0
        # print (i, 'a')
        for j in range (l , r):
            if a[j] < y :
                count += 1
        print (count)

        
    elif req == 'b':
        # print(i, 'b')
        count = 0
        for j in range (l , r):
            if a[j] == y :
                count += 1
        print (count)        


    else :
        # print(i, 'c')
        # sub_sorted = sorted(a[l:r])
        # print (sub_sorted[y-1])
        
        # print( kthSmallest(a[l:r], len(a[l:r]), y))
        print ('45')


    