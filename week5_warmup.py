# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
text = "abracadabra"
print(text[4])
# b. Retrieve the second to last character.
print(text[-2])
# c. Find the first occurrence of the letter 'c'.
print( text.find("c"))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
text="abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(text[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(text[0:14:2])
# c. Reverse the entire string using slicing.
print(text[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text="ask not what your country can do for you - ask what you can do for your country. - John F. Kennedy"
print( text.find("John F. Kennedy"))
print( text[83:98])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.c",
info = "Python is fun. Fun is good. Good is subjective.c"
info_t= info
# a. Extract the word 'subjective' without knowing its exact position.
info= info_t.find("subjective")
(info_t)
print(info_t[36:46])
# b. Extract every third word.
print(info_t[0::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(info_t[::-1])

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text= "MAY THE FORCE BE WITH YOU."
lowercase_text=text.lower()
print(lowercase_text)

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto= ["make"," haste", " slowly"]
single_string='' .join(motto) 
print(single_string)
# b. Now, split the string at every occurrence of the letter 'a'.
single_split= single_string.split("a")
print("join string", single_string)
print ( "split string", single_split)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
text= "Life is what happens when you are busy making other plans."
single_replace= text.replace("busy","distracted")
print( single_replace)
# b. Replace "plans" with "mistakes".
text= "Life is what happens when you are busy making other plans."
single_replace= text.replace("plans","mistakes")
print( single_replace)
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
text="Iteration"
print(text * 7)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text= "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(text.find("moonlight"))
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
text= "Supercalifragilisticexpialidocious."
print(len(text))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
count=text.count("i")
print(count)