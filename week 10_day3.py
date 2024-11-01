# Problem 1: Student Grade Categorization
# Ask the user to enter a list of student scores (one by one).
# Use a while loop to continuously accept scores until the user enters a negative number.
# For each score, use nested if statements to categorize the score:
# 90-100: Print "Excellent"
# 70-89: Print "Good"
# 50-69: Print "Pass"
# Below 50: Print "Fail"
# Stop the loop and print the final count of each category when the user enters a negative number.

# question=int(input("please provide me with a set scores all individually:"))# varible is saved as question it allows us to save the users input. In addition it provides us a variable to continuously use. 
# while not question<0: # if input score is less than zero loop continues till score is an effectivie number
#     if question>=90: # if score provided is greater than or equal to 90 excellent is printed 
#          print("excellent")
#     elif 70<=question<=89: # if score provided is greater than 70 or less than or equal to 89 good is printed
#          print("good")
#     elif 50<=question<=69: # if score provided is greater than 50 or less than or equal to 69 pass is printed
#          print("pass")
#     elif 0<question<50: # if score provided os greater than 0 or less than 50  fail is printed 
#          print("Fail")
#     question=int(input("please provide me with a set scores all individually:")) # allows for question for continue until not valid is read and printed 
# print("not vaild bye") # if score is invaled meaning greater than 100 or less than 0 not valid bye is printed
#####################################################################################################################################     
              
# Problem 2:Even and Odd Counter with Conditions
# Ask the user for a starting and ending number.
# Use a for loop to iterate from the starting to the ending number.
# Inside the loop:
# Use nested if to check if the number is both even and greater than 10. If true, count it as a “special even” number.
# If it’s odd and less than 20, count it as a “special odd” number.
# Print the counts for both “special even” and “special odd” numbers.

num1=int(input("please give me a starting number"))
num2=int(input('please provided me with a ending number'))

for x in range(num1,num2+1): 
     if x % 2==0:
        if x>10:
          print( "special even")
     elif not x % 2==0:
            if x<20:
               print("special odd")

