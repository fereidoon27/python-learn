nm=input()
nm=nm.split(' ')
n=int(nm[0])
t=int(nm[1])

a=input()
a=a.split(' ')
for i in range(n):
    a[i]=float(a[i])
ij=[]

for i in range(t):
    ij1=input()
    ij1=ij1.split(' ')
    ij1[0]=int(ij1[0])
    ij1[1]=int(ij1[1])
    ij.append(ij1)

print (n)
print (t)
print (a)   
print (ij)


# # # test1
# n = 7 
# t= 3
# a = [1, 2, 1, 1, 2, 2, 1] 
# ij = [[3, 4], [6, 4], [1, 1]]    

for i in range(t):
    a1=0
    b1=0
   
    for j in range(n):
        if(a[ij[i][0]-1] > a[j] ):
            a1=a1+1
        if(a[ij[i][0]-1] == a[j] ):
            if (ij[i][0]>j):
                a1=a1+1
        if(a[ij[i][1]-1] > a[j] ):
            b1=b1+1
        if(a[ij[i][1]-1] == a[j] ):
            if (ij[i][1]>j):
                b1=b1+1



    st=str(a1)+' '+str(b1)
    print(st)








