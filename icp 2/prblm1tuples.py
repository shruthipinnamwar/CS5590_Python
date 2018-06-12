list1 = ["PHP", "exercise","backend"]
finallist = []
print("------------------------------------------Problem 1 List Operations-------------------------------------------------------------")

print(list1)
for x in list1:
    list2 = []

    list2.append(len(x))
    list2.append(x)
    finallist.append(list2)

print("Appended Length to list",finallist)
finallist.sort()
print("Sorted list ",finallist)

last = len(finallist)-1
print("Last tuple",finallist[last])

