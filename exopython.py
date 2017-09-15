t1 = [32, 5, 12, 8, 3, 75, 2, 15]
max = 0

while i < len(t1):
    if t1[i] > max:
        max = t1[i]
    i = i + 1


print ("Le plus grand nombre de la liste est " + str(max) + "." )
