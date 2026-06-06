# # a=int(input("enter the number:"))
# # b=int(input("enter the number:"))
# from random import *
# a=randint(1,6)
# b=randint(1,6)
# print(a)
# print(b)
# c=a+b
# if c<=7:
#     print(c)
# elif c==7:
#     print(c)
# else:
#     print(c)


import random

# Dictionary to store user data
user_data = {}

def register():
    name = input("Enter username: ")
    pwd = input("Enter password: ")
    user_data[name] = {'password': pwd, 'wins': 0, 'score': 0}
    print("User registered successfully!\n")

def play(name):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    total = num1 + num2
    print(f"Current numbers: {num1} and {num2}, Sum = {total}")

    guess = input("Guess (+7 or -7): ")

    new1 = random.randint(1, 6)
    new2 = random.randint(1, 6)
    new_total = new1 + new2
    diff = new_total - total

    print(f"Next numbers: {new1} and {new2}, Sum = {new_total}")
    print(f"Actual difference = {diff}")

    if (guess == "+7" and diff == 7) or (guess == "-7" and diff == -7):
        print("You win this round!\n")
        user_data[name]['wins'] += 1
        user_data[name]['score'] += 10
    else:
        print("You lost this round.\n")
        user_data[name]['score'] -= 5

def view_score(name, pwd):
    if name in user_data and user_data[name]['password'] == pwd:
        print(f"Wins: {user_data[name]['wins']}, Score: {user_data[name]['score']}\n")
    else:
        print("Invalid username or password!\n")

while True:
    print("1. Register")
    print("2. Play Game")
    print("3. View Score")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        register()
    elif ch == '2':
        name = input("Username: ")
        pwd = input("Password: ")
        if name in user_data and user_data[name]['password'] == pwd:
            play(name)
        else:
            print("Invalid login!\n")
    elif ch == '3':
        name = input("Username: ")
        pwd = input("Password: ")
        view_score(name, pwd)
    elif ch == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")




