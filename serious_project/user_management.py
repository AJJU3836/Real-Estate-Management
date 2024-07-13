import csv

# Initialize dictionary to store user data
users = {}

def load_users():
    try:
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users[row[0]] = {'password': row[1], 'role': row[2]}
    except FileNotFoundError:
        pass

def save_users():
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for uname, details in users.items():
            writer.writerow([uname, details['password'], details['role']])

def register_user():
    uname = input("Enter a new username: ")
    upass = input("Enter a new password: ")
    role = input("Enter role (admin/customer): ")
    users[uname] = {'password': upass, 'role': role}
    save_users()
    print("User registered successfully.")

def login():
    load_users()
    count = 3
    while count != 0:
        uname = input("Enter the User name: ")
        upass = input("Enter User Password: ")
        if uname in users and users[uname]['password'] == upass:
            print("Login successful")
            return uname, users[uname]['role']
        else:
            print("Invalid username or password!")
            count -= 1
            print("Remaining attempts =", count)
            if count == 0:
                print("Access denied.")
                return None, None