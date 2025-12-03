import os

folder = "."

for i in range(1, 13):
    os.mkdir(f"{folder}/Dia{i}")
    with open(f"{folder}/Dia{i}/input.txt", "w") as f:
        f.write("")

    with open(f"{folder}/Dia{i}/sol1.py", "w") as f:
        f.write("")

    with open(f"{folder}/Dia{i}/input2.txt", "w") as f:
        f.write("")

    with open(f"{folder}/Dia{i}/sol2.py", "w") as f:
        f.write("")