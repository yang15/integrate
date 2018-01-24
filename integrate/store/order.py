"""
Example introduction to OOP in Python
"""

class Item(object):

#    count = 0 # static variable

    def __init__(self, name, num_items, unit_price):
        self.name = name
        self.num_items =  num_items
        self.unit_price = unit_price
        print ('Hello world OOP')
#        Item.count += 1
        
    
    def total(self):
        """ Calculate the totla of the Item"""
        
        return self.num_items * self.unit_price

class Order(object):
    """ Order of multiple items """
    

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item) # O(N) complexity very slow for numpy

    def remove_item(self, item):
        self.items.remove(item)

    def order_total(self):
        summ = 0
        for item in self.items:
            summ += item.total()

        return summ

