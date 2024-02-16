class Passenger:                #Passanger create class
    id=0
    name=''
    age=0
    berth=''
    confirmBerth=None
    seatNo=0
    def __init__(self,id,name,age,berth):
        self.id=id
        self.name=name
        self.age=age
        self.berth=berth
