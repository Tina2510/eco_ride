from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,vehicle_id,model,battery_percentage,maintenance_status,rental_price):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = battery_percentage
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

    def __eq__(self, other):
        return isinstance(other, Vehicle) and self.vehicle_id == other.vehicle_id
    
    def __str__(self):
        return (
            f"ID: {self.vehicle_id}, "
            f"Model: {self.model}, "
            f"Battery: {self.battery_percentage}%, "
            f"Status: {self.maintenance_status}, "
            f"Price: {self.rental_price}"
        )
        
    @property
    def battery_percentage(self):
        return self.__battery_percentage
    @battery_percentage.setter
    def battery_percentage(self,value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            print("Battery percentage should be in between 0 and 100")

    @property
    def maintenance_status(self):
        return self.__maintenance_status    
    
    @maintenance_status.setter
    def maintenance_status(self, status):
        self.__maintenance_status = status

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, price):
        if price >=0 :
            self.__rental_price = price
        else:
            print("rental price cannot be negative.") 

    @abstractmethod
    def calculate_trip_cost(self,value):   
        pass           

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_precentage, maintenance_status, rental_price,seating_capacity):
        super().__init__(vehicle_id, model, battery_precentage, maintenance_status, rental_price)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        base_fare = 5.0
        per_km  = 0.5
        return base_fare + (per_km * distance)

                

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_precentage, maintenance_status, rental_price,max_speed_limit):
        super().__init__(vehicle_id, model, battery_precentage, maintenance_status, rental_price)     
        self.max_speed_limit = max_speed_limit  

    def calculate_trip_cost(self,min):
        base_fare = 1.0
        per_min = 0.15
        return base_fare + (per_min * min)

hubs = {}

def add_hub(hub_name):
    if hub_name in hubs:
        print(f"Hub '{hub_name}' already exists.")
    else:
        hubs[hub_name] = []
        print(f"Hub '{hub_name}' added successfully.")


def add_vehicle_to_hub(hub_name, vehicle):
    if hub_name not in hubs:
        print(f"Hub '{hub_name}' does not exist.")
        return
    if vehicle.vehicle_id in [v.vehicle_id for v in hubs[hub_name]]:
        print(f"Vehicle with ID '{vehicle.vehicle_id}' already exists in '{hub_name}'.")
        return
    hubs[hub_name].append(vehicle)
    print(f"Vehicle '{vehicle.model}' added to hub '{hub_name}'.")

def search_by_hub(hub_name):
    if hub_name not in hubs:
        print(f"Hub '{hub_name}' does not exist.")
        return []
    return hubs[hub_name]

def search_by_battery(min_battery=80):
    result = []

    for hub_name, vehicles in hubs.items():
        high_battery_vehicles = list(
            filter(lambda v: v.battery_percentage > min_battery, vehicles)
        )

        if high_battery_vehicles:
            result.append((hub_name, high_battery_vehicles))

    return result

def categorized_view():
    categorized_vehicles = {
        "ElectricCar": [],
        "ElectricScooter": []
    }

    for vehicles in hubs.values():
        for vehicle in vehicles:
            if isinstance(vehicle, ElectricCar):
                categorized_vehicles["ElectricCar"].append(vehicle)
            elif isinstance(vehicle, ElectricScooter):
                categorized_vehicles["ElectricScooter"].append(vehicle)
    print("Electric Cars:")
    for car in categorized_vehicles["ElectricCar"]:
        print(car)

    print("\nElectric Scooters:")
    for scooter in categorized_vehicles["ElectricScooter"]:
        print(scooter)

def fleet_status_summary():
    summary = {
        "Available": 0,
        "On Trip": 0,
        "Under Maintenance": 0
    }
    for vehicles in hubs.values():
        for vehicle in vehicles:
            status = vehicle.maintenance_status
            if status in summary:
                summary[status] += 1

    print("\nFleet Status Summary")
    for status, count in summary.items():
        print(f"{status}: {count}")

    return summary    

def sort_vehicles_by_model(hub_name):
    if hub_name not in hubs:
        print(f"Hub '{hub_name}' does not exist.")
        return []
    return sorted(hubs[hub_name], key=lambda v: v.model.lower()) 


def sort_vehicles_by_battery(hub_name):
    if hub_name not in hubs:
        print(f"Hub '{hub_name}' does not exist.")
        return []

    return sorted(
        hubs[hub_name],
        key=lambda v: v.battery_percentage,
        reverse=True
    )

def sort_vehicles_by_rental_price(hub_name, descending=False):
    if hub_name not in hubs:
        print(f"Hub '{hub_name}' does not exist.")
        return []
    return sorted(
        hubs[hub_name],
        key=lambda v: v.rental_price,
        reverse=descending
    )