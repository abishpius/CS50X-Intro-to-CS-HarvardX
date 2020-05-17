# TODO
from sys import *
import cs50
import csv


if len(argv) != 2:
    print("missing command-line argument")
    exit(1)

var_1 = str(argv[1])

db = cs50.SQL("sqlite:///students.db")

q = "SELECT first, middle, last, birth FROM students WHERE house =="+" \'"+str(var_1)+"\'"+" ORDER BY last, first"

#print(q)

t = db.execute(q)

tt=[]
for i in t:
    tt.append(list(i.values()))

for j in tt:
    if j[1] == None:
        print(j[0]+" "+j[2]+", born "+str(j[3]))
    else:
        print((j[0]+" "+j[1]+" "+j[2]+", born "+str(j[3])))
