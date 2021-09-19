import random
from ex1 import gen_list_random_int
from ex2 import mix_list

def perf_mix(function1:callable,
             function2:callable,
             list_taille_a_tester:list,
             int_nbr_exec_moyen:int) -> tuple(list,list):
    """Compare les performances entre deux fonctions passées en paramètre,
    tests basés sur les ordre de grandeur contenue dans la liste list_taille_a_tester et
    cela int_nbr_exec_moyen fois

    Args:
        function1 (callable): Premiere fonction a tester
        function2 (callable): Deuxieme fonction a tester
        list_taille_a_tester (list): Liste contenant les ordre de grandeur des valeurs a tester
        int_nbr_exec_moyen (int): Nombre d'exection

    Returns:
        tuple(list,list): retourne un tuple composé de deux listes contenant les temps d'execution des fonctions
    """
    list_test = []
    for ordre_grandeur in list_taille_a_tester:
        list_test = gen_list_random_int(0,ordre_grandeur)
        for _ in range(ordre_grandeur):
            

print(
    perf_mix(
        mix_list,
        random.shuffle,
        [10,100,1000,10000,100000,1000000],
        10
    )
)