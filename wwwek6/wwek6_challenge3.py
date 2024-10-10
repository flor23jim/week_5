#Flor Jimenez, Ashley Lopez, Cedahlia Iniguez, Cristal Calderon
text=(input("Give me a sentence. :"))
text=text.lower()  # we need to ask for a sentence and have it be all lowercase 
text_list=list(text) # creates a list from the text provided by the user
print(text_list) # print  out the list 
print("Please give me three random letters and enter them one by one") # ask for the letters you are trying to find
first=(input("first letter")).lower () # get each letter in lowercase
second=(input("second letter")).lower() # get each letter in lowercase
third=(input("third letter")).lower () # get each letter in lowercase
count1= (text_list.count(first)) #how many time the letter is in the sentence
print(count1)
count2= (text_list.count(second))#how many time the letter is in the sentence
print(count2)
count3= (text_list.count(third))#how many time the letter is in the sentence
print(count3)
print(len(text))  #how long the sentence is 
print(text[0]) # the first letter
print(text[-1]) # the last letter
print(text[::-1]) # revered 
word=("python")
if word in text:
    print('python is in the text')
else:
    print("python is not in the text")
 # See of python is in the sentence
# input = asks for the readers to provide information such as a sentence (when you type something with your keyboard)
# output
# abstration = list, .lower()  = the abstraction was used to make finding the letter easier and makign all of the letter lowercase incase the user input capital letters
# what is your list and why are you using it = For our list we tranformed our text(output) into a list ot make it easier to find the letters
# what is the purpose of your list = the purpose of the list to to find words faster



