from Passenger import Passenger
class TrainRerservation:
    staticmethod                            #Initial Value assignment
    tickets={}      
    lower,lTotalSize,lCurrentSize=[],5,0
    upper,uTotalSize,uCurrentSize=[],5,0
    rac,racTotalSize,racCurrentSize=[],5,0
    wl,wlTotalSize,wlCurrentSize=[],5,0
    lAvailableSeatSize=lTotalSize-lCurrentSize
    uAvailableSeatSize=lTotalSize-uCurrentSize
    racAvailableSeatSize=lTotalSize-racCurrentSize
    wlAvailableSeatSize=lTotalSize-wlCurrentSize

    def lowerBerthAdd(self,p):              #Add a passanger to Lower bearth
        p.confirmBerth="L"
        self.lCurrentSize+=1
        p.seatNo=self.lCurrentSize
        self.lower.append(p)
        self.lTotalSize-=1
        self.lAvailableSeatSize-=1
        self.tickets['L']=self.lower
        print(p.name,p.seatNo,p.confirmBerth,'has Lower Berth Booked Successfully !')
    
    def upperBerthAdd(self,p):                #Add a passanger to Upper bearth
        p.confirmBerth="U"
        self.uCurrentSize+=1
        p.seatNo=self.uCurrentSize
        self.upper.append(p)
        self.uTotalSize-=1
        self.uAvailableSeatSize-=1
        self.tickets['U']=self.upper
        print(p.name,p.seatNo,'has Upper Berth Booked Successfully !')

    def racAdd(self,p):                     #Add a passanger to RAC bearth
        p.confirmBerth="RAC"
        self.racCurrentSize+=1
        p.seatNo=self.racCurrentSize
        self.rac.append(p)
        self.racTotalSize-=1
        self.racAvailableSeatSize-=1
        self.tickets['RAC']=self.rac
        print(p.name,p.seatNo,'has RAC Booked Successfully !')
        return
    
    def wlAdd(self,p):                          #Add a passanger to WaitingList bearth
        p.confirmBerth="WL"
        self.wlCurrentSize+=1
        p.seatNo=self.wlCurrentSize
        self.wl.append(p)
        self.wlTotalSize-=1
        self.wlAvailableSeatSize-=1
        self.tickets['WL']=self.wl
        print(p.name,p.seatNo,'has WL Booked Successfully !')
        return

    def addTicket(self,p):                                  #Add ticket method
        if p.berth=='L':
            if self.lTotalSize>0:
                self.lowerBerthAdd(p)
                return
            elif self.uTotalSize>0:
                print("Oops! Lower berth is not available")
                self.upperBerthAdd(p)
                return
            elif self.racTotalSize>0:
                print('Oops! Upper Berth also is not Available')
                self.racAdd(p)
                return
            elif self.wlTotalSize>0:
                print('Oops! RAC is not Available')
                self.wlAdd(p)
                return
            else:
                print("Sorry Train is not availble")
                return
        else:
            if self.uTotalSize>0:
                self.upperBerthAdd(p)
                return
            elif self.lTotalSize>0:
                print("Oops! Upper berth is not available")
                self.lowerBerthAdd(p)
                return
            elif self.racTotalSize>0:
                print('Oops! Lower Berth also is not Available')
                self.racAdd(p)
                return
            elif self.wlTotalSize>0:
                print('Oops! RAC is not Available')
                self.wlAdd(p)
                return
            else:
                print("Sorry Train is not availble")
                return
            
    def deleteTickets(self,seatNo,berth):                   #Cancel ticket method
        if berth=='L':
            print(seat,'----',self.lTotalSize)
            if seatNo<=self.lTotalSize and self.lower[seatNo-1] in self.lower:
                r=self.lower.pop(seatNo-1)
                self.lTotalSize+=1
                print(r.id,"has Deleted Successfully ***!!!")
                if self.racCurrentSize:
                    self.addTicket(self.rac.pop(0))
                
            else:
                print("SeatNo is not exists")
                return

        elif berth=='U':
            if seatNo<=self.uTotalSize and self.upper[seatNo-1]:
                r=self.upper.pop(seatNo-1)
                self.uTotalSize+=1
                print(r.id,"has Deleted Successfully ***!!!")
                if self.racCurrentSize:
                    self.addTicket(self.rac.pop(0))
            else:
                print("SeatNo is not exists")
                return
            
        elif berth=='RAC':
            if seatNo<=self.racTotalSize and self.rac[seatNo-1]:
                r=self.rac.pop(seatNo-1)
                self.racTotalSize+=1
                print(r.id,"has Deleted Successfully ***!!!")
                if self.wlCurrentSize:
                    self.addTicket(self.wl.pop(0))
            else:
                print("SeatNo is not exists")
                return 
            
        elif berth=='WL':
            if seatNo<=self.wlTotalSize and self.wl[seatNo-1]:
                r=self.wl.pop(seatNo-1)
                self.wlTotalSize+=1
                print(r.id,"has Deleted Successfully ***!!!")
                if self.racCurrentSize:
                    self.addTicket(self.rac.pop(0))
                return
            else:
                print("SeatNo is not exists")
                return
        else:
            print("Please enter a correct berth type")
            return

            

    def displayAllDetails(self):                               #Passanger details display method
        print(len(self.tickets))
        for keys,values in self.tickets.items():
            for i in values:
                print(keys,'===>',i.id,'---->>',i.name)
    
    def showSeatAvailabilities(self):                           #Seat Availability method
        print("Lower seats:{}".format(self.lAvailableSeatSize))
        print("Upper seats:{}".format(self.uAvailableSeatSize))
        print("Rac seats:{}".format(self.racAvailableSeatSize))
        print("Wlist seats:{}".format(self.wlAvailableSeatSize))

                
if __name__=='__main__':
    tr=TrainRerservation()
    id=0
    while(True):
        #Input from User for Choices
        print('1) Add ticket.')
        print('2) Delete ticket.')
        print('3) Display all availability.')
        print('4) Passangers Details.')
        print('5) Exit.')
        
        while(True):
            choice=input('Enter a choice')
            if choice.isdigit():
                choice=int(choice)
                break
        if choice==1:                           #1 => AddTicket
            id+=1
            name=input('Enter your name:')
            while(True):
                age=input('Enter your age: ')
                if age.isdigit():
                    age=int(age)
                    break
            while(True):
                seat=input('Enter a Coach type L-lower U-upper')
                if seat=='L' or seat=='U':
                    break
            p1=Passenger(id,name,age,seat)      #Create a New Passanger
            tr.addTicket(p1)                    #Add Passanger using id and berth
            
        elif choice==2:                         #Cancel a Booked Ticket   
            if id!=0:
                while(True):
                    id=input('Enter SeatNo: ')     
                    if id.isdigit():
                        id=int(id)
                        break
                while(True):
                    seat=input('Enter a Coach type L-lower U-upper')
                    if seat=='L' or seat=='U' or seat=='RAC' or seat=='WL':
                        break
                tr.deleteTickets(id,seat)         #Remove Passanger using id and berth
            else:
                print("No tickets are booked. So you don't delete anyone")
                continue
        elif choice==3:
            res=tr.showSeatAvailabilities()     #Seat Availabilty Checking
        elif choice==4:
            tr.displayAllDetails()              #Display All Passanger Details
        elif choice==5:
            break                               #Exit from option
        else:
            print('Please a valid options')     #Any user input has wrong throw the message and again to loop
                
