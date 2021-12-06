import csv

def day_three(csv_file_name):
    with open("day_three.csv", newline="") as csv_file:
        tree_lines = csv.reader(csv_file, delimiter=" ")

        i = 0
        rows = []
        for line in tree_lines:
            rows.append(line)
            i += 1
        print(rows)

        map_width = len(str(rows[0]))
        map_height = len(rows)
        print(map_width)
        print(map_height)
        x = 0
        trees = 0
        for y in range(map_height):
            if [x] == "#" and [y] == "#":
                trees += 1
            x = (x+3) % map_width
        print(trees)


        # i = 0
        # rows = []
        # for line in tree_lines:
        #     rows.append(line)
        #     i +=1
        #
        # tree = 0
        # not_tree = 0
        # height = len(rows)
        # width = len(str(rows[0]))
        # coord =(height,width)
        # for i in range(height):
        #     if coord == "#":
        #         tree +=1
        #     else:
        #         not_tree +=1
        # # print(height)
        # # print(width)
        # print(tree)
        # print(not_tree)
            #print(height,width)




day_three("day_three.csv")