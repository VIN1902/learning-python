class Random_Class:

    total_instance = 0 # class variable -> shared among all instance of this class

    def __init__(self):
        Random_Class.total_instance += 1 # class variables can only be accessed by class
        # type(self).total_instance += 1 (alt)

random_object = Random_Class()
Random_Class()
Random_Class()
Random_Class()
Random_Class()
print(Random_Class.total_instance)