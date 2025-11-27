class Car:
    total_cars = 0 # class variable

    def __init__( self, model, brand): # constructor and self is used to call the variables inside the class
        self.__model = model # private variable
        self.brand = brand
        Car.total_cars += 1 #will give total cars object created as this method is called every time an object is created
        # self.total_cars += 1 # will give error as total_cars is a class variable not instance variable
        
    def full_name(self): # method and self is used to call the variables inside the class
        return f"The car is {self.brand} and this model {self.__model} "

    def get_model(self): # getter method to access private variable encapsulation example
        return self.__model
    
    def set_model(self, model): # setter method to modify private variable encapsulation example
        self.__model = model

    def fuel_type(self): # polymorphism method
        return "Petrol/diesal"
    
    @staticmethod
    def gen_description(): # method
        return "This is a car"

class ElectricCar(Car): # inheritance
    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand) # calling the parent class constructor
        self.battery_size = battery_size # new variable for child class

    def fuel_type(self): # polymorphism method
        return "electric"

my_ev_1 = ElectricCar("tesla", "mod 123345", 650)
# print(my_ev_1.full_name())

my_car = Car("suzuki", "venue")
# print(my_car.model) # will give error because model is private variable
# print(my_car.get_model()) # accessing private variable using getter method
# print(my_car.brand)


my_car.set_model("honda") # modifying private variable using setter method
# print(my_car.get_model())  # accessing modified private variable using getter method encapsulation

# print(my_car.full_name()) # calling the method

safari = Car("Toyota", "Land Cruiser")
# print(safari.fuel_type()) # calling the method polymorphism

tesla2 = ElectricCar("Tesla", "Model S", 1000)
# print(tesla2.fuel_type()) # calling the method polymorphism

# print(Car.total_cars) # accessing class variable without creating object

print(safari.gen_description()) # calling parent class method from parent class object
# but if i add staticmethod on gen_description method then i can call it using child class object 

print(Car.gen_description()) # calling parent class method from parent class 
