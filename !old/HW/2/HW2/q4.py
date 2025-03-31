
n = int(input())
t_list = []
for i in range (n):
    t_list.append(list (map (int, input().split(' ') ) ))

##test1
# n=3
# t_list = [[2,3], [1,0], [1,0]]
# n=6
# t_list = [[2,3], [1,0], [1,0], [2,1], [1,3], [1,3]]

##test2
# n=1
# t_list = [ [1,0]]

# t_list.sort(reverse = True)
# print (t_list)
# barg =[]
for i in range (n):
    t_list[i].append(i)
    # if t_list[i][0] == 1 :
    #     barg.append(t_list[i])
# print(t_list)

 
yal =[]
# global count
count = 0
# def f (t_list , n):

for i in range (n) :
    # print(i)
    while t_list[i][0] == 1 :
        t_list[i][0] = 0
        parent = t_list[i][1]
        t_list[parent][0] -=1
        t_list[parent][1] = t_list[parent][1] ^  t_list[i][2]
        count +=1
        # print (i , t_list[parent])
        if t_list[i][2] > t_list[parent][2] :
            yal.append([t_list[parent][2] , t_list[i][2]])
        else:
            yal.append([ t_list[i][2] , t_list[parent][2] ])
        i =  parent

        # while t_list[parent][0] == 1 :
            

        
nor = 0
for i in range (n):
    nor = t_list[i][0] or nor

if nor == 0 :
    print(count)
    for i in yal :
        print (i[0], i[1])
else :
  print ('NOT POSSIBLE')  












# deg =[]
# for i in t_list:
#     deg.append(i[0])

# print(t_list, deg, barg)

# def hawel (degs):
#     # flag =0
#     while 1:
#         degs.sort(reverse = True)
#         if degs[0]== 0 and degs[len(degs)-1]== 0:
#             return 1
#         a = degs.pop(0)
#         degs = list( map(lambda x: x-1 , degs[0:a]  ) ) 
        
#         for i in degs :
#             if i < 0:
#                 return 0     


# print ('NOT POSSIBLE')

