l1 = ["A", "B", "C", "D"]
l2 = [1, 2, 3]
# print(len(l2))
# j = int(input("write a num: "))
# print(j)
newlist = []
for i in range(len(l1)):
    newlist.append(l2[i])
    newlist.append(l1[i])
print(newlist)
