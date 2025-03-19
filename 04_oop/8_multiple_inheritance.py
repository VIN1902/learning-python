class Battery:
    def battery_info(self):
        return 'This is battery.'

class Engine:
    def engine_info(self):
        return 'This is engine.'

class Electronic_Vehicle(Battery, Engine):
    pass

my_ev = Electronic_Vehicle()
print(my_ev.battery_info())
print(my_ev.engine_info())