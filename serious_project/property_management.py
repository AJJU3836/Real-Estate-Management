import csv
import customer_management as cm
import user_management as um

# Initialize lists to store property data
property_id = []
property_name = []
property_location = []
property_price = []

def load_properties():
    try:
        with open('property.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                property_id.append(row[0])
                property_name.append(row[1])
                property_location.append(row[2])
                property_price.append(row[3])
    except FileNotFoundError:
        pass

def save_properties():
    with open('property.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(property_id)):
            writer.writerow([property_id[i], property_name[i], property_location[i], property_price[i]])

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

def average_property_rate():
    if len(property_price) == 0:
        print("No properties available.")
        return
    
    total_price = sum(int(price) for price in property_price)
    avg_price = total_price / len(property_price)

    print("\nAverage Property Rate")
    print("Average Price: ", avg_price)

def cheapest_property():
    if len(property_price) == 0:
        print("No properties available.")
        return
    
    min_price = int(property_price[0])
    min_index = 0

    for i in range(1, len(property_price)):
        if int(property_price[i]) < min_price:
            min_price = int(property_price[i])
            min_index = i

    print("\nCheapest Property")
    print("ID: ", property_id[min_index])
    print("Name: ", property_name[min_index])
    print("Location: ", property_location[min_index])
    print("Price: ", property_price[min_index])

def generate_report():
    print("\nProperty Report")
    print("="*30)
    print(f"Total Properties: {len(property_id)}")
    
    if len(property_price) == 0:
        print("No properties available.")
        return
    
    total_price = sum(int(price) for price in property_price)
    avg_price = total_price / len(property_price)
    
    max_price = int(property_price[0])
    max_index = 0
    min_price = int(property_price[0])
    min_index = 0
    
    for i in range(1, len(property_price)):
        if int(property_price[i]) > max_price:
            max_price = int(property_price[i])
            max_index = i
        if int(property_price[i]) < min_price:
            min_price = int(property_price[i])
            min_index = i
    
    print(f"Average Property Rate: {avg_price}")
    print("\nCostliest Property")
    print("-------------------")
    print(f"ID: {property_id[max_index]}")
    print(f"Name: {property_name[max_index]}")
    print(f"Location: {property_location[max_index]}")
    print(f"Price: {property_price[max_index]}")
    
    print("\nCheapest Property")
    print("------------------")
    print(f"ID: {property_id[min_index]}")
    print(f"Name: {property_name[min_index]}")
    print(f"Location: {property_location[min_index]}")
    print(f"Price: {property_price[min_index]}")
    
    print("\nDetailed List of Properties")
    print("---------------------------")
    print("ID \t Name \t\t Location \t\t Price")
    for i in range(len(property_id)):
        print(f"{property_id[i]} \t {property_name[i]} \t {property_location[i]} \t {property_price[i]}")


# Load initial data
cm.load_customers()
load_properties()
um.load_users()

# Main loop
while True:
    print("1. Register User \n2. Login \n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        um.register_user()
    elif choice == 2:
        username, role = um.login()
        if username:
            if role == 'admin':
                while True:
                    print("1. Add Property \n2. View Properties \n3. Update Property \n4. Delete Property \n5. Total Properties \n6. Costliest Property \n7. Average Property Rate \n8. Cheapest Property \n9. Generate Report \n10. Add Customer \n11. View Customers \n12. Update Customer \n13. Delete Customer \n14. Logout")
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
                        average_property_rate()
                    elif ch == 8:
                        cheapest_property()
                    elif ch == 9:
                        generate_report()
                    elif ch == 10:
                        cm.add_customer()
                    elif ch == 11:
                        cm.view_customers()
                    elif ch == 12:
                        cm.update_customer()
                    elif ch == 13:
                        cm.delete_customer()
                    elif ch == 14:
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
                        cm.view_customers()
                    elif ch == 3:
                        break
                    else:
                        print("Invalid choice, please try again.")
    elif choice == 3:
        break
    else:
        print("Invalid choice, please try again.")
