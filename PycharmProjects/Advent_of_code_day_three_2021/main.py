# Gamma rate and epsilon rate
import csv
inputfile = open("day_three.txt")
data = [x.strip() for x in inputfile.readlines()]

def section1(data):

    print(len(data[0])) # width of data
    col_1=[]
    col_2=[]
    col_3=[]
    col_4=[]
    col_5=[]
    col_6=[]
    col_7=[]
    col_8=[]
    col_9=[]
    col_10=[]
    col_11=[]
    col_12=[]

    for rows in data:
        col_1.append(rows[0])
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
    # print(col_1)

    gamma_rate = ""
    epsilon_rate = ""
##############################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_1:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
##############################################
    col_2_one = 0
    col_2_zero = 0
    i = 0
    for i in col_2:
        if i == "1":
            col_2_one += 1
        else:
            col_2_zero += 1
    if col_2_one > col_2_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
###############################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_3:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
#################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_4:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
#################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_5:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
#################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_6:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
##################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_7:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
##################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_8:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
##################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_9:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
###################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_10:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
###################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_11:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
####################################################
    col_1_one = 0
    col_1_zero = 0
    i = 0
    for i in col_12:
        if i == "1":
            col_1_one += 1
        else:
            col_1_zero += 1
    if col_1_one > col_1_zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)


    print(gamma_rate)
    print(epsilon_rate)

    print(gamma_rate*epsilon_rate)

section1(data)
