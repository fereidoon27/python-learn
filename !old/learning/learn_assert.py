

# def eshterak(b,c) :
#     for i in b:
#         assert i not in c , 'b eshterak c != tohiii'
#     return 'b va c eshterak nadaran '
count = 0
for i in range (0,10):
    
    try :

        def square(x):
            cc = 1

            assert x>=5, 'Only positive numbers are allowed'
            cc = cc/0
            return x*x

        print ( '%i be tavan 2 mishe : %i' %(i ,square(i) ))
        

        # z = [1,2,3,4,5]
        # q = [6,7,8,9,10]

        # try:
        #     print (eshterak(z,q))
        # except AssertionError as msg :
        #     print(msg)
        
    except AssertionError as msg  :
        count +=1
        print(msg )
        
    except ZeroDivisionError :
        count +=1
        print('ridi')
        
print ('count is :' ,count )

# def square(x):
    

#     assert x>=5, 'Only positive numbers are allowed'
    
#     return x*x
# print ( '%i be tavan 2 mishe : %i' %(2 ,square(2) ))

