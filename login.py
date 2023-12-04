def register():
    # Function to register a new user
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!\n")


def login():
    # Function to check login credentials
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!\n")
    else:
        print("Login failed. Invalid username or password.\n")


# Dictionary to store usernames and passwords

users = {}

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")
