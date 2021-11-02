from Domain.cheltuiala import get_suma


def ordering_chelt_descending_by_amount(lst_cheltuieli):
    """
    Ordoneaza cheltuielile descrescator dupa suma.
    :param lst_cheltuieli: Lista de cheltuieli.
    :return: Cheltuielile ordonate descrescator dupa suma.
    """
    return sorted(lst_cheltuieli, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)