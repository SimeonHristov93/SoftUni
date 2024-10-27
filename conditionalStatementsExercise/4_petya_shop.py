

price_trip = float(input())
puzzle_number = int(input())
dolls_number = int(input())
teddybear_number = int(input())
minion_number = int(input())
truck_number = int(input())

total_amount = (puzzle_number * 2.60 + dolls_number * 3 + teddybear_number * 4.10 + minion_number * 8.20 + truck_number * 2)

if puzzle_number + dolls_number + teddybear_number + minion_number + truck_number >= 50:
    total_amount *= 0.75

rent = total_amount * 0.10
profit = total_amount - rent

if profit >= price_trip:
    left_money = profit - price_trip
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = price_trip - profit
    print(f"Not enough money! {needed_money:.2f} lv needed.")


