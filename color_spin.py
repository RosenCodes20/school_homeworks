number_spins = int(input())
red = 0
orange = 0
yellow = 0
white = 0
black = 0
total_points = 0
others = 0
for spins in range(number_spins):
    color = input()
    if color == "red":
        total_points += 5
        red+=1
    elif color == "orange":
        total_points += 10
        orange+=1
    elif color == "yellow":
        total_points += 15
        yellow+=1
    elif color == "white":
        total_points += 20
        white+=1
    elif color=="black":
        total_points //= 2
        black+=1
    else:
        others+=1
print(f"Total points: {total_points}")
print(f"Red sector: {red}")
print(f"Orange sector: {orange}")
print(f"Yellow sector: {yellow}")
print(f"White sector: {white}")
print(f"Other colors picked: {others}")
print(f"Divides from black sector: {black}")

