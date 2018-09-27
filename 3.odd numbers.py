lis = []

for odd in range(904, 1100):
    if odd % 2 == 1:
        lis.append(odd)
print(lis)
print("length=", len(lis))
