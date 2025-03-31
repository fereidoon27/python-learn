class Node:
     def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
 
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    return node

def minValueNode(node):
    current = node
 
    while(current.left is not None):
        current = current.left
 
    return current

def deleteNode(root, key):
 
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif(key > root.key):
        root.right = deleteNode(root.right, key)

    else:
 
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        temp = minValueNode(root.right)
 
        root.key = temp.key
 
        root.right = deleteNode(root.right, temp.key)
 
    return root

def findPreSuc(root, key):
 
    if root is None:
        return
 
    if root.key == key:
 
        if root.left is not None:
            tmp = root.left
            while(tmp.right):
                tmp = tmp.right
            findPreSuc.pre = tmp
 
 
        if root.right is not None:
            tmp = root.right
            while(tmp.left):
                tmp = tmp.left
            findPreSuc.suc = tmp
 
        return
 
    if root.key > key :
        findPreSuc.suc = root
        findPreSuc(root.left, key)
 
    else: 
        findPreSuc.pre = root
        findPreSuc(root.right, key)

n = 0
root = None
med = []
q = int(input())
temp = input()
temp = temp.split(' ')
x = int(temp[1])
med.append(x)
root = insert(root,x)
n += 1

for i in range(1,q):
    temp = input()
    temp = temp.split(' ')
    x = int(temp[1])
    if (temp[0] == '+'):
        n += 1
        insert(root, x)
        if (x < med[i-1]):
            if (n%2 == 1):
                med.append(med[i-1])
            else:
                findPreSuc.pre = None
                findPreSuc(root, med[i-1])
                med.append(findPreSuc.pre.key)
        else:
            if (n%2 == 0):
                med.append(med[i-1])
            else:
                findPreSuc.suc = None
                findPreSuc(root, med[i-1])
                med.append(findPreSuc.suc.key)

    if (temp[0] == '-'):
        n -= 1
        deleteNode(root, x)
        if (x < med[i-1]):
            if (n%2 == 0):
                med.append(med[i-1])
            else:
                findPreSuc.suc = None
                findPreSuc(root, med[i-1])
                med.append(findPreSuc.suc.key) 

        elif (x > med[i-1]):
            if (n%2 == 1):
                med.append(med[i-1])
            else:
                findPreSuc.pre = None
                findPreSuc(root, med[i-1])
                med.append(findPreSuc.pre.key)  
        else:
            if (n%2 == 0):
                findPreSuc.pre = None
                findPreSuc(root, med[i-1])
                med.append(findPreSuc.pre.key)                 
            else:
                findPreSuc.suc = None
                findPreSuc(root, med[i-1])
                med.append(findPreSuc.suc.key) 

for i in range(q):
    print(med[i])
