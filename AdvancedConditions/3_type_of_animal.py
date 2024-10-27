animals_type = input()

if animals_type == 'dog':
    print("mammal")
elif animals_type == 'crocodile' or animals_type == 'snake' or animals_type == 'tortoise':
    print('reptile')
else:
    print('unknown')