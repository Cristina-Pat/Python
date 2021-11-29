class Vehicle:
    def __init__(self, c, p):
        self.color = c
        self.plate = p
        self.next = None
    
    def print1(self):
        print(self.plate + ' - ' + self.color + '\n')


class Stack:
    def __init__(self):
        self.head = None

    def addVehicle(self, c, p):
        v = Vehicle(c, p)
        v.next = self.head
        self.head = v

    def removeVehicle(self):
        x = self.head
        self.head = x.next

    def print2(self):
        i = self.head
        while (i != None):
            i.print1()
            i = i.next

       
s = Stack()
s.addVehicle('green', 'ac 34')
s.addVehicle('blue', 'cv 67')
s.addVehicle('white', 'gf 98')
#s.print2()
s.removeVehicle()
s.print2()


