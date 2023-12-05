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

        def add_to_cart(username, item):
    # Function to add an item to the shopping cart
    if username in shopping_carts:
        shopping_carts[username].append(item)
    else:
        shopping_carts[username] = [item]
    print(f"{item} added to the cart.\n")


# Dictionary to store usernames and passwords
users = {}

# Dictionary to store shopping carts
shopping_carts = {}

while True:
    print("1. Register")
    print("2. Login")
    print("3. Add to Cart")
    print("4. Exit")

    choice = input("Select an option (1/2/3/4): ")

    if choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            # If login is successful, allow the user to perform other actions
            while True:
                print("1. Add to Cart")
                print("2. Logout")
                sub_choice = input("Select an option (1/2): ")

                if sub_choice == "1":
                    item_to_add = input("Enter the item to add to the cart: ")
                    add_to_cart(username, item_to_add)
                elif sub_choice == "2":
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.\n")

    elif choice == "3":
        print("You need to login first to add items to the cart.\n")
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

    # Add to carn & register button #

    import tkinter as tk
from tkinter import messagebox

# Dictionary to store usernames and passwords
users = {}

# Dictionary to store shopping carts
shopping_carts = {}

def register():
    # Function to register a new user
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        users[username] = password
        messagebox.showinfo("Registration", "Registration successful!")
    else:
        messagebox.showerror("Error", "Please enter both username and password.")

def login():
    # Function to check login credentials
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        return username
    else:
        messagebox.showerror("Error", "Login failed. Invalid username or password.")
        return None

def add_to_cart(username):
    # Function to add an item to the shopping cart
    item_to_add = entry_item.get()
    if username in shopping_carts:
        shopping_carts[username].append(item_to_add)
    else:
        shopping_carts[username] = [item_to_add]
    
    messagebox.showinfo("Add to Cart", f"{item_to_add} added to the cart.")

# Create the main window
root = tk.Tk()
root.title("Shopping App")

# Username and Password Entry
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")  # Show * for password
entry_password.pack()

# Login Button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

# Item Entry for Add to Cart
label_item = tk.Label(root, text="Item:")
label_item.pack()
entry_item = tk.Entry(root)
entry_item.pack()

# Add to Cart Button
button_add_to_cart = tk.Button(root, text="Add to Cart", command=lambda: add_to_cart(username))
button_add_to_cart.pack()

# Register Button
button_register = tk.Button(root, text="Register", command=register)
button_register.pack()

# Run the GUI
root.mainloop()

