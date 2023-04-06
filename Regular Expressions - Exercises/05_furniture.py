import re

information = input()
items = []
money_spend_per_product = []

pattern = r"(^|(?<=\s))>>(?P<product>[A-Za-z]+)<<(?P<price>\d{0,}\.?\d{1,})!(?P<quantity>\d+)\b"
while information != "Purchase":
    products = re.finditer(pattern, information)
    for product in products:
        items.append(product.group("product"))
        total_price_for_product = float(product.group("price")) * int(product.group("quantity"))
        money_spend_per_product.append(total_price_for_product)
    information = input()

print("Bought furniture:")
for item in items:
    print(item)

print(f"Total money spend: {sum(money_spend_per_product):.2f}")

