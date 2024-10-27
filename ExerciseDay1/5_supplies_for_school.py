pen = int(input())
marker = int(input())
liquid = int(input())
discount = int(input())

pen_price = 5.80 * pen
marker_price = 7.20 * marker
liquid_price = 1.20 * liquid
total_price = pen_price + marker_price + liquid_price

total_price_with_discount = total_price - (total_price * 0.25)

print(f"Total price is: {total_price_with_discount}")



