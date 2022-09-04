#Q4] Python Program to Calculate the Area of a Triangle

area_of_triangle = lambda b,h : (0.5)*b*h

base = float(input("Enter base of the triangle : "))
height = float(input("Enter height of the triangle : "))

res = area_of_triangle(base, height)
print(res)