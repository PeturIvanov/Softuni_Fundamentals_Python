list_of_tickets = input().split(",")
list_of_tickets = [list_of_tickets[i].strip() for i in range(len(list_of_tickets))]
WINING_SYMBOLS = ["@", "#", "$", "^"]

for ticket in list_of_tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    jackpot = False
    normal_win = False
    win_amount = 0
    first_half = ticket[:10]
    second_half = ticket[10:]

    for symbol in WINING_SYMBOLS:
        if symbol * 20 in ticket:
            jackpot = True
            break

        elif symbol * 6 in first_half and symbol * 6 in second_half:
            win_amount += 6
            for i in range(7, 11):
                if symbol * i in first_half and symbol * i in second_half:
                    win_amount += 1
            normal_win = True
            break

    if jackpot:
        print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
    elif normal_win:
        print(f'ticket "{ticket}" - {win_amount}{symbol}')
    else:
        print(f'ticket "{ticket}" - no match')
