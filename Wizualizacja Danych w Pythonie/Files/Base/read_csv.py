if __name__ == "__main__":
    with open("grades.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            grades = parts[1:]
            print("Name:", name)
            print("Grades:", grades)
