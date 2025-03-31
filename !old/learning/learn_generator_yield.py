# this func return 0 to n-1
def gene ( n ) : 
    i = 0
    while i < n :
        yield i*i
        i += 1
        
def regular (n) :
    my_list = []
    for i in range (0,n) :
        my_list.append(i*i)
    return my_list

print ('gene(5) is : ', gene(5))
print ('type gene(5) is : ',type(gene(5)))

for i in gene(5) : 
    print (i)

print ('------------')
print ('regular (5): ', regular (5))
for i in regular (5) :
    print (i)

print ('------------\n')
# another example
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)



print ('------------\n')
# another example
# A Python program to generate squares from 1
# to 100 using yield and therefore generator
  
# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1
  
    # An Infinite loop to generate squares 
    while True:
        yield i*i                
        i += 1  # Next execution resumes 
                # from this point     
  
# Driver code to test above generator 
# function
for num in nextSquare():
    if num > 100:
         break    
    print(num)


print ('------------\ndifferent between yield and return')
l = [10,20,30,40,50,60]

def ret (l):
    i=0
    for i in range (0,len(l)):
        return l[i]
        i +=1
print ( 'ret(l) is :' ,(ret(l)) )

# for i in ret (l):
#     print (i)

def ret_yield (l):
    i=0
    for i in range (0,len(l)):
        yield l[i]
        i +=1
print ( 'set(ret_yield(l)) is : ',set(ret_yield(l)) )

for i in ret_yield (l):
    print (i)