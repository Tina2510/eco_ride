from abc import ABC, abstractmethod
import csv
import json

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
    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "model": self.model,
            "battery_percentage": self.__battery_percentage,
            "maintenance_status": self.maintenance_status,
            "rental_price": self.rental_price
    }

        
    @property
    def battery_percentage(self):
        return self.__battery_percentage
    @battery_percentage.setter
    def battery_percentage(self,value):
        if 0 < value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError ("Battery percentage should be in between 0 and 100")

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
           raise ValueError ("rental price cannot be negative.") 

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
    
    def to_dict(self):
        data = super().to_dict()
        data["vehicle_type"] = "ElectricCar"
        data["seating_capacity"] = self.seating_capacity
        return data


                

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_precentage, maintenance_status, rental_price,max_speed_limit):
        super().__init__(vehicle_id, model, battery_precentage, maintenance_status, rental_price)     
        self.max_speed_limit = max_speed_limit  

    def calculate_trip_cost(self,min):
        base_fare = 1.0
        per_min = 0.15
        return base_fare + (per_min * min)
    
    def to_dict(self):
        data = super().to_dict()
        data["vehicle_type"] = "ElectricScooter"
        data["max_speed_limit"] = self.max_speed_limit
        return data


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


def save_fleet_to_csv(filename="fleet.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "hub_name", "vehicle_type", "vehicle_id", "model",
            "battery_percentage", "maintenance_status", "rental_price",
            "seating_capacity", "max_speed_limit"
        ])
        for hub_name, vehicles in hubs.items():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    writer.writerow([
                        hub_name, "ElectricCar", v.vehicle_id, v.model,
                        v.battery_percentage, v.maintenance_status, v.rental_price,
                        v.seating_capacity, ""
                    ])
                elif isinstance(v, ElectricScooter):
                    writer.writerow([
                        hub_name, "ElectricScooter", v.vehicle_id, v.model,
                        v.battery_percentage, v.maintenance_status, v.rental_price,
                        "", v.max_speed_limit
                    ])
                    
    print(f"Fleet saved to {filename}.")


def load_fleet_from_csv(filename="fleet.csv"):
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                hub_name = row["hub_name"]
                vehicle_type = row["vehicle_type"]
                vehicle_id = row["vehicle_id"]
                model = row["model"]
                battery_percentage = float(row["battery_percentage"])
                maintenance_status = row["maintenance_status"]
                rental_price = float(row["rental_price"])
                print(f" --->{row}")
                if vehicle_type == "ElectricCar":
                    seating_capacity = int(row["seating_capacity"])
                    vehicle = ElectricCar(vehicle_id, model, battery_percentage, maintenance_status, rental_price, seating_capacity)
                elif vehicle_type == "ElectricScooter":
                    max_speed_limit = int(row["max_speed_limit"])
                    vehicle = ElectricScooter(vehicle_id, model, battery_percentage, maintenance_status, rental_price, max_speed_limit)

                if hub_name not in hubs:
                    hubs[hub_name] = []
                hubs[hub_name].append(vehicle)
        print(f"Fleet loaded from {filename}.")
    except FileNotFoundError:
        print(f"No CSV file found at {filename}. Starting fresh fleet.")

def save_fleet_to_json(filename="fleet.json"):
    data = {}

    for hub_name, vehicles in hubs.items():
        data[hub_name] = [v.to_dict() for v in vehicles]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Fleet saved to {filename}.")

def load_fleet_from_json(filename="fleet.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        hubs.clear()

        for hub_name, vehicles in data.items():
            hubs[hub_name] = []

            for v in vehicles:
                if v["vehicle_type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery_percentage"],
                        v["maintenance_status"],
                        v["rental_price"],
                        v["seating_capacity"]
                    )

                elif v["vehicle_type"] == "ElectricScooter":
                    vehicle = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery_percentage"],
                        v["maintenance_status"],
                        v["rental_price"],
                        v["max_speed_limit"]
                    )

                hubs[hub_name].append(vehicle)

        print(f"Fleet loaded from {filename}.")

    except FileNotFoundError:
        print(f"No JSON file found at {filename}. Starting fresh fleet.")
