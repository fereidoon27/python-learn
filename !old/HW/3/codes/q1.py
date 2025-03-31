def insert_to_sorted_list(list, n):
  
    index = len(list)
    # Searching for the position
    for i in range(len(list)):
      if list[i] > n:
        index = i
        break
  
    # Inserting n in the list
    if index == len(list):
      list = list[:index] + [n]
    else:
      list = list[:index] + [n] + list[index:]
    return list

q = int(input())
temp = input()
temp = temp.split(' ')
x = int(temp[1])
n = 1
my_list = [x]
print(x)

for i in range(1,q):
    temp = input()
    temp = temp.split(' ')
    x = int(temp[1])
    if (temp[0] == '+'):
        n += 1
               
        my_list = insert_to_sorted_list (my_list , x)

        # print ('my list is : ' , my_list)
        print (my_list[((n-1)//2)])
        

    else:

        index = my_list.index(x)
        my_list.pop(index)
        n -= 1

        # print ('my list is : ' , my_list)
        print (my_list[((n-1)//2)])
        




# x = binary_search2 ([1,2,5,6,40,50],0,5,70)
# print (x)

