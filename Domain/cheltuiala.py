def creeaza_cheltuiala(nr_apartament: int, suma, data, tipul):
    '''
    Creeaza un dictionar ce reprezinta o cheltuiala.
    :param nr_apartament: Numarul apartamentului, trebuie sa fie unic.
    :param suma: Suma de cheltuit.
    :param data: Data cheltuielii.
    :param tipul: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    :return: O cheltuiala.
    '''
    return {
        'nr_ap': nr_apartament,
        'suma': suma,
        'data': data,
        'tip': tipul,
    }


def get_nr_apartament(cheltuiala):
    '''
    Getter pentru numarul apartamentului.
    :param cheltuiala: Cheltuiala.
    :return: Nr de apartament al cheltuielii.
    '''
    return cheltuiala['nr_ap']


def get_suma(cheltuiala):
    '''
    Getter pentru suma.
    :param cheltuiala: Cheltuiala.
    :return: Suma cheltuita.
    '''
    return cheltuiala['suma']


def get_data(cheltuiala):
    '''
    Getter pentru data.
    :param cheltuiala: Cheltuiala.
    :return: Data cheltuielii.
    '''
    return cheltuiala['data']


def get_tipul(cheltuiala):
    '''
    Getter pentru tip.
    :param cheltuiala: Cheltuiala.
    :return: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    '''
    return cheltuiala['tip']


def get_str(cheltuiala):
    return f'Cheltuiala apartamentului cu numarul {get_nr_apartament(cheltuiala)}, din data de {get_data(cheltuiala)} are o suma totala de {get_suma(cheltuiala)}, fiind o cheltuiala de tipul {get_tipul(cheltuiala)}. '