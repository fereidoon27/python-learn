# nt = list (map (int, input().split(' ') ) )
# a = list (map (int, input().split(' ') ) )
# t_list =[]
# for i in range (nt[1]):
#     t_list.append(list (map (int, input().split(' ') ) ))

# print (nt , a , t_list)


### test1


nt = [7, 3] 
n = 7
t = 3
a = [1, 2, 1, 1, 2, 2, 1] 
t_list = [[3, 4], [6, 4], [1, 1]]

def binary_search1(arr, low, high, x):
    global mid
    if high == low:
        mid = 0
        if arr[mid] >= arr[low]:
            mid = 1

    elif high >= low:
        

        mid = (high + low) // 2
        print('mid is:' , mid)
        if arr[mid] == x :
            if mid < high:
                while arr[mid+1] == x:
                        mid +=1
                        if mid >= high :
                            break
                return mid+1

        elif arr[mid] > x:
            return binary_search1(arr, low, mid - 1, x)
        else:
            return binary_search1(arr, mid + 1, high, x)
        
    else:
        return mid
def binary_search2(arr, low, high, x):
    global mid
    if high == low:
        mid = 0
        if arr[mid] > arr[low]:
            mid = 1

    elif high >= low:

        mid = (high + low) // 2
        # print('mid is:' , mid)

        if arr[mid] == x :
            while mid[mid-1] == x:
                mid -=1
                if mid == 0:
                    break
            return mid

        elif arr[mid] > x:
            return binary_search2(arr, low, mid - 1, x)
        else:
            return binary_search2(arr, mid + 1, high, x)
        
    else:
        # Element is not present in the array
        return mid
# aa = a.copy()

def cal (a , q):
    aa = sorted(a[0:q])
    bb = sorted(a[q:n])
    l =  binary_search1(aa, 0, q-1, a[q-1] )
    r = binary_search2(bb, 0, n-q-1, a[q-1])
    nahae = l + r 
    print (l, r, aa, bb, nahae)
    return nahae

# for i in range (t):
#     q = t_list[i][0]
#     w = t_list[i][1]
#     print (cal(a , q), cal(a , w))
  
print (cal(a , 1))