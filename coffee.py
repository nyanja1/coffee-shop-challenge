# Coffee  
class Coffee:
    def __init__(self, name):
        self._name = ""  
        self.name = name  
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        # Check if string and is least 3 characters
        if not isinstance(value, str):
            print("Error: Coffee name must be a string!")
            return
        if len(value) < 3:
            print("Error: Coffee name must be 3 or more characters!")
            return

        # only set name if not set
        if self._name == "":
            self._name = value
    
    name = property(get_name, set_name)


      Get all orders for this coffee
    def orders(self):
       
        from order import Order  
        my_orders = []
        for order in Order.all_orders:
            if order.coffee == self:
                my_orders.append(order)
        return my_orders

    # Get specific customers who ordered this coffee
    def customers(self):
        
        my_customers = []
        for order in self.orders():
            if order.customer not in my_customers:
                my_customers.append(order.customer)
        return my_customers

       # Count combined orders
    def num_orders(self):
    
        return len(self.orders())


     # Calculate average price
    def average_price(self):
    
        orders = self.orders()
        if len(orders) == 0:
            return 0
        total_price = 0
        for order in orders:
            total_price = total_price + order.price
        average = total_price / len(orders)
        return average