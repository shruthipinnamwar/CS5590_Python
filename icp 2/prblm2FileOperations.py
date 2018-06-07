fname = "test5.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
        data = line + str(len(line))
        print(line, len(line))
    writefile = open("write5.txt", "w+")
    writefile.write(data)




# print(num_lines)
# print(num_words)
# print(num_chars)





# f= open("test5.txt", "r")
# num_lines = len(f.splitlines())
# num_words = 0
# num_chars = 0
# for line in lines:
#         num_words += len(line.split())

#         words = line.split()
#         num_lines += 1
#         num_words += len(words)
#         num_chars += len(line)
# print(words)
# print(num_lines)
# print(num_words)
# print(num_chars)
