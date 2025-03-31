#include <bits/stdc++.h>
//#include <conio.h>
#include <string>
#include <cstring>
#include <cstdlib>
#include <typeinfo>
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
int query(int ci, int st, int end,
		int l, int r, int k)
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


int main()
{
	
	int nnn , q;
	
	string nq;
	getline(cin, nq);
	int arr[6] = { 0 };
	int j = 0, i;
	for (i = 0; nq[i] != '\0'; i++)
	{
		if (nq[i] == ' ')
		{j++;}
		else {arr[j] = arr[j] * 10 + (nq[i] - 48);}
	}


nnn = arr[0] ;
q = arr[1] ;

//cout<<"nq is :"<< nq<< endl;
//cout<<"arr[1]"<< arr[1]<<endl;
//cout<<"n is:"<<n<<endl;
//cout<<"q is:"<<q<<endl;

//n = atoi(nq);
//cout << typeid(nq[0]).name() << endl;
//cout << typeof(nq);
//n = atoi(nq[0]);
//q = atoi(nq[2]);
//cout<<typeid(n).name();

	
	
	string aa;
	getline(cin, aa);
	int aa_ar[nnn+1] = { 0 };
	int jj = 0, mm;
	for (mm = 0; aa[mm] != '\0'; mm++)
	{
		if (aa[mm] == ' ')
		{jj++;}
		else {aa_ar[jj] = aa_ar[jj] * 10 + (aa[mm] - 48);}
	}
//	cout<<"aa_ar[1]"<< aa_ar[1]<<endl;

// iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii	
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
// iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii	
	
	for (int ii =0 ; ii<q ; ii++)
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
      


    else 
    {
//			cout << y<<endl;


//	cout <<y<< "rd smallest element in range " <<l<<" to "<<r <<" is : " << aa_ar[query(0, 0, n - 1, l, r-1, y)] <<endl ;
	cout << aa_ar[query(0, 0, n - 1, l, r-1, y)] <<endl ;
	
	}
	
	}



}
