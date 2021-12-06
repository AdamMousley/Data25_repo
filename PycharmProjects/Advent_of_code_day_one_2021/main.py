
inputfile = open("day_one_2021.txt")
data = [x.strip() for x in inputfile.readlines()]

def section1(data):
    list=[]
    for depth in data:
        list.append(depth)
    increased = []
    decreased = 0
    same = 0
    for i in range(0, len(list)-1,1):
        if int(list[i]) < int(list[i+1]):
            increased.append(list[i])
        elif int(list[i]) == int(list[i+1]):
            same += 1
        else:
            decreased += 1
    print(increased)
    print(len(increased))
    print(same)
    print(decreased)

def section2(data):
    list=[]
    for depth in data:
        list.append(depth)
    deeper =[]
    for i in range(0,len(list)-3):
        x = int(list[i]) + int(list[i+1]) + int(list[i+2])
        y = int(list[i+1]) + int(list[i+2]) + int(list[i+3])
        if x < y:
            deeper.append(y)
    print(len(deeper))


section1(data)
section2(data)