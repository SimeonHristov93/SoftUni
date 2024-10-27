junior_count = int(input())
senior_count = int(input())
race_type = input()

junior = 0.0
senior = 0.0

if race_type == "trail":
    junior = 5.50
    senior = 7
elif race_type == "cross-country":
    junior = 8
    senior = 9.50
    if senior_count + junior_count >= 50:
        junior = 8 * 0.75
        senior = 9.50 * 0.75
elif race_type == "downhill":
    junior = 12.25
    senior = 13.75
elif race_type == "road":
    junior = 20
    senior = 21.50

total_amount = junior_count * junior + senior_count * senior
amount_after_expenses = total_amount * 0.95

print(f"{amount_after_expenses:.2f}")