# while loops = execute some code WHILE some condition remain true
# name= input('enter your name')
# while name=="":
#     print("You did not enter your name")
#     name= input('enter your name:')

# print(f"hello{name}")

#iteration= Loops 
#infinite loops- happens when the output goes on for ever and will lead your computer to crash, you use control c to stop it


# age= int(input("enter your age"))

# while age<0:
#     print("age can not be negative")
#     age= int(input("enter your age"))
# print (f"you are {age} year old")

# food= input( "entyer a food you like(q to quit):")
# while not food=="q":
#     print(f"you like{food}")
#     food= input( "enter a food you like(q to quit):")
# print("bye")



# num= int(input('enter a number betwen 1-10:'))

# while num< 1 or num >10:
#    print(f"{num}is not vaild")
#    num=int(input("enter a number between 1-10:"))

# print(f"your number is {num}")


# FOR loops = execute a block of code a fixed number of times.
#you can iterate over a range string,sequence,etc. 

# credit_card="123-3454-6554-7653"

# for x in credit_card:
#     print(x)

# "continue skips the number or whatever you put"
# for x in range(1,21):
#     if x==13:
#         continue
#     else:
#         print(x)

# for x in range(1,21):
#     if x==13:
#         break # it stop counting once it gets to the number 
#     else:
#         print(x)

#challenge 

list_of_name=['John','paul','george','ringo']
#if the name is "george", print 'geroge was fpund!"
#otherwise,print george was not found! and print out the other name using a loop
list_of_names2=['thanos','iroman','thor','hulk']
#loop thouhg the list_of_names2 an is the name is 'ironman' skip over it 
#and print out the other names 

# for name in list_of_name:
#     if name=='george':
#         print("george was found!")
#     else:
#         print ("george was not found!")
#         print(name)


# for name in list_of_names2: 
#     if name=='iroman':
#         continue
#     print(name)
    
# for name in list_of_names2:
#     if name=="hulk":
#         update="wonderwomen"
#         print(update)
#     else:
#         print(name)