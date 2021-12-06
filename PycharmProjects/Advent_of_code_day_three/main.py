import csv

inputfile = open("day_three.csv")
data = [x.strip() for x in inputfile.readlines()]

def section1(data):
    x=0  # initial start point (x,y) = (0,0)
    map_width = len(data[0])
    map_height = len(data)
    trees= 0
    for y in range(map_height):
        if data[y][x] == "#":
            trees += 1
        x = (x+3) % map_width
    # print(trees)
    # print(map_width)
    # print(map_height)

def section2(data):
    def slope(right, down):
        x = 0  # initial start point (x,y) = (0,0)
        map_width = len(data[0])
        map_height = len(data)
        trees = 0
        for y in range(map_height):
            if y % down != 0:
                continue
            if data[y][x] == "#":
                trees += 1
            x = (x + right) % map_width
        print(trees)

    x1 = slope(1,1)
    x2 = slope(3,1)
    x3 = slope(5,1)
    x4 = slope(7,1)
    x5 = slope(1,2)

print(70*171*48*60*35)
section1(data)
section2(data)