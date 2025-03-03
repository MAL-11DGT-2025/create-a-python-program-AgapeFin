print("Hello there, User.")
print("My name is Agape!")

User_Name = input("What is your name? ")
print(f"Hello {User_Name}! It is nice to meet you!")

User_Age = int(input("How old are you? "))
if User_Age < 18:
    print(f"Wow, you are {User_Age}? You are quite young!")
elif User_Age < 49:
    print(f"You are {User_Age}? You are aging.")
elif User_Age > 50:
    print(f"You are way over your 50s? You are old.")


