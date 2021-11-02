def creeaza_cheltuiala(id_cheltuiala, nr_apartament: int, suma, data, tipul):
    """
    Creeaza un dictionar ce reprezinta o cheltuiala.
    :param id_cheltuiala: Id-ul apartamentului, trebuie sa fie unic.
    :param nr_apartament: Numarul apartamentului.
    :param suma: Suma de cheltuit.
    :param data: Data cheltuielii.
    :param tipul: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    :return: O cheltuiala.
    """
    """
    return {
        "nr_apartament": nr_apartament,
        "suma": suma,
        "data": data,
        "tipul": tipul,
    }
    """
    return [id_cheltuiala, nr_apartament, suma, data, tipul]


def get_id_cheltuiala(cheltuiala):
    """
    Getter pentru id-ul cheltuielii.
    :param cheltuiala: Cheltuiala.
    :return: Id-ul cheltuielii.
    """
    return cheltuiala[0]


def get_nr_apartament(cheltuiala):
    """
    Getter pentru numarul apartamentului.
    :param cheltuiala: Cheltuiala.
    :return: Nr de apartament al cheltuielii.
    """
    # return cheltuiala["nr_apartament"]
    return cheltuiala[1]


def get_suma(cheltuiala):
    """
    Getter pentru suma.
    :param cheltuiala: Cheltuiala.
    :return: Suma cheltuita.
    """

    # return cheltuiala["suma"]
    return cheltuiala[2]


def get_data(cheltuiala):
    """
    Getter pentru data.
    :param cheltuiala: Cheltuiala.
    :return: Data cheltuielii.
    """
    # return cheltuiala["data"]
    return cheltuiala[3]


def get_tipul(cheltuiala):
    """
    Getter pentru tip.
    :param cheltuiala: Cheltuiala.
    :return: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    """
    # return cheltuiala["tipul"]
    return cheltuiala[4]


def get_str(cheltuiala):
    return f'Cheltuiala apartamentului cu numarul {get_nr_apartament(cheltuiala)}, din data de {get_data(cheltuiala)} ' \
           f'are o suma totala de {get_suma(cheltuiala)}, fiind o cheltuiala de tipul {get_tipul(cheltuiala)}' \
           f', in timp ce id-ul cheltuielii este: {get_id_cheltuiala(cheltuiala)} . '
