budget = float(input())
flour_kg_price = float(input())
pack_eggs_price = flour_kg_price * 0.75
lt_milk_price = flour_kg_price * 1.25

price_for_one_loaf = flour_kg_price + pack_eggs_price + (lt_milk_price / 4)

current_budget = budget
counter_loaves = 0
colored_eggs_counter = 0

while current_budget >= price_for_one_loaf:
    current_budget -= price_for_one_loaf
    counter_loaves += 1
    colored_eggs_counter += 3

    if counter_loaves % 3 == 0:
        colored_eggs_counter -= (counter_loaves - 2)

print(f"You made {counter_loaves} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and "
      f"{current_budget:.2f}BGN left.")

