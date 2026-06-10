# encapsilation
# data hidding

# abstraction
# implimentation hidding




# abc  abstract base class



from abc import ABC,abstractmethod

'# abc -> Module  , ABC -> class    ,abstractclassmethod -> Decorator'


class Vehcle(ABC):
    
    @abstractmethod
    def breaks(self):
        pass
    
    @abstractmethod
    def accelareto(self):
        pass
    
class Bike(Vehcle):
    def breaks(self,price):
        self.price=price
        print("Bike has disc breaks")
        
    def accelareto(self):
        print("Bike has good accelareto")
        
yas=Bike()
yas.breaks(5000)