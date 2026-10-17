# 1) Fonction est_palindrome utilisant le slicing
def est_palindrome(conteneur):
    """Vérifie si un container séquentiel est un palindrome."""
    return conteneur == conteneur[::-1]


# 2) Fonction nettoyer_et_verifier
def nettoyer_et_verifier(chaine):
    
    # a) Conserver uniquement les caractères alphanumériques convertis en minuscules
    container_nettoye = "".join([c.lower() for c in chaine if c.isalnum()])
    
    # b) Vérifier si c'est un palindrome
    est_pal = est_palindrome(container_nettoye)
    
    # c) Retourner le tuple (bool, container_nettoye)
    return (est_pal, container_nettoye)


# 3) Fonction trouver_palindromes utilisant une compréhension de liste
mots = ["radar", "kayak", "python", "level", "coucou", "abcba"]

def trouver_palindromes(liste_mots):
    """Retourne une nouvelle liste contenant uniquement les palindromes extraits de la liste d'origine."""
    return [mot for mot in liste_mots if est_palindrome(mot)]


# --- Tests et exemples d'utilisation ---
if __name__ == "__main__":
    print("--- Test 1 ---")
    print(est_palindrome("radar"))  # True
    print(est_palindrome("python")) # False
    
    print("\n--- Test 2 ---")
    phrase_test = "A man, a plan, a canal: Panama"
    print(nettoyer_et_verifier(phrase_test))  # (True, 'amanaplanacanalpanama')
    
    print("\n--- Test 3 ---")
    print(trouver_palindromes(mots))  # ['radar', 'kayak', 'level', 'abcba']