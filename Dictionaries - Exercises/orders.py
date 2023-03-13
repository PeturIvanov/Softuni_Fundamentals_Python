product = input()
shop = {"products": {}}
while product != "buy":
    product_name, price, quantity = product.split()
    price = float(price)
    quantity = float(quantity)

    # creating the product with value list with price and quantity in the our shop.
    if product_name not in shop["products"]:
        shop["products"][product_name] = [price, quantity]

    # change na price of our product and increase the quantity in the shop.
    else:
        shop["products"][product_name][0] = price
        shop["products"][product_name][1] += quantity
    product = input()


# k = product
# v = list with price and quantity
for k, v in shop["products"].items():
    total_price = v[0] * v[1]
    print(f"{k} -> {total_price:.2f}")
