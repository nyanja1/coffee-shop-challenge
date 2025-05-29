
class Order:
    all_orders = []  
    
    def __init__(self, customer, coffee, price):
        # Validate inputs
        from customer import Customer 
        from coffee import Coffee
        if not isinstance(customer, Customer):
            print("Customer must be a Customer object!")
            return
        if not isinstance(coffee, Coffee):
            print("Coffee must be a Coffee object!")
            return
        if not isinstance(price, float):
            print("Price must be in decimals!")
            return
        if price < 1.0 or price > 10.0:
            print("Price must be between 1.0 and 10.0!")
            return
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)
    
    def get_customer(self):
        return self._customer
    
    def get_coffee(self):
        return self._coffee
    
    def get_price(self):
        return self._price
    
    customer = property(get_customer)
    coffee = property(get_coffee)
    price = property(get_price)