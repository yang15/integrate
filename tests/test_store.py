"""
THes the store package for creating orders
"""

from integrate.store.order import Item, Order
import pytest


@pytest.fixture #fixture function
def one_item():
    return Item('Apple', 2, 10)

def test_create_order():
    my_item = Item('', 2, 10)
    print(my_item)

    n = my_item.num_items
    
    assert n == 2


def test_total():
    my_item = Item('', 2, 10)

    total = my_item.total()

    assert total == 20

#def test_count():
#    print('count=', Item.count)

def test_order(one_item):
    my_order = Order()
    
    my_order.add_item(one_item)
    my_order.add_item(one_item)

    assert len(my_order.items) == 2

    assert my_order.order_total()  == 40
