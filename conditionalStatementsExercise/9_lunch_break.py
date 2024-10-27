import math

name = str(input())
length_of_episode = int(input())
duration_of_break = int(input())

lunch_time = duration_of_break * 1/8
time_for_relax = duration_of_break * 1/4

remaining_time = duration_of_break - lunch_time - time_for_relax

if remaining_time >= length_of_episode:
    time_left = math.ceil(remaining_time - length_of_episode)
    print(f"You have enough time to watch {name} and left with {time_left} minutes free time.")
else:
    time_needed = math.ceil(length_of_episode - remaining_time)
    print(f"You don't have enough time to watch {name}, you need {time_needed} more minutes.")