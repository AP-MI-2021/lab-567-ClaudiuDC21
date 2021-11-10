import datetime

from Domain.cheltuiala import creeaza_cheltuiala, get_str, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.functionalitate_2 import add_sum_to_all_chelt_by_date, decreases_sum_to_all_chelt_by_date
from Logic.crud import create, update, delete, read
from Logic.functionalitate_1 import delete_all_costs_for_apartement, add_costs_for_apartament
from Logic.functionalitate_3 import the_biggest_chelt_for_every_type
from Logic.functionalitate_4 import ordering_chelt_descending_by_amount
from Logic.functionalitate_5 import show_montly_amount_for_each_apartament
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD ')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament dat. ')
    print('3. Adunarea unei valori la toate cheltuielile dintr-o dată citită. ')
    print('4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială. ')
    print('5. Ordonarea cheltuielilor descrescător după sumă. ')
    print('6. Afișarea sumelor lunare pentru fiecare apartament.')
    print('u. Undo. ')
    print('r. Redo. ')
    print('x. EXIT ')


def read_date():
    try:
        date_str = input('Dati data cu elementele separate printr-o liniuta: ')
        date = date_str.split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        return datetime.date(year, month, day)
    except ValueError as ve:
        print('Eroare: {ve}')
        return None


def handle_add(cheltuieli, undo_list, redo_list, obiect):
    try:
        if len(obiect) == 0:
            id_cheltuiala = int(input('Dati id-ul cheltuielii: '))
            nr_apartament = int(input('Dati numarul apartamentului: '))
            suma = float(input('Dati suma ce trebuie cheltuita: '))
            date = read_date()
            tip = input('Dati tipul: ')
        else:
            id_cheltuiala = int(obiect[0])
            nr_apartament = int(obiect[1])
            suma = float(obiect[2])
            an = obiect[3].year
            luna = obiect[3].month
            zi = obiect[3].day
            date = datetime.date(an, luna, zi)
            tip = obiect[4]
        result = create(cheltuieli, id_cheltuiala, nr_apartament, suma, date, tip)
        undo_list.append([
            lambda: delete(result, id_cheltuiala),
            lambda: create(cheltuieli, id_cheltuiala, nr_apartament, suma, date, tip)
        ])
        redo_list.clear()
        return result
    except ValueError as ve:
        print('Eroare:  {ve}')
    return cheltuieli


def handle_modify(cheltuieli, undo_list, redo_list, obiect):
    try:
        if len(obiect) == 0:
            id_cheltuiala = int(input('Dati id-ul cheltuielii ce trebuie modificata: '))
            nr_apartament = int(input('Dati numarul noului apartament: '))
            suma = float(input('Dati noua suma: '))
            data = read_date()
            tip = input('Dati noul tip: ')
        else:
            id_cheltuiala = int(obiect[0])
            nr_apartament = int(obiect[1])
            suma = float(obiect[2])
            an = obiect[3].year
            luna = obiect[3].month
            zi = obiect[3].day
            data = datetime.date(an, luna, zi)
            tip = obiect[4]
        result = update(cheltuieli, id_cheltuiala, nr_apartament, suma, data, tip)
        cheltuiala_nemodificata = read(cheltuieli, id_cheltuiala)
        undo_list.append([
            lambda: update(result,
                           id_cheltuiala,
                           get_nr_apartament(cheltuiala_nemodificata),
                           get_suma(cheltuiala_nemodificata),
                           get_data(cheltuiala_nemodificata),
                           get_tipul(cheltuiala_nemodificata)
                           ),
            lambda: update(cheltuieli, id_cheltuiala)
        ])
        redo_list.clear()
        return result
    except ValueError as ve:
        print('Eroare: ', ve)
    return cheltuieli


def handle_delete(cheltuieli, undo_list, redo_list, obiect):
    try:
        if len(obiect) == 0:
            id_cheltuiala = int(input('Dati id-ul cheltuielii ce se a sterge: '))
        else:
            id_cheltuiala = obiect[0]
        result = delete(cheltuieli, id_cheltuiala)
        cheltuiala_de_sters = read(cheltuieli, id_cheltuiala)
        undo_list.append([
            lambda: create(result,
                           id_cheltuiala,
                           get_nr_apartament(cheltuiala_de_sters),
                           get_suma(cheltuiala_de_sters),
                           get_data(cheltuiala_de_sters),
                           get_tipul(cheltuiala_de_sters)
                           ),
            lambda: delete(cheltuieli, id_cheltuiala)
        ])
        redo_list.clear()
        return result
    except ValueError as ve:
        print('Eroare:  {ve}')
    return cheltuieli


def handle_show_all(cheltuieli):
    for chelt in cheltuieli:
        print(get_str(chelt))


def handle_show_details(cheltuieli):
    id_cheltuiala = int(input('Dati id-ul cheltuielii pentru care doriti detalii: '))
    chelt = read(cheltuieli, id_cheltuiala)
    print(f'Numarul apartamentului este: {get_nr_apartament(chelt)}')
    print(f'Suma ce trebuie cheltuita este: {get_suma(chelt)}')
    print(f'Data la care s-au generat costurile: {get_data(chelt)}')
    print(f'Tipul cheltuielii este: {get_tipul(chelt)}')


