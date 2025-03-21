clients = []

def add_client():
    name = input("Enter client name: ")
    age = input("Enter client age: ")
    contact = input("Enter client contact details: ")
    weight = input("Enter client weight: ")
    height = input("Enter client height: ")

    client = {
        "name": name,
        "age": age,
        "contact": contact,
        "weight": weight,
        "height": height,
        "diet": None  
    }

    clients.append(client)
    print("Client added successfully!")

def update_client():
    name = input("Enter client name to update: ")
    for client in clients:
        if client["name"] == name:
            client["name"] = input("Enter new name (leave empty to keep the same): ") or client["name"]
            client["age"] = input("Enter new age (leave empty to keep the same): ") or client["age"]
            client["contact"] = input("Enter new contact details (leave empty to keep the same): ") or client["contact"]
            client["weight"] = input("Enter new weight (leave empty to keep the same): ") or client["weight"]
            client["height"] = input("Enter new height (leave empty to keep the same): ") or client["height"]
            print("Client information updated successfully.")
            return
    print("Client not found.")

def view_client():
    name = input("Enter client name to view: ")
    for client in clients:
        if client["name"] == name:
            print("Client Information:")
            print(f"Name: {client['name']}")
            print(f"Age: {client['age']}")
            print(f"Contact: {client['contact']}")
            print(f"Weight: {client['weight']}")
            print(f"Height: {client['height']}")
            return
    print("Client not found.")

def add_diet_for_client():
    name = input("Enter client name to add diet for: ")
    for client in clients:
        if client["name"] == name:
            diet = input("Enter diet information for the client: ")
            client["diet"] = diet
            print("Diet information added successfully.")
            return
    print("Client not found.")

def view_diet_for_client():
    name = input("Enter client name to view diet for: ")
    for client in clients:
        if client["name"] == name:
            if client["diet"]:
                print("Diet Information:")
                print(f"Name: {client['name']}")
                print(f"Diet: {client['diet']}")
            else:
                print("No diet information found for this client.")
            return
    print("Client not found.")

def update_diet_for_client():
    name = input("Enter client name to update diet for: ")
    for client in clients:
        if client["name"] == name:
            if client["diet"]:
                new_diet = input("Enter new diet information (leave empty to keep the same): ") or client["diet"]
                client["diet"] = new_diet
                print("Diet information updated successfully.")
            else:
                print("No existing diet information found for this client. Please use 'Add Diet for Client' first.")
            return
    print("Client not found.")


while True:
    print("Dietitian Record Management System")
    print("1. Add Client")
    print("2. Update Client")
    print("3. View Client")
    print("4. Add Diet for Client")
    print("5. View Diet for Client")
    print("6. update Diet for Client")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_client()
    elif choice == "2":
        update_client()
    elif choice == "3":
        view_client()
    elif choice == "4":
        add_diet_for_client()
    elif choice == "5":
        view_diet_for_client()
    elif choice == "6":
        update_diet_for_client()
    elif choice == "7":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
