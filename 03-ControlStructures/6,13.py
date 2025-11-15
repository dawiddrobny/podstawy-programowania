speed_limit_min = 40
speed_limit_max = 140

car_speed = float(input("Enter car speed: "))

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
