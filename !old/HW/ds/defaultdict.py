from collections import defaultdict


d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d)
print(list(d))
print(d.keys())
print(list(d.keys()))
print(d["a"])
print(d["b"])
print(d["c"])


#---------------
print('-----------')
a = defaultdict(list)
  
for i in range(5):
    a[i].append(i)
      
print("Dictionary with values as list:")
print(a)