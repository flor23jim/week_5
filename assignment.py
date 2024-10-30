gpa=float(input("what is your GPA?")) #ask user of their gpa 
if gpa>=3.8: # checking if they can meet the standard of passing with honors 
    if gpa==4:
        print("highest honors")  # having the highest honors
    if 3.9<=gpa and gpa<4:
        print("high honors")  # high honros 
    if 3.8<=gpa and gpa<3.9:
        print("honors")
elif gpa==3.5 and gpa<3.8:
        print("good standing") # is passing with a good standing 
else:
    print("needs improvement") # would  have to n=imporve their gpa 

type= input("would you like stanard or express?")# ask the user what type of delivery service they would like 
location= input("is your location local or international?") # and how far they need to deliever the package 
if type=="standard": # if they package is getting delievered with standard shipping they will then determer how long it will take depending on the location
     if location=="local":
          print ("Estimated delivery in 5-7 days")
     if location=="international":
          print("estimated devlivery 15-20 days")
else:
     if type=="express": # if the user chose an express shipping the if statement will determine how long it will take depending on their location
          if location=="local":
               print("Estimated delivery in 1-2 days")
          if location=="international":
               print("Estimated delivery in 5-10 days")