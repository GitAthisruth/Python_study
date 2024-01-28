# youtuber = "RaptorXGamer"
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# adj=input("adjective: ")

# verb1=input("Verb1: ")
# verb2=input("Verb2: ")
# famous_person=input("Name: ")


# madlib=f"computer programming is so {adj}! It means me so excited all the time because\
#     I love to {verb1}.Stay hydrated and {verb2} like you are an {famous_person}! "

# print(madlib)

# import random

# def guess(x):
#     random_number = random.randint(1,x)
#     print(random_number)
#     guess = 0
#     # A function can only return one output at a time.
#     while guess != random_number:
#         guess=int(input("guess a number between 1 and {x}: "))
#         if guess < random_number:
#             return "Sorry,guess again. Too low."
#         elif guess > random_number:
#             return "Sorry,guess again.Too low"
#     return f'yay,congrats.Yo have guessed the number {random_number} correctly'


# print(guess(10))


# import random

# def guess(x):
#     random_number = random.randint(1,x)
#     print(random_number)
#     guess = 0
#     # A function can only return one output at a time.
#     while guess != random_number:
#         guess=int(input("guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry,guess again. Too low.")
#         elif guess > random_number:
#             print("Sorry,guess again.Too low")
#     print(f'yay,congrats.Yo have guessed the number {random_number} correctly')


# guess(10)

# a="abc"
# print(a,end = "\n") #\n - new line
# print("Hi how are you?")

# import random


# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ""
#     while feedback != "c":
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  # could also be high b/c low = high
#         feedback = input(
#             f"Is {guess} too high (H),too low (L),or correct (C) ?? "
#         ).lower()
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             low = guess + 1

#     print(f"Yay! The computer guessed your number,{guess},correctly!")

# computer_guess(1000)

# import random

# def play():
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
#     print(user)
#     computer = random.choice(['r','p','s'])
#     print(computer)

#     if user == computer:
#         return 'It\'s a tie'

#     elif is_win(user,computer):
#         return 'You won!'

#     else:
#         return "You lost"


# def is_win(player,opponent):
#     #return true if player wins
#     #r > s, s > p, p > r

#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
#     or (player == 'p' and opponent == 'r'):
#         return True


# print(play())


import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    # print(word)
    # print("hiiiii")
    word_letters = set(word) #letters in the word
    # print(word_letters)
    # print("hiiiii")
    alphabet = set(string.ascii_uppercase)
    # print(alphabet)
    # print("hiiiii")
    used_letters = set() # what the user has guessed
    print(used_letters)
    lives=6
    # print("hiiiii")
    #getting user input
    while len(word_letters) > 0 and lives>0:
        #letters used
        print('You have used these letters: ',' '.join(used_letters))
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        # print(user_letter)
        # print("hiiiii")
        if user_letter in alphabet - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letters:
              word_letters.remove(user_letter)
    
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print('Invalid character,Please try again.')
    if lives == 0:
        print('You died, sorry', word)
    else:
        print('You guessed the word',word,'!!')    

user_input = input('Type something: ')
print(user_input)

hangman()

 


