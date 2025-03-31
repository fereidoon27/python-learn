def prime(n):
    f=1
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            f=0
    return f

last_prime_num=0
count=0
for i in range(10,30):
    if prime(i):
        last_prime_num=i
        print( i , "is prime" , )
        count=count+1
print ( "counting: " , count )
print ( "last_prime_num: " ,  last_prime_num )