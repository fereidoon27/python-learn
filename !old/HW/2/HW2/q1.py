n = int(input())
pesar_khale = input()
kolah_ghermezi = input()
famil_door = input()

pesar_khale = pesar_khale.split(' ')
kolah_ghermezi = kolah_ghermezi.split(' ')
famil_door = famil_door.split(' ')

pesar_khale = list(map(int, pesar_khale))
kolah_ghermezi = list(map(int, kolah_ghermezi))
famil_door = list(map(int, famil_door))

## test1
# n=2
# pesar_khale = [1, 4]
# kolah_ghermezi= [3, 2]
# famil_door = [9,8]
## test2
# n=3
# pesar_khale = [1, 12, 1]
# kolah_ghermezi= [8, 35, 2]
# famil_door = [10, 9, 11]

pesar_khale.sort()
kolah_ghermezi.sort()
famil_door.sort()

pes = 0
kol = 0
fam = 0
dif_all = float('inf')
sum_all = float('inf')

def max_min (x, y, z):
    if x > y : 
        max1 , min1, pro = x, y, 2
        if z > max1 : max1 = z
        elif z < min1 : min1, pro = z, 3
        
    else : 
        max1 , min1, pro = y, x, 1
        if z > max1 : max1 = z
        elif z < min1 : min1, pro = z, 3
    dif1 = max1 - min1
    sum1 = x+ y+ z
    return [dif1, sum1, pro]

p1= p2= p3= 0
while p1 < n and p2 < n and p3 < n:
    
    d = max_min (famil_door[p1] , pesar_khale[p2] , kolah_ghermezi[p3] )
    # print(d)

    if dif_all > d[0]:
        dif_all, pes, kol, fam, sum_all = d[0], p1, p2, p3, d[1]          
    elif dif_all == d[0]:
        if d[1] < sum_all:
            pes, kol, fam, sum_all = p1, p2, p3, d[1]

    if d[2] == 1:
        p1 +=1
    elif d[2] == 2:
        p2 +=1
    elif d[2] == 3:
        p3 +=1






# for i in (famil_door):
#     for j in (pesar_khale):
#         for k in (kolah_ghermezi):
#             sum1 = i+ j+ k
#             max1 = max(i, j, k)
#             min1 = min(i, j, k)
#             dif1 = max1 - min1
#             # print(sum1, max1, min1, dif1)

#             if dif_all > dif1:
#                 dif_all = dif1 
#                 pes = j 
#                 kol = k 
#                 fam = i
#                 sum_all = sum1
           
#             elif dif_all == dif1:
#                 if sum1 < sum_all:
#                     sum_all = sum1
#                     pes = j 
#                     kol = k 
#                     fam = i
#             # print ('pes:%s, kol:%s, fam:%s, sum_all:%s, sum1:%s, ' %(pes, kol, fam, sum_all, sum1))

print (sum_all)

            
