import csv

# Property management functions
def add_property():
    print("\nAdd Property")
    prop_id = input("Enter Property ID: ")
    prop_name = input("Enter Property Name: ")
    prop_location = input("Enter Property Location: ")
    prop_price = input("Enter Property Price: ")

    property_id.append(prop_id)
    property_name.append(prop_name)
    property_location.append(prop_location)
    property_price.append(prop_price)

    save_properties()

def view_properties():
    print("\nView Properties")
    print("ID \t Name \t\t Location \t\t Price")
    for i in range(len(property_id)):
        print(property_id[i], "\t", property_name[i], "\t", property_location[i], "\t", property_price[i])

def update_property():
    print("\nUpdate Property")
    prop_id = input("Enter Property ID to update: ")
    for i in range(len(property_id)):
        if property_id[i] == prop_id:
            new_id = input("Enter new Property ID: ")
            new_name = input("Enter new Property Name: ")
            new_location = input("Enter new Property Location: ")
            new_price = input("Enter new Property Price: ")

            property_id[i] = new_id
            property_name[i] = new_name
            property_location[i] = new_location
            property_price[i] = new_price

            save_properties()
            break

def delete_property():
    print("\nDelete Property")
    prop_id = input("Enter Property ID to delete: ")
    for i in range(len(property_id)):
        if property_id[i] == prop_id:
            property_id.pop(i)
            property_name.pop(i)
            property_location.pop(i)
            property_price.pop(i)
            save_properties()
            break

def total_properties():
    print("\nTotal Properties")
    print("Total number of properties:", len(property_id))

def costly_property():
    if len(property_price) == 0:
        print("No properties available.")
        return
    
    max_price = int(property_price[0])
    max_index = 0

    for i in range(1, len(property_price)):
        if int(property_price[i]) > max_price:
            max_price = int(property_price[i])
            max_index = i

    print("\nCostliest Property")
    print("ID: ", property_id[max_index])
    print("Name: ", property_name[max_index])
    print("Location: ", property_location[max_index])
    print("Price: ", property_price[max_index])

def save_properties():
    with open('property.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(property_id)):
            writer.writerow([property_id[i], property_name[i], property_location[i], property_price[i]])

# Customer management functions
def add_customer():
    print("\nAdd Customer")
    cust_id = input("Enter Customer ID: ")
    cust_name = input("Enter Customer Name: ")
    cust_contact = input("Enter Customer Contact: ")

    customer_id.append(cust_id)
    customer_name.append(cust_name)
    customer_contact.append(cust_contact)

    save_customers()

def view_customers():
    print("\nView Customers")
    print("ID \t Name \t\t Contact")
    for i in range(len(customer_id)):
        print(customer_id[i], "\t", customer_name[i], "\t", customer_contact[i])

def update_customer():
    print("\nUpdate Customer")
    cust_id = input("Enter Customer ID to update: ")
    for i in range(len(customer_id)):
        if customer_id[i] == cust_id:
            new_id = input("Enter new Customer ID: ")
            new_name = input("Enter new Customer Name: ")
            new_contact = input("Enter new Customer Contact: ")

            customer_id[i] = new_id
            customer_name[i] = new_name
            customer_contact[i] = new_contact

            save_customers()
            break

def delete_customer():
    print("\nDelete Customer")
    cust_id = input("Enter Customer ID to delete: ")
    for i in range(len(customer_id)):
        if customer_id[i] == cust_id:
            customer_id.pop(i)
            customer_name.pop(i)
            customer_contact.pop(i)
            save_customers()
            break

def save_customers():
    with open('customers.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(customer_id)):
            writer.writerow([customer_id[i], customer_name[i], customer_contact[i]])

# User management functions
def load_users():
    users = {}
    try:
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users[row[0]] = {'password': row[1], 'role': row[2]}
    except FileNotFoundError:
        pass
    return users

def save_users(users):
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for uname, details in users.items():
            writer.writerow([uname, details['password'], details['role']])

def register_user():
    uname = input("Enter a new username: ")
    upass = input("Enter a new password: ")
    role = input("Enter role (admin/customer): ")
    users[uname] = {'password': upass, 'role': role}
    save_users(users)
    print("User registered successfully.")

def login(users):
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

# Initialize lists to store property and customer data
property_id = []
property_name = []
property_location = []
property_price = []

customer_id = []
customer_name = []
customer_contact = []

users = load_users()

# Load property data from CSV file if it exists
try:
    with open('propertyak.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            property_id.append(row[0])
            property_name.append(row[1])
            property_location.append(row[2])
            property_price.append(row[3])
except FileNotFoundError:
    pass

# Load customer data from CSV file if it exists
try:
    with open('customersak.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            customer_id.append(row[0])
            customer_name.append(row[1])
            customer_contact.append(row[2])
except FileNotFoundError:
    pass

# Main program logic
while True:
    print("1. Register User \n2. Login \n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register_user()
    elif choice == 2:
        username, role = login(users)
        if username:
            if role == 'admin':
                while True:
                    print("1. Add Property \n2. View Properties \n3. Update Property \n4. Delete Property \n5. Total Properties \n6. Costliest Property \n7. Add Customer \n8. View Customers \n9. Update Customer \n10. Delete Customer \n11. Logout")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        add_property()
                    elif ch == 2:
                        view_properties()
                    elif ch == 3:
                        update_property()
                    elif ch == 4:
                        delete_property()
                    elif ch == 5:
                        total_properties()
                    elif ch == 6:
                        costly_property()
                    elif ch == 7:
                        add_customer()
                    elif ch == 8:
                        view_customers()
                    elif ch == 9:
                        update_customer()
                    elif ch == 10:
                        delete_customer()
                    elif ch == 11:
                        break
                    else:
                        print("Invalid choice, please try again.")
            elif role == 'customer':
                while True:
                    print("1. View Properties \n2. View Customers \n3. Logout")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        view_properties()
                    elif ch == 2:
                        view_customers()
                    elif ch == 3:
                        break
                    else:
                        print("Invalid choice, please try again.")
    elif choice == 3:
        break
    else:
        print("Invalid choice, please try again.")
