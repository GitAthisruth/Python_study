# import json

# json - javascript object notation

# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4,separators=(': ','= '))
# personJSON = json.dumps(person, indent=4,sort_keys=True)
# print(personJSON)#dumps convert a python object to a json string.

# with open('person.json','w') as file:
#     json.dump(person,file,indent=10)#dump used to store and transfer data


#deserialising

# person = json.loads(personJSON)#back to original python object
# print(person)

# with open('person.json','r') as file:
#     person = json.load(file)#it takes a file object and returns the json object.
#     print(person)


# import json

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# user = User('Max',27)

# def encode_user(o):
#     # print(o)
#     # print(isinstance(o,User))are classes
#     if isinstance(o,User):#both 
        
#         return  {'name':o.name, 'age':o.age,o.__class__.__name__:True}
#     else:
#         raise TypeError('Object of type User is not JSON serializable')

# # print(user.age)      
# userJSON = json.dumps(user,default=encode_user)
# print(userJSON)



import json

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('Max',27)

def encode_user(o):
    # print(o)
    # print(isinstance(o,User))
    if isinstance(o,User):#both are class
        
        return  {'name':o.name, 'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self,o):
        if isinstance(o,User):
            return {'name':o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)




# print(user.age)      
# userJSON = UserEncoder().encode(user)
# print(userJSON)
# user = json.loads(userJSON)#used to deserialise a json file to a dictionary.
# print(user)


# userJSON = UserEncoder().encode(user)
# # print(userJSON)

# def decode_user(dct):
#     if User.__name__ in dct:
#         return User(name=dct['name'],age=dct['age'])
#     return dct   

# user = json.loads(userJSON,object_hook=decode_user)#used to deserialise a json file to a dictionary.
# print(type(user))
# print(user)