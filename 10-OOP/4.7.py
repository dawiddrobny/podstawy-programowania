import statistics

class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print(*self.numbers)

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)

    def get_mean(self):
        return statistics.mean(self.numbers)

    def get_median(self):
        return statistics.median(self.numbers)

    def print_stats(self):
        print(f"Min: {self.get_min()}")
        print(f"Max: {self.get_max()}")
        print(f"Mean: {self.get_mean()}")
        print(f"Median: {self.get_median()}")

def main():
    stats = Statistics()
    for n in [12, 37, 6, 9, 17]:
        stats.add_number(n)
    
    stats.display_numbers()
    stats.print_stats()

if __name__ == "__main__":
    main()
