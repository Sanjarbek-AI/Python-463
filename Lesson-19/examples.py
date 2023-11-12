"""
------------------------------------------------------------------------------------
try:
    num = int("abc")  # Raises ValueError
except ValueError:
    print("Invalid value!")
------------------------------------------------------------------------------------
try:
    result = "Hello" + 5  # Raises TypeError
except TypeError:
    print("Unsupported operation!")
------------------------------------------------------------------------------------
try:
    mylist = [1, 2, 3]
    item = mylist[5]  # Raises IndexError
except IndexError:
    print("Index out of range!")
------------------------------------------------------------------------------------
try:
    mydict = {"name": "John", "age": 25}
    value = mydict["city"]  # Raises KeyError
except KeyError:
    print("Key not found!")
------------------------------------------------------------------------------------
try:
    file = open("myfile.txt", "r")  # Raises FileNotFoundError
except FileNotFoundError:
    print("File not found!")
------------------------------------------------------------------------------------
try:
    file = open("myfile.txt", "r")
    content = file.read()
    file.write("Hello")  # Raises IOError
except IOError:
    print("Input/output error!")
------------------------------------------------------------------------------------
try:
    result = 10 / 0  # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Division by zero!")
-------------------------------------------------------------------------------------
try:
    x = 5
    x.append(10)  # Raises AttributeError (int object has no attribute 'append')
except AttributeError:
    print("Attribute error!")
-------------------------------------------------------------------------------------
"""