import datetime
from typing import List, Dict

from Domain.cheltuiala import creeaza_cheltuiala, get_str, get_nr_apartament, \
    get_suma, get_data, get_tipul
from Logic.functionalitate_2 import add_sum_to_all_chelt_by_date
from Logic.crud import create, update, delete, read
from Logic.functionalitate_1 import delete_all_costs_for_apartement
from Logic.functionalitate_3 import the_biggest_chelt_for_every_type
from Logic.functionalitate_4 import ordering_chelt_descending_by_amount
from Logic.functionalitate_5 import show_montly_amount_for_each_apartament
from Logic.undo_redo import undo, redo


def show_menu():
    print('1. CRUD ')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament dat. ')
    print(
        '3. Adunarea unei valori la toate cheltuielile dintr-o dată citită. ')
    print(
        '4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială. ')
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
        print(f'Eroare: {ve}')
        return None


def handle_add(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii: '))
        nr_apartament = int(input('Dati numarul apartamentului: '))
        suma = float(input('Dati suma ce trebuie cheltuita: '))
        date = read_date()
        tip = input('Dati tipul: ')
        redo_list.clear()
        return result
    except ValueError as ve:
        print(f'Eroare:  {ve}')
    return cheltuieli


def handle_modify(cheltuieli, undo_list, redo_list):
    try:

        id_cheltuiala = int(
            input('Dati id-ul cheltuielii ce trebuie modificata: '))
        nr_apartament = int(input('Dati numarul noului apartament: '))
        suma = float(input('Dati noua suma: '))
        data = read_date()
        tip = input('Dati noul tip: ')
        cheltuieli = update(cheltuieli, id_cheltuiala, nr_apartament, suma,
                            data, tip, undo_list, redo_list)
        return result
    except ValueError as ve:
        print('Eroare: ', ve)
    return cheltuieli


def handle_delete(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii ce se a sterge: '))
        result = delete(cheltuieli, id_cheltuiala, undo_list, redo_list)
    except ValueError as ve:
        print(f'Eroare: {ve}')
    else:
        print('Cheltuiala s-a sters cu succes! ')
    return cheltuieli


def handle_show_all(cheltuieli):
    for chelt in cheltuieli:
        print(get_str(chelt))


def handle_show_details(cheltuieli):
    id_cheltuiala = int(
        input('Dati id-ul cheltuielii pentru care doriti detalii: '))
    chelt = read(cheltuieli, id_cheltuiala)
    print(f'Numarul apartamentului este: {get_nr_apartament(chelt)}')
    print(f'Suma ce trebuie cheltuita este: {get_suma(chelt)}')
    print(f'Data la care s-au generat costurile: {get_data(chelt)}')
    print(f'Tipul cheltuielii este: {get_tipul(chelt)}')


def handel_crud(cheltuieli, undo_list, redo_list):
    while True:
        print('1. Adaugare cheltuiala')
        print('2. Modificare cheltuiala')
        print('3. Stergere cheltuiala')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('r. Revenire')

        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_modify(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'r':
            break
        else:
            print('Optiune invalida, incercati din nou! ')
    return cheltuieli


def delete_all_costs(cheltuieli, undo_list, redo_list):
    try:
        nr_ap = int(input(
                'Dati numarul apartamentului caruia i se vor sterge cheltuielile: '))
        result = delete_all_costs_for_apartement(cheltuieli, nr_ap, undo_list, redo_list)
    except ValueError as ve:
        print(f'Eroare:  {ve}')
    return cheltuieli


def add_sum_to_date(cheltuieli, undo_list, redo_list):
    try:
        data = read_date()
        valoare = float(input('Dati valoarea ce trebuie adunata: '))
        result = add_sum_to_all_chelt_by_date(cheltuieli, data, valoare, undo_list, redo_list)
    except ValueError as ve:
        print(f'Eroare: {ve}')
    return cheltuieli


def get_biggest_chelt(cheltuieli):
    result = the_biggest_chelt_for_every_type(cheltuieli)
    for tipul in result:
        print(f'Tipul {tipul} are suma maxima {result[tipul]}. ')


def get_ordering_descending_by_amount(cheltuieli, undo_list, redo_list):
    handle_show_all(ordering_chelt_descending_by_amount(cheltuieli, undo_list, redo_list))


def get_sum_each_month_for_apartament(cheltuieli):
    result = show_montly_amount_for_each_apartament(cheltuieli)
    for nr_apartament in result:
        for an in result[nr_apartament]:
            for luna in result[nr_apartament][an]:
                print(
                    f'Apartamentul cu numarul {nr_apartament} are cheltuieli lunare '
                    f'de {result[nr_apartament][an][luna]} in luna {luna} a anului {an}. ')


def handle_undo(cheltuieli, undo_list, redo_list):
    undo_result = undo(undo_list, redo_list, cheltuieli)
    if undo_result is not None:
        return undo_result
    return cheltuieli


def handle_redo(cheltuieli, undo_list, redo_list):
    redo_result = redo(undo_list, redo_list, cheltuieli)
    if redo_result is not None:
        return redo_result
    return cheltuieli


def run_ui(cheltuieli, undo_list, redo_list):
    while True:
        show_menu()
        handle_show_all(cheltuieli)
        optiune = input('Alegeti o optiune: ')
        print()
        if optiune == '1':
            cheltuieli = handel_crud(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = delete_all_costs(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = add_sum_to_date(cheltuieli, undo_list, redo_list)

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
