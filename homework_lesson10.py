with open("example.csv", "r") as csv_file:
    csv_lines = csv_file.read().splitlines()  # splits files in lines

    for line in csv_lines:
        x = line.split(",")  # split elements in the array using , as a separator
        t = ""  # empty string that we are going to compose
        for y in range(len(x)):
            if y == 0:
                t = x[y] + " is "
            elif y == 1:
                t = t + x[y] + " years old and "
            elif 1 < y < len(x)-1:
                t = t + x[y] + " and "
            else:
                t = t + x[y]
        print(t)
