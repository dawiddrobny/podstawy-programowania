class TV:
    def __init__(self):
        self.is_on = False

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")

def main():
    tv = TV()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.turn_off()
    tv.show_status()

if __name__ == "__main__":
    main()
