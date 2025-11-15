def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    elif time_format == '12':
        if hours == 0:
            hour_str = 12
            period = 'am'
        elif hours == 12:
            hour_str = 12
            period = 'pm'
        elif hours < 12:
            hour_str = hours
            period = 'am'
        else:
            hour_str = hours - 12
            period = 'pm'
        return f"{hour_str}:{minutes:02d}{period}"


test_cases = [
    (15, 38, '24', '15:38'),
    (8, 3, '24', '08:03'),
    (0, 5, '24', '00:05'),
    (11, 15, '12', '11:15am'),
    (0, 7, '12', '12:07am'),
    (7, 30, '12', '7:30am'),
    (12, 46, '12', '12:46pm'),
    (13, 10, '12', '1:10pm'),
    (19, 2, '12', '7:02pm'),
]

for hours, minutes, time_format, expected in test_cases:
    result = time_string(hours, minutes, time_format)
    print(
        f"time_string({hours}, {minutes}, '{time_format}') = '{result}'", end=' ')
    print("zgadza sie" if result ==
          expected else f"nie zgadza sie (Expected: '{expected}')")