def handel_crud(cheltuieli, undo_list, redo_list, obiect):
    while True:
        print('1. Adaugare cheltuiala')
        print('2. Modificare cheltuiala')
        print('3. Stergere cheltuiala')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('r. Revenire')

        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli, undo_list, redo_list, obiect)
        elif optiune == '2':
            cheltuieli = handle_modify(cheltuieli, undo_list, redo_list, obiect)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli, undo_list, redo_list, obiect)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'r':
            break
        else:
            print('Optiune invalida, incercati din nou! ')
    return cheltuieli


def delete_all_costs(cheltuieli, undo_list, redo_list, obiect):
    try:
        if len(obiect) == 0:
            nr_ap = int(input('Dati numarul apartamentului caruia i se vor sterge cheltuielile: '))
        else:
            nr_ap = int(obiect[0])
        result = delete_all_costs_for_apartement(cheltuieli, nr_ap)
        cheltuieli_de_sters = []
        for cheltuiala in cheltuieli:
            if get_nr_apartament(cheltuiala) == nr_ap:
                cheltuieli_de_sters.append(cheltuiala)
        undo_list.append([
            lambda: add_costs_for_apartament(cheltuieli_de_sters, result),
            lambda: delete_all_costs_for_apartement(cheltuieli, nr_ap)
        ])
        redo_list.clear()
        return result
    except ValueError as ve:
        print('Eroare:  {ve}')
    return cheltuieli


def add_sum_to_date(cheltuieli, undo_list, redo_list, obiect):
    try:
        if len(obiect) == 0:
            data = read_date()
            if data is None:
                raise ValueError("Data nu a fost introdusa corespunzator")
            valoare = float(input('Dati valoarea ce trebuie adunata: '))
        else:
            an = obiect[0].year
            luna = obiect[0].month
            zi = obiect[0].day
            data = datetime.date(an, luna, zi)
            valoare = obiect[1]
        result = add_sum_to_all_chelt_by_date(cheltuieli, data, valoare)
        cheltuieli_de_modificat = []
        for cheltuiala in cheltuieli:
            if get_data(cheltuiala) == data:
                cheltuieli_de_modificat.append(cheltuiala)
        undo_list.append([
            lambda: decreases_sum_to_all_chelt_by_date(result, data, valoare),
            lambda: add_sum_to_all_chelt_by_date(cheltuieli, data, valoare)
        ])
        redo_list.clear()
        return result
    except ValueError as ve:
        print('Eroare:  {ve}')
    return cheltuieli


def get_biggest_chelt(cheltuieli):
    result = the_biggest_chelt_for_every_type(cheltuieli)
    for tipul in result:
        print(f'Tipul {tipul} are suma maxima {result[tipul]}. ')


def get_ordering_descending_by_amount(cheltuieli):
    handle_show_all(ordering_chelt_descending_by_amount(cheltuieli))


def get_sum_each_month_for_apartament(cheltuieli):
    result = show_montly_amount_for_each_apartament(cheltuieli)
    for nr_apartament in result:
        for an in result[nr_apartament]:
            for luna in result[nr_apartament][an]:
                print(f'Apartamentul cu numarul {nr_apartament} are cheltuieli lunare '
                      f'de {result[nr_apartament][an][luna]} in luna {luna} a anului {an}. ')


def handle_undo(cheltuieli, undo_list, redo_list):
    if len(undo_list) > 0:
        undo_result = do_undo(undo_list, redo_list, cheltuieli)
        if undo_result is not None:
            return undo_result
    else:
        print('Nu se poate efectua undo! ')
        return cheltuieli


def handle_redo(cheltuieli, undo_list, redo_list):
    if len(redo_list) > 0:
        redo_result = do_redo(undo_list, redo_list, cheltuieli)
        if redo_result is not None:
            return redo_result
    else:
        print('Nu se poate efectua redo! ')
        return cheltuieli


def run_ui(cheltuieli):
    while True:
        undo_list = []
        redo_list = []
        obiect = []
        show_menu()
        optiune = input('Alegeti o optiune: ')
        print()
        if optiune == '1':
            cheltuieli = handel_crud(cheltuieli, undo_list, redo_list, obiect)
        elif optiune == '2':
            cheltuieli = delete_all_costs(cheltuieli, undo_list, redo_list, obiect)
        elif optiune == '3':
            cheltuieli = add_sum_to_date(cheltuieli, undo_list, redo_list, obiect)
        elif optiune == '4':
            get_biggest_chelt(cheltuieli)
        elif optiune == '5':
            get_ordering_descending_by_amount(cheltuieli)
        elif optiune == '6':
            get_sum_each_month_for_apartament(cheltuieli)
        elif optiune == 'u':
            cheltuieli = handle_undo(cheltuieli, undo_list, redo_list)
        elif optiune == 'r':
            cheltuieli = handle_redo(cheltuieli, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune incorecta, incercati din nou! ')
    return cheltuieli
