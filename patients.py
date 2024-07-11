# List to store patients
patients = []

# Function to add a new patient
def add_patient(name, age, illness):
    patient = {
        'name': name,
        'age': age,
        'illness': illness
    }
    patients.append(patient)
    print(f"Patient {name} added successfully.")

# Function to display all patients
def display_patients():
    if patients:
        print("List of patients:")
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
    else:
        print("No patients found.")

# Function to search for a patient by name
def search_patient(name):
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print(f"No patient found with the name {name}.")

# Function to remove a patient by name
def remove_patient(name):
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.")
            return
    print(f"No patient found with the name {name}.")

# Main program loop
def main():
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            illness = input("Enter patient illness: ")
            add_patient(name, age, illness)
        elif choice == '2':
            display_patients()
        elif choice == '3':
            name = input("Enter patient name to search: ")
            search_patient(name)
        elif choice == '4':
            name = input("Enter patient name to remove: ")
            remove_patient(name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main program loop
if __name__ == "__main__":
    main()
