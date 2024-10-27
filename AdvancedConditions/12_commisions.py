city = input()
sales_amount = float(input())
commission = 0.0

if city == "Sofia" and 0 <= sales_amount <= 500:
    commission = sales_amount * 0.05
elif city == "Sofia" and 500 <= sales_amount <= 1000:
    commission = sales_amount * 0.07
elif city == "Sofia" and 1000 < sales_amount <= 10000:
    commission = sales_amount * 0.08
elif city == "Sofia" and 10000 < sales_amount:
    commission = sales_amount * 0.12
if city == "Varna" and 0 <= sales_amount <= 500:
    commission = sales_amount * 0.045
elif city == "Varna" and 500 <= sales_amount <= 1000:
    commission = sales_amount * 0.075
elif city == "Varna" and 1000 < sales_amount <= 10000:
    commission = sales_amount * 0.10
elif city == "Varna" and 10000 < sales_amount:
    commission = sales_amount * 0.13
if city == "Plovdiv" and 0 <= sales_amount <= 500:
    commission = sales_amount * 0.055
elif city == "Plovdiv" and 500 <= sales_amount <= 1000:
    commission = sales_amount * 0.08
elif city == "Plovdiv" and 1000 < sales_amount <= 10000:
    commission = sales_amount * 0.12
elif city == "Plovdiv" and 10000 < sales_amount:
    commission = sales_amount * 0.145

print(f"{commission:.2f}")