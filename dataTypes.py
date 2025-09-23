# Data types
# Python has various data types including:
# - int (Integer)
# - float (Floating point number)
# - str (String)
# - list (List)
# - tuple (Tuple)
# - dict (Dictionary)
# - set (Set)
# - bool (Boolean)
# - NoneType (None)
# Each data type serves a different purpose and is used to store different kinds of data.
# You can check the data type of a variable using the type() function.
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
#---------------------------------------------------

x = 5

#display x:
print(x)

print(type(x))

x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x))

x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = range(10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))
#display the data type of x:
print(type(x))


x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x))

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x))

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x))

x = True

#display x:
print(x)

#display the data type of x:
print(type(x))

x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x))

x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x))

x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x))

x = None

#display x:
print(x)

#display the data type of x:
print(type(x))



#Setting the data type
#---------------------------------------------------

x = str("Hello World")

#display x:
print(x)

#display the data type of x:
print(type(x)) 
x = int(20)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = float(20.5)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = complex(1j)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = list(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x))

x = tuple(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x))

x = range(6)
#display x:
print(x)
#convert to list to display the content of x:

print(list(x))
#display the data type of x:
print(type(x))

x = dict(name="John", age=36)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = set(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x))

x = bool(5)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = bytes(5)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = bytearray(5)
#display x:
print(x)
#display the data type of x:
print(type(x))

x = memoryview(bytes(5))
#display x:
print(x)
#display the data type of x:
print(type(x))

x = None
#display x:
print(x)
#display the data type of x:
print(type(x))

#---------------------------------------------------

