#include <bits/stdc++.h>
#include <conio.h>
#include <string>
using namespace std;
main()
{
	string name;
	int a;
	cin >> a>>name;
	cout << a<< name ;
//####test1
//# n , q , a = 5 , 3 , [1, 4, 0, 1, 3]
//# req1 , req2 , req3 = ['a', 1, 4, 2,] , ['b', 0, 4, 1,] , ['c', 1, 5, 2]

NQ = list(map(int , input().split(' ')))
n , q = NQ
a = list(map(int , input().split(' ')))



//for i in range (q):
	for (int i =0 ; i<q ; i++)
	{
		    temp = input().split(' ')
    req = temp[0]
    l = int(temp[1])
    r = int(temp[2])
    y = int(temp[3])

    if (req == 49)
	{
    	count = 0
        # print (i, 'a')
        for j in range (l , r):
            if a[j] < y :
                count += 1
        print (count)
    	
	}


        
    else if (req == 50)
    	{
    	# print(i, 'b')
        count = 0
        for j in range (l , r):
            if a[j] == y :
                count += 1
        print (count)  
		}
      


    else 
    {
            # print(i, 'c')
        # sub_sorted = sorted(a[l:r])
        # print (sub_sorted[y-1])
        
        # print( kthSmallest(a[l:r], len(a[l:r]), y))
        print (find_kth_smallest(a[l:r], y))	
	}
	
	}



}
