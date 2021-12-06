import csv

def day_two(csv_file_name):
    with open("day_two.csv", newline="") as csv_file:
        new_passwords = csv.reader(csv_file, delimiter=" ")
        good_password = 0
        for line in new_passwords:
            constraint = line[0].split("-")
            lower = constraint[0]
            upper = constraint[-1]
            letter = line[1].replace(":","")
            password = line[-1]
            letter_count = password.count(letter)
            #print(lower)
            #print(upper)
            if int(lower) <= letter_count <= int(upper):
                good_password +=1
        print(good_password)


#            constraint.append(line[0])
#            letter.append(line[1])
#            password.append(line[-1])
#            print(letter)


day_two("day_two.csv")