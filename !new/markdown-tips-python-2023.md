# 🐍 Python Reference Guide for Students

## Table of Contents
- [Number Systems](#number-systems)
- [Naming Conventions](#naming-conventions)
- [Variables and References](#variables-and-references)
- [Number Types and Operations](#number-types-and-operations)
- [String Manipulation](#string-manipulation)
- [Collection Types](#collection-types)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Sets](#sets)
- [Unpacking and Packing](#unpacking-and-packing)
- [Code Style](#code-style)

## Number Systems

Python supports multiple numerical representations:

```python
# Binary (prefix: 0b)
0b10  # = 2 in decimal

# Octal (prefix: 0o)
0o10  # = 8 in decimal

# Hexadecimal (prefix: 0x)
0x10  # = 16 in decimal

# Example:
0b10 + 0o10 + 0x10  # = 2 + 8 + 16 = 26
```

## Naming Conventions

- **Camel Case**: `numberOfCollegeGraduates` (variables, functions)
- **Pascal Case**: `NumberOfCollegeGraduates` (classes)
- **Snake Case**: `number_of_college_graduates` (variables, functions - preferred in Python)

**Constants** in Python (by convention):
```python
PI = 3.14159
MAX_SIZE = 100
```

## Variables and References

**Important**: Assigning one variable to another creates a new reference to the same object, not a new object.

```python
a = 10
b = a    # b references the same object as a
c = b    # c references the same object as a and b

a is b   # Returns True
```

## Number Types and Operations

### Floating-Point Issues

```python
# Floating-point arithmetic isn't always exact
0.1 + 0.1 + 0.1 == 0.3  # Returns False!

# Better approach for float comparison:
import math
math.isclose(0.1 + 0.1 + 0.1, 0.3)  # Returns True
```

### Type Conversion

```python
# This will raise an error:
int('4.2')  # ValueError: invalid literal for int() with base 10: '4.2'

# Correct approach:
int(float('4.2'))  # Works! Returns 4

# Scientific notation creates float:
type(4e7)  # <class 'float'>
```

### Common Operations

- **Floor Division (`//`)**: `7 // 3` results in `2`
- **Exponentiation (`**`)**: `3 ** 2` results in `9`
- **Add and assign (`+=`)**: `x += 3` is equivalent to `x = x + 3`

## String Manipulation

### Creating Strings

```python
# Multi-line strings
multiline = """
This is a
string 
"""

# Raw strings (ignore escape characters)
raw_str = r'foo\\bar\n'  # Backslashes and \n treated as literal characters

# File paths
path1 = "C:\\Users\\Bob\\Documents"  # Using escaped backslashes
path2 = r"C:\Users\Bob\Documents"    # Using raw string (preferred for paths)

# Line continuation
continued = 'a\
 b\
 c\
'  # Results in "a b c"
```

### String Methods

```python
text = "  hello,world  "

# Common string methods (strings are immutable)
text.split(",")           # ['  hello', 'world  ']
text.find("world")        # 8
text.strip()              # "hello,world"
text.replace("world", "Python")  # "  hello,Python  "
```

### Escape Sequences

- `\t`: Tab
- `\n`: Newline
- `\\`: Backslash
- `\'`: Single quote
- `\"`: Double quote

### String Slicing

The format is `string[start:stop:step]`:
- `start` is the starting index (**inclusive**)
- `stop` is the ending index (**exclusive**)
- `step` is the interval between characters

Reverse a string: `s[::-1]`

### String Formatting

#### 1. `.format()` Method

```python
name = "Hamidreza"
age = 22
template = 'In ten years, {name} will be {age} years old.'
new_rec = template.format(name=name, age=age+10)
# "In ten years, Hamidreza will be 32 years old."
```

#### 2. f-strings (Python 3.6+)

```python
name = "Hamidreza"
age = 22
f_string = f"In ten years, {name} will be {age + 10} years old."
# "In ten years, Hamidreza will be 32 years old."
```

## Collection Types

### Lists

Lists are mutable ordered collections.

#### Creating Lists

```python
empty_list = list()       # Using the list constructor
empty_list = []           # Using square brackets
set_to_list = list({3, 1, 2})  # Convert set to list
none_list = [None] * 10   # Create list with 10 None values
consecutive = list(range(10))  # List of numbers 0-9
```

#### List Operations

```python
fruits = ['apple', 'banana', 'cherry', 'date']

# Add elements
fruits.append('elderberry')      # Add single element to end
fruits.extend(['fig', 'grape'])  # Add multiple elements to end
fruits.insert(2, 'apricot')      # Insert at specific position (not efficient)

# Remove elements
popped = fruits.pop(2)      # Remove and return element at index (not efficient)
fruits.remove('cherry')     # Remove first occurrence of value (not efficient)
del fruits[1:3]             # Delete slice

# Find elements
fruits.index('banana')      # Find index of first occurrence
fruits.count('banana')      # Count occurrences
```

#### Sorting and Reversing

```python
numbers = [10, 2, 34, 14, 5]

# Sort in-place
numbers.sort()              # [2, 5, 10, 14, 34]

# Create new sorted list
sorted_nums = sorted(numbers)

# Reverse in-place
numbers.reverse()

# Create new reversed list
reversed_list = list(reversed(numbers))
# OR
reversed_list = numbers[::-1]
```

### Tuples

Tuples are immutable ordered collections.

```python
empty_tuple = ()
single_element_tuple = (4,)  # Note the comma - required for single-element tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenating tuples
combined_tuple = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)
```

### Dictionaries

Dictionaries are mutable key-value pair collections.

```python
# Creating dictionaries
empty_dict = dict()
empty_dict = {}
person_info = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Safe access with default value
occupation = person_info.get('occupation', 'Not specified')  # 'Not specified'

# Creating from list of tuples
portfolio = dict([('AAPL', 100), ('GOOG', 25)])

# Updating multiple values
portfolio.update({'TSLA': 50, 'AAPL': 200})  # Updates 'AAPL' and adds 'TSLA'

# Adding new key-value pair
portfolio['MSFT'] = 75

# Using keyword arguments for update
portfolio.update(NVDA=100, AMZN=30)
```

### Sets

Sets are unordered collections of unique elements.

```python
# Creating sets
empty_set = set()  # Note: {} creates an empty dict, not a set
words = set('hello hello i am feri . ha ha ha ha . :)))) '.split())

# Adding elements
words.add('new_word')

# Adding multiple elements
another_set = {'1', '2', '3'}
words.update(another_set)  # Add elements from another set
words |= {9, 10}  # Add elements using the union operator
```

#### Set Operations

```python
# Removing elements (two approaches)
try:
    words.remove('nonexistent')  # Raises KeyError if element doesn't exist
except KeyError:
    pass
    
words.discard('nonexistent')  # No error if element doesn't exist

# Clear all elements
words.clear()

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_a | set_b  # Union: {1, 2, 3, 4, 5}
set_a & set_b  # Intersection: {3}
set_a - set_b  # Difference: {1, 2}
set_a ^ set_b  # Symmetric difference: {1, 2, 4, 5}

# Immutable sets
frozen = frozenset([1, 2, 3, 4, 5])
```

> **Performance Note**: Sets use hash tables internally, making membership testing (`element in set_name`) much faster than lists for large collections.

## Unpacking and Packing

### Tuple Unpacking

```python
point = (7, 14, 21)
x, y, z = point  # x=7, y=14, z=21
```

### NumPy Array Packing

```python
import numpy as np
data_array = np.array([1, 2, 3, 4, 5])
```

### Star Unpacking

```python
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
# first = 1, middle = [2, 3, 4, 5], last = 6
```

### Dictionary Unpacking

```python
student_grades_1 = {'Math': 90, 'English': 92}
student_grades_2 = {'Science': 88, 'History': 94}

# Merging dictionaries (Python 3.5+)
combined_grades = {**student_grades_1, **student_grades_2}
# {'Math': 90, 'English': 92, 'Science': 88, 'History': 94}

# In Python 3.9+, you can also use:
# combined_grades = student_grades_1 | student_grades_2
```

## Code Style

### Line Continuation

```python
# Explicit line continuation with backslash
total = a + b + \
        c + d

# Long string with line continuation
long_string = "This is a really long string that just keeps going " \
              "and going and doesn't seem to stop anywhere soon."
```

### Docstrings

```python
def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int): The first number to add.
    b (int): The second number to add.

    Returns:
    int: The sum of a and b.
    """
    return a + b
```