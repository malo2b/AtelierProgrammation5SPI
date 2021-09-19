import random

def extract_elements_list(list_in_which_to_choose:list,int_nbr_of_element_to_extract:int) -> list:
    """Tire aléatoirement int_nbt_of_element_to_extract dans la liste et retourne une liste composée de ces nombres

    Args:
        list_in_which_to_choose (list): Liste dans laquelle le tirage va se faire
        int_nbr_of_element_to_extract (int): Nombre d'éléments a tirer dans la liste

    Returns:
        list: Liste des éléments tirés
    """
    taille_list_in_which_to_choose = len(list_in_which_to_choose)
    list_element_choose = []     # Liste mixée
    tab_index_choose = [0] * taille_list_in_which_to_choose
    first_iteation = True
    index_aleatoire = 0
    for _ in range(int_nbr_of_element_to_extract):
        while tab_index_choose[index_aleatoire] == 1 or first_iteation:
            index_aleatoire = random.randint(0,taille_list_in_which_to_choose-1)
        if first_iteation:
            first_iteation = False
        tab_index_choose[index_aleatoire] += 1

    return list_element_choose
