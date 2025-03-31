


nq = list (map (int, input().split(' ') ) )
n , q = nq

sett , rank = [] , []
### test 
# 8 6
# 3 2 5
# 1 2 5
# 3 2 5
# 2 4 7
# 2 1 2
# 3 1 7
# n = 8 
# q = 6
import math 
for i in range (1,n+1):
    sett.append (i)
    rank.append(0)

def Find (z) : 
    # w = z
    w = [z]
    global sett 
    # if (sett[x] == x) :
    #     return x;
    # return Find(Par[x]);

    while (sett[z-1] != z) :
        z = sett[z-1]
        w.append(z)
    # print ('w is :' , w)
    for u in w :
        sett[u-1] = z
    # print ('sett is : ',sett)    
    return z
   
def Union(s,d) :
    i , j = Find(s) , Find(d)
    if i != j:
        global sett
        if rank[i-1] > rank[j-1] :
            sett[j-1] = i

        else :
            sett[i-1] = j
            if rank[i-1] == rank[j-1] :
                rank[j-1] += 1
        # print ('set after union : ', sett)

def Union_interval(l,r) :

    if l+1 < r :
        mid = l + (r - l) // 2
        # print (s)
        Union_interval(l, mid)
        Union_interval(mid+1, r)
    elif l+1 == r :
        Union(l, r)
    

    for h in range (1 , int(math.log2(n)-1)) :
        ll = l
        i = 2**h
        t = 2**(h+1)
        while ll+i < r :
            # for i in range (l, r//i):
            # print (ll, i , t)
            Union(ll , ll+i)
            ll += t
            
    # print ('Union_interval(%s,%s) is %s : ' %(l , r , sett))

    # i , j = Find(s) , Find(d)
    # if i != j:
    #     global sett
    #     if rank[i-1] > rank[j-1] :
    #         sett[j-1] = i

    #     else :
    #         sett[i-1] = j
    #         if rank[i-1] == rank[j-1] :
    #             rank[j-1] += 1
    #     # print ('set after union : ', sett)

for i in range (q) :
    opp = list (map (int, input().split(' ') ) )
    op = opp[0]
    x = opp[1]
    y = opp[2]

    if op == 1 :
        Union(x,y)
         
    elif op == 2 :
        mid = x + (y - x) // 2
        mid1= x + (mid - x) // 2
        mid2= mid + (y - mid) // 2

        for i in range (x,mid1):
            i = x
            while i != mid1 :
                i += 1
                Union(x,i)

        for i in range (mid1,mid):
            i = mid1
            while i != mid :
                i += 1
                Union(mid1,i)

        for i in range (mid,mid2):
            i = mid
            while i != mid2 :
                i += 1
                Union(mid2,i)
        
        for i in range (mid2,y+1):
            i = mid2
            while i != y :
                i += 1
                Union(mid2,i)      

        Union (x , y)
        Union (mid1 , mid)
        Union (x , mid)

        # Union_interval(x,y)


    elif op == 3 :

        if Find (x) == Find (y):
            print ('YES')
        else :
            print ('NO')