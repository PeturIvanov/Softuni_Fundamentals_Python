elements = input().split()
products_to_search = input().split()

products_in_store = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    products_in_store[key] = int(value)

for el in products_to_search:
    if el in products_in_store:
        print(f"We have {products_in_store.get(el)} of {el} left")

    else:
        print(f"Sorry, we don't have {el}")
