tabs_open = int(input())
salary_amount = float(input())

for _ in range(tabs_open):
    current_tab = input()
    if current_tab == "Facebook":
        salary_amount -= 150
        if salary_amount <= 0:
            break
    elif current_tab == "Instagram":
        salary_amount -= 100
        if salary_amount <= 0:
            break
    elif current_tab == "Reddit":
        salary_amount -= 50
        if salary_amount <= 0:
            break

if salary_amount <= 0:
    print("You have lost your salary.")
else:
    print(int(salary_amount))
