// C++ program to find the kth smallest element in a range
#include <bits/stdc++.h>
using namespace std;
#define N (int)1e5

// Declaring a global segment tree
vector<int> seg[N];

// Function to build the merge sort
// segment tree of indices
void build(int ci, int st, int end,
		pair<int, int>* B)
{
	if (st == end) {
		// Using second property of B
		seg[ci].push_back(B[st].second);
		return;
	}

	int mid = (st + end) / 2;
	build(2 * ci + 1, st, mid, B);
	build(2 * ci + 2, mid + 1, end, B);

	// Inbuilt merge function
	// this takes two sorted arrays and merge
	// them into a sorted array
	merge(seg[2 * ci + 1].begin(), seg[2 * ci + 1].end(),
		seg[2 * ci + 2].begin(), seg[2 * ci + 2].end(),
		back_inserter(seg[ci]));
}

// Function to return the index of
// kth smallest element in range [l, r]
int query(int ci, int st, int end,int l, int r, int k)
		
{
	// Base case
	if (st == end)
		return seg[ci][0];

	// Finding value of 'p' as described in article
	// seg[2*ci+1] is left node of seg[ci]
	int p = upper_bound(seg[2 * ci + 1].begin(),
						seg[2 * ci + 1].end(), r)
			- lower_bound(seg[2 * ci + 1].begin(),
						seg[2 * ci + 1].end(), l);

	int mid = (st + end) / 2;
	if (p >= k)
		return query(2 * ci + 1, st, mid, l, r, k);
	else
		return query(2 * ci + 2, mid + 1, end, l, r, k - p);
}

// Driver code
int main()
{
	int aa_ar[] = { 3, 1, 5, 2, 4, 7, 8, 0 };
	
	int n = sizeof(aa_ar) / sizeof(aa_ar[0]);

	pair<int, int> B[n];

	for (int i = 0; i < n; i++) {
		B[i] = { aa_ar[i], i };
	}

	// After sorting, B's second property is
	// something upon which we will build our Tree
	sort(B, B + n);

	// Build the tree
	build(0, 0, n - 1, B);

	 int r = 1 ;
	 int l = 0 ;
	 int y = 1 ;
	 
//	cout << "3rd smallest element in range 3 to 7 is: "<< aa_ar[query(0, 0, n - 1, 0, 1, 1)] << "\n";

	for (int ii =0 ; ii<n ; ii++)
	{
		
	string temp;
	getline(cin, temp);
	int temp_arr[6] = { 0 };
	int jjj = 0, mmm;
	for (mmm = 0; temp[mmm] != '\0'; mmm++)
	{
		if (temp[mmm] == ' ')
		{jjj++;}
		else {temp_arr[jjj] = temp_arr[jjj] * 10 + (temp[mmm] - 48);}
	}
//	cout<<"temp_arr[1]"<< temp_arr[1]<<endl;

		    
    int req = temp_arr[0];
    int l = temp_arr[1];
    int r = temp_arr[2];
    int y = temp_arr[3];

//cout << "req is: "<< req<<endl;


    if (req == 49)
	{
//			cout << l<<endl;

        int count1 = 0;
//        int aa_ar[] = { 3, 1, 5, 2, 4, 7, 8, 6 };
        
        	for (l ; l<r; l++)
        	{
        		if (aa_ar[l] < y) 
        		{
				count1 += 1 ;
        		
				}
			}
			cout<<count1<<endl;

    	
	}


        
    else if (req == 50)
	    {
//			cout << r <<endl;
        int count2 = 0;
//        int aa_ar[] = { 3, 1, 5, 2, 4, 7, 8, 6 };
        
        	for (l ; l<r; l++)
        	{
        		if (aa_ar[l] == y) 
        		{
				count2 += 1 ;
        		
				}
			}
			cout<<count2<<endl;
		}
      

	
	
	}		
}

