#Lab Exam 1
game_library = {
    "Donkey Kong":{"Copies": 3, "Cost": 2},
    "Donkey Kong":{"Copies": 3, "Cost": 2},
    "Donkey Kong":{"Copies": 3, "Cost": 2} 
}

user_account = {}
user_inventory = {}
admin_pass = "adminpass"
admin_username = "admin"

def main_menu()
    print("\nWelcome to Game Rental")
    print("1. Register")
    print("2. Sign-in")
    print("3. Administrator")
    print("4. Exiting...")
    choice = int(input('Enter your choice: '))

    while True:
        try:
            if choice == 1:
            pass
            if choice == 2:
            pass
            if choice == 3:
            pass
            if choice == 4:
            pass
            else:
            pass
            break
        except ValueError as e:
            print(e)

def register()
    while True:
        try:
            username = str(input("Enter your username (Leave blank to return): "))
            balance = 0.0
            points = 0
            if not username:
                return
            if username in user_account:
                print("Username already exist. Please try again")
                continue
            try:
                password = str(input("Enter your password (Should not contain any numbers or special characters): "))
                password1 = str(input("Re-enter"))
                if password == password1:
                    user_account[username] = {
                        "Username" = username, 
                        "Password" = password,
                        "Balance" = balance,
                        "Points" = points,
                    }
                    main_menu()
                else:
                    print('Invalid Output')
                    continue
                break
            except ValueError as e:
                print(e)

def sign_in()
    print("\nSign-in")
    while True:
        try:
            username = input("Please enter your username(Leave Blank to Return): ")
            if not username:
                return
            if username in user_account:
                password = input("Enter your password(Leave Blank to Return): ")
                #to be continued

def user_menu(username)
    print("\nUser Menu")
    print("1. Available Games")
    print("2. Rent Games")
    print("3. Return Games")
    print('4. Top-up')
    print("5. Check Points")
    print("6. Redeem Points")
    print("7. Check Inventory")
    print("8. Exit")
    choice = int(input("\nEnter your Choice: "))
    
    while True:
        try:
            if choice == 1:
                pass
            if choice == 2:
                pass
            if choice == 3:
                pass
            if choice == 4:
                pass
            if choice == 5:
                pass
            if choice == 6:
                pass
            if choice == 7:
                pass
            if choice == 8:
                pass
            else:
                pass
        except ValueError as e:
            print(e)

def available_games(username)
    print(f"\nAvailable Games:\n{game_library}")
    print("Leave Blank to return to User Menu")
    available_games(username)

def rent_game(username)
    print(f"{available_games}")
    while True:
        try:
            game_name = str(input("Enter the name of the game you want to rent"))
            if game_name in game_library and game_library[game_name]["quantity"] > 0:
                if user_account[username]["balance"] >= game_library[game_name]["cost"]:
                    user_account[username]["balance"] -= game_library[game_name]["cost"]:
                    game_library[game_name]["quantity"] -= 1
                    user_account[username]["points"] += 1
                    if username not in user_inventory:
                        user_inventory[username] = game_name
                    else:
                        user_inventory[username].append(game_name)
                        print(f"Game Successfully Rented. Remaining Balance {balance}. Current points {points}")
                else:
                    print("Insufficient Balance")       
            if  game_name in game_library and game_library[game_name]["quantity"] < 0:
                print("Game is out of stock")
            else:
                print("Invalid game name")
        except ValueError as e
        print(e)
        choice = int(input("Rent another game (1) or Go back to menu (2)"))
            if choice == 1:
            rent_game(username)
            if choice == 2:
            user_menu(username)
            else:
                print("Invalid Output")
        rent_game(username)   
def return_game(username)
    print("\nReturn Game!")
    print(user_inventory[username])
    while True:
        try:
            game_name = str(input("Enter the name of the game you want to return"))
            if game_name in user_inventory and game_library[game_name]["quantity"] > 0:
                if user_account[username]["balance"] >= game_library[game_name]["cost"]:
                    user_account[username]["balance"] -= game_library[game_name]["cost"]:
                    game_library[game_name]["quantity"] -= 1
                    user_account[username]["points"] += 1
                    if username not in user_inventory:
                        user_inventory[username] = game_name
                    else:
                        user_inventory[username].append(game_name)
                        print(f"Game Successfully Rented. Remaining Balance {balance}. Current points {points}")
                else:
                    print("Insufficient Balance")       
            if  game_name in game_library and game_library[game_name]["quantity"] < 0:
                print("Game is out of stock")
            else:
                print("Invalid game name")
        except ValueError as e
        print(e)
        choice = int(input("Rent another game (1) or Go back to menu (2)"))
            if choice == 1:
            rent_game(username)
            if choice == 2:
            user_menu(username)
            else:
                print("Invalid Output")
        rent_game(username)  

    
def top_up(username)
    print("\nTop-up")
    print(f"Username {username}, Current Balance {balance}")
    amount = float(input("Enter amount to top-up: "))
    user_account[username]['balance'] += amount
    print(f'Top up Successful. New Balance {balance}')
    top_up(username)

def check_points(username)
    print(f"Current points{points}")
    check_points(username)
def redeem_points()
    pass
def check_inventory(username)
    print(f"Current inventory{check_inventory}")
    check_inventory(username)