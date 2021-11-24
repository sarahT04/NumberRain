import os
from letTheMatrixRain import animate

def clear_screen():
    _ = os.system('cls')

os.system('color B')
while True:
    choice = input("Infinity, under a range, or once? [0, 1, 2]\n> ")
    clear_screen()
    if choice == '0':
        print("Let the matrix rain!! (╯°□°)╯\n")
        animate(1000)
        continue
    if choice == '1':
        sum_range = int(input("Range?\n> "))
        print("Let the matrix rain!! (╯°□°)╯\n")
        animate(sum_range)
        continue
    if choice == '2':
        print("Let the matrix rain!! (╯°□°)╯\n")
        animate(1)
        continue
