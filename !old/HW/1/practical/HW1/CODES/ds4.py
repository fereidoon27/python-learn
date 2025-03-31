import time
start = time.time()

# test_str = input()
dictio = dict()

test_str = 'bbaabcbaa'

# print(symmetry('aabcbaa'))
### Get all substrings of string
# res = [test_str[i: j] for i in range(len(test_str))
#           for j in range(i + 1, len(test_str) + 1)]

### taghaaaron_yab
# def ispalindrome (string):
#     n = len(string)
#     for i in range (int(n/2)) :
#         n = n - 1
#         if string[i] != string[n] :
#             return 0
#     return 1

### Function to find keys for the Hashmap
def to_str(a, b):
	return str(a) + str(b)


def ispalindrome(test_str, b, e):
    while (b < e):
        if (test_str[b] != test_str[e]):
            return 0
        b += 1
        e -= 1
    return 1


### def function due to finding min cuts for split a string
def min_founder(test_str, i, j, dictio):

	if (i > j):
		return 0

	## creating key for dic 
	ij = to_str(i, j)

	## if min cut available for key "ij" , return it
	if (ij in dictio):
		return dictio[ij]
	
	## (str with len 1)  & (palindrome str) dont need cut
	if ( (i == j) | ispalindrome(test_str, i, j) ) :
		dictio[ij] = 0
		return 0

	minimum = float('inf')
	
	# Get all substrings of string from i to j
	for k in range(i, j):

		left_min =  float('inf')
		left = to_str(i, k)

		right_min =  float('inf')
		right = to_str(k + 1, j)

		# If left cut founded already
		if (left in dictio):
			left_min = dictio[left]
		
		# If right cut founded already
		if (right in dictio):
			right_min = dictio[right]
		
		# Recursively calculating for left and right strings
		if (left_min ==  float('inf')):
			left_min = min_founder(test_str, i, k, dictio)
		if (right_min ==  float('inf')):
			right_min = min_founder(test_str, k + 1, j, dictio)

		# Taking minimum of all k possible cuts
		minimum = min(minimum, left_min + 1 + right_min)
	dictio[ij] = minimum
	
	# Return the min cut value for complete string.
	return dictio[ij]


# test_str = "ababbbabbababaababbbabbababacddc"

print(min_founder(test_str, 0, len(test_str) - 1, dictio))

# print("All substrings of string are : " + str(res))
# print("Run Time: " + str( time.time() - start ))