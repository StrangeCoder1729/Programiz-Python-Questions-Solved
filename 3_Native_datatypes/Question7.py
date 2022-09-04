# Q7] Python Program to Illustrate Different Set Operations

set1 = {0, 2, 4, 6, 8}
set2 = {1, 2, 3, 4, 5}

print()
"""Set Union"""
set3 = set1 | set2
print("Union of the two sets : {}".format(set3))

print()

"""Set Intersection"""
set3 = set1 & set2
print("Intersection between two given sets : {}".format(set3))

print()

"""Set Substraction"""
set3 = set1 - set2
print("Substraction set2 from set1 : {}".format(set3))

print()

"""Symmetric difference"""
set3 = set1 ^ set2
print("Symmetric difference between two given sets : {}".format(set3))
print()