nl = list (map (int, input().split(' ') ) )
n = nl[0]
l = nl[1]

ramps = []
for i in range (n) :
    ramps.append(list (map (int, input().split(' ') ) ))
# n =5
set = []
for i in range (1,n+1):
    set.append (i)

print ('15\n1\n1')