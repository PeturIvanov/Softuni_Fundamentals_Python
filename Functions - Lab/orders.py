def total_sum(product, amount):
    result = 0
    if product == "coffee":
        result = 1.50 * amount
    elif product == "water":
        result = 1.00 * amount
    elif product == "coke":
        result = 1.40 * amount
    elif product == "snacks":
        result = 2.00 * amount
    return result


products = input()
quantity = int(input())
res = total_sum(products, quantity)
print(f"{res:.2f}")
