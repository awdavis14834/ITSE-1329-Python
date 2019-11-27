# DO NOT TOUCH ============================================
from random import randint
pizzas = [
   'Pizza - Pepperoni',
   'Pizza - Cheese',
   'Pizza - Sausage',
   'Pizza - Supreme',
   'Pizza - Veggie'
   ]
selected_pizza = pizzas[randint(0, 4)]
# DO NOT TOUCH ============================================

pizza_type = selected_pizza.replace('Pizza - ', '')  # fill in blank 

print(pizza_type)