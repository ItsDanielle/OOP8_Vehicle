class Vehicle:
    
    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed  
        self.fuel_type = fuel_type

class Car(Vehicle):
    
    def __init__(self, color, speed, fuel_type, num_doors, is_electric):
        super().__init__(color, speed, fuel_type)
        self.num_doors = num_doors
        self.is_electric = is_electric

my_car = Car("Purple", 80, "Gasoline", num_doors=4, is_electric=False)

print("Color:", my_car.color)
print("Speed:", my_car.speed, "mph")
print("Fuel type:", my_car.fuel_type)
print("Number of doors:", my_car.num_doors)
print("Is electric:", my_car.is_electric)