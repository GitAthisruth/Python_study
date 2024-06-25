# print(help(print))
#range
# print(list(range(1,-10,-1)))from 1 to -10
#map
# strings = ["my","world","apple","pear","pneumonoultramicroscopicsilicovolcanoconiosis"]
# lengths = map(len,strings)
# print(list(lengths))

# lengths = map(lambda x : x + "s"  ,strings)
# print(list(lengths))

#filter

# def string_4(val):
#     return len(val) > 4


# strings = ["my","world","apple","pear","pneumonoultramicroscopicsilicovolcanoconiosis"]
# filtered = filter(string_4,strings)
# print(list(filtered))

#sum

# numbers = {1,4,5,23,2}
# print(sum(numbers,start=-10))

#sorted

# numbers = [1,4,5,23,2,-1,5,3,0]
# sorted_nums = sorted(numbers,reverse = True)
# print(sorted_nums)

# people = [
#     {"name":"Alice","age":30},
#     {"name":"Bob","age":35},
#     {"name":"David","age":20}
# ]




# sorted_people = sorted(people,key = lambda person:person["age"])#sorted based on age
# print(sorted_people)


#enumerate

# tasks = ["Write report","Attend meeting","Review code","Submit timesheet"]

# for index,task in enumerate(tasks):
#     print(f"{index+1},{task}")


# names = ["Alice","Bob","Charlie","David","Tim"]
# ages = [30,25,35,20]

# for idx in range(min(len(names)),len(ages)):
#     name = names[idx]
#     age = ages[idx]
#     print(f"{name} is {age} years old")

#zip

# names = ["Alice","Bob","Charlie","David","Tim"]
# # print("tuple",tuple(names))
# ages = [30,25,35,20]
# gender = ["Female","Male","Male"]

# # combined = zip(names,ages)#convert to an ordered tuple
# combined = list(zip(names,ages,gender))
# print(combined)

# for name, age,gender in combined:
#     print(f"{name} is {age} years old and is {gender}")

#open

file = open("testingmegatron.txt","w")
file.write("hello world\nmy name is Tim")
