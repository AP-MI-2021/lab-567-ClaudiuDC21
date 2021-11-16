from Domain.cheltuiala import get_tipul, get_suma


def the_biggest_chelt_for_every_type(lst_cheltuieli):
    """
    Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
    :param lst_cheltuieli: Lista de cheltuieli.
    :return: Cele mai mari cheltuieli pentru fiecare tip de cheltuiala.
    """
    result = {}
    for cheltuiala in lst_cheltuieli:
        tipul = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tipul in result:
            if suma > result[tipul]:
                result[tipul] = suma
        else:
            result[tipul] = suma
    return result
