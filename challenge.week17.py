import random

name=input("Thank you for joinging the game, what is your name? ")
game=input(f"Hello {name}, you have 8 try to guess a number between 1-100")
tries=0

# guess= range(1,101)
random_number = random.randint(1, 100)
while tries<8:
    first=int(input("Please insert your guess "))
    tries +=1
    if first > 100 or first < 1:
        print("Your out of range")
    elif first > random_number:
        print("your guess is greater than the answer")
        print(f"try a number between 0 and {random_number +15}")
    elif first < random_number:
        print("your guess is less than the answer")
        print(f"try a number between 100 and {random_number -5}")
    if first==random_number: 
      print("You have guess correctly, WINNER WINNER CHICKEN DINNER")
      print ("it took you {} tries".format(tries))
      break 
    else:
       if tries == 8:
        print (f"You ran out of tries and the number is {random_number}")



    




