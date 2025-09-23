print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print('It\'s alright')
print("He is called \"Johnny\"")
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print(r"C:\Users\name")
print("""\This is a multi-line string.
It can span multiple lines.""")
print('''\This is a multi-line string.
It can span multiple lines.''')
print("Hello" + " " + "World")
#---------------------------------------------------

a = "Hello, World!"
print(a[1])
print(a[-1])
print(a[0:5])

for x in "banana":
  print(x)
print(len(a))
print(a.lower())
print(a.upper())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))
print("Hello" in a)
print("hello" not in a)
print(a.startswith("Hello"))
print(a.endswith("World!"))
print(a.find("W"))
print(a.count("l"))
print(a.index("W"))
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.islower())
print(a.isupper())
print(a.isspace())
print(a.title())
print(a.capitalize())
print(a.center(50))
print(a.zfill(50))
print(a.encode())
print(a.format())
print(a.format_map({'name': 'John'}))
print(a.removeprefix("Hello, "))
print(a.removesuffix("World!"))
print(a.partition(", "))
print(a.rpartition(", "))
print(a.splitlines())
print(a.swapcase())
print(a.translate(str.maketrans("Helo", "Jalo")))
print(a.casefold())
print(a.isprintable())
print(a.isidentifier())
print(a.isnumeric())
print(a.isdecimal())
print(a.lstrip("H"))
print(a.rstrip("!"))
print(a.rjust(50))
print(a.ljust(50))
print(a.expandtabs(4))
print(a.split(",", 1))
print(a.rsplit(",", 1))
print(a.removeprefix("Hello, "))
print(a.removesuffix("World!"))
print(a.encode("utf-8"))
print(a.encode("utf-16"))
print(a.encode("ascii", "ignore"))
print(a.encode("ascii", "replace"))
print(a.encode("ascii", "backslashreplace"))
print(a.encode("ascii", "xmlcharrefreplace"))
print(a.translate(str.maketrans("Helo", "Jalo")))
print(a.translate(str.maketrans("", "", "Helo")))
print(a.translate(str.maketrans("Helo", "Jalo", "l")))
print(a.casefold())
print(a.isprintable())
print(a.isidentifier())
print(a.isnumeric())
print(a.isdecimal())
print(a.lstrip("H"))
print(a.rstrip("!"))
print(a.rjust(50))
print(a.ljust(50))
print(a.expandtabs(4))
print(a.split(",", 1))
print(a.rsplit(",", 1))
print(a.encode("utf-8"))
print(a.encode("utf-16"))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#---------------------------------------------------
#Slices

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenation
#---------------------------------------------------


a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Formatting
#---------------------------------------------------

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 49.9467899
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#Escape Characters
#---------------------------------------------------

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello\rWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#String Methods
#---------------------------------------------------

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print(a.lstrip()) # returns "Hello, World! "
print(a.rstrip()) # returns " Hello, World!"
print(a.replace("H", "J")) # returns " Jello, World!"
print(a.split(",")) # returns [' Hello', ' World! ']
print(a.lower()) # returns " hello, world! "
print(a.upper()) # returns " HELLO, WORLD! "
print(a.capitalize()) # returns " hello, world! "
print(a.title()) # returns " Hello, World! "
print(a.count("o")) # returns 2
print(a.find("W")) # returns 8
print(a.index("W")) # returns 8
print(a.startswith(" Hello")) # returns True
print(a.endswith("World! ")) # returns True
print(a.isalpha()) # returns False
print(a.isdigit()) # returns False
print(a.isalnum()) # returns False
print(a.isspace()) # returns False
print(a.center(50)) # returns a centered string of length 50
print(a.zfill(50)) # returns a string of length 50, padded with zeros on the left
print(a.encode()) # returns a bytes object
print(a.format()) # returns " Hello, World! "
print(a.format_map({'name': 'John'})) # returns " Hello, World! "
print(a.removeprefix(" Hello")) # returns ", World! "
print(a.removesuffix("World! ")) # returns " Hello, "
print(a.partition(", ")) # returns (' Hello', ', ', 'World! ')
print(a.rpartition(", ")) # returns (' Hello', ', ', 'World! ')
print(a.splitlines()) # returns [' Hello, World! ']

