
# 1. Liste des pronoms personnels
pronoms = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]

# 2. Listes des terminaisons
terminaisons_1 = ["e", "es", "e", "ons", "ez", "ent"]
terminaisons_2 = ["is", "is", "it", "issons", "issez", "issent"]

# 3. Fonction de conjugaison
def conjuguer(verbe):

    if verbe.endswith("er"):
        radical = verbe[:-2]
        terminaisons = terminaisons_1

    elif verbe.endswith("ir"):
        radical = verbe[:-2]
        terminaisons = terminaisons_2

    else:
        print("Verbe non valide")
        return

    print("\nConjugaison du verbe :", verbe)

    for i in range(len(pronoms)):
        print(pronoms[i], radical + terminaisons[i])


# 4. Liste des verbes
verbes = ["parler", "chanter", "finir", "choisir"]

# Appel de la fonction pour chaque verbe
for v in verbes:
    conjuguer(v)

