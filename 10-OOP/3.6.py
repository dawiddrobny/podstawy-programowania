class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
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
    
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
    
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

def main():
    tv = TV()
    tv.turn_on()
    tv.show_status()
    tv.increase_volume()
    tv.show_status()
    tv.decrease_volume()
    tv.show_status()

if __name__ == "__main__":
    main()
