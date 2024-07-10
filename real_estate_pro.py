import csv

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

    with open('property.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(property_id)):
            writer.writerow([property_id[i], property_name[i], property_location[i], property_price[i]])

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

            with open('property.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for j in range(len(property_id)):
                    writer.writerow([property_id[j], property_name[j], property_location[j], property_price[j]])
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
            break

    with open('property.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for j in range(len(property_id)):
            writer.writerow([property_id[j], property_name[j], property_location[j], property_price[j]])

def total_properties():
    print("\nTotal Properties")
    print("Total number of properties:", len(property_id))

def costly_property():
    if not property_price:
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


property_id = []
property_name = []
property_location = []
property_price = []

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

count = 3
while count != 0:
    uname = input("Enter the User name: ")
    upass = input("Enter User Password: ")
    if uname == "admin" and upass == "password":
        print("Login successful")
        cnt = 1
        while cnt != 0:
            print("1. Add Property \n2. View Properties \n3. Update Property \n4. Delete Property \n5. Total Properties \n6. Costliest Property \n7. Exit")
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
                exit()
            else:
                print("Invalid choice, please try again.")
    else:
        print("Invalid username or password!")
        count -= 1
        print("Remaining attempts =", count)
        if count == 0:
            print("Access denied.")