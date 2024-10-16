# main.py
from item import Item
from inventory import Inventory


def main():
    # Create an inventory with a capacity of 10
    inventory = Inventory(capacity=10)

    # Create an item
    item = Item(name='palla++', category='Pokeball')

    # Add item to the inventory
    inventory.add(item)

    # List items in the inventory
    inventory.list_items()

    inventory.use(item)
    inventory.list_items()



if __name__ == "__main__":
    main()