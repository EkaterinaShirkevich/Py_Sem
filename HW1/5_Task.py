# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# AB = √(xb - xa)2 + (yb - ya)2
import math
xa = int(input("Enter X for the A-point: "))
ya = int(input("Enter Y for the A-point:  "))
xb = int(input("Enter X for the B-point: "))
yb = int(input("Enter Y for the B-point:  "))
dis = f"{(math.sqrt((xb - xa)**2 + (yb - ya)**2)):.3f}"
print("Distance from A to B is ", dis)
