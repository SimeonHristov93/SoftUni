budget = float(input())  # Бюджет
category = input().strip()  # Категория "VIP" или "Normal"
group_size = int(input())  # Брой хора

# Цени на билетите
ticket_prices = {
    "VIP": 499.99,
    "Normal": 249.99
}

# Определете процента от бюджета за транспорт
if group_size >= 1 and group_size <= 4:
    transport_percentage = 0.75
elif group_size >= 5 and group_size <= 9:
    transport_percentage = 0.60
elif group_size >= 10 and group_size <= 24:
    transport_percentage = 0.50
elif group_size >= 25 and group_size <= 49:
    transport_percentage = 0.40
else:
    transport_percentage = 0.25

# Изчислете парите, заделени за транспорт
transport_cost = budget * transport_percentage

# Наличен бюджет за билети
available_budget = budget - transport_cost

# Изчислете общата цена на билетите
total_ticket_price = ticket_prices[category] * group_size

# Проверка на бюджета
if available_budget >= total_ticket_price:
    remaining_money = available_budget - total_ticket_price
    print(f"Yes! You have {remaining_money:.2f} leva left.")
else:
    needed_money = total_ticket_price - available_budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")