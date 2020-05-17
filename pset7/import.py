# TODO
import cs50
from sys import *
import csv

if len(argv) != 2:
    print("missing command-line argument")
    exit(1)

var_1 = argv[1]
var_1 = str(var_1)

db = cs50.SQL("sqlite:///students.db")

with open(var_1, "r") as houses:
    reader = csv.DictReader(houses)

    for row in reader:

        if row["name"] != "\\n":
            str2 = row["name"].split()
            if len(str2) == 3:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                str2[0], str2[1], str2[2], row["house"], row["birth"])

            elif len(str2) < 3:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                str2[0], None, str2[1], row["house"], row["birth"])
