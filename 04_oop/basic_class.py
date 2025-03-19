class Car:
    def __init__(self, user_brand, user_model):
        self.brand = user_brand
        self.model = user_model

    def display_name(self):
        print("The car is of brand {} and model is {}".format(self.brand, self.model))



if __name__ == "__main__":
    my_car1 = Car('Toyota', 'Corolla')
    my_car1.display_name()

    my_car2 = Car('Kia', 'Carens')
    my_car2.display_name()


# constructor method auto runs whenever a class is instanciated.

'''
self.brand = user_brand
means jo 'user_brand' parameter ki value hogi vo uthka ke jis object ne call (invoke) kiya h, uske ander ek variable 'brand' bna ke store krdo
'''

'''
Think of self in python context like this: (and why we pass it as a parameter)
You need to setup a telephone line to establish talking between class and the instance of it.
If no self keyword even in methods, then you won't be able to access or talk to variable belonging to an instance while you are present in class.
'''