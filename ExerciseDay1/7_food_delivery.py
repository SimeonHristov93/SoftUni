c_menu = int(input())
f_menu = int(input())
v_menu = int(input())

c_price = c_menu * 10.35
f_price = f_menu * 12.40
v_price = v_menu * 8.15

total_price = c_price + f_price + v_price
desert = total_price * 0.20
delivery = 2.50
order_price = total_price + desert + delivery

print(f"Total price of the order is {order_price}")
