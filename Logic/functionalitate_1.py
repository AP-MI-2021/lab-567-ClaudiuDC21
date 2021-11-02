from Domain.cheltuiala import get_nr_apartament
from Logic.crud import update, read


def delete_all_costs_for_apartement(lst_cheltuieli, nr_apartament):
    """
    Sterge toate cheltuielile pentru un apartament dat.
    :param lst_cheltuieli:  lista de cheltuieli.
    :param nr_apartament: Nr-ul apartamentului.
    :return: Lista in care cheltuielile partamentului dat s-au sters.
    """
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_list.append(cheltuiala)
    return new_list
