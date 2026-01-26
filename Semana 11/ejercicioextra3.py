class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryItem(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

class Inventory(Product):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def update_quantity(self, item, new_quantity):
        item.quantity = new_quantity

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def get_total_value(self):
        total_value = 0
        for item in self.items:
            total_value += item.total_value()
        return total_value

class InventoryItem(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def total_value(self):
        return self.price * self.quantity
# Example usage
inventory = Inventory()
item1 = InventoryItem("Milk", 2.5, 10, "2024-12-01")
item2 = InventoryItem("Bread", 1.5, 20, "2024-11-15")
inventory.add_item(item1)
inventory.add_item(item2)
print(f"Total value of inventory: ${inventory.get_total_value()}")
