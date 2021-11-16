from Domain.cheltuiala import get_suma


def ordering_chelt_descending_by_amount(lst_cheltuieli, undo_list, redo_list):
    """
    Ordoneaza cheltuielile descrescator dupa suma.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param undo_list: Undo list
    :param redo_list: redo list
    :return: Cheltuielile ordonate descrescator dupa suma.
    """
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return sorted(lst_cheltuieli, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)
