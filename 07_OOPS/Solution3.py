class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
# Class inherit
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__ (brand,model)  
        self.battery_size = battery_size


my_tesala = ElectricCar("Tesla","Model S","85KWH")
print(my_tesala.model)
print(my_tesala.full_name())

my_car = Car("Toyota","Corolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())





# Practice

# class Chai:
#     def __init__(self,name,flavour):
#         self.name = name
#         self.flavour = flavour

#     def fullName_chai(self):
#         return f"{self.name} {self.flavour}"

# class Tea(Chai):
#     def __init__(self, name, flavour,colour):
#         super().__init__(name, flavour)
#         self.colour = colour

# new_chai = Tea("Masala","Spicy","Brown")
# print(new_chai.name)
# print(new_chai.flavour)
# print(new_chai.colour)
# print(new_chai.fullName_chai())

# my_chai = Chai("Green","Fresh")
# print(my_chai.name)
# print(my_chai.flavour)