#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("Enter X for the point: "))
y = int(input("Enter Y for the point:  "))
if x > 0 and y > 0:
    print("The point is in I quarter")
if x < 0 and y > 0:
    print("The point is in II quarter")
if x < 0 and y < 0:
    print("The point is in III quarter")
if x > 0 and y < 0:
    print("The point is in IV quarter")
if x == 0 :
    print("The point is on the X-axis")   
if y == 0:
    print("The point is on the Y-axis") 
