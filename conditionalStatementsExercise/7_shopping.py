budget = float(input())
videocards_count = int(input())
processors_count = int(input())
ram_count = int(input())


videocards_price = videocards_count * 250
processors_price = videocards_price * 0.35
ram_price = videocards_price * 0.10
total_price = videocards_price + processors_count * processors_price + ram_count * ram_price

if videocards_count > processors_count:
    total_price *= 0.85

if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")