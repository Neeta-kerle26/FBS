
cp = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))

dis = (cp * discount) / 100
sp = cp - dis

print("Discount amount:", dis)
print("Selling price:", sp)