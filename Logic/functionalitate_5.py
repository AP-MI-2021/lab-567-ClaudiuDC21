from Domain.cheltuiala import get_nr_apartament, get_suma, get_data


def show_montly_amount_for_each_apartament(lst_cheltuieli):
    """
    Afiseaza sumele lunare pentru fiecare apartament.
    :param lst_cheltuieli: Lista de cheltuieli.
    :return: Suma lunara pentru fiecare apartament.
    """
    result = {}
    for cheltuiala in lst_cheltuieli:
        nr_apartament = get_nr_apartament(cheltuiala)
        suma = get_suma(cheltuiala)
        data = get_data(cheltuiala)
        an = data.year
        luna = data.month
        if nr_apartament in result:
            if an in result[nr_apartament]:
                if luna in result[nr_apartament][an]:
                    result[nr_apartament][an][luna] += suma
                else:
                    result[nr_apartament][an][luna] = suma
            else:
                result[nr_apartament][an] = {luna: suma}
        else:
            result[nr_apartament] = {an: {luna: suma}}
    return result
