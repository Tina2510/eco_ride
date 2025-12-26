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
        
    @property
    def battery_precentage(self):
        return self.battery_precentage
    @battery_precentage.setter
    def battery_precentage(self,value):
        if 0 <= value <= 100:
            self.__battery_precentage = value
        else:
            print("Battery precentage should be in between 0 and 100")

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