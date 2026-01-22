# 1. تهيئة القوائم
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]

# 2. إنشاء القائمة الرئيسية وطباعتها
deli_dept = [meat, cheese]
print("Initial Deli List:", deli_dept)

# 3. إعادة تعبئة كمية Ham إذا كانت أقل من 100
if meat[2] < 100:
    meat[2] = 100

# 4. فرز القائمة أبجدياً بناءً على العنصر الأول في كل قائمة فرعية
deli_dept.sort()

# طباعة النتيجة النهائية
print("Updated Deli List:", deli_dept)