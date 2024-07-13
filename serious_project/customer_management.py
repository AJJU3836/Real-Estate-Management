import csv

# Initialize lists to store customer data
customer_id = []
customer_name = []
customer_contact = []

def load_customers():
    try:
        with open('customers.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                customer_id.append(row[0])
                customer_name.append(row[1])
                customer_contact.append(row[2])
    except FileNotFoundError:
        pass

def save_customers():
    with open('customers.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(customer_id)):
            writer.writerow([customer_id[i], customer_name[i], customer_contact[i]])

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