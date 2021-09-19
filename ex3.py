import random

def choose_element_list(list_in_which_to_choose:list) -> any:
    """Retourne un nombre au hasard dans la liste

    Args:
        list_in_which_to_choose (list): Liste dans laquelle effectuer le tirage

    Returns:
        any: valeur tirée dans la liste
    """
    return list_in_which_to_choose[random.randint(0,len(list_in_which_to_choose)-1)]
