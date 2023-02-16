cards = input().split()
shuffles = int(input())

for shuffles in range(shuffles):
    first_half = []
    second_half = []

    for idx in range(1, len(cards) - 1):
        if idx < len(cards) / 2:
            first_half.append(cards[idx])
        else:
            second_half.append(cards[idx])

    result = []
    first_half_idx = 0
    second_half_idx = 0

    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            result.append(second_half[second_half_idx])
            second_half_idx += 1
        else:
            result.append(first_half[first_half_idx])
            first_half_idx += 1

        cards = [cards[0]] + result + [cards[-1]]

print(cards)
