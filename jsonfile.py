# jdata='''
# {
#     "people":[
#         {
#         "name":"devin",
#         "phone":"1234567890",
#         "email":"devin@gmail.com",
#         "has_license":true
#         },
#         {
#         "name":"dainty",
#         "phone":"1234444444",
#         "email":null,
#         "has_license":false
        
#         }
#     ]
# }'''

#null denotes none in json 
#JavaScript Object Notation (JSON) is a standard text-based format 
# representing structured data based on JavaScript object syntax

# print(type(jdata))

# import json

# data=json.loads(jdata)
#here json convert the string to dictionary format.
# print(data)
# print(type(data))

#loads() json. loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary

# print(data['people'])

# for person in data['people']:
    # print(person)
    # print(person['name'])
   

# import json

# data=json.loads(jdata)
# for person in data['people']:
#     del person['phone']

# newjdata=json.dumps(data)
# print(newjdata)

# newjdata=json.dumps(data,indent=2,sort_keys=True)
#sort keys used to get data in alphabetical order
# print(newjdata)

# import json

# with open("states.json") as f:
#     data=json.load(f)
#     for people in data['states']:
#         del people['areacode']
#         with open('newstates.json','w') as nf:
#             json.dump(data,nf,indent=2)

#The dump() method is used when the Python objects have to be stored in a file.
# The dumps() is used when the objects are required to be in string format and is used for parsing, printing, etc,.
# The dump() needs the json file name in which the output has to be stored as an argument.

#load() is used to read the JSON document from file and 
# The json. loads() is used to convert the JSON String document into the Python dictionary.