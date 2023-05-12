class Vehicle:
    def __init__(self, vehicleMake, vehicleModel):
        self.vehicleMake = vehicleMake
        self.vehicleModel = vehicleModel
    
    def set_vehicle_make(self, vehicleMake):
        self.vehicleMake = vehicleMake
    
    def set_vehicle_model(self, vehicleModel):
        self.vehicleModel = vehicleModel
    
    def get_vehicle_make(self):
        return self.vehicleMake
    
    def get_vehicle_model(self):
        return self.vehicleModel


class Car(Vehicle):
    def __init__(self, vehicleMake, vehicleModel, doors):
        super().__init__(vehicleMake, vehicleModel)
        self.doors = doors
    
    def set_car_doors(self, doors):
        self.doors = doors
    
    def get_car_doors(self):
        return self.doors


class Truck(Vehicle):
    def __init__(self, vehicleMake, vehicleModel, bed_length):
        super().__init__(vehicleMake, vehicleModel)
        self.bed_length = bed_length
    
    def set_bed_length(self, bed_length):
        self.bed_length = bed_length
    
    def get_bed_length(self):
        return self.bed_length


def add_car():
    vehicleMake = input("Enter car vehicleMake: ")
    vehicleModel = input("Enter car vehicleModel: ")
    doors = input("Enter number of doors: ")
    car = Car(vehicleMake, vehicleModel, doors)
    return car


def add_pickup():
    vehicleMake = input("Enter pickup vehicleMake: ")
    vehicleModel = input("Enter pickup vehicleModel: ")
    bed_length = input("Enter bed length: ")
    pickup = Truck(vehicleMake, vehicleModel, bed_length)
    return pickup


def main():
    vehicles = []
    while True:
        print("\n1. Add Car\n2. Add Truck\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            car = add_car()
            vehicles.append(car)
        elif choice == "2":
            pickup = add_pickup()
            vehicles.append(pickup)
        elif choice == "3":
            break
        else:
            print("Invalid choice")
    
    print("\nVehicles in garage:")
    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            print("Car Make:", vehicle.get_vehicle_make())
            print("Car Model:", vehicle.get_vehicle_model())
            print("Number of Doors:", vehicle.get_car_doors())
        elif isinstance(vehicle, Truck):
            print("Truck Make:", vehicle.get_vehicle_make())
            print("Truck Model:", vehicle.get_vehicle_model())
            print("Bed Length:", vehicle.get_bed_length())
        else:
            print("Invalid Vehicle")


if __name__ == "__main__":
    main()
