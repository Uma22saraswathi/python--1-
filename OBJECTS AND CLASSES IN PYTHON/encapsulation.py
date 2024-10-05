class company():
    def __init__(self):
        self.__company_name = "Google" #private variables__

    def company_name(self):
        print(self.__company_name)   
c1 = company() 
c1.company_name()
print("_____________________")
#task:2
class car:
    def open_door(self):
        print("door opened")
        print("enter into car and started")
        self._accelerate()#protected

    def _accelerate(self): #protected 
        print("throttle increased")
        self.__engine_performing() #private

    def __engine_performing(self):#private
        print("burst inside")
        print("car is moving")


my_car=car()
my_car.open_door()        

                                                                                                                                                                                                                                                                      