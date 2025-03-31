#include <iostream>

using namespace std;

struct node
{
	int size;
	int *array;
	node *link;
};

class linkedlist
{
	private:
		node *first;
		
	public:
		linkedlist()
		{
			first = 0;
		}
		
		node *getFirst()
		{
			return first;
		}
		
		void append(int n, int *arr)
		{
			node *p = new node;
			
			p -> size = n;
			p -> array = arr;
			p -> link = 0;
			
			if (first == 0)
				first = p;
			else
			{
				node *q = first;
				
				while (q -> link != 0)
					q = q -> link;
				
				q -> link = p;
			}
			
		}
};

int main()
{
	int test;
	int n;
	int *array;
	int counter = 0;
	int x;
	int nx;
	int y;
	int c;
	int d;
	bool flag;
	bool flag1;
	node *f;
	linkedlist list;
	
	cin >> test;
	
	while (counter < test)
	{
		cin >> n;
		
		array = new int[n];
		for (int i = 0; i < n; i++)
			cin >> array[i];
		
		y = 0;
		x = 0;
		nx = 0;
		flag = true;
		while (array[x] == array[nx] && flag)
		{
			if (nx == n - 1)
				flag = false;
			else
				nx++;
		}
		
		if (flag)
		{
			y = nx;
			
			for (int i = y + 1; i < n; i++)
			{
				if (array[i] != array[x])
					y = i;
				else
				{
					d = 0;
					for(int k = i; array[k] == array[x]; k++)
						d++;
					if (d > nx)
					{
						if (array[i + d] == array[x + nx])
						{
							y = i + d - nx - 1;
							i = i + d - nx;
						}
					}
					
					c = 0;
					flag1 = false;
					for(int j = i; j < i + y; j++)
					{	
						if (j >= n)
						{
							flag1 = true;
							break;
						}
							
						if (array[j] != array[x + c])
						{
							y = j;
							break;
						}	
						c++;
					}
					
					if (flag1)
						break;
					
					i = i + c;
				}
			}
		}
		
		int *result = new int[y + 1];
		for (int i = 0; i <= y; i++)
			result[i] = array[i];
			
		list.append(y - x + 1, result);
		
		delete array;
		
		counter++;
	}
	
	f = list.getFirst();
	while(f != 0)
	{
		cout << f -> size << endl;
		for (int i = 0; i < f -> size; i++)
			cout << f -> array[i] << " ";
		cout << endl;
		f = f -> link;
	}
	
	return 0;
}
