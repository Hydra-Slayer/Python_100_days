def add(*args):
    #args is a tuple
    sum = 0
    for arg in args:
        sum +=arg
    return(sum)

def calculate(n,**kwargs):
    #kwargs is a dictionary
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
    
calculate(2, add = 3, multiply = 5)

class Car:
    def __init__(self,**kwargs):
            self.make = kwargs.get("make")
            self.model = kwargs.get["model"]
            
my_car = Car(make="Nissan", model = "Fairlady 350 Z")