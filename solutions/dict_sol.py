# 1. Creating and Accessing
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}
print("Quantity of apples:", inventory["apples"])

# 2. Adding and Modifying
inventory["grapes"] = 12
inventory["pears"] = 6
inventory["bananas"] = 7
print("Updated inventory:", inventory)

# 3. Removing
del inventory["oranges"]
print("After removing oranges:", inventory)
pear_quantity = inventory.pop("pears")
print("After removing pears, inventory:", inventory)
print("Removed pears, quantity was", pear_quantity)

# 4. Looping
for item, quantity in inventory.items():
    print(f"The quantity of {item} is {quantity}")
