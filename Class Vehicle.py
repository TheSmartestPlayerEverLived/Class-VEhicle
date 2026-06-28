class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

tata = vehicle(240, 18)

print("Tata Max Speed:", tata.max_speed)
print("Tata Mileage:", tata.mileage)