taille = input("Entrez votre taille en m.")
imc_mini = 18.5
imc_max = 25

if imc_mini == 18.5:
    masse_min = imc_mini * float(taille)**2

if imc_max == 25:
    masse_max = imc_max * float(taille)**2

print("Votre poids idéal doit etre situé entre " + str(masse_min) + "kg et " + str (masse_max) + " kg.")
