

# n = int(input())
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
n = 6
a = [4, 0, 8, 3, 6, 12]
b = [12, 0, 24, 4, 8, 36]

hash_table_value = []
hash_table_count = []
for i in b :
    for j in a :
        if j!=0 and i!=0 :
            x = i/j
            index_ij = hash_table_value.index(x) if x in hash_table_value else -1
            if (index_ij == -1) :
            
                hash_table_value.append(x)
                hash_table_count.append(1)
                
            else :
                hash_table_count[index_ij] +=1



answer = max(hash_table_count)
            
if 0 in a and 0 in b :
    answer = answer + 1


# print (hash_table_value)
# print (hash_table_count)
# print (len(hash_table_value))
# print (len(hash_table_count))
print (answer)









