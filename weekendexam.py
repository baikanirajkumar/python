import random
user_data={}
def register():
    name=input("Enter username: ")
    pwd=input("Enter password: ")
    user_data[name] = {'password':pwd,'wins':0,'score':0}
    print("registration successful")
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
    if (guess == "+7" and diff == 7) or (guess == "-7" and diff == -7):
            print("You win this round!")
            user_data[name]['wins'] += 1
            user_data[name]['score'] += 10
    else:
            print("You lost this round")
            user_data[name]['score'] -= 5
def view_score(name, pwd):
    if name in user_data and user_data[name]['password'] == pwd:
        print(f"Wins: {user_data[name]['wins']}, Score: {user_data[name]['score']}\n")
    else:
        print("Invalid username or password!")

while True:
    print("1. Register")
    print("2. Play Game")
    print("3. View Score")
    print("4. Exit")
    select=input("select option")
    if select == '1':
        register()
    elif select == '2':
        name = input("Username: ")
        pwd = input("Password: ")
        if name in user_data and user_data[name]['password'] == pwd:
            play(name)
        else:
            print("Invalid login!")
    elif select == '3':
        name = input("Username: ")
        pwd = input("Password: ")
        view_score(name, pwd)
    elif select=='4':
        print("exited")
        break
    else:
        print("Invalid choice!")




