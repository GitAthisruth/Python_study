from cryptography.fernet import Fernet


# b"hello"#byte string

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key


key = load_key() 
fer = Fernet(key)



def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            # print(line.rstrip())
            data = line.rstrip()
            user,passw = data.split("|")
            print(f"User:{user} Password:{passw}",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt",'a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view,add)?,press q to quit ").lower()

    if mode == "q":
        break

    elif mode == "view":
        view()
    

    elif mode == "add":
        add()
        

    else:
        print("Invalid mode.")
        continue
