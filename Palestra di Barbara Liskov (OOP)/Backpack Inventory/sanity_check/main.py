from item import Item
from inventory import Inventory


def main():
    inventory = Inventory(capacity=10)

    item = Item(name='palla++', category='Pokeball')

    inventory.add(item)

    inventory.list_items()

    inventory.use(item)

    inventory.list_items()



if __name__ == "__main__":
    main()