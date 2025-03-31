#include <iostream>

using namespace std;

void heapify(int *arr, int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
  
    if (l < n && arr[l] > arr[largest])
        largest = l;
  
    if (r < n && arr[r] > arr[largest])
        largest = r;
  
    if (largest != i) {
        swap(arr[i], arr[largest]);
  
        heapify(arr, n, largest);
    }
}

void heapSort(int *arr, int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
  
    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
  
        heapify(arr, i, 0);
    }
}

int main()
{
	int n, m;
	int test;
	int l, r, s, t;
	int *temp1;
	int *temp2;
	int counter = 0;
	int *array;
	bool flag;
	
	cin >> n >> m;
	
	int *a = new int [n + 1];
	int *b = new int [m + 1];
	
	a[0] = -1;
	b[0] = -1;
	
	for(int  i = 1; i <= n; i++)
		cin >> a[i];
	for(int  i = 1; i <= m; i++)
		cin >> b[i];
	
	cin >> test;
	
	array = new int[test];
	
	while (counter < test)
	{
		cin >> l >> r >> s >> t;
		
		if ((r - l) > (t - s) || (t - s) > (r - l))
			array[counter] = 0;
		else
		{
			temp1 = new int [r - l + 1];
			temp2 = new int [t - s + 1];
			
			for (int i = 0; i < r - l + 1; i++)
			{
				temp1[i] = a[l + i];
				temp2[i] = b[s + i];
			}
			
			heapSort(temp1, r - l + 1);
			heapSort(temp2, t - s + 1);
			
			flag = true;
			for (int i = 0; i < r - l + 1; i++)
				if (temp1[i] != temp2[i])
				{
					array[counter] = 0;
					flag = false;
					break;
				}
			
			if (flag)
				array[counter] = 1;
			
			delete temp1;
			delete temp2;
		}
		
		counter++;
	}
	
	for (int i = 0; i < test; i++)
		if (array[i] == 0)
			cout << "NO" << endl;
		else
			cout << "YES" << endl;
	return 0;
}
