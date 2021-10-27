from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament


def create(lst_cheltuieli, nr_apartament, suma, data, tipul):
    """
    Adauga o cheltuiala.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id_apartament: Id-ul apartamentului.
    :param nr_apartament: Numar partament.
    :param suma: Suma.
    :param data: Data
    :param tipul: Tipul
    :return: O noua lista formata din lst_cheltuieli si noua cheltuiala adaugata.
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament, suma, data, tipul)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, nr_apartament: int = None):
    """
    Citeste o cheltuiala din "baza de date".
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id_apartament: Id apartament.
    :return: Cheltuiala cu nr-ul nr_apartament sau lsta cu toate cheltuielile, daca nr_apartament=None.
    """
    cheltuiala_nr = None
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_nr = cheltuiala
    if cheltuiala_nr:
        return cheltuiala_nr
    return lst_cheltuieli


def update(lst_cheltuieli, nr_apartament, suma, data, tipul):
    """
    Actualizeaza o cheltuiala.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id_apartament: Id apartament.
    :param nr_apartament: Numar partament.
    :param suma: Suma.
    :param data: Data
    :param tipul: Tipul
    :return: O lista de cheltuieli actualizata.
    """
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_noua = creeaza_cheltuiala(nr_apartament, suma, data, tipul)
            new_list.append(cheltuiala_noua)
        else:
            new_list.append(cheltuiala)
    return new_list


def delete(lst_cheltuieli, nr_apartament):
    """
    Sterge o cheltuiala din "baza de date".
    :param lst_cheltuieli: O lista de cheltuieli.
    :param id_apartament: ID apartament.
    :return: O lista fara cheltuiala cu nr-ul nr_apartament.
    """
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_list.append(cheltuiala)
    return new_list
