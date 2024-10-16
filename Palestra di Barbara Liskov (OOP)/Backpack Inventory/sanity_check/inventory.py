

class Inventory:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Added {item.name}")
        else:
            print('Capacity reached')

    def remove(self, item):
        self.items.remove(item)

    def list_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory contains:")
            for item in self.items:
                print(f" - {item.name}")

    def use(self, item):
        if item in self.items:
            self.remove(item)
            print(f"Used {item.name}")

    def get_capacity(self):
        print(self.capacity)
        return self.capacity
