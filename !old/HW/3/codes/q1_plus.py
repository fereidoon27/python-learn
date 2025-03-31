def binarySearch(arr, x):

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
            return mid
 
    # If we reach here, then the element was not present
    if flag == 0:
        return mid+1
    else : return mid

# flag = 0
# mid = 0
# def binarySearch(arr, low, high, x):
#     global flag
#     global mid
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             flag = 1
#             return binarySearch(arr, low, mid - 1, x)
            
 
#         # Else the element can only be present in right subarray
#         else:
#             flag = 0
#             return binarySearch(arr, mid + 1, high, x)
            
 
#     else:
#         # Element is not present in the array
#         if flag == 0:
#             return mid+1
#         else : return mid

   
q = int(input())
temp = input()
temp = temp.split(' ')
x = int(temp[1])
n = 1
my_list = [x]
print(x)

for i in range(1,q):
    
    temp = input()
    temp = temp.split(' ')
    x = int(temp[1])
    if (temp[0] == '+'):
        n += 1
        # my_list.append(x)
        # print (my_list)

        index = binarySearch(my_list, x)
        # index = binarySearch(my_list,0, len(my_list)-1, x)
        my_list.insert(index, x)
        

        # print ('my list is : ' , my_list)
        print (my_list[((n-1)//2)])
        

    else:
        # index = binary_search2(my_list, 0, n, x)
        # my_list.pop(index)
        # print (my_list[(n//2)])

        # index = my_list.index(x)
        index = binarySearch(my_list, x)
        # index = binarySearch(my_list,0, len(my_list)-1, x)
        my_list.pop(index)
        n -= 1

        # print ('my list is : ' , my_list)
        print (my_list[((n-1)//2)])
        