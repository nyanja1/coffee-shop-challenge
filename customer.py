# class customer
class Customer:
    def __init__(self, name):
        self._name = ""  
        self.name = name  
    
    def get_name(self):
        return self._name
    
        # check if the name is between 1-15 characters
    def set_name(self, value):
        
        if not isinstance(value, str):
            print("Error: Name must be a string!")
            return
        if len(value) < 1 or len(value) > 15:
            print("Error: Name must be 1 to 15 characters!")
            return
        self._name = value
    
    name = property(get_name, set_name)

   
        # Get all orders for  customer 
    def orders(self):
        
        from order import Order  
        my_orders = []
        for order in Order.all_orders:
            if order.customer == self:
                my_orders.append(order)
        return my_orders
    
       # Get the coffees ordered
    def coffees(self):
       
        my_coffees = []
        for order in self.orders():
            if order.coffee not in my_coffees:
                my_coffees.append(order.coffee)
        return my_coffees
    
    # Creating new order

    def create_order(self, coffee, price):
        
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order