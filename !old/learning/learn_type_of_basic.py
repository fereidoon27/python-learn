import time
start = time.time()

# Defining a positive infinite integer
positive_infinity = float('inf')
print('Positive Infinity: ', positive_infinity)
 
# Defining a negative infinite integer
negative_infinity = float('-inf')
print('Negative Infinity: ', negative_infinity)
print('--------------')


# isinstance(x,y) --> x ozve y hast ya na?
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

# multiline srtring
print('multiline srtring')
s = '''salam 
chetori?
keili khari ! '''
print(s)
print(s[6:18])
print('--------------')


# set()---> without order , immutable
print('set()')
a = {1,2,3,4,5}
b = {4,5,6,7,8}

# ejtema--> union() or |
print ('ejtema is :' , a|b)
# print(a.union(b)) 

# eshterak
print( 'eshterak is : ' , a & b )
# print(a.intersection(b)) 

# add , update
a.add(80)
new_nums = [90, 15, 13]
b.update(new_nums)

# remove() , discard() --> different = if elemnt dose not exist in set --> remove give us error 
# a.remove(98) ---> leads to error
a.discard(98) 

# difference() or -
print('a-b is :' , a-b)
# print(a.difference(b))
print('--------------')

# converting
print('converting')
print (list('hello'))
print(dict( [(3,26),(4,44)]) )
print(set([1,2,3]))
print(complex('3+5j'))
print('--------------')


# binary or oct or hex 
print('binary or oct or hex ')
print('0b1011 is :' , 0b1011)
print('0o15 is : ' , 0o15)
print('0xFB + 0b10 is :' , 0xFB + 0b10)
print('--------------')

# fraction
print('fraction')
from fractions import Fraction as F

from sympy import N
print(F(8.32541))
print(F('8.32541'))
print(F(1,3))
print('--------------')

import math as m
print('math: ')
print('pi is: ' , m.pi)
print('cos(pi) is: ' , m.cos(m.pi))
print('exp(10): ' , m.exp(10))
print('m.log10(1000)', m.log10(1000))
print('m.sinh(1)' , m.sinh(1))
print('m.factorial(6)' , m.factorial(6))
print('--------------')


import random as ra
print('random')
# 1-Output: 16
print('1=' , ra.randrange(10,20))
x = ['a', 'b', 'c', 'd', 'e']
# 2-Get random choice
print('2=' ,ra.choice(x))
# 3-Print the shuffled x
ra.shuffle(x)
print('3=' ,x)
# 4-Print random element
print('4=' , ra.random())

print('--------------')

print("Run Time: " + str( time.time() - start ))

