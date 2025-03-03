print("Hello there, User.") # Introduction
print("My name is Agape!")

User_Name = input("What is your name? ") # This asks the user for their name.
print(f"Hello {User_Name}! It is nice to meet you!")

User_Age = int(input("How old are you? ")) # This asks the user for their age.
if User_Age < 18:
    print(f"Wow, you are {User_Age}? You are quite young!") # Here are the different outcomes for giving a different age range.
elif User_Age < 49:
    print(f"You are {User_Age}? You are aging.")
elif User_Age > 50:
    print("You are way over your 50s? You are old.")


