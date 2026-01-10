import random

class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            temp = round(random.uniform(34.0, 42.0), 1)
            message = f"Temperature: {temp}C"
            if temp >= 37.0:
                message += " (fever)"
            if temp >= 41.0:
                message += " CRITICAL TEMPERATURE!!"
            print(message)
        else:
            print("Thermometer is off")
