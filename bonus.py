import random

rosen_time = 0
ivcho_time = 0
gosho_time = 0
ioco_time = 0
kalata_time = 0
sasho_time = 0
blago_time = 0
time = 0
while True:

    students = ["Rosen", "Ivcho", "Gosho", "Ioco", "Kalata", "Sasho", "Blago"]

    computer_choice = random.choice(students)

    if computer_choice == "Rosen":
        rosen_time += 1
    elif computer_choice == "Ivcho":
        ivcho_time += 1
    elif computer_choice == "Gosho":
        gosho_time += 1
    elif computer_choice == "Ioco":
        ioco_time += 1
    elif computer_choice == "Kalata":
        kalata_time += 1
    elif computer_choice == "Sasho":
        sasho_time += 1
    else:
        blago_time += 1

    if rosen_time == 2 \
            or ivcho_time == 2 \
            or gosho_time == 2 \
            or ioco_time == 2 \
            or kalata_time == 2 \
            or sasho_time == 2 \
            or blago_time == 2:
        break
    print("The student to answer is:", computer_choice)
