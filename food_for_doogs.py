food_for_dog = int(input()) * 1000
command = input()
sum_food = 0
price_for_kg = 5.5
leftovers = 0
end_sum = 0
price = 0
sum_price = 0
while command != "Stop":
    eated_food = int(command)
    sum_food += eated_food
    leftovers = food_for_dog - sum_food
    price = leftovers / 1000
    sum_price = abs(price * price_for_kg)

    command = input()
if leftovers == 0:
    sum_price = food_for_dog / 1000 * price_for_kg
difference = abs(leftovers)
if difference >= food_for_dog:
    print(f"Food is not enough! You need {difference} grams more.")
    print(f"So you spent {sum_price:.2f} leva for food.")
else:
    print(f"Food is enough! Leftovers: {leftovers} grams.")
    print(f"So you spent {sum_price:.2f} leva for food.")