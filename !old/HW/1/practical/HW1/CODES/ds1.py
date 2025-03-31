n = int(input())
interval = input()
array = input()

interval = interval.split(' ')
array = array.split(' ')
helper = [0]*n

###mytest
# interval = ['10', '10']
# ## a a a b b b c c d e e
# ## ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e', 'e']
# array = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e', 'e']
# n = len(array)
# helper = [0]*n

#preprocessing
for i in range (n-1) :
    if array[i] == array[i+1] :
        helper[i] = 1

#function
def counter(l, r, helper) :
    if r == 1 | r <= l | len(helper) <= r | len(helper) <= l | r <= 0 | l <= 0 :
        return 0
    count = 0
    for i in range (l,r):
        if helper[i] == 1:
            count +=1
    return count

# print(array)
# print (helper)
print ( counter(int(interval[0]), int(interval[1]) ,helper) )
    

