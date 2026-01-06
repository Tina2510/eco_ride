import pytest
from scr.vehicle import ElectricScooter

@pytest.fixture
def scooter1():
    return ElectricScooter("S1", "Ola ", 75, "Available", 40, 90)

@pytest.fixture
def scooter2():
    return ElectricScooter("S2", "Ather 450X", 65, "On Trip", 45, 80)

@pytest.fixture
def scooter3():
    return ElectricScooter("S3", "TVS ", 55, "Under Maintenance", 35, 75)

def test_scooter_to_dict(scooter1):
    d = scooter1.to_dict()
    assert d["vehicle_id"] == scooter1.vehicle_id
    assert d["model"] == scooter1.model
    assert d["battery_percentage"] == scooter1.battery_percentage
    assert d["maintenance_status"] == scooter1.maintenance_status
    assert d["rental_price"] == scooter1.rental_price
    assert d["vehicle_type"] == "ElectricScooter"
    assert d["max_speed_limit"] == scooter1.max_speed_limit

def test_object_creation(scooter1, scooter3):
    assert scooter1.max_speed_limit == 90
    assert scooter3.battery_percentage == 55
    assert scooter3.maintenance_status == "Under Maintenance"

@pytest.mark.parametrize(
    "minutes, expected",
    [(0, 1.0), (20, 4.0), (40, 7.0)]
)
def test_electric_scooter_trip_cost(scooter1, minutes, expected):
    assert scooter1.calculate_trip_cost(minutes) == expected
