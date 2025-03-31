     # ctrl + / = multiple line comment
# items=[1,2,3,4,5]
# for i in items[0:5]:
#      items.append(i**2)
# print(items)

import numpy as np
mm = np.array([1,2,3,4],dtype=np.float32)
np.append(mm, [12,2,1])
np.delete(mm, 0)
np.sort(mm, kind='quicksort')
np.sort(mm, kind='mergresort')


c = np.array(range(1,5)).reshape(2,2) # == c = np.arange(1,5).reshape(2,2)
d = np.array(range(5,9)).reshape(2,2)

#size of matrix
print (' matrix c is : \n%s \n has %s row&clumn and \nhas %i row , \n %i column \n and %s entry\n\
and the dimansion is %s\nand type is : %s' %(c , c.shape , len(c) , len (c[0]) , c.size , c.ndim , c.dtype))
print ('------------------')

# zarb be 2 ravesh
print ( '\nc.dot(d) is : \n' ,c.dot(d))
print ( '\nnp.matmul(c,d) is : \n' ,np.matmul(c,d))

# transpose
print('\ntranspose c is : \n' , c.T)
# determinant 
print( '\n det(c) is : %5.2f \n '  %(np.linalg.det(c)) )
# Dot product
print ( '\nc*d is : \n' ,c*d )
# inverse 
print ( '\n inverse c is : \n' , np.linalg.inv(c))

#ضرب «یک ماتریس» در «معکوس خودش» یک ماتریس همانی را می‌دهد!
check=c.dot(np.linalg.inv(c))
c1=0
for arrayy in check :
     c2=0
     for i in arrayy :
          check[c1,c2]=round(i,2)
          c2+=1
     c1=+1
print ('\ncheck is : \n' , check)

hand_made_prouct = np.zeros((2,2))
print ( hand_made_prouct)

testo = hand_made_prouct.dot(check)
print(testo)