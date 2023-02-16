collection_of_items = input().split("|")
budget = int(input())

init_money = budget
profit = 0
total_money_from_sell = 0
for el in collection_of_items:
    list_of_items = el.split("->")
    price = float(list_of_items[1])
    item = list_of_items[0]

    if item == "Clothes" and price <= 50.00:
        if price <= init_money:
            init_money -= price
            profit += price * 0.40
            new_price = price * 1.40
            total_money_from_sell += new_price
            print(f"{new_price:.2f}", end=" ")
    elif item == "Shoes" and price <= 35.00:
        if price <= init_money:
            init_money -= price
            profit += price * 0.40
            new_price = price * 1.40
            total_money_from_sell += new_price
            print(f"{new_price:.2f}", end=" ")
    elif item == "Accessories" and price <= 20.50:
        if price <= init_money:
            init_money -= price
            profit += price * 0.40
            new_price = price * 1.40
            total_money_from_sell += new_price
            print(f"{new_price:.2f}", end=" ")


print()
print(f"Profit: {profit:.2f}")

result = init_money + total_money_from_sell
if result >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
