from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_id_cheltuiala


def create(lst_cheltuieli, id_cheltuiala, nr_apartament, suma, data, tipul):
    """
    Adauga o cheltuiala.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id_cheltuiala: Id-ul cheltuielii.
    :param nr_apartament: Numar partament.
    :param suma: Suma.
    :param data: Data
    :param tipul: Tipul
    :return: O noua lista formata din lst_cheltuieli si noua cheltuiala adaugata.
    """
    if read(lst_cheltuieli, id_cheltuiala) is not None:
        raise ValueError(f'Exista deja o cheltuiala cu id-ul {id_cheltuiala}')
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tipul)
    lst_cheltuieli.append(cheltuiala)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int = None):
    """
    Citeste o cheltuiala din "baza de date" dupa id-ul cheltuielii.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id_cheltuiala: Id-ul cheltuielii.
    :return: Cheltuiala cu nr-ul nr_apartament sau lsta cu toate cheltuielile, daca nr_apartament=None.
    """
    if not id_cheltuiala:
        return lst_cheltuieli
    cheltuiala_nr = None
    for cheltuiala in lst_cheltuieli:
        if get_id_cheltuiala(cheltuiala) == id_cheltuiala:
            cheltuiala_nr = cheltuiala
    if cheltuiala_nr:
        return cheltuiala_nr
    return None


def read_by_nr_apartament(lst_cheltuieli, nr_apartament):
    """
    Citeste o cheltuiala din "baza de date" dupa numarul apartamentului.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param nr_apartament: Numarul apartamentului.
    :return: Cheltuiala cu numarul apartamentului dat, respectiv None daca acesta nu exista.
    """
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            return cheltuiala
    return None


def update(lst_cheltuieli, id_cheltuiala, nr_apartament, suma, data, tipul):
    """
    Actualizeaza o cheltuiala.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id_cheltuiala: Id cheltuiala.
    :param nr_apartament: Numar partament.
    :param suma: Suma.
    :param data: Data
    :param tipul: Tipul
    :return: O lista de 0cheltuieli actualizata.
    """
    if read(lst_cheltuieli, id_cheltuiala) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {id_cheltuiala} pe care sa o actualizam. ')
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_id_cheltuiala(cheltuiala) == id_cheltuiala:
            cheltuiala_noua = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tipul)
            new_list.append(cheltuiala_noua)
        else:
            new_list.append(cheltuiala)
    return new_list


def delete(lst_cheltuieli, id_cheltuiala):
    """
    Sterge o cheltuiala din "baza de date".
    :param lst_cheltuieli: O lista de cheltuieli.
    :param id_cheltuiala: ID cheltuiala.
    :return: O lista fara cheltuiala cu nr-ul nr_apartament.
    """
    if read(lst_cheltuieli, id_cheltuiala) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {id_cheltuiala} pe care sa o stergem. ')
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_id_cheltuiala(cheltuiala) != id_cheltuiala:
            new_list.append(cheltuiala)
    return new_list
