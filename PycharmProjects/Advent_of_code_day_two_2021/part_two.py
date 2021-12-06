inputfile = open("day_two.txt")
data = [x.strip() for x in inputfile.readlines()]

def section2(data):
    command = []
    amount = []
    for values in data:
        gap = values.index(" ")
        command.append(values[0:gap])
        amount.append(values[gap:])

    amount = [int(item) for item in amount]
    #print(amount)

    horizontal = 0
    depth = 0
    aim = 0
    i = 0
    while i < len(command):
        if str(command[i]) == "forward":
            horizontal += amount[i]
            depth += amount[i]*aim
        elif str(command[i]) == "down":
            #depth += amount[i]
            aim += amount[i]
        else:
            #depth -= amount[i]
            aim -= amount[i]
        i += 1
    # print(horizontal)
    # print(depth_down)
    # print(depth_up)
    print(horizontal*depth)

section2(data)