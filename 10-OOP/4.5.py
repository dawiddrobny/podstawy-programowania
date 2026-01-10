from thermometer import Thermometer

def main():
    t = Thermometer()
    t.turn_on()
    t.measure()
    t.turn_off()

if __name__ == "__main__":
    main()
