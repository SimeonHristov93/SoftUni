l = int(input())
w = int(input())
h = int(input())
p = int(input())

volume = l * w * h
litre_vol = volume / 1000
litres_needed = litre_vol * (1-0.17)

print(litres_needed)