# 1. أنشئ القائمة الأولى
vegetables = ["tomatoes", "potatoes", "onions"]

# 2. احذف "onions"
vegetables.remove("onions")

# 3. أضف "carrots" إذا لم تكن موجودة
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# 4. أضف "cucumbers" إذا لم تكن موجودة
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# 5. رتب القائمة أبجدياً
vegetables.sort()

# 6. اطبع النتيجة
print("Updated Vegetable Inventory:", vegetables)