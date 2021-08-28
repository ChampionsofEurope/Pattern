
p = int(input("ENTER ROWS:"))

for i in range(0,p):
    for j in range(0, i+1):
        print("*", end = "")
    print()
for i in range(1, p):
    for j in range(0, p-i):
        print("*", end="")
    print()

