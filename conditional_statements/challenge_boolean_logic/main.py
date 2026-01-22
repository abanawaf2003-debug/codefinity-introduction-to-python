seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Step 1: determine overstock risk
overstock_risk = seasonal and current_stock > high_stock_threshold

# Step 2: determine discount eligibility
discount_eligible = not selling_well and not on_sale

# Step 3: decide if we make a discount
make_discount = overstock_risk or discount_eligible

# Step 4: print the result
print("Should the item be discounted?", make_discount)