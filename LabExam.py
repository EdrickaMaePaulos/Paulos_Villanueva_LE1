#Lab Exam 1
#Edricka Mae Paulos/Daniel Villanueva
game_library = {
    "Donkey Kong" : {"Quantity" : 3, "Cost" : 2},
    "Super Mario Bros" : {"Quantity" : 5, "Cost" : 2},
    "Tetris" : {"Quantity" : 2, "Cost" : 1},
}

user_account = {}

admin_pass = "adminpass"
admin_username = "admin"

def main_menu():
    print("\nWelcome to Game Rental")
    print("1. Register")
    print("2. Sign-in")
    print("3. Administrator")
    print("4. Exit")
    choice = int(input('Enter your choice: '))

    while True:
        if choice == 1:
            register()
        if choice == 2:
            sign_in()
        if choice == 3:
            admin_login()
        if choice == 4:
            print("Exiting...")
        else:
            print("Invalid Choice")
            break
       
def register():
    while True:
        try:
            username = input("Enter Username: ")
            balance = 0
            points = 0
            if not username:
                main_menu()
            if username in user_account:
                print("Username already exists. Try another username.")
                continue
            
            password = input("Input password (Should not contain any numbers or special characters): ")
            user_account[username] = {"password": password, "balance": balance, "points": points}  
            print("Sign Up successful!")
            main_menu()
            
        except ValueError as e:
            print(e)
            register()

def sign_in():
    print("Sign In")
    while True:
        try:
            username = input("Enter username: ")
            if not username:
                main_menu()
            password = input("Enter password: ")
            if user_account.get(username) and user_account[username]['password'] == password:
                print("Login Successful")
                user_menu(username)
            else:
                print("Invalid username or password")
        except ValueError as e:
            print(e)
            main_menu()
    
def user_menu(username):
    print(f"Welcome to Game Rental Store {username}")
    print("1. Rent Game")
    print("2. Return")
    print("3. Top-Up")
    print("4. Display")
    print("5. Check Points")
    print("6. Log Out")
    print("7. Exiting")
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            rent_game(username)
        elif choice == 2:
            return_game(username)
        elif choice == 3:
            top_up(username)
        elif choice == 4:
            display_available_games()
            break
        elif choice == 5:
            checkpoints(username)
            break
        elif choice == 6:
            main_menu()
        elif choice == 7:            
            print("Exiting...")
            break
        else:
            print("Invalid Choice.")

def display_available_games(username):
    print("Available Games:")
    for game, info in game_library.items():
        print(f"{game} - Quantity: {info['Quantity']}, Cost: {info['Cost']}")
    while True:
        choice = input("Press 'B' to return to the main menu: ")
        if choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please try again.")
    user_menu(username)
       
def rent_game(username):
    print("Rent a game")
    print(game_library)

    gamename = input("Select Game: ")
    if not gamename:
        user_menu(username)
        return  
    if gamename not in game_library:
        print("Invalid game selection.")
        user_menu(username)
        return  
    if game_library[gamename]['Quantity'] <= 0:
        print("Cannot Rent, the game is out of stock.")
        user_menu(username)
        return  

    print("1. Pay using Balance")
    print("2. Pay using points")
    pay = int(input("Choose how to pay: "))

    if pay == 1:
        if user_account[username]['balance'] < game_library[gamename]['Cost']:
            print("Not enough balance to rent. Top up")
        else:
            user_account[username]['balance'] -= game_library[gamename]['Cost']
            if game_library[gamename]['Cost'] >= 2:
                user_account[username]['points'] += 1
            print(f"Rented Successfully. User Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']} ")
    elif pay == 2:
        if user_account[username]['points'] < game_library[gamename]['Cost']:
            print("Not enough points to rent.")
            user_menu(username)
            return  
        user_account[username]['points'] -= game_library[gamename]['Cost']
        print("Rented Successfully using points.")
    else:
        print("Invalid Input")

    user_menu(username)  
                   
def return_game(username):
    print("Return Item")
    item_to_return = input("Enter the name of the item you want to return: ")
    quantity_of_item = int(input("Enter the quantity of item to return: "))
    game_library[item_to_return]['Quantity'] += quantity_of_item
    print(f"Successfully returned {item_to_return}, {quantity_of_item}")
    user_menu(username)

def top_up(username):
    print("Top Up")
    print(f"Username: {username}, Current Balance: {user_account[username]['balance']}")

    topup_amount = float(input("Enter amount to top up: "))
    user_account[username]['balance'] += topup_amount
    print("Top up Successful")
    print(f"Username: {username}, New Balance: {user_account[username]['balance']}")
    user_menu(username)

def checkpoints(username):
    print(f"Available Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']}")
    while True:
        choice = input("Press 'B' to return to the main menu: ")
        if choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please try again.")
    user_menu(username)

def admin_login():
    while True:
        username = input("Enter admin username: ")
        password = input("Input admin password: ")
        if username == admin_username and password == admin_pass:
            print("Log in Successfully")
            admin_menu()
        else:
            print("Invalid username or password")

def admin_menu():
    while True: 
        try:
            print("Welcome Admin")
            print("1. Add Quantity")
            print("2. Increase Price")
            print("3. Add Game")
            print("4. Go back to Main Menu")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                admin_add_quantity()
            if choice == 2:
                increase_price()
            if choice == 3:
                add_game()
            if choice == 4:
                main_menu()
            else:
                print("Invalid Input.")
        except ValueError as e:
            main_menu()

def admin_add_quantity():
    while True: 
        try:    
            print(game_library)
            game_name = input("Enter the name of the item you want to add a quantity: ")
            quantity_of_item = int(input("Enter the quantity of the game: "))
            game_library[game_name]['Quantity'] += quantity_of_item

            if not game_name:
                admin_menu()
            if game_name not in game_library:
                print("Invalid Input. Try again")
                admin_add_quantity()
            else:
                print(f"Successfully added another {quantity_of_item} copies in {game_name}. ")
                print(f"Updated Library: {game_library}")
                print("1. Add quantity to another game")
                print("2. Go back")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    admin_add_quantity()
                if choice == 2:
                    admin_menu()
                else:
                    print("Invalid Input")
        except ValueError as e:
            admin_menu()

def increase_price():
    while True: 
        try:
            print("Change Price")
            print(game_library)
            print("1. Increase the price")
            print("2. Decrease the price")

            choice = int(input("Enter your choice: "))

            if not choice:
                admin_menu()
            if choice == 1:
                game_name = input("Enter the name of the item you want to increase the price: ")
                new_price = int(input("Enter the new price of the game: "))
                game_library[game_name]['cost'] = new_price
                print("Price changed successfully. \n")

                print("1. To change the price of another game.")
                print("2. Go back to main menu")
                choice = int(input("Enter your choice: "))

                if not game_name:
                    admin_menu()
                if not choice:
                    admin_menu()
                if choice == 1:
                    increase_price()
                if choice == 2:
                    admin_menu()
                else:
                    print("Invalid Input")
                    increase_price()
            if choice == 2:
                game_name = input("Enter the name of the item you want to decrease the price: ")
                new_price = int(input("Enter the new price of the game: "))
                game_library[game_name]['cost'] = new_price

                print("Price changed successfully.")
                print(f"Updated Library: {game_library}")
        
                print("1. To change the price of another game.")
                print("2. Go back to main menu")
                choice = int(input("Enter your choice: "))
        
                if not choice:
                    admin_menu()
                if not game_name:
                    admin_menu()
                if choice == 1:
                    increase_price()
                if choice == 2:
                    admin_menu()
            else:
                print("Invalid Input.")
                increase_price()
        except ValueError as e:
            admin_menu()

def add_game():
    while True: 
        try:
            print("Add Game")
            print(game_library)
            new_game_name = input("Input the name of the game you want to add: ")
            
            if new_game_name in game_library:
                print("This game is already on the data base. Try again.")
                add_game()
            else:
                new_game_quantity = int(input("Input the quantity of the new game: "))
                
                if new_game_quantity <= 0:
                    print("Quantity can't be less than zero")
                    continue
                else:
                    new_game_cost = int(input("Enter the price of the new game: "))
                    if new_game_cost <= 0:
                        print("Cost can't be less then 0")
                        continue
                    else:
                        game_library[new_game_name] = {"Quantity" : new_game_quantity, "Cost" : new_game_cost}
                        
                        print(f"{game_library[new_game_name]} Successfully Added to Library")
                        
                        print(f"Updated Library: {game_library}")
                        
                        choice = str(input("Would you like to add another game? (y/n): "))
                        
                        if choice == 'y':
                            add_game()
                        else:
                            admin_menu()

        except ValueError as e:
            admin_menu()

main_menu()

    
