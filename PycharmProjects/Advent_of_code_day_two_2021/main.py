inputfile = open("day_two.txt")
data = [x.strip() for x in inputfile.readlines()]

def section1(data):
    command = []
    amount = []
    for values in data:
        gap = values.index(" ")
        command.append(values[0:gap])
        amount.append(values[gap:])

    horizontal = []
    depth_down = []
    depth_up = []
    aim = 1
    i = 0
    while i < len(command):
        if str(command[i]) == "forward":
            horizontal.append(amount[i]*aim)
        elif str(command[i]) == "down":
            depth_down.append(amount[i])
        else:
            depth_up.append(amount[i])
        i += 1

    tot_h = [int(item) for item in horizontal]
    tot_dd = [int(item) for item in depth_down]
    tot_du = [int(item) for item in depth_up]
    tot_h = sum(tot_h)
    tot_dd = sum(tot_dd)
    tot_du = sum(tot_du)

    new_depth = tot_dd-tot_du
    print(tot_h*new_depth)

section1(data)