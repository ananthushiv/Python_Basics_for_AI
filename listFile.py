#List constructors
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#output: ['apple', 'banana', 'cherry']
print(type(thislist))
#output: <class 'list'>
print(len(thislist))
#output: 3
print(thislist[1])
#output: banana
print(thislist[-1])
#output: cherry
print(thislist[1:3])
#output: ['banana', 'cherry']
print(thislist[:2])
#output: ['apple', 'banana']
print(thislist[1:])
#output: ['banana', 'cherry']
print(thislist[-2:-1])
#output: ['banana']
thislist[1] = "blackcurrant"
print(thislist)
#output: ['apple', 'blackcurrant', 'cherry']
for x in thislist:
  print(x)
#output:
#apple
#blackcurrant
#cherry
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#output: Yes, 'apple' is in the fruits list
thislist.append("orange")
print(thislist)
#output: ['apple', 'blackcurrant', 'cherry', 'orange']
thislist.insert(1, "banana")
print(thislist)
#output: ['apple', 'banana', 'blackcurrant', 'cherry', 'orange']
thislist.remove("banana")
print(thislist)
#output: ['apple', 'blackcurrant', 'cherry', 'orange']
thislist.pop()
print(thislist)
#output: ['apple', 'blackcurrant', 'cherry']
thislist.pop(1)
print(thislist)
#output: ['apple', 'cherry']
del thislist[0]
print(thislist)
#output: ['cherry']
thislist.clear()
print(thislist)
#output: []

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10)]

print(newlist)

