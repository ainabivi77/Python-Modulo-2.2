import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices) #ordenar la lista
num_of_sales = len(sorted_list)#numero de elemntos de la lista
half_slice = math.floor(num_of_sales/2) # dividir la lista en dos
first_sales_items = sorted_list[:half_slice] #primera mitad de la lista
last_sales_items = sorted_list[-(half_slice):] # segunda mitad de la lista
median = sorted_list[half_slice:(half_slice + 1)] #mediana

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)