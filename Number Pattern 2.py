
p = int(input("Enter Rows:"))

for i in range(p, 0, -1):
    for j in range(1, i-1):
        print(j, end = "")
    print()
