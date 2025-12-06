import json


def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_stats(data):
    reservations = data.get('reservations', [])
    num_rooms = len(reservations)
    paid_res = sum(1 for r in reservations if r['paid'])
    unpaid_res = num_rooms - paid_res

    total_paid = sum(r['price_per_night'] * r['nights']
                     for r in reservations if r['paid'])
    total_unpaid = sum(r['price_per_night'] * r['nights']
                       for r in reservations if not r['paid'])

    return num_rooms, paid_res, unpaid_res, total_paid, total_unpaid


def print_summary(stats):
    print(f"Number of rooms: {stats[0]}")
    print(f"Number of paid reservations: {stats[1]}")
    print(f"Number of unpaid reservations: {stats[2]}")
    print(f"Total value of paid reservations: {stats[3]:.2f}")
    print(f"Total value of unpaid reservations: {stats[4]:.2f}")


data = load_reservations('reservations.json')
if data:
    stats = calculate_stats(data)
    print_summary(stats)
