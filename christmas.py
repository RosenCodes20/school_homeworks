toys_lenght = input()
color_of_the_toys = input()
number_toys = int(input())
price_for_toy = 0

if color_of_the_toys == "Red":
    if toys_lenght == "Large":
        price_for_toy = 16
    elif toys_lenght == "Medium":
        price_for_toy = 13
    else:
        price_for_toy = 9
elif color_of_the_toys == "Green":
    if toys_lenght == "Large":
        price_for_toy = 12
    elif toys_lenght == "Medium":
        price_for_toy = 9
    else:
        price_for_toy = 8
else:
    if toys_lenght == "Large":
        price_for_toy = 9
    elif toys_lenght == "Medium":
        price_for_toy = 7
    else:
        price_for_toy = 5

end_sum=price_for_toy*number_toys
end_sum*=0.65
print(f"You have earned {end_sum:.2f} leva.")
