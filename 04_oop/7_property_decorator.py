class Demo_Property:
    def __init__(self, kuch_bhi):
        self.__kuch_bhi = kuch_bhi
    
    def view_kuch_bhi_attribute(self):
        return self.__kuch_bhi

instance = Demo_Property('aloo')
print(instance.view_kuch_bhi_attribute())

'''
TL;DR:
@property decorator can be used to define a getter method that allows accessing a private attribute (__kuch_bhi) as if it were a regular attribute.
usecase: when you want that instance can access the attribute normally (not through a method like getter) AND unable to change/modify it.

view_kuch_bhi_attribute right now is just a getter method.
but we can use @property decorator to change the behaviour of our getter method in a way, that allows attribute can be get by not calling it like a method, but instead normally accessing method now just with a different name.
'''

class Demo_Property:
    def __init__(self, kuch_bhi):
        self.__kuch_bhi = kuch_bhi
    
    @property
    def view_kuch_bhi_attribute(self):
        return self.__kuch_bhi

instance = Demo_Property('aloo')
print(instance.view_kuch_bhi_attribute) # attribute name changed to view_kuch_bhi_attribute from kuch_bhi