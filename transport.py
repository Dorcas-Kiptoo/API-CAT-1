class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Car: {self.registration_number}, {self.make} {self.model}, Seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"Truck: {self.registration_number}, {self.make} {self.model}, Cargo Capacity: {self.cargo_capacity}kg"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return f"Motorcycle: {self.registration_number}, {self.make} {self.model}, Engine Capacity: {self.engine_capacity}cc"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added successfully.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            print("List of vehicles:")
            for vehicle in self.vehicles:
                print(vehicle)

    def search_vehicle_by_registration_number(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f"Vehicle found: {vehicle}")
                return
        print(f"No vehicle found with registration number {registration_number}.")

# Demonstration
def main():
    fleet = Fleet()

    # Adding vehicles
    car = Car("KDF 123Y", "Toyota", "Corolla", 5)
    truck = Truck("KCM 234M", "Ford", "F-150", 1200)
    motorcycle = Motorcycle("MNO456", "Yamaha", "MT-07", 689)

    fleet.add_vehicle(car)
    fleet.add_vehicle(truck)
    fleet.add_vehicle(motorcycle)

    # Display all vehicles
    fleet.display_all_vehicles()

    # Search for a vehicle by registration number
    fleet.search_vehicle_by_registration_number("KDF 123Y")
    fleet.search_vehicle_by_registration_number("KDH 891J")

if __name__ == "__main__":
    main()
