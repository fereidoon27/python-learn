
## nm = list (map (int, input().split(' ') ) )
n = int(input())
m = int(input())
kolah_ghermezi = list (map (int, input().split(' ') ) )
pesar_khale = list (map (int, input().split(' ') ) )


###test1
# n=5
# m=6
# kolah_ghermezi = [1,2,0,8,1]
# pesar_khale = [3,6,100,1,0,5]

def binary_search2(arr, low, high, x):
    global mid
    global flag

    
    if high >= low:

        mid = (high + low) // 2
        # print('mid is :' , mid)
        if arr[mid] == x :

            if mid >0 :
                while arr[mid-1] == x:
                    mid -=1
                    if mid == 0:
                        break
                return mid

        elif arr[mid] > x:
            flag = 1
            return binary_search2(arr, low, mid - 1, x)
        else:
            flag = 0
            return binary_search2(arr, mid + 1, high, x)
        
    else:
        if flag == 1:
            return mid
        else :
          return mid+1

kolah_ghermezi.sort()
pesar_khale.sort()

sefr_p, yekha_p, do_p, se_p, char_p, sefr_k, yekha_k, do_k, se_k, char_k  = 0,0,0,0,0,0,0,0,0,0
# kk = list(filter(lambda a: a != 1, kolah_ghermezi))
# pp = list(filter(lambda a: a != 1, pesar_khale))   
for i in kolah_ghermezi: 
    if i == 0: sefr_k += 1
    if i == 1: yekha_k += 1
    if i == 2: do_k += 1
    if i == 3: se_k += 1
    if i == 4: char_k += 1    

# for i in pesar_khale: 
#     if i == 0: sefr_p += 1
#     if i == 1: yekha_p += 1
#     if i == 2: do_p += 1
#     if i == 3: se_p += 1
#     if i == 4: char_p += 1

count = 0
for i in pesar_khale:   
    if i == 0:
        count = count + n -sefr_k

    elif i == 1 :
        count = count + n -sefr_k - yekha_k

    elif i == 2 :
            # print(count)
            # count = count + binary_search2(kolah_ghermezi, 0, n-1, 2)
            count = count + (se_k) 
            # print('i=2 , count is: ' , count)
    elif i == 3 :
            # print(count)
            count = count + binary_search2(kolah_ghermezi, 0, n-1, 3)    
            count = count - (do_k) -sefr_k - yekha_k  
            # print('i=3 , count is: ' ,count) 
    elif i == 4 :
            count = count + binary_search2(kolah_ghermezi, 0, n-1, 4)    
            count = count - (do_k) -sefr_k - yekha_k
            # print('i=4 , count is: ' ,count) 

    else :   
        # print('i=%i , count is:%i ' %(i,count) )
        count = count + binary_search2(kolah_ghermezi, 0, n-1, i)
        count = count -sefr_k - yekha_k
        # print('i=%i , count is:%i ' %(i,count) )

print(count)



# yekha_p*(len(kk))
# print(pp)
# print(kk)



# def check (x,y):
#     if x**y > y**x:
#         return 1
#     else : return 0

# count = 0
# for i in kolah_ghermezi:
#     for j in pesar_khale:
#         count += check (i,j)

# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# print ("The original list is : " +  str(test_list))
  
# # using naive method
# # to remove duplicated 
# # from list 
# res = []
# for i in test_list:
#     if i not in res:
#         res.append(i)
  
# # printing list after removal 
# print ("The list after removing duplicates : " + str(res))

# # using list comprehension
# # to remove duplicated 
# # from list 
# res = []
# [res.append(x) for x in test_list if x not in res]

# X = [0,5,0,0,3,1,15,0,12]
# X = [i for i in X if i != 0]