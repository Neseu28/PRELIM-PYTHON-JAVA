class Vehicle:
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.daily_rate = daily_rate

    def calculate_rental(self, days):
        return self.daily_rate * days

    def __str__(self):
        return (f"Vehicle: {self.brand} | "
                f"Daily rate: PHP {self.daily_rate:.2f}")


class Car(Vehicle):
    def __init__(self, brand, daily_rate, seat_capacity):
        super().__init__(brand, daily_rate)
        self.seat_capacity = seat_capacity


    def __str__(self):
        return (f"Car: {self.brand} | "
                f"Daily rate: PHP {self.daily_rate:.2f} | "
                f"Seats: {self.seat_capacity}")


class Motorcycle(Vehicle):
    def __init__(self, brand, daily_rate, engine_capacity_cc):
        super().__init__(brand, daily_rate)
        self.engine_capacity_cc = engine_capacity_cc


    def __str__(self):
        return (f"Motorcycle: {self.brand} | "
                f"Daily rate: PHP {self.daily_rate:.2f} | "
                f"Engine: {self.engine_capacity_cc} cc")


def main():
    vehicles = [
        Car("Toyota", 1500, 5),
        Motorcycle("Honda", 500, 150)
    ]


    for vehicle in vehicles:
        print(vehicle)
        print(f"Rental charge for 3 days: "
              f"PHP {vehicle.calculate_rental(3):.2f}")
        print()




if __name__ == "__main__":
    main()