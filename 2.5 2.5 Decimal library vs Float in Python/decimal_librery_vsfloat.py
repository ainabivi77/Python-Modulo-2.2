from decimal import Decimal
#product_cost = 88.40 
#commision_rate = 0.08 #8% comision del vendedor
#qty = 450 #objetos vendidos
#product_cost += (commision_rate * product_cost)
#print(product_cost * qty)#42962.4

product_cost = Decimal(88.40) 
commision_rate = Decimal(0.08) #8% comision del vendedor
qty = 450 #objetos vendidos

product_cost += (commision_rate * product_cost)
print(product_cost * qty)#42962.40000000000282883716451