# JS vs Python differences:
## Minor syntax differences
- No 'new' keyword in python for object creation unlike JS
- def __init__(): is just the constructor function
- self keyword is exactly same as 'this' from JS
- self/this just means a variable that stores the context of whoever is calling the method(function) or attribute(variable)

## Import/export
- JS: explicitly need to export and follow the ES6 syntax for import, plus the top-level code from the imported file doesn't run within the importing file.

```js
// inside basicClass.js
export class Car {
    constructor(userBrand, userModel) {
        this.brand = userBrand;
        this.model = userModel;
    }

    displayName() {
        console.log(`The car is of brand ${this.brand} and model is ${this.model}`);
    }
}

// This code runs only when directly executed within this file, not when imported.
const myCar = new Car('Toyota', 'Corolla');
myCar.displayName();

// inside main.js
import { Car } from './basicClass.js';

const newCar = new Car('Ford', 'Mustang');
newCar.displayName();  // Only this runs, not the code in basicClass.js
```

- PY: no need to export anything, implictly import with a different syntax, plus the top level code from imported file runs within exported file unless given a conditional in your imported file to handle that case.

```py
# inside basic_class.py
class Car:
    def __init__(self, user_brand, user_model):
        self.brand = user_brand
        self.model = user_model

    def display_name(self):
        print(f"The car is of brand {self.brand} and model is {self.model}")

# This code runs even when imported unless guarded by __name__ check
my_car1 = Car('Toyota', 'Corolla')
my_car1.display_name()

my_car2 = Car('Kia', 'Carens')
my_car2.display_name()


# inside main.py
from basic_class import Car

new_car = Car('Ford', 'Mustang')
new_car.display_name()  
# Output also includes unwanted prints from basic_class.py!


# To prevent top-level code from running, make this change in imported file.
if __name__ == "__main__":
    my_car1 = Car('Toyota', 'Corolla')
    my_car1.display_name()

    my_car2 = Car('Kia', 'Carens')
    my_car2.display_name()
```

## super()
- works the same in both just syntax difference
```js
class ElectricCar extends Car {
    constructor(brand, model, batterySize) {
        super(brand, model)
        this.batterySize = batterSize
    }
}
```
```py
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
```

## Overriding and Overloading
- Overriding exits in both and works in both the same.
- Overloading is not there in both. The last defination overrides the previous one.

## Encapsulation
- Same concept and getter/setter in both.
- In JS can't really privatize the variables of a class to prohibit access to the objects. 
- In Python '__' before a varible can make it private to that class.