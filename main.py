class Car:
    total_cars = 0 #class variable

    def __init__(self, brand: str, model: str, year: int): #constructor methods
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        Car.total_cars += 1

    def accelerate(self, increment: int) -> str:
        self.speed += increment
        return f"{self.brand} {self.model} is now at {self.speed} km/h"

    def brake(self, decrement: int) -> str:
        self.speed = max(0, self.speed - decrement)
        return f"{self.brand} {self.model} is now at {self.speed} km/h"

    def stop(self) -> str:# speeds=0
        self.speed = 0
        return f"{self.brand} {self.model} has stopped."

    def is_moving(self) -> bool:#if def isMoving(self)>0, true
        return self.speed > 0

    
    def display_info(self) -> str:
        return (f"Car Info:\n"
                f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}\n"
                f"Current Speed: {self.speed} km/h\n"
                f"Total Cars: {Car.total_cars}")

class ElectricCar(Car): #inheritance(inherits from Car)
    def __init__(self, brand: str, model: str, year: int, battery_capacity: float):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity  
        self.battery_level = battery_capacity     

    def charge(self, amount: float) -> str: 
        if amount <= 0:
            return "Charge amount must be positive."
        if self.battery_level + amount > self.battery_capacity:
            self.battery_level = self.battery_capacity
            return f"{self.brand} {self.model} is now fully charged."
        else:
            self.battery_level += amount
            return f"{self.brand} {self.model} charged. Battery: {self.battery_level:.1f} kWh"

    def accelerate(self, increment: int) -> str:#override parent class
        energy_needed = increment * 0.05  
        if self.battery_level >= energy_needed:
            self.battery_level -= energy_needed
            self.speed += increment
            return f"{self.brand} {self.model} accelerated to {self.speed} km/h. Battery left: {self.battery_level:.1f} kWh"
        else:
            return f"Not enough battery to accelerate. Battery left: {self.battery_level:.1f} kWh"

    def display_info(self) -> str:
        base_info = super().display_info()
        return (f"{base_info}\n"
                f"Battery Level: {self.battery_level:.1f} kWh / {self.battery_capacity} kWh")


if __name__ == "__main__":
    print("\n----- Electric Car Example -----")
    electric_car = ElectricCar("Tesla", "Model 3", 2023, 75.0)
    print(electric_car.display_info())
    print(electric_car.accelerate(30))
    print(electric_car.brake(10))
    print(electric_car.charge(10))
    print(electric_car.stop())
    print(electric_car.display_info())
