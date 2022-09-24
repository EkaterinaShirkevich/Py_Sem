# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input("Enter quarter number (in the format 1, 2, 3, 4): "))
if num == 1:
    print("Coordinate range is any value where x > 0 and y > 0")
elif num == 2:
    print("Coordinate range is any value where x < 0 and y > 0")
elif num == 3:
    print("Coordinate range is any value where x < 0 and y < 0")
elif num == 4:
    print("Coordinate range is any value where x > 0 and y < 0")
else:
    print("Error! Incorrect number entered. Try again")
