class Vehicle():
    def __init__(self,vehicle_id,model,battery_percentage,maintenance_status,rental_price):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = battery_percentage
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

        
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

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_precentage, maintenance_status, rental_price,seating_capacity):
        super().__init__(vehicle_id, model, battery_precentage, maintenance_status, rental_price)
        self.seating_capacity = seating_capacity

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_precentage, maintenance_status, rental_price,max_speed_limit):
        super().__init__(vehicle_id, model, battery_precentage, maintenance_status, rental_price)     
        self.max_speed_limit = max_speed_limit  
