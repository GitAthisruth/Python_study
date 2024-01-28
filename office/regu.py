# #Regular Expression


# # import re #used to find out the patterns 


# # print('\ttelevision')

# # print('hii\new')

# # print('\ttab')

# # print(r'new\tab')#we can use rowstring('r') to unconsider the special characters in a string (like \t,\n ...).

# # print('tab\new')

#Regular expression used to fetch special characters or names from a string.

# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 900-555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''

# patternce=re.compile(r"abc")

#We can combine a regular expression pattern into pattern objects, which can be used for pattern matching.
# It also helps to search a pattern again without rewriting it.

# matches=patternce.finditer(text_to_search)

#The finditer() function matches a pattern in a string and returns an iterator that yields the Match objects of all non-overlapping matches.
# In this syntax: pattern is regular expression that you want to search for in the string. string is the input string.


# Iterable is an object which can be looped over or iterated over with the help of a for loop. Objects like lists, tuples, sets, dictionaries, strings, etc. are called iterables.
# In short and simpler terms, iterable is anything that you can loop over.
# An iterator is an object that contains a countable number of values. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__() .


# for match in matches:
#     print(match)

# print(text_to_search[1:4])   


# patternce=re.compile(r".")#using '.' to fetch all characters inside a string.

# matches=patternce.finditer(text_to_search)
# for match in matches:
#     print(match)


# # patternce=re.compile(r"\.")#using a backward slash before '.' to match a '.' in it.

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)

# patternce=re.compile(r".com") #'.' is used to match 

# matches=patternce.finditer(text_to_search)
# for match in matches:
#     print(match)


# print(text_to_search[151:155])

# # patternce=re.compile(r"\d")#'\d' used to match all integers(digits) in a string. 

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)


# # patternce=re.compile(r"\D")#all characters except numbers.

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)


# # patternce=re.compile(r"\w")#'\w' avoids all special  characters fetch all words ,digits and underscore.

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)


# # patternce=re.compile(r"\W")#'\W' match   all special  characters

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)


# # patternce=re.compile(r"\s")#'\s' mention all spaces,new line(\n) and tabs(\t)

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)


# # patternce=re.compile(r"\S")#'\w' avoid all spaces,new line and tabs.

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)


# patternce=re.compile(r"\bHa")#'\b' only take Ha with a boundary.( (Ha) (Ha)Ha).(have space in the starting)
#                              #take all boundary words.(\bHa is our pattern)

# matches=patternce.finditer(text_to_search)
# for match in matches:
#     print(match)

# print(text_to_search[69:71])


# # patternce=re.compile(r"\BHa")#'\B'  take all Ha without a boundary.( Ha Ha(Ha))
# #                              ##take all unboundary words.(\bHa is our pattern)

# # matches=patternce.finditer(text_to_search)
# # for match in matches:
# #     print(match)
# import re

# sentence='Start a sentence and then bring it to an end'

# patterns=re.compile(r'^Start')#'^' used to match the starting word or letter of a string.('^' -Circumflex)
#                                           # otherways no output.
# matches=patterns.finditer(sentence)
# for match in matches:
#     print(match)

# print(sentence[0:5])

# patternce=re.compile(r"^Sta") #it also match starting words like this.
# matches=patternce.finditer(sentence)
# for match in matches:
#     print(match)



# sentence='Start a sentence and then bring it to an end'

# patterns=re.compile(r'end$')#'$' used to match the ending word or letter of a string .
#                                           #otherways no output.
# matches=patterns.finditer(sentence)
# for match in matches:
#     print(match )   

# sentence='Start a sentence and then bring it to an end'

# # patterns=re.compile(r'd$'))#'$' used to find the ending word or letter of a string only match.
# #                                           #otherways no output.
# # matches=patterns.finditer(sentence)
# # for match in matches:
# #     print(match )   


# import re
# patterns=re.compile(r'nd$')#it will work this way also.
# matches=patterns.finditer(sentence)
# for match in matches:
#     print(match )   


# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 900-555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''


# patterns=re.compile(r'\.\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W')
# matches=patterns.finditer(text_to_search)
# for match in matches:
#     print(match )   


# patterns=re.compile(r'\d\d\d\W\d\d\d\W\d\d\d\d')##here we can specify special patterns seperately.#here we can use '.' instead of '\w'.
# matches=patterns.finditer(text_to_search)
# for match in matches:
#     print(match )   



# patterns=re.compile(r'\d{3}.\d{3}.\d{4}')##'\d{3}' here we specify first 3 digits,'.'specify all characters like that we can fetch special patterns.
# matches=patterns.finditer(text_to_search)
# for match in matches:
#     print(match )   

# import re
# patterns=re.compile(r'\d{3}.\d{3}.\d{4}')
# with open("C:/Users/athis/Downloads/data.txt",'r') as file:#This is a manual method to download a file using location instead of a filename.
                                                             #'file location.<file_name>.txt' (use forward slash('/') instead of backward slash)
#      contents=file.read()
#      matches= patterns.finditer(contents)

# for match in matches:
#     print(match)
     



# pattern=re.compile(r'Eric')
# with open('C:/Users/athis//Downloads/data.txt','r') as file:
#      content=file.read()
#      matches=pattern.finditer(content)
# for match in matches:
#     print(match)     




# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ -] \ / ( )
# coreyms.com
# 321--555--4321
# 123.555.1234
# 123*555*1234
# 900-555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''


# import re

# pattern=re.compile(r"\d{3}[--].\d{3}[--].\d{4}")
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# # print(text_to_search[157:171])

# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ ] \ / ( )
# coreyms.com
# 321-555--4321
# 123.555.1234
# 123*555*1234
# 800*-555-1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''




