import random

def gen_list_random_int(int_nbr:int,int_binf:int=0,int_bsup:int=10) ->list:
    """Génere et retourne une liste de nombre aléatoire compris entre
    int_binf inclus et int_bsup exclus avec 0 et 10 en valeur par défaut

    Args:
        int_nbr (int): Nombre de nombres aléatoires
        int_binf (int, optional): Borne inferieur nombres aléatoires. Defaults to 0.
        int_bsup (int, optional): Borne superieur nombres aléatoires. Defaults to 10.

    Returns:
        list: Liste des nombres aléatoires
    """
    liste_nombres_aleatoires = []   # Liste de retour
    for _ in range(int_nbr):
        liste_nombres_aleatoires.append(
            random.randint(int_binf,int_bsup)
        )
    return liste_nombres_aleatoires

print(gen_list_random_int(20000,0,1000))