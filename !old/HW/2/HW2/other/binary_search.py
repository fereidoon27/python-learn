# Python 3 program for recursive binary search.

def binary_search(arr, low, high, x):
	if high >= low:
		global mid

		mid = (high + low) // 2
		# print('mid is:' , mid)

		# If element is present at the middle itself
		if arr[mid] == x :
			while arr[mid+1] == x:
					mid +=1
			return mid

		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
		
	else:
		# Element is not present in the array
		return mid

# Test array
# arr = [ 2, 2, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 40 ]
arr = [10, 11, 11, 20]
x = 15

# Function call
result = binary_search(arr, 0, len(arr)-1, x)
print("Element is present at index", str(result))

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array",str(mid) )
