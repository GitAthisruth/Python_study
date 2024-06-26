print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
# print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")



# while True:
#     answer = input("What does GPU stand for? ").lower()
#     if answer == "graphics processing unit":
#         print("Correct!")
#         break # if the answer is correct the while loop will break.otherwise it again and again run the code. 
#     else:
#         print("Incorrect! Please try again.")


max_attempts = 3

attempts = 0

score = 0

# answers =["cpu","gpu","ram"]
user_input = []

while attempts < max_attempts:
    answer = input("What does CPU stand for? ").lower()
    if answer.lower() == "central processing unit":
        user_input.append("cpu")
        score+=1
        print("Correct!")
        break # if the answer is correct the while loop will break.otherwise it again and again run the code. 
    else:
        attempts+=1
        if attempts <max_attempts:
            print(f"Incorrect! Please try again.\nYou have {max_attempts-attempts} attempts remaining")
        else:
            print("you reached your maximum attempts")
            break
if attempts ==3:
    print(f"you corrected {score}\nyour score is {(score/3)*100}%\nBetter Luck Next Time!!!!")
    quit()

while attempts < max_attempts:
    answer = input("What does GPU stand for? ").lower()
    if answer.lower() == "graphics processing unit":
        user_input.append("gpu")
        score+=1
        print("Correct!")
        break # if the answer is correct the while loop will break.otherwise it again and again run the code. 
    else:
        attempts+=1
        if attempts <=max_attempts:
            print(f"Incorrect! Please try again.\nYou have {max_attempts-attempts} attempts remaining")
        else:
            print("you reached your maximum attempts")
            break

if attempts ==3:
    print(f"you corrected {score}\nyour score is {(score/3)*100}%\nBetter Luck Next Time!!!!")
    quit()
    

attempts = 0

while attempts < max_attempts:
    answer = input("What does RAM stand for? ").lower()
    if answer.lower() == "random access memory":
        user_input.append("ram")
        score+=1
        print("Correct!")
        break # if the answer is correct the while loop will break.otherwise it again and again run the code. 
    else:
        attempts+=1
        if attempts <=max_attempts:
            print(f"Incorrect! Please try again.\nYou have {max_attempts-attempts} attempts remaining")
        else:
            print("you reached your maximum attempts")
        
if attempts ==3:
    print(f"you corrected {score}\nyour score is {(score/3)*100}%\nBetter Luck Next Time!!!!")
    quit()


# print(user_input)

if "gpu" and "cpu" and "ram" in user_input:
    print(f"you corrected {score}\nyour score is {(score/3)*100}\nCongratulations!!! You win the quiz!!!")
else:
    print(f"you corrected {score}\nyour score is {(score/3)*100}%\nBetter Luck Next Time!!!!")