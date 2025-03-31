n = int(input())
pesar_khale = list (map (int, input().split(' ') ) )
kolah_ghermezi = list (map (int, input().split(' ') ) )
famil_door = list (map (int, input().split(' ') ) )

# # test1
# n=2
# pesar_khale = [1, 4]
# kolah_ghermezi= [3, 2]
# famil_door = [9,8]

# ## test2
# n=3
# pesar_khale = [1, 12, 1]
# kolah_ghermezi= [8, 35, 2]
# famil_door = [10, 9, 11]

pesar_khale.sort()
kolah_ghermezi.sort()
famil_door.sort()

pes = kol= fam=  0
dif_all = sum_all=  float('inf')


pointer_1= pointer_2= pointer_3= 0
while pointer_1 < n and pointer_2 < n and pointer_3 < n:
    max1 = max(famil_door[pointer_1] , pesar_khale[pointer_2] , kolah_ghermezi[pointer_3] )
    min1 = min(famil_door[pointer_1] , pesar_khale[pointer_2] , kolah_ghermezi[pointer_3] )
    sum1 = famil_door[pointer_1] + pesar_khale[pointer_2] + kolah_ghermezi[pointer_3]
    dif1 = max1 - min1

    # print(d)

    if dif_all > dif1:
        dif_all, pes, kol, fam, sum_all = dif1, pointer_1, pointer_2, pointer_3, sum1         
    elif dif_all == dif1:
        if sum1 < sum_all:
            pes, kol, fam, sum_all = pointer_1, pointer_2, pointer_3, sum1

    if min1 == famil_door[pointer_1]:
        pointer_1 +=1
    elif min1 == pesar_khale[pointer_2]:
        pointer_2 +=1
    elif min1 == kolah_ghermezi[pointer_3]:
        pointer_3 +=1


print (sum_all)

            
