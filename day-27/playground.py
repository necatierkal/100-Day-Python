def add(*args):
    total=0
    for item in args:
        total+=item
    print (total)

add(3,6,8,2)

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)



class Car:
    def __init__(self,**kw):
        self.make = kw.get("make") # get metodunu kullanırsak değer atanmazsa none değeri döndürür ve kodu patlatmaz
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model="GT-R")
print(my_car.model)

my_car = Car(make = "Nissan")
print(my_car.model)