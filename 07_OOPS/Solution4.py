class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    @property
    def brand(self):
        return self.__brand + "!"
    @brand.setter
    def brand(self,NewName):
        if isinstance(NewName, str):
            self.__brand = NewName
        else:
            raise ValueError("Name should be in string")
    


    def fullName(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def  __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

my_tesla = ElectricCar("Tesla","Model S","85kwh")
print(my_tesla.brand)
# print(my_tesla.fullName())

# print(my_tesla.brand())

my_tesla.set_brand = "Tesla MOO"
print(my_tesla.set_brand)


my_car = Car("Toyota","Corolla")
# print(my_car.brand())
print(my_car.brand)