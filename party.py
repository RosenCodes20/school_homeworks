command = input()
kids = 0
adults = 0
sweets = 5
bottles = 15
while command != "Party":
    ages = int(command)
    if ages <= 16:
        kids += 1
    else:
        adults += 1

    command = input()
sweets_price = sweets * kids

bottles_price = bottles * adults
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for sweets: {sweets_price}")
print(f"Money for bottels: {bottles_price}")
