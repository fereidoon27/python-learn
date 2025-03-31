import random 
# tupple
t1 = (1, 2, 3, 4, 5)
# nasted tupple  تو در تو
t2 = (("Sajjad",12),("Ali Reza",20),2,5,10)
# t2[-1] == t2[4]
print('t2[-1] == t2[4] : ' , t2[-1])
print ('t2 is: ' , t2 , ' and t2[0][1] is:' , t2[0][1])

# list
my_list = ["Happy", [2,0,1,5],1,2,3,4,5,6]
# Nested indexing
print('my_list ', my_list , 'my_list[1][3]:' , my_list[1][3])

#extend 
my_list.extend([15, 14, 13])
print ('.extend([15, 14, 13])' , my_list)
# concat (+)
l = my_list + [90, 70, 50]
# insert(): insert element in specific position
my_list.insert(1,225)
print ('insert 225 in pos 1 : ' , my_list)
my_list[3:3] = [90,78,66,69]
print ('put list in pos 3' , my_list)

#replacing :
my_list[3:4] = [5000]
print ('replacing my_list[3:4] = [5000] is : ' , my_list)
my_list[3:7] = ['ali', 'hasan', 'amir', 69999]
print ('replacing my_list[3:7]  is : ' , my_list)

# removing : remove & pop & clear & del
del my_list[1:4] 
# my_list[1:4] = []  == del my_list[1:4] 
print ('del my_list[1:5] is : ' , my_list)
if 13 in my_list :
    my_list.remove(13)
print ('my_list.remove(13) is : ' , my_list)
poped = my_list.pop(0)
print ('poped is : ' , poped)
poped = my_list.pop()
print ('poped is : ' , poped)
print ('my_list after pop is : ' , my_list)

# other methods
my_list[0:3] = [15,15,15] 
print('my_list is :' , my_list)
print('my_list.index(5) is :', my_list.index(5))
print('my_list.count(15) is : ' , my_list.count(15))
my_list.reverse()
print ('my_list.reverse() is : ', my_list)
my_list.sort()
print ('my_list.sort() is : ', my_list)

# making list funny 
pow2 = [2 ** x for x in range(10)]

# == 
# pow2 = []
# for x in range(10):
#    pow2.append(2 ** x)
odd = [x for x in range(20) if x % 2 == 1]

print ('enumerate is : ' , list(enumerate(odd)))
random.shuffle(odd)
print ('random.shuffle(odd)', odd)
print ('sorted(odd)', sorted(odd))

# any() ،enumerate() ،len() ،max() ،min() ،sorted() , all(), ()copy