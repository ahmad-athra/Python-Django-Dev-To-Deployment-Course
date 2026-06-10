class Car():
    wheels = 4
    def __str__(self):
        print('__str__')
        return 'my car class'
    def __init__(self):
        print('__init__')
        print(self.wheels)
        print(self)
        print('__init__ End')



my_new_car = Car()
my_new_car.wheels = 5
print(my_new_car)