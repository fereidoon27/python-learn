XSize = int(input())
YSize = int(input())

XString = input()
XArray = list(map(int, XString.split(' ')))

YString = input()
YArray = list(map(int, YString.split(' ')))
YArray.sort()

tempArray = [0] * 5
for i in range(YSize):
    if (YArray[i] < 5):
        tempArray[YArray[i]] += 1

def YGreaterThanX(x):
    if (x > YArray[YSize - 1]):
        return 0
    if (x < YArray[0]):
        return YSize

    left = 0
    right = YSize - 1
    leftGreater = YSize

    while (left <= right):
        mid = int(left + (right - left) / 2)
        if (YArray[mid] > x):
            leftGreater = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return YSize - leftGreater

def countForEachX(x):
    if (x == 0):
        return 0
    if (x == 1):
        return tempArray[0]

    forThisX = YGreaterThanX(x)
    forThisX += tempArray[0] + tempArray[1]

    if (x == 2):
        forThisX -= tempArray[3] + tempArray[4]
    if (x == 3):
        forThisX += tempArray[2]
    
    return forThisX
    
count = 0
for x in XArray:
    count += countForEachX(x)

print(count)
            