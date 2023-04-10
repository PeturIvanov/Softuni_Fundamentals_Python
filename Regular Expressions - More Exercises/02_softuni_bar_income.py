import re

pattern = r"[\%](?P<customer>[A-Z]{1}[a-z]+)[\%][^\|\$\%\.]*?[\<]" \
          r"(?P<product>[\w]+)[\>][^\|\$\%\.]*?[\|]" \
          r"(?P<count>[\d]+)[\|][^\|\$\%\.]*?" \
          r"(?P<price>[\d]+[\.]*[\d]+)[\$]"
pattern_regex = re.compile(pattern)

input_line = input()

total_price = 0
while input_line != "end of shift":
    data = re.finditer(pattern_regex, input_line)
    for person in data:
        person_data = person.groupdict()
        total_price += float(person_data["count"]) * float(person_data["price"])
        product_total_price = float(person_data["count"]) * float(person_data["price"])
        print(f"{person_data['customer']}: {person_data['product']} - {product_total_price:.2f}")
    input_line = input()

print(f"Total income: {total_price:.2f}")
