

from customer import Customer
from coffee import Coffee
from order import Order

#  test data
customer1 = Customer("Omondi")
coffee1 = Coffee("kenyan")
order1 = customer1.create_order(coffee1, 5.0)

# Prints
print("Customer name:", customer1.name)
print("Coffee name:", coffee1.name)
print("Order price:", order1.price)
print("Customer orders count:", len(customer1.orders()))
print("Customer coffees:", [coffee.name for coffee in customer1.coffees()])
print("Coffee orders count:", coffee1.num_orders())
print("Coffee average price:", coffee1average_price())