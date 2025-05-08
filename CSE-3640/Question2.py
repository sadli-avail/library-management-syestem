class CustomerOrder:
    def __init__(self, orderID, customerName, orderAmount):
        self.orderID = orderID
        self.customerName = customerName
        self.orderAmount = orderAmount

    def display_order(self):
        print(f"Order ID: {self.orderID}, Customer Name: {self.customerName}, Order Amount: ${self.orderAmount:.2f}")


def main():
    orders = [
        CustomerOrder(101, "Alice", 250.75),
        CustomerOrder(102, "Bob", 320.50),
        CustomerOrder(103, "Charlie", 150.00),
        CustomerOrder(104, "Diana", 400.00)
    ]

    print("\nCustomer Orders:")
    for order in orders:
        order.display_order()

    total_amount = sum(order.orderAmount for order in orders)
    print(f"\nTotal Order Amount: ${total_amount:.2f}")
