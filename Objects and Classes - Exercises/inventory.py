class Inventory:
    def __init__(self, __capacity: int):
        self.items = []
        self.capacity = __capacity

    def add_item(self, item: str):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        capacity_left = self.capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {capacity_left}"
