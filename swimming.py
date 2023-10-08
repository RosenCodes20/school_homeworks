minutes_of_the_control = int(input())
seconds_of_the_comtrol = int(input())
lenght_of_the_pool = float(input())
seconds_for_a_100_metres = int(input())
down_time = 2.5

sum_time = minutes_of_the_control * 60 + seconds_of_the_comtrol

slow = lenght_of_the_pool / 120
sum_slow_time = slow * down_time

time = (lenght_of_the_pool / 100) * seconds_for_a_100_metres - sum_slow_time
difference = abs(time - sum_time)
if time <= sum_time:
    print("Petar Mitsin won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Petar failed! He was {difference:.3f} second slower.")
