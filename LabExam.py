#Lab Exam 1
game_library = {
    "Donkey Kong":{"copies": 3, "cost": 2},
    "Donkey Kong":{"copies": 3, "cost": 2},
    "Donkey Kong":{"copies": 3, "cost": 2} 
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
            username = input("Please enter your username: ")
            password = input("Enter your password: ")
            if username in user_account and user_account[username]["password"] == [password]
                print("Log in successful")
                user_menu()
            else:
                print('Invalid Output')
                continue
            break
        except ValueError as e:
            print(e)
            sign_in()


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
                    game_library[game_name]["copies"] -= 1
                    user_account[username]["points"] += 1
                    if username not in user_inventory:
                        user_inventory[username] = game_name
                    else:
                        user_inventory[username].append(game_name)
                        print(f"Game Successfully Rented. Remaining Balance {balance}. Current points {points}")
                else:
                    print("Insufficient Balance")       
            if  game_name in game_library and game_library[game_name]["copies"] < 0:
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
            if game_name in user_inventory.get(username, ):
                user_inventory[username].remove(game_name)
                game_library[game_name]['copies'] += 1
                print(f"Game {game_name} successfully returned") 
            else:  
                print("Game not found in inventory")
        except ValueError as e:
            print(e)
        choice = int(input("Return another game (1) or Go back to menu (2)"))
            if choice == 1:
            return_game(username)
            if choice == 2:
            user_menu(username)
            else:
                print("Invalid Output")
            return_game(username) 

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

def admin_login()
    while True:
        username = input("Enter admin username: ")
        password = input("Input admin password: ")
        if username == admin_username and password == admin_pass:
            print("Log in Successfully")
            admin_menu()
        else:
            print("Invalid username or password")

def admin_menu()
    print('Welcome Admin')
    print("1. Edit Library")
    print("2. Exit")
    choice = int(input("Enter Choice: "))
    
    while True:
        if choice == 1:
        edit_library()
        if choice == 2:
        main_menu()
        else:
            print("Invalid Output")
            break

def edit_library()
    print("1. Edit price")
    print("2. Edit quantity")
    print("3. Add new game")
    print("4. Log out")
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            game_name = input("Enter the name of the game you want to edit the price: ")
            if game_name in game_library:
                new_cost = int(input("Enter the new price"))
                game_library[game_name]["cost"] = new_cost
                print('Price updated successfully')
                edit_library()
            else:
                print("Game not found")
        if choice == 2:
            game_name = input("Enter the name of the game you want to edit the quantity: ")
            if game_name in game_library:
                new_quantity = int(input("Enter the new number of copies"))
                game_library[game_name]["copies"] = new_quantity
                print('Copies updated successfully')
                edit_library()
            else:
                print("Game not found")
        if choice == 3:
            game_name = input("Enter the game you want to add: ")
            copies = int(input("Enter the number of copies: "))
            cost = int(input("Enter the cost of the game: "))
            game_library[game_name] = {'copies': copies, "cost": cost}
            print(f"Game {game_name} added successfully")
        if choice == 4:
            main_menu() 

            
def add_new_game


    