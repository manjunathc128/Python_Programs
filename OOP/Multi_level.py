# example of multi-level inheritance

class Vehical:
    def __init__(self,seat,gear):
        self.seat=seat
        self.gear=gear
        
    def display_info(self):
        return f"Seat: {self.seat}, Gear:{self.gear}"
        
class Car(Vehical):
    def __init__(self,seat,gear,brand,color):
        super().__init__(seat,gear)
        self.brand=brand
        self.color=color
            
    def display_info(self):
        return f"{super().display_info()} Brand: {self.brand} color: {self.color}"
        
        
class Electric_car(Car):
    def __init__(self,seat,gear,brand,color,battery_range):
        super().__init__(seat,gear,brand,color)
        self.br=battery_range
            
    def display_info(self):
        return f"{super().display_info()} BatteryRange:{self.br}"

hundai=Car(5,6,"hundai","red")
print(hundai.display_info())
               
tesla=Electric_car(5,6,"tesla","Blue","120000mh")   
print(tesla.display_info())
    
    
