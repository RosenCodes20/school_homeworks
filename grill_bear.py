import math

name_of_the_friend = input()
budget = float(input())
bottles_of_bear = int(input())
number_steaks = int(input())
price_for_a_beer = 3.2
sum_of_the_beers = price_for_a_beer * bottles_of_bear
price_for_a_steak = math.ceil(sum_of_the_beers * 35 / 100)
sum_of_the_steak = number_steaks * price_for_a_steak
sum = sum_of_the_beers + sum_of_the_steak
difference = abs(sum - budget)
if sum <= budget:
    print(f"{name_of_the_friend} bought everything and has {difference:.2f} leva left.")
else:
    print(f"{name_of_the_friend} needs {difference:.2f} more leva!")

