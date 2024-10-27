
numbers_count = int(input())
total_sum = 0
biggest_number = 0

for _ in range(numbers_count):
    current_number = int(input())

    total_sum += current_number
    if current_number > biggest_number:
        biggest_number = current_number


if biggest_number == total_sum - biggest_number:
    print("Yes")
    print(f"Sum = {biggest_number}")
else:
    diff = abs(biggest_number - (total_sum - biggest_number))
    print("No")
    print(f"Diff = {diff}")

