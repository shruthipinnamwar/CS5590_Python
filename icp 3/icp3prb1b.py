#
line = input("type a line:")
s = set()
count = 0
vowels = {'a','e','i','o','u'}
for x in sorted(line):
     s.add(x)

for x in s:
     if  x in vowels:
         count = count+1

print(count)











