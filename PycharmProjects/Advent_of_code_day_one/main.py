
def open_and_print(file):
    try:
        with open(file, "r") as opened_file:
            file_line_list = opened_file.readlines()

        x = 0
        y = 0
        z = 0

        for i in range(len(file_line_list)):
            for j in range(i+1, len(file_line_list)):
                for k in range(i+2, len(file_line_list)):
                    if int(file_line_list[i]) + int(file_line_list[j]) + int(file_line_list[k]) == 2020:
                        x += int(file_line_list[i])
                        y += int(file_line_list[j])
                        z += int(file_line_list[k])
                        print("Value one", int(file_line_list[i]))
                        print("Value Two", int(file_line_list[j]))
                        print("Value Three", int(file_line_list[k]))
                        return ("Multiplication",x*y*z)

        print("x",x)
        print("y",y)
        print("z",z)
        print("The multiplication", x*y*z)

    except FileNotFoundError as errmsg:
        print("There is no file", errmsg)
        raise
    finally:
        print("Execution Complete")

print(open_and_print("day_one.txt"))