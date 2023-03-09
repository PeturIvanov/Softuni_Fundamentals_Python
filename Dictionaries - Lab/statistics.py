key_value = input()
store = {}

while key_value != "statistics":
    product, value = key_value.split(":")
    if product in store:
        store[product] += int(value)
    else:
        store[product] = int(value)

    key_value = input()

total_products = len(store.keys())
total_quantity = sum(store.values())
print("Products in stock:")

for (product, quantity) in store.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
