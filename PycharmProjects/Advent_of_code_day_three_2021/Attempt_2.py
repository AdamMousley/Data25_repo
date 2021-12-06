inputfile = open("day_three.txt")
data = [x.strip() for x in inputfile.readlines()]


def section1(data):
    # cols = data.split("")
    # print(cols)

    print(len(data[0]))  # width of data
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    col_6 = []
    col_7 = []
    col_8 = []
    col_9 = []
    col_10 = []
    col_11 = []
    col_12 = []

    for rows in data:
        x=rows[0]
        y=rows[1]
        col_1.append(x)
        col_1.append(y)
        col_2.append(rows[1])
        col_3.append(rows[2])
        col_4.append(rows[3])
        col_5.append(rows[4])
        col_6.append(rows[5])
        col_7.append(rows[6])
        col_8.append(rows[7])
        col_9.append(rows[8])
        col_10.append(rows[9])
        col_11.append(rows[10])
        col_12.append(rows[11])

    all_col = []
    test = True
    while test:
        all_col.append(col_1)
        all_col.append(col_2)
        all_col.append(col_3)
        all_col.append(col_4)
        all_col.append(col_5)
        all_col.append(col_6)
        all_col.append(col_7)
        all_col.append(col_8)
        all_col.append(col_9)
        all_col.append(col_10)
        all_col.append(col_11)
        all_col.append(col_12)
        test = False
    print(all_col)

    # i = 0
    #
    # gamma_rate = []
    # epsilon_rate = []
    #
    # col_1_one = 0
    # col_1_zero = 0
    # for i in range(1, 12):
    #     for i in col_1:
    #         if i == 1:
    #             col_1_one += 1
    #         else:
    #             col_1_zero += 1
    #
    # if col_1_one > col_1_zero:
    #     gamma_rate.append("1")
    #     epsilon_rate.append("0")
    # else:
    #     gamma_rate.append("0")
    #     epsilon_rate.append("1")
    #
    # print(gamma_rate)
    # print(epsilon_rate)


section1(data)
