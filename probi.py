#  faktoriel

def find_fac(n):
    if n == 1:
        return  1
    return n * find_fac(n - 1)

print(f"faktoriel od 4 iznesuva: {find_fac(4)}")




# Напиши функција која ќе пресметува степен на број ( exponential product x^y )

def stepenuvanje(x, y):
    return x ** y

broj = 5
stepen = 4
resultat = stepenuvanje(broj, stepen)
print(f"{broj} na stepen {stepen}  e {resultat}")



# rekurzija

def stepenuvanje(x, y):
    if y == 0:
        return 1
    else:
        return x * stepenuvanje(x, y - 1)

broj = 5
stepen = 4
resultat = stepenuvanje(broj, stepen)
print(f"{broj} na stepen {stepen}  e {resultat}")
