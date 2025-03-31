n = 5
a = [5, 1, 6, 2, 3]
a.sort()
b = [9, 3, 1, 4, 4]
b.sort()
result = []
for i in range (n) :
       result.append ([a[i] , i + 1 , b[i]]) 
result.sort()
print (result)