#include <iostream>

using namespace std;

void heapify(float *arr, int n, int i)
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

void heapSort(float *arr, int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
	int n;
	int s = 1;
	int g = 0;
	int z = 0;
	
	cin >> n;
	
	if (n == 1)
		cout << 1 << endl;
	else
	{
		int *a = new int [n];
		int *b = new int [n];
		float *c = new float [n];
		
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			cin >> b[i];
		
		for (int i = 0; i < n; i++)
		{
			if (a [i] == 0 || b[i] == 0)
				c[i] = 0;
			else
				c[i] = float(b[i]) / float(a[i]);
		}
		
		heapSort(c, n);
		
		for (int i = 0; i < n; i++)
		{
			if (i < n - 1)
			{
				if (c[i] == 0)
					z++;
				else if (c[i] == c[i + 1])
					s++;
				else if (s > g)
				{
					g = s;
					s = 1;
				}
				else
					s = 1;
			}
			else
				if (c[i] == c[i - 1])
				{	
					if (s > g)
						g = s;
				}
				else
				{
					s = 1;
					
					if (s > g)
						g = s;
				}
		}
		
		cout << z + g << endl;
	}
	
	return 0;
}
