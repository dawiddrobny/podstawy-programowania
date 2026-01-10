class Phone():
    def __init__(self, battery_level, is_on, is_locked):
        self.battery_level = battery_level
        self.is_on = is_on
        self.is_locked = is_locked
    
    def turn_on(self):
        self.is_on = True
        print("Phone is on")

    def unlock(self):
        if self.is_on:
            self.is_locked = False
            print("Phone is unlocked")
    
    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        print(f"Battery level: {self.battery_level}%")

def main():
    my_phone = Phone(50, False, True)
    my_phone.turn_on()
    my_phone.unlock()
    my_phone.charge(20)
    print(f"Phone status: On={my_phone.is_on}, Locked={my_phone.is_locked}, Battery={my_phone.battery_level}")

if __name__ == "__main__":
    main()
