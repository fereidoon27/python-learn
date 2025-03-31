def multiple(n):
    sum=0
    for i in range (3 , n):
        if i%3==0:
            sum=i+sum
        if i%5==0:
            sum=i+sum
        if i%15==0:
            sum=sum-i
    return sum 

print (multiple(1000))

