x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#casting:
#---------------------------------------------------
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


#getType:
#---------------------------------------------------
print(type(x))
print(type(y))
print(type(z))

#Variable names:
#---------------------------------------------------
myvar = "John1"
my_var = "John2"
_my_var = "John3"
myVar = "John4"
MYVAR = "John5"
myvar2 = "John6"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Variable names are case-sensitive
#---------------------------------------------------
a = 4
A = "Sally" # A is different from a
print(a)
print(A)

#Many values to multiple variables
#---------------------------------------------------
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One value to multiple variables
#---------------------------------------------------
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a collection
#---------------------------------------------------
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output variables
#---------------------------------------------------
x = "Python is \"awesome\""
print(x)
x = 'Python is \'awesome\''
print(x)

x = "Python is \nawesome"
print(x)

x = "Python is \tawesome"
print(x)

x = "Hello"
y = "World"
print(x + " " + y)

x = 5
y = 10
print(x + y)
print(x, y)
print(f"{x} {y}")
print("{} {}".format(x, y))
print("{1} {0}".format(x, y))
print("%d %d" % (x, y))
print("The value of x is " + str(x) + " and y is " + str(y))
print("The value of x is {} and y is {}".format(x, y))
print(f"The value of x is {x} and y is {y}")
print("The value of x is %d and y is %d" % (x, y))
print("The value of x is", x, "and y is", y)
#---------------------------------------------------

#Global variables
#---------------------------------------------------
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
#---------------------------------------------------

#Local variables
#---------------------------------------------------

def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
#---------------------------------------------------

#Global vs. Local variables
#---------------------------------------------------

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
#---------------------------------------------------



#Global keyword
#---------------------------------------------------

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
#---------------------------------------------------