# pattern=re.compile(r'[89]00[*--].\d{3}[-]\d{4}')#here [*--] check a digits with  * then - and last again -(we should give it orderly otherwise it fetch error ) 
# matches=pattern.finditer(text_to_search)        
# for match in matches:
#     print(match)









# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ -] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''


# import re

# pattern=re.compile(r"[89]00[--].\d{3}[-]\d{4}")#[89] inside the square bracket we can mention the starting character of words or letter.
#                                             #here we give a digit starting with 8 or a digit with 9 it first check for 8 the 9 we need to keep the order correctly.(here we can't give like this '[--.]')
#                                             #   here '00' fetch the actual values in the string([89]00 means 800 and 900 ).
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# print(text_to_search[196:209])

###########################################################################################


# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ -] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800--555-1234
# 900--555-1234,3455266626
# Mr. Schafer
# Mr Smith
# ms Davis
# Mrs. Robinson
# Mr. T
# '''


# import re

# pattern=re.compile(r"[1-5]")#return values from 1 t0 5.
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# pattern=re.compile(r"[a-z]")#return values from small letter a t0 z.
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# pattern=re.compile(r"[A-Z]")#return values from capital A to  Z.
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# pattern=re.compile(r"[a-zA-z]")#return values from a to z (Both cases)
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# pattern=re.compile(r"[^1-5]")#return all  values except 1 t0 5.
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# pattern=re.compile(r"[^a-z]")#return all  values except a t0 z.('^' means 'not')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)





# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ -] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith 
# ms Davis
# Mrs. Robinson
# Mr. T
# cat
# pat
# mat
# bat
# '''


# import re

# pattern=re.compile(r'[cpm]at')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# pattern=re.compile(r'[^b]at')
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

###############################################################################################

#Regex codes

# .  - Any characters except new line.

# \d - Digit (0-9)  

# \D -Not a digit(0-9)

# \w -Word character (a-z,A-Z,0-9,_)

# \W -not a word character(return only special characters)

# \s -Whitespace(space,tab,newline)

# \S - return except Whitespace(space,tab,newline)

# [] - Matches Characters in brackets 

# [^ ] - Matches Characters Not in brackets 

# | - Either or

# ( ) - Group


#Quantifiers

# * - 0 or more

# + - 1 or more

# ? - 0 or 1

# {3} - exact  number

# {3,4} - range of numbers(minimum,maximum)


# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa .077
# MetaCharacters (need to be escaped):
# . ^ $ * + ? { } [ -] \ / ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800--555-1234
# 900--555-1234
# Mr. Schafer
# Mr Smith 
# ms Davis
# Mrs. Robinson
# Mr. T

# '''

# import re

# pattern=re.compile(r"(Mr|ms|Mrs)\.?")#here '(Mr|ms|Mrs)' this means grouping.here we group the words with possibilities.
#                                     #    (Mr|ms|Mrs) means Mr or ms or Mrs match for them.
#                                      #'\.?', '?' means with or without '.'.

# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# pattern=re.compile(r"(Mr|ms|Mrs)\.?\s[A-Z]\w*")##we are using this way to match the name to avoid any other mismatchings.
# matches=pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# import re

# emails ='''
# miketyson@gmail.com 
# miketyghhffson@gmail.com 
# henry.cavill@university.edu
# jason-321-statham@my-work.net
# '''

# pattern=re.compile(r"(mik|hen|jas).*(com|edu|net)")
# matches=pattern.finditer(emails)
# for match in matches:
#     print(match)



# emails ='''
# miketyson@gmail.com ,fsgsshshsh
# miketyghhffson@gmail.com 
# henry.cavill@university.edu,fgghhh
# jason-321-statham@my-work.net,fggg
# '''

# import re

# pattern=re.compile(r"[\w+-.].+[\w+-]\.+(com|edu|net)")#'[\w+-.]+' this combination checks one or more than one times,in this '+'(1 or more).
# matches=pattern.finditer(emails)                      #('+' is a quantifier here)
# for match in matches:
#     print(match)


# pattern=re.compile(r"[\w+-.]+@[\w+-]+.(\w*)")
# matches=pattern.finditer(emails)
# for match in matches:
#     print(match)


# urls ='''
# https://www.google.com
# http://isro.com
# https://youtube.com
# https://www.nasa.gov
# '''


# pattern=re.compile(r"[h]ttp.*\w*.\w*.\w*")
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)

# pattern=re.compile(r"[h]ttp.*\S*.\S*.\S*")
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)



# urls ='''
# https://www.google.com
# http://isro.com
# https://youtube.com
# https://www.nasa.gov
# '''
# import re



# pattern=re.compile(r'(https|http).*\w*.(com|nasa.gov)')
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)


# pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)



# pattern=re.compile(r'https?.*(www\.)?(\w+)(\.\w+)')
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)


# pattern=re.compile(r'[h]ttps?.{3}[\w+.]+(com|gov)')##In 'ttps?', '?' apply to s only. s takes 0 or 1 times only.
# matches=pattern.finditer(urls)
# for match in matches:
#     print(match)



###################################################################################

#Search


# import re

# sentence='Start a sentence and then bring it to an end'

# patterns=re.compile(r'Start')#this is a search method.
# matches=patterns.finditer(sentence)
# for match in matches:
#     print(match )   





# patterns=re.compile(r'^start',re.IGNORECASE)#'re.IGNORECASE' we can use this method to avoid the case sensitive when matching.
# matches=patterns.finditer(sentence)
# for match in matches:
#     print(match )   

# pattern=re.compile(r'THEN',re.IGNORECASE)

# matches=pattern.finditer(sentence)

# for match in matches:
#     print(match)