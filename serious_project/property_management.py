import csv
import customer_management as cm
import user_management as um

# Initialize lists to store property data
prop_ids = []
prop_names = []
prop_locations = []
prop_prices = []

def load_properties():
    try:
        with open('property.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                prop_ids.append(row[0])
                prop_names.append(row[1])
                prop_locations.append(row[2])
                prop_prices.append(row[3])
    except FileNotFoundError:
        pass

def save_properties():
    with open('property.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(prop_ids)):
            writer.writerow([prop_ids[i], prop_names[i], prop_locations[i], prop_prices[i]])

def add_property():
    print("\nAdd Property")
    prop_id = input("Enter Property ID: ")
    prop_name = input("Enter Property Name: ")
    prop_location = input("Enter Property Location: ")
    prop_price = input("Enter Property Price: ")

    prop_ids.append(prop_id)
    prop_names.append(prop_name)
    prop_locations.append(prop_location)
    prop_prices.append(prop_price)

    save_properties()

def view_properties():
    print("\nView Properties")
    print("ID \t Name \t\t Location \t\t Price")
    for i in range(len(prop_ids)):
        print(prop_ids[i], "\t", prop_names[i], "\t", prop_locations[i], "\t", prop_prices[i])

def update_property():
    print("\nUpdate Property")
    prop_id = input("Enter Property ID to update: ")
    for i in range(len(prop_ids)):
        if prop_ids[i] == prop_id:
            new_id = input("Enter new Property ID: ")
            new_name = input("Enter new Property Name: ")
            new_location = input("Enter new Property Location: ")
            new_price = input("Enter new Property Price: ")

            prop_ids[i] = new_id
            prop_names[i] = new_name
            prop_locations[i] = new_location
            prop_prices[i] = new_price

            save_properties()
            break

def delete_property():
    print("\nDelete Property")
    prop_id = input("Enter Property ID to delete: ")
    for i in range(len(prop_ids)):
        if prop_ids[i] == prop_id:
            prop_ids.pop(i)
            prop_names.pop(i)
            prop_locations.pop(i)
            prop_prices.pop(i)
            save_properties()
            break

def total_properties():
    print("\nTotal Properties")
    print("Total number of properties:", len(prop_ids))

def costly_property():
    if len(prop_prices) == 0:
        print("No properties available.")
        return
    
    max_price = int(prop_prices[0])
    max_index = 0

    for i in range(1, len(prop_prices)):
        if int(prop_prices[i]) > max_price:
            max_price = int(prop_prices[i])
            max_index = i

    print("\nCostliest Property")
    print("ID: ", prop_ids[max_index])
    print("Name: ", prop_names[max_index])
    print("Location: ", prop_locations[max_index])
    print("Price: ", prop_prices[max_index])

def main():
    cm.load_customers()
    load_properties()
    um.load_users()

    while True:
        print("1. Register User \n2. Login \n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            um.register_user()
        elif choice == 2:
            username, role = um.login()
            if username:
                if role == 'admin':
                    admin_menu()
                elif role == 'customer':
                    customer_menu()
        elif choice == 3:
            break
        else:
            print("Invalid choice, please try again.")

def admin_menu():
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
            cm.add_customer()
        elif ch == 8:
            cm.view_customers()
        elif ch == 9:
            cm.update_customer()
        elif ch == 10:
            cm.delete_customer()
        elif ch == 11:
            break
        else:
            print("Invalid choice, please try again.")

def customer_menu():
    while True:
        print("1. View Properties \n2. View Customers \n3. Logout")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            view_properties()
        elif ch == 2:
            cm.view_customers()
        elif ch == 3:
            break
        else:
            print("Invalid choice, please try again.")

main()
