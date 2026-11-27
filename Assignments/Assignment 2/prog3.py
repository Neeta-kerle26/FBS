
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

meters = (feet * 0.3048) + (inches * 0.0254)
centimeters = meters * 100

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)