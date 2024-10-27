budget = float(input())
walk_on_count = int(input())
clothes_price = float(input())

decor = budget * 0.10
total_clothes_price = walk_on_count * clothes_price
if walk_on_count > 150:
    total_clothes_price *= 0.90

total_cost = decor + total_clothes_price

if budget >= total_cost:
    money_left = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

else:
    money_needed = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
    