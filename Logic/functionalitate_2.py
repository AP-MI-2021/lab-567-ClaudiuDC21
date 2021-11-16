from Domain.cheltuiala import get_data, creeaza_cheltuiala, get_id_cheltuiala, get_nr_apartament, get_suma, get_tipul


def add_sum_to_all_chelt_by_date(lst_cheltuieli, data, valoare, undo_list, redo_list):
    """
    Aduna o valoare la toate cheltuielile dintr-o data ctita.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param data: Data citita.
    :param valoare: Valoarea ce trebuie adaugata
    :param undo_list: Undo list
    :param redo_list: redo list.
    :return: Lista modificata.
    """
    if valoare < 0:
        raise ValueError('Valoarea data trebuie sa fie un numar pozitiv')
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(
                get_id_cheltuiala(cheltuiala),
                get_nr_apartament(cheltuiala),
                get_suma(cheltuiala) + valoare,
                get_data(cheltuiala),
                get_tipul(cheltuiala)
            )
            new_list.append(cheltuiala_noua)
        else:
            new_list.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_list

