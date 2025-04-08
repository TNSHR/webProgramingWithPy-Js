# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# p = Point(20,30)
# print(p.x)
# print(p.y)
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passengers(self,name):
        if not self.open_seats()==0:
            return False

        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = Flight(3)
people = ["herry","Ron", "hermione", "Ginny"]
for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"added {person} to flight successfully")
    else:
        print(f"No available seate for {person}")