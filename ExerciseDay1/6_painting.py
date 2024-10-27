nailon_amount = int(input())
paint_amount = int(input())
paint_liquid = int(input())
work_time = int(input())

nailon_price = (nailon_amount + 2) * 1.50
paint_price = (paint_amount * (1 + 0.10)) * 14.50
paint_liquid_price = paint_liquid * 5

materials_price = (nailon_price + paint_price + paint_liquid_price) + 0.40
work_price_for_1_hour = (materials_price * 0.30)
work_price = work_price_for_1_hour * work_time

final_price = (materials_price + work_price)
print(final_price)
