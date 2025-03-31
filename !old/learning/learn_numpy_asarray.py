# Array in py eith numpy

# numpy.asarray()function is used when we want to convert input to an array.
# Input can be lists, lists of tuples, tuples, tuples of tuples, tuples of lists and arrays.


import numpy as np

my_list = [1, 3, 5, 7, 9]  
print ("Input  list : ", my_list)

out_arr = np.asarray(my_list)
print ("output as an array from input list : ", out_arr)

# lst = [ [1,2,3,4,5], [6,7,8,9] ]
# converted_lst = np.asarray(lst)
   
# print(type(converted_lst))  
# print(converted_lst)  

#Numpy array VS Numpy asarray
arr = np.array([5,6,7])
 
x = np.array(arr)
y = np.asarray(arr)
arr[1] = 0
 
print("Array : ",x)
print("Asarray : ",y)

# type of elements in array :
np.array([1, 2, 3], dtype=complex)

# 10 random number
msk = np.random.rand(10) < 0.8
print(msk)
print(type(msk))

h = np.arange(-5.0, 5.0, 0.1)
# print ('h is :\n ', h)
print (len(h), h.size)
