"""
Ce module contient un programme pour vérifier si des mots sont des palindromes.
"""

def is_palindrome(p):
    """
    Vérifie si une chaîne de caractères est un palindrome.

    Args:
        p (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si la chaîne est un palindrome, sinon False.
    """
    length = len(p)  # Longueur du mot
    for i in range(length // 2):  # On compare les caractères des deux extrémités
        if p[i] != p[length - i - 1]:  # Si les caractères opposés ne correspondent pas
            return False
    return True

def main():
    """
    Fonction principale pour tester une liste de mots et déterminer
    s'ils sont des palindromes.
    """
    for word in ["radar", "kayak", "level", "rotor", "civique", "deifie"] :
        print(f"{word}: {'Palindrome' if is_palindrome(word) else 'Not a palindrome'}")

if __name__ == "__main__":
    main()