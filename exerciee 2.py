def tri_select(tab):
    for i in range(len(tab)):
        minimum = min(tab[i:])
        position = tab[i:].index(minimum) + i

        tab[i], tab[position] = tab[position], tab[i]

    return tab


# Programme principal
tab = list(map(int, input("Donner les éléments séparés par des virgules : ").split(",")))

print("Tableau initial :", tab)
print("Tableau trié par ordre croissant :", tri_select(tab))
