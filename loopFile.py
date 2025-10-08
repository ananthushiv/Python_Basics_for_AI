from __future__ import print_function
n=5
for i in range(0, n):
    print(i)

li = ["geeks", "for", "geeks"]
for item in li:
    print(item)

tup = ("geeks", "for", "geeks")
for item in tup:
    print(item)

s = "abc"
for char in s:
    print(char)

d = dict({'x':123, 'y':354})
for key in d:
    print(f"{key} : {d[key]}")

for x in d:
    print("%s  %d" % (x, d[x]))

li = ["geeks", "for", "geeks"]
for index, item in enumerate(li):
    print(index, item)

for index in range(len(li)):
    print(li[index])

cnt = 0
while cnt < 5:
    print(cnt)
    cnt += 1


for i in range(5):
    for j in range(i):
        print(i, end=' | ')
    print()
print("Looping done.")# --- IGNORE ---

for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)