import random

def mix_list(list_to_mix:list) -> list:
    """Mélange les valeurs de la liste passée en paramètre et retourne une nouvelle liste

    Args:
        list_to_mix (list): Liste a mélanger

    Returns:
        list: Liste mélangée
    """
    while list_to_mix != list_mixee:
        taille_list_to_mix = len(list_to_mix)
        copie_list_to_mix = list_to_mix.copy()  # Copie de la liste a mixer
        list_mixee = []     # Liste mixée
        for i in range(taille_list_to_mix):
            index_aleatoire = random.randint(0,taille_list_to_mix-i-1)
            list_mixee.append(copie_list_to_mix[index_aleatoire])   # On ajoute a la liste mixée
            copie_list_to_mix.pop(index_aleatoire)  # On enleve de la liste des éléments a mixer
    return list_mixee
