class Helicopter():
    def __init__(self, family, production):
        self.family = family
        self.production = production
        self.isOn = False
        self.maxSpeed = 293
        self.currentSpeed = 0
        self.maxHeight = 7620
        self.currentHeight = 0
        
    def get_currentSpeed(self):
        print(self.currentSpeed)

    def get_currentHeight(self):
        print(self.currentHeight)

    def get_maxSpeed(self):
        print(self.maxSpeed)

    def get_maxHeight(self):
        print(self.maxHeight)

    def start(self):
        self.isOn = True

    def land(self):
        self.isOn = False
    
    def speedUp(self, speed):
        if self.isOn == False:
            return
        if self.currentSpeed + speed > self.maxSpeed:
            print("Warning!Can not get faster than 293mph")
        else:
            self.currentSpeed = self.currentSpeed + speed
        
    def slowDown(self, speed):
        if self.isOn == False:
            return
        if self.currentSpeed - speed <= 0:
            self.currentSpeed = 0
        else:
            self.currentSpeed = self.currentSpeed - speed
    
    def getHigher(self, height):
        if self.isOn == False:
            return
        if self.currentHeight + height > self.maxHeight:
            print("Warning!Can not get higher than 7620meters")
        else:
            self.currentHeight = self.currentHeight + height
    
    def getLower(self, height):
        if self.isOn == False:
            return
        if self.currentHeight - height <= 0:
            self.currentHeight = 0
        else:
            self.currentHeight = self.currentHeight - height
