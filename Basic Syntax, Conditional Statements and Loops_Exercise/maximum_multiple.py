divisor = int(input())
boundary = int(input())

n = 0

for num in range(boundary + 1):
    if num % divisor == 0:
       n = num

print(n)
