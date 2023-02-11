orders_count = int(input())

total_price = 0

for _ in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    price = capsules_needed_per_day * days * price_per_capsule
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f'Total: ${total_price:.2f}')
