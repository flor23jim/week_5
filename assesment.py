gpa=float(input("what is your GPA?"))
if gpa>=3.8:
    if gpa==4:
        print("highest honors")
    if 3.9<=gpa and gpa<4:
        print("high honors")
    if 3.8<=gpa and gpa<3.9:
        print("honors")
elif gpa==3.5 and gpa<3.8:
        print("good standing")
else:
    print("needs improvement")

type= input("would you like stanard or express?")
location= input("is your location local or international?")
if type=="standard":
     if location=="local":
          print ("Estimated delivery in 5-7 days")
     if location=="international":
          print("estimated devlivery 15-20 days")
else:
     if type=="express":
          if location=="local":
               print("Estimated delivery in 1-2 days")
          if location=="international":
               print("Estimated delivery in 5-10 days")