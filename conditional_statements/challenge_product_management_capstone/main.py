# Input variables
days_until_expiration = 5  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

# تحقق من نوع المنتج أولاً
if product_type == "Perishable":
    # إذا قابل للفساد، قرر حجم الخصم حسب الأيام المتبقية
    if days_until_expiration <= 3:
        print("Big discount applied")
    else:
        print("Small discount applied")
else:
    # غير قابل للفساد
    print("No discount for non-perishable items.")