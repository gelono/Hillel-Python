# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний
# засіб". Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    speed: float = 0.0
    mass: float = 0.0

    def calculate_speed(self, distance: float, dis_time: float) -> None:
        self.speed = distance / dis_time

    def setup_mass(self, new_mass):
        self.mass = new_mass


class Car(Vehicle):
    manufacturer: str = None
    color: str = None
    engine: float = None

    def __init__(self, manufacturer, color, engine):
        self.manufacturer = manufacturer
        self.color = color
        self.engine = engine


class Plane(Vehicle):
    company: str = None
    number_of_seats: int = None
    base_airport: str = None

    def __init__(self, company, number_of_seats, base_airport):
        self.company = company
        self.number_of_seats = number_of_seats
        self.base_airport = base_airport


class Ship(Vehicle):
    ship_type: str = None
    displacement: float = 0.0

    def __init__(self, displacement, ship_type='Tanker'):
        self.ship_type = ship_type
        self.displacement = displacement


car = Car('BMW', 'Black', 2000.0)
plane = Plane('Boing', 120, 'Heathrow Airport')
ship = Ship(10000.0)

print(f'Ship type: {ship.ship_type}, displacement: {ship.displacement}')

print(f'Start speed of car: {car.speed} km/h')
car.calculate_speed(100.0, 1.5)
print(f'new speed of car: {car.speed} km/h')

print(f'Default plane mass: {plane.mass} kg')
plane.setup_mass(50000.0)
print(f'New plane mass: {plane.mass} kg')
