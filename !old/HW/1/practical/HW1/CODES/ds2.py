# n = int(input())
# k = int(input())
# array_in = input()
# array_in = array_in.split(' ')
# array_in = list(map(int, array_in))

# n = 4
# k = 2
# array_in = [1, 2, -1, -2]

n = 7
k = 5
array_in = [-2, -3, 4, -1, -2, 5, -3 ]



def max_finder (array_in, n):

    helper = [0]*n
    helper[0] = array_in[0]
    start = [i for i in range (n)]

    for i in range (1, n):
        if array_in[i] + helper[i-1] > array_in[i] :
            helper[i] = array_in[i] + helper[i-1]

            start [i] = start [i-1]

        else :
            helper[i] = array_in[i]

    print('array_in is : ', array_in)
    print ('helper is : ', helper)
    print ('start is : ', start)

    print (max(helper))
    z = helper.index(max(helper))
    array_in[ start[z]: z+1 ] = [float('-inf') for i in range (start[z], z+1)]
    print('array_in is : ', array_in)


for i in range (k):
    max_finder(array_in,n)  

