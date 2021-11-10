from Domain.cheltuiala import get_nr_apartament
from Logic.crud import update, read_by_nr_apartament


def delete_all_costs_for_apartement(lst_cheltuieli, nr_apartament):
    """
    Sterge toate cheltuielile pentru un apartament dat.
    :param lst_cheltuieli:  lista de cheltuieli.
    :param nr_apartament: Nr-ul apartamentului.
    :return: Lista in care cheltuielile partamentului dat s-au sters.
    """
    if read_by_nr_apartament(lst_cheltuieli, nr_apartament) is None:
        raise ValueError('Numarul apartamentului nu exista! ')
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_list.append(cheltuiala)
    return new_list


def add_costs_for_apartament(cheltuieli, lista):
    """
    Adauga inapoi cheltuielile ce au fost sterse la prima functionalitate.(pentru Undo)
    :param cheltuieli: Lista cu cheltuieli ce trebuie adaugate.
    :param lista_noua: Lista in care se vor adauga cheltuielile adaugate anterior.
    :return: Lista in care cheltuielile au fost adaugate inapoi.
    """
    result = []
    for cheltuiala in lista:
        result.append(cheltuiala)
    for cheltuiala_de_adaugat in cheltuieli:
        result.append(cheltuiala_de_adaugat)
    return result

