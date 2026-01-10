class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]})")
            else:
                print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, channels_list):
        self.channels = channels_list
    
    def show_channels(self):
        print("Channel list:")
        for i, channel in enumerate(self.channels, 1):
            print(f"{i}. {channel}")

def main():
    tv = TV()
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "HBO"])
    tv.turn_on()
    for i in range(1, 8):
        tv.set_channel(i)
        tv.show_status()

if __name__ == "__main__":
    main()
