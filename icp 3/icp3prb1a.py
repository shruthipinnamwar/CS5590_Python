dict = {}
sentence = input("Give a sentence:")
words = sentence.split()
print(words)

for x in sorted(words):
    if x in dict:
       dict[x] += 1
    else:
       dict[x] = 1

print(dict)













