# 🐍 Python Advanced Programming Tips

A guide to more advanced Python concepts and techniques.

## Table of Contents
1. [Enumeration](#1-enumeration)
2. [Flow Control](#2-flow-control)
3. [Comprehensions](#3-comprehensions)
4. [Functions](#4-functions)
   - [Parameters vs Arguments](#parameters-and-arguments)
   - [Positional vs Keyword Arguments](#positional-arguments-vs-keyword-arguments)
   - [Default Parameters](#default-parameters)
   - [Returning Multiple Values](#returning-multiple-values)
   - [Variable-Length Arguments](#variable-length-arguments)
   - [Function Documentation](#function-documentation)
   - [Type Hints](#annotations-and-type-hints)
5. [Lambda Functions](#5-lambda-functions)

## 1. Enumeration

The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object.

```python
colors = ['red', 'green', 'blue', 'yellow']
list(enumerate(colors))
# Output: [(0, 'red'), (1, 'green'), (2, 'blue'), (3, 'yellow')]
```

## 2. Flow Control

### `continue` and `pass` statements

```python
# continue statement causes the loop to skip the rest of its body for that iteration.
for i in range(5):
    if i == 2:
        continue
    print(i)  # Will print 0, 1, 3, 4
    
# The pass statement is a null operation; nothing happens when it executes.
for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    print(i)  # Will print 0, 1, 2
```

## 3. Comprehensions

List comprehensions provide a concise way to create lists.

```python
# Create list of squares using comprehension
squares = [x**2 for x in range(10)]
squares
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Flattening a nested list using nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
flattened
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 4. Functions

### Parameters and Arguments

- **Parameters** are used when defining a function. They are the names created in the function definition.
- **Arguments** are used when calling a function. They are the values you pass into the function's parameters.

### Positional Arguments vs Keyword Arguments

**Important Rule**: Once you've used a keyword argument, you cannot go back to positional arguments. All positional arguments must come before any keyword arguments.

```python
def print_purchase(book_title, author, price):
    print(f"Purchased book: {book_title} by {author} for ${price}")

# Valid: All positional
print_purchase("The Great Gatsby", "F. Scott Fitzgerald", 12.99)

# Valid: Mix of positional and keyword
print_purchase("The Great Gatsby", author="F. Scott Fitzgerald", price=12.99)

# Invalid: Keyword argument followed by positional
# print_purchase("The Great Gatsby", author="F. Scott Fitzgerald", 12.99)
# SyntaxError: positional argument follows keyword argument
```

### Default Parameters

**Important Rule**: Default parameters must follow non-default parameters in the function definition. Attempting to define a default parameter before a non-default one will result in a syntax error.

When you provide default values for parameters, all subsequent parameters must also have default values.

```python
# Valid default parameters
def user_profile(name, language="English", country="Unknown"):
    print(f"Name: {name}, Country: {country}, Language: {language}")

# Invalid default parameters - will cause SyntaxError
# def user_profile_invalid(country="Unknown", name, language="English"):
#     print(f"Name: {name}, Country: {country}, Language: {language}")
# SyntaxError: non-default argument follows default argument
```

### Returning Multiple Values

Python functions can return multiple values. These values are packaged into a tuple, enabling you to unpack them into separate variables.

```python
def get_dimensions():
    return 500, 300, 200  # Returns a tuple (500, 300, 200)

# Unpacking the returned values
width, height, depth = get_dimensions()
print(f"Width: {width}, Height: {height}, Depth: {depth}")
# Output: Width: 500, Height: 300, Depth: 200
```

### Variable-Length Arguments

#### Using `*args` (Arbitrary Positional Arguments)

```python
def concatenate_strings(separator, *args):
    return separator.join(args)

# Concatenate with a hyphen separator
concatenate_strings("-", "2023", "04", "21")
# Output: '2023-04-21'
```

#### Using `**kwargs` (Arbitrary Keyword Arguments)

The `**` operator for argument dictionary packing enables the creation of highly flexible and adaptable functions.

```python
def introduce_yourself(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Introducing a person with multiple attributes
introduce_yourself(name="Alice", age=30, profession="Engineer")
# Output:
# name: Alice
# age: 30
# profession: Engineer
```

#### Unpacking dictionaries with `**`

When unpacking dictionaries with `**`, all keys must match the function's parameters exactly.

```python
def display_info(name, age, profession):
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
    
# Dictionary with exact matching keys
person_info_valid = {'name': 'Alice', 'age': 30, 'profession': 'Engineer'}
display_info(**person_info_valid)  # This works

# Dictionary with extra key
person_info_invalid = {'name': 'Alice', 'age': 30, 'profession': 'Engineer', 'a': 'ss'}
# display_info(**person_info_invalid)  
# TypeError: display_info() got an unexpected keyword argument 'a'
```

### Function Documentation

Python functions can be documented using docstrings, which can be accessed programmatically.

```python
def my_function():
    """This is a simple docstring."""
    pass

# Access the docstring directly
my_function.__doc__
# Output: 'This is a simple docstring.'

# Get help information
help(my_function)
# Output:
# Help on function my_function in module __main__:
# my_function()
#     This is a simple docstring.
```

### Annotations and Type Hints

Type hints allow you to specify expected types for function parameters and return values.

#### Syntax
Type hints are added using a colon `:` after the parameter name followed by the type, and the return type is indicated with an arrow `->` followed by the type before the colon ending the function definition.

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"

# More complex examples
from typing import List, Dict, Tuple, Optional

def process_items(items: List[int]) -> Dict[str, int]:
    result = {}
    for i, item in enumerate(items):
        result[f"item_{i}"] = item * 2
    return result

def get_user_info(user_id: int) -> Optional[Tuple[str, int]]:
    # Returns None or a tuple of (name, age)
    if user_id == 1:
        return "Alice", 30
    return None
```

## 5. Lambda Functions

Lambda functions (also called anonymous functions) are small, one-line functions defined with the `lambda` keyword.

### Syntax
```
lambda arguments: expression 
```

#### Components:
- `lambda`: Keyword that signifies the start of a lambda function
- `arguments`: Parameters that the lambda function can receive (comma-separated)
- `:`: Separates the arguments from the body
- `expression`: Single line of code that gets evaluated and returned

### Examples

#### Using lambda with map()

```python
# map() applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
list(squared)
# Output: [1, 4, 9, 16, 25]
```

#### Using lambda as a sort key function

```python
# Sort a list of tuples based on the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda element: element[1])  # Sort by string value
pairs
# Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

#### Lambda with keyword arguments

```python
# A lambda that accepts variable number of keyword arguments
merge_strings = lambda **kwargs: " ".join(kwargs.values())
merge_strings(a='Python', b='is', c='awesome')
# Output: 'Python is awesome'
```

#### Using lambda with filter()

```python
# filter() creates an iterator of elements for which a function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
list(even_numbers)
# Output: [2, 4, 6, 8]
```