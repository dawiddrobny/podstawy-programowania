time_24 = input("Enter time (24-hour format, hh:mm): ")

hh, mm = time_24.split(':')
hh = int(hh)
mm = int(mm)
if hh == 0:
    period = 'am'
    hh_12 = 12
elif hh < 12:
    period = 'am'
    hh_12 = hh
elif hh == 12:
    period = 'pm'
    hh_12 = 12
elif hh > 12:
    period = 'pm'
    hh_12 = hh - 12

print(f"Time in 12-hour format: {hh_12}:{mm:02d}{period}")
