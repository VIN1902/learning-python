class Diseal_Car:
    def __init__(self, brand):
        self.brand = brand
    
    def fuel_type(self):
        return f"Cars of {self.brand} comes with only diseal fuel type."

class Bi_Fuel_Car(Diseal_Car):
    def __init__(self, brand):
        super().__init__(brand)
    
    def fuel_type(self):
        return super().fuel_type().rstrip('.') + f", but {self.brand} comes with both diseal and petrol fuel type."

old_car = Diseal_Car('abc')
print(old_car.fuel_type())

new_car = Bi_Fuel_Car('xyz')
print(new_car.fuel_type())