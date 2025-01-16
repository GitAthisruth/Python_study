# string = input("give a string: ").lower()

# for i in enumerate(string):
#     if i in ["a","e","i","o","u"]:
#         print(i)
#         string = string.replace(i,"")
#         print(string) 
#     else:
#         new_val = "." + i
#         print(new_val)
#         string = string.replace(i,new_val)

# print(string)


val = input("give a string: ").lower()
val =val.lower()

new_val = []
for i in val:
    if i in ["a","e","i","o","u"]:
        pass
    else:
        new_val.append("."+i)

print(new_val)
print("".join(new_val))
