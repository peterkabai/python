import fileinput

for line in fileinput.input(["../data/cpu.csv"]):
    print(line, end="")
print("")
    