numbers = [int(n) for n in input().split(", ")]

positive = ", ".join([str(p) for p in numbers if p >= 0])
negative = ", ".join([str(n) for n in numbers if n < 0])
even = ", ".join([str(e) for e in numbers if e % 2 == 0])
odd = ", ".join([str(o) for o in numbers if o % 2 == 1])

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
