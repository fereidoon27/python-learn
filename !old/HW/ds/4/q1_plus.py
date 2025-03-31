

# n = int(input())
# a = input().split(' ')
# for i in range (n):
#     a[i] = int(a[i])

# b = input().split(' ')
# for i in range (n):
#     b[i] = int(b[i])

# a = input().split(' ')
# a = list(map (int , a))
# b = input().split(' ')
# b = list(map (int , b))


# aa = input()
# aa = aa.split(' ')
# a =[]
# for i in aa:
#     a.append(int(i))

# bb = input()
# bb = bb.split(' ') 
# b = []
# for i in bb:
#     b.append(int(i))


## test1
# n = 6
# a = [4, 0, 8, 3, 6, 12]
# b = [12, 0, 24, 4, 8, 36]
a = [4,3, 0, 0, 0, 0, 0,10,11,12,13,4,3]
b = [12, 12,9, 0, 0,0,5,5,5,5,6]
answer = 0
hash_table_value = []
hash_table_count = []
for i in b :
    for j in a :
        if j==0 and i==0 :
            answer +=1
        else:
            if j!=0  :  
                # x = i/j
                # print(i/j)
                if (i/j in hash_table_value) :
                    # print ('-----------',hash_table_count.index(i/j))
                    hash_table_count[hash_table_value.index(i/j)] +=1
                else :
                    hash_table_value.append(i/j)
                    hash_table_count.append(1)
                # print (hash_table_value)
                # print (hash_table_count)

u = hash_table_value.index(0)
hash_table_count.pop(u)
answer = answer + max(hash_table_count)

# if 0 in a and 0 in b :
#     answer = answer + 1
# print (hash_table_value)
# print (hash_table_count)
# print (len(hash_table_value))
# print (len(hash_table_count))
print (answer)









