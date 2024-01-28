# import random
# value=random.random()  #it will print random values between zero and one
# print(value)


# value=random.uniform(1,10)
# print(value) #will generate random values between one and ten

# value=random.randint(1,10)
# print(value) # integer values between one and ten

# value=random.randrange(1,10)#print value between 1 t0 9
# print(value)

# values=['red','blue','black','green','orange','yellow']
# v=random.choices(values,k=3)# will print random list value from the given list
# #(k is no if values)
# print(v) 

# values=['red','blue','black','green','orange','yellow']
# v=random.choices(values,k=2)
# print(v)

# values=['red','blue','black','green','orange','yellow']
# v=random.choice(values) # it will return just one value
# print(v)

# values=['red','blue','black']
# v=random.choices(values,weights=[20,20,2],k=2) #it will give the priority to the most weighted elements
#         #and return that list of elements
# print(v)

# values=['hi','hello','howdy','hola','hey']
# v=random.choice(values) #it will return one value
# print(v,"abin")

# a=list(range(1,20))
# random.shuffle(a) #will return shuffled values

# print(a)

# a=list(range(1,20))
# v=random.sample(a,k=8) #return any 'k'  number of values random values with in the range
# print(v)

###############################################################

######use case 1############

##random lotterty pick

# from time import sleep
# import random
# lottery_tickets=[]
# print("creating lottery tickets.....")
# for i in range(100):
#   lottery_tickets.append(random.randrange(100000,999999)) #randrange returns only one value at a time
# v=random.sample(lottery_tickets,k=2)
# print("finding the winners... please weight")
# sleep(5)
# print(f"the winners are {v}")


#####use case 2 #################

# import random


# firstname=['devin','Dainty','Abin','Jessica','Ashna','Afitha']
# lastname=['mathew','Mathew','Eldhose','Joseph','Hasif','Jabbar']
# streetname=['High','Low','Lose','Hola','Warks','Rody']
# states=['Kerala','Tamilnadu','Karnataka','Andhra','Delhi','Maharashtra']
# fakecities=["Logsow",'Florida','Poland','Germany','Prague','Asutria']

# for i in range(6):
#     first=random.choice(firstname)
#     last=random.choice(lastname)
#     phone=f"{random.randint(100,999)} --55--  {random.randint(100,999)}"

#     street=random.choice(streetname)
#     state=random.choice(states)
#     city=random.choice(fakecities)
#     zipcode=random.randint(100000,999999)
#     address=f'{zipcode} {street} {city} {state}'
    # email= first+last+"@fakemail.com"
    # print(f'Name:-{first} {last}\n Phone:- {phone}\n Email:- {email}\n Address:- {address}')
    # print()


