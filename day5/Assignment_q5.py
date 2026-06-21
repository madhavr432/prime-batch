class vehicle:
    def __init__(self,brand, model):
        self.brand= brand
        self.model= model
    def desplay_info(self):
        print(f"the brand of vehicle is {self.brand}, model is {self.model}")
class car(vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
    def display_car_info(self):
        self.display_info()
        print(f"Seats: {self.seats}")
class bike(vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine= engine
    def display_bike_info(self):
        self.desplay_info()
        print(f"Engine: {self.engine}")
my_car = car("Toyota", "Corolla", 5)
my_bike = bike("Yamaha", "R15", 155)

print("Car Details:")
my_car.display_car_info()

print("Bike Details:")
my_bike.display_bike_info()