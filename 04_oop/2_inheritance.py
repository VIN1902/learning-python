from basic_class import Car

class Electric_Car(Car):
    def __init__(self, brand, model, batter_size):
        super().__init__(brand, model) # It calls the constructor of the parent class when using class inheritance.
        self.batter_size = batter_size
    
    def display_name(self): # method overriding
        super().display_name() # super can also call parent's method
        print(f"The {self.model}'s battery size is {self.batter_size}")
    
my_ev = Electric_Car('Mahindra', 'BE-6', 59)
my_ev.display_name()

# isinstance():

print(isinstance(my_ev, Electric_Car))
print(isinstance(my_ev, Car))