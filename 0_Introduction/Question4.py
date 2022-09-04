# Q4] Python Program to Calculate the Area of a Triangle

def areaOfTriangle(b,h):
    sol = (b*h)/2
    return round(sol,3)


base = float(input("Enter base of the triangle : "))
height = float(input("Enter height of the triangle : "))

res = areaOfTriangle(base,height)
print("Area of the triangle is {}".format(res))