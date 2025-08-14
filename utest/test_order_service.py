
import pytest
from order_service import Order, DATABASE

@pytest.fixture
def db_fixture():
    """
    Simulates database setup before each test
    and clears it after the test.
    """
    # Setup: clear DB before test
    DATABASE["orders"].clear()
    yield DATABASE 
    
    # Teardown: clear DB after test
    DATABASE["orders"].clear()
    

@pytest.fixture
def order_fixture(db_fixture):
    """
    Creates an order with default items and saves it to the simulated DB.
    """
    order = Order("John Doe")
    order.add_item("Laptop", 1200, quantity=1)
    order.add_item("Mouse", 50, quantity=2)
    order.save()
    return order



def test_total_amount(order_fixture):
    assert order_fixture.total_amount() == 1300, "not much"
    


def test_order_saved_to_db(order_fixture):
    orders = Order.get_all_orders()
    assert len(orders) == 1
    assert orders[0]["customer"] == "John Doe"

def test_add_additional_order(db_fixture):
    order = Order("Jane Smith")
    order.add_item("Keyboard", 100, quantity=1)
    order.save()
    assert len(Order.get_all_orders()) == 1
    assert Order.get_all_orders()[0]["customer"] == "Jane Smith"
    
    
def test_fixture(db_fixture, order_fixture):
    assert db_fixture["orders"] and db_fixture["orders"][0]["customer"] == "John Doe"
    
    order = Order("Giramata Sheilla")
    order.add_item("Oil", 100, quantity=1)
    order.add_item("Chicken", 50, quantity=2)
    order.save()
    
    assert db_fixture["orders"][1]["customer"] == "Giramata Sheilla", "User not added in db"    
    
    assert len(Order.get_all_orders()) == 2, "oders not added in db"
    


def test_division():
    with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
        assert Order.division(34, 0)

