class Hospital():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.maxRoom = 0
        self.maxPatientsInRoom = 0
        self.occupiedRooms = 1
        self.currentPatientsInRoom = 0

    def set_maxRoom(self, rooms):
        self.maxRoom = rooms
    def get_maxRoom(self):
        print(f"The hospital has {self.maxRoom} rooms")

    def set_maxPatientsInRoom(self, maxPatients):
        self.maxPatientsInRoom = maxPatients
    def get_maxPatientsInRoom(self):
        print(f"Each room may have at most {self.maxPatientsInRoom} patients")

    def checkIn(self):
        self.currentPatientsInRoom = self.currentPatientsInRoom + 1
        if self.currentPatientsInRoom > self.maxPatientsInRoom:
            self.currentPatientsInRoom = 0
            self.occupiedRooms = self.occupiedRooms + 1
            if self.occupiedRooms > self.maxRoom:
                print("The hospital is full!")
        
    def checkOut(self):
        self.currentPatientsInRoom = self.currentPatientsInRoom - 1
        if self.currentPatientsInRoom == 0:
            self.occupiedRooms = self.occupiedRooms - 1
