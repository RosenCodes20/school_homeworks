from sys import maxsize

number_players = int(input())
the_most_points = -maxsize
for players in range(number_players):
    name_of_the_player = input()
    command = input()
    sum_grades = 0
    while command != "Stop":
        grade_from_the_judge = int(command)

        sum_grades += grade_from_the_judge

        command = input()
    print(f"{name_of_the_player} has {sum_grades} points.")
    if sum_grades > the_most_points:
        the_most_points = sum_grades
        name_of_the_winner = name_of_the_player
        print(f"{name_of_the_player} is the new number 1!")
print(f"{name_of_the_winner} won competition with {the_most_points} points!")
