list1 =["D", "a", "a", "n", "y"]
set1 = set(list1)
print(f"Length of list1: {len(list1)}")
print(f"length of set1:  {len(set1)}")
set2 = {8, 2, 5, 7, 9, 4, 3, 7, 7, 7}
tuple1 = (10, 2, 3, 4, 5, 6, 7, 8, 9)
if len(list1) == len(set1):
    print("No duplicates")
else:
    print("Duplicates")
print(set2)
print(tuple1)