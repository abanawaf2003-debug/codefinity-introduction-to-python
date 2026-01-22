
discounted = False
lowStock = True
is_perishable = True
item_quantity = 110
perishable_highStockRisk = 100
consider_discount = is_perishable and (item_quantity >= perishable_highStockRisk)
print("Is the item perishable and high in stock?", consider_discount)