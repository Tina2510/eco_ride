import pytest
from scr.vehicle import (
    ElectricCar, ElectricScooter, hubs,
    add_hub, add_vehicle_to_hub,
    search_by_hub, search_by_battery,
    categorized_view, fleet_status_summary,
    sort_vehicles_by_model,
    sort_vehicles_by_battery,
    sort_vehicles_by_rental_price
)

@pytest.fixture(autouse=True)
def reset_hubs():
    hubs.clear()
    yield
    hubs.clear()

@pytest.fixture
def car1():
    return ElectricCar("C1", "Tesla", 85, "Available", 100, 5)

@pytest.fixture
def scooter1():
    return ElectricScooter("S1", "Ola ", 75, "Available", 40, 90)

def test_add_hub(capsys):
    add_hub("Hub1")
    out = capsys.readouterr().out
    assert "added successfully" in out
    assert "Hub1" in hubs

def test_add_existing_hub(capsys):
    add_hub("Hub1")
    add_hub("Hub1")
    out = capsys.readouterr().out
    assert "already exists" in out

def test_add_vehicle_to_hub(capsys, car1):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", car1)
    out = capsys.readouterr().out
    assert "added to hub" in out
    assert car1 in hubs["HubA"]

def test_search_by_hub(car1):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", car1)
    assert search_by_hub("HubA") == [car1]

def test_search_by_hub_nonexistent(capsys):
    result = search_by_hub("HubX")
    out = capsys.readouterr().out
    assert result == []
    assert "does not exist" in out

def test_search_by_battery(car1, scooter1):
    add_hub("HubA")
    add_hub("HubB")
    add_vehicle_to_hub("HubA", car1)
    add_vehicle_to_hub("HubB", scooter1)
    result = search_by_battery(70)
    assert ("HubA", [car1]) in result
    assert ("HubB", [scooter1]) in result

def test_categorized_view(car1, scooter1, capsys):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", car1)
    add_vehicle_to_hub("HubA", scooter1)
    categorized_view()
    out = capsys.readouterr().out
    assert "Electric Cars:" in out
    assert "Electric Scooters:" in out

def test_fleet_status_summary(car1, scooter1):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", car1)
    add_vehicle_to_hub("HubA", scooter1)
    summary = fleet_status_summary()
    assert summary["Available"] == 2
    assert summary["On Trip"] == 0
    assert summary["Under Maintenance"] == 0

def test_sort_vehicles_by_model(car1, scooter1):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", scooter1)
    add_vehicle_to_hub("HubA", car1)
    sorted_list = sort_vehicles_by_model("HubA")
    assert sorted_list[0] == scooter1
    assert sorted_list[1] == car1

def test_sort_vehicles_by_battery(car1, scooter1):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", scooter1)
    add_vehicle_to_hub("HubA", car1)
    sorted_list = sort_vehicles_by_battery("HubA")
    assert sorted_list[0] == car1

def test_sort_vehicles_by_rental_price(car1, scooter1):
    add_hub("HubA")
    add_vehicle_to_hub("HubA", scooter1)
    add_vehicle_to_hub("HubA", car1)
    sorted_list = sort_vehicles_by_rental_price("HubA", descending=True)
    assert sorted_list[0] == car1
