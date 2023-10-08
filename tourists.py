number_locations = int(input())
total_sandwiches = 0
expected_sandwiches = 0

for _ in range(number_locations):
    average_number_of_sandwiches = int(input())
    days = int(input())
    expected_sandwiches += average_number_of_sandwiches

    for day in range(days):
        eaten_sandwiches_for_a_day = int(input())
        total_sandwiches += eaten_sandwiches_for_a_day

difference = abs(total_sandwiches - expected_sandwiches)
if total_sandwiches <= expected_sandwiches:
    print(f"Good job! {difference:.2f} left.")
else:
    print(f"You need {difference:.2f} sandwiches.")

