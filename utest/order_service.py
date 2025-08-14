

DATABASE = {
    "orders": []
}

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total_amount(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def save(self):
        # Simulate saving to a DB
        DATABASE["orders"].append({
            "customer": self.customer_name,
            "items": self.items.copy(),
            "total": self.total_amount()
        })
        
    @staticmethod
    def division(a, b) -> int | float:
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        return a / b

    @staticmethod
    def get_all_orders():
        return DATABASE["orders"]