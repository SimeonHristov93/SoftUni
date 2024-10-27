fee = int(input())

sneakers = fee * 0.60
# fee * (1 - 40 / 100)
tier = sneakers * 0.80
# tier * (1 - 20 / 100)
ball = tier * 0.25
# ball = tier / 4
acc =  ball * 0.20
# acc = ball / 5
total_price = fee + sneakers + tier + ball + acc

print(f"Total price for one year will be {total_price}")

