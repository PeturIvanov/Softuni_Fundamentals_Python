class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        init_capacity = self.capacity
        if init_capacity > 0:
            self.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return self.storage
