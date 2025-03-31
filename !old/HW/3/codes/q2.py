def binarySearch(arr, x):
    # global v
    # v = 1
    flag = 1
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
            flag = 0
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
            flag = 1
 
        # means x is present at mid
        else:
            if mid > low :
                while arr[mid] == x :
                    mid = mid -1
                    if mid == low :
                        break
            if arr[mid] == x :
                return mid
            else: return mid+1
 
    # If we reach here, then the element was not present
    # v = 0
    if flag == 0:
        return mid+1
    else : return mid

def binarySearch2(arr, x):
    # global v
    # v = 1
    flag = 1
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
            flag = 0
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
            flag = 1
 
        # means x is present at mid
        else:
            if mid < high :
                while arr[mid] == x :
                    mid = mid + 1
                    if mid == high :
                        break
            if arr[mid] == x :
                return mid+1
            else: return mid
 
    # If we reach here, then the element was not present
    # v = 0
    if flag == 0:
        return mid+1
    else : return mid  

def binarySearch3(arr, x):

    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
            flag = 0
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
            flag = 1
 
        # means x is present at mid
        else:
            return 1
 
    # If we reach here, then the element was not present
    return 0

my_list = []
q = int(input())

temp = input()
temp = temp.split(' ')
x = int(temp[1])
n = 1
my_list.append(x)


for i in range(1,q):
    temp = input()
    temp = temp.split(' ')

    if len(temp) == 3 :

        a = int(temp[1])
        b = int(temp[2])

        c = binarySearch(my_list, a)  
        d = binarySearch2(my_list, b)
        
        # print('my_list is:' ,my_list)
        # if my_list[]
        if c <= d :
            print(d-c)
        else : print (0)

    else :
               
        x = int(temp[1])

        if (temp[0] == '+'): 
            n += 1
            index = binarySearch(my_list, x)
            my_list.insert(index, x)

        else :
            if binarySearch3(my_list, x) :
                index = binarySearch(my_list, x)
                my_list.pop(index)
                n -= 1


          
        
