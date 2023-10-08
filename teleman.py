import math

name_of_the_serial = input()
number_seasons = int(input())
number_episodes = int(input())
continoue_of_episode = float(input())
ads_time = continoue_of_episode * 0.20
full_time = continoue_of_episode + ads_time
special = number_seasons * 10
total = (full_time * number_episodes * number_seasons) + special
print(f"I needed {math.floor(total)} minutes to watch the {name_of_the_serial} all series.")
