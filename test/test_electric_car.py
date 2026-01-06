import pytest
from scr.vehicle import ElectricCar, Vehicle

@pytest.fixture
def car1():
    return ElectricCar("C1", "Tesla", 85, "Available", 100, 5)

@pytest.fixture
def car2():
    return ElectricCar("C2", "Maruthi", 70, "On Trip", 90, 4)

@pytest.fixture
def car3():
    return ElectricCar("C3", "MG", 60, "Under Maintenance", 80, 5)

def test_car_to_dict(car1):
    d = car1.to_dict()
    assert d["vehicle_id"] == car1.vehicle_id
    assert d["model"] == car1.model
    assert d["battery_percentage"] == car1.battery_percentage
    assert d["maintenance_status"] == car1.maintenance_status
    assert d["rental_price"] == car1.rental_price
    assert d["vehicle_type"] == "ElectricCar"
    assert d["seating_capacity"] == car1.seating_capacity

def test_object_creation(car1, car2):
    assert car1.vehicle_id == "C1"
    assert car1.seating_capacity == 5
    assert car2.model == "Maruthi"

def test_vehicle_is_abstract():
    with pytest.raises(TypeError):
        Vehicle("V1", "Test", 80, "Available", 100)

@pytest.mark.parametrize(
    "distance, expected",
    [(0, 5.0), (10, 10.0), (20, 15.0)]
)
def test_electric_car_trip_cost(car1, distance, expected):
    assert car1.calculate_trip_cost(distance) == expected

@pytest.mark.parametrize("battery_value", [1, 25, 50, 75, 100])
def test_valid_battery_percentage(car1, battery_value):
    car1.battery_percentage = battery_value
    assert car1.battery_percentage == battery_value

@pytest.mark.parametrize("battery_value", [0, -1, 101, 150])
def test_invalid_battery_percentage(car1, battery_value):
    with pytest.raises(ValueError):
        car1.battery_percentage = battery_value
