# import random
# import string

# def generate_password(min_length,numbers=True,special_characters = True):
#     letters = string.ascii_letters
#     digits = string.digits
#     special = string.punctuation
#     # print(f"letters {letters}\n digits {digits}\n special {special}")
#     characters = letters
#     if numbers: #if we use if statement here check both if conditions.
#         characters += digits
#         # print(f"if numbers {characters} \n")
#     if special_characters:
#         characters += special
#         # print(f"if special charac {characters} \n")


#     pwd = ""
#     meets_criteria = False
#     has_number = False
#     has_special = False
#     # print(f"before while loop Characters {characters}")
#     while not meets_criteria or len(pwd) < min_length:
#         # print(f"minimum length {min_length}\npwd: {pwd}\nlength of pwd {len(pwd)}")
#         new_char = random.choice(characters)
#         pwd += new_char

#         if new_char in digits:
#             has_number = True
#         elif new_char in special:
#             has_special = True
#         meets_criteria = True
#         if numbers:
#             meets_criteria = has_number
#         if special_characters:
#             meets_criteria = meets_criteria and has_special

#     return pwd
# min_length = int(input("Enter the minimum length: "))
# has_number = input("Do you want to have numbers (y/n)?").lower() == "y"
# has_special = input("Do you want to have special characters (y/n)?").lower() == "y"
# print(f"has_number {has_number}\n has_special {has_special}")
# pwd = generate_password(min_length,has_number,has_special)
# print("The generated password is:",pwd)