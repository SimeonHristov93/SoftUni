tournament_count = int(input())
starting_points = int(input())

points_gained = 0
tournament_win = 0

for _ in range(tournament_count):
    current_result = input()
    if current_result == "W":
        points_gained += 2000
        tournament_win += 1
    elif current_result == "F":
        points_gained += 1200
    elif current_result == "SF":
        points_gained += 720

final_score = starting_points + points_gained
average_points = points_gained / tournament_count
winning_percent = (tournament_win / tournament_count) * 100

print(f"Final points: {final_score}")
print(f"Average points: {int(average_points)}")
print(f"{winning_percent :.2f}%")