traffic_light = "Green"

speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."
        print(message)


class Car(Vehicle):
    def __init__(self, make):
        self.make = make  
    
    def start_engine(self):
        message = "Car engine started."
        print(message)


class Bike(Vehicle):
    def __init__(self, type):
        self.type = type  
    
    def start_engine(self):
        message = "Bike engine started."
        print(message)

if __name__ == "__main__":

    my_car = Car("CarName")
    my_bike = Bike("BikeType")

    my_car.start_engine() 
    my_bike.start_engine() 

    