import datetime

from Domain.cheltuiala import creeaza_cheltuiala, get_str, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.crud import create, update, delete, read


def show_menu():
    print('1. CRUD ')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament dat. ')
    print('x. EXIT ')


def read_date():
    date_str = input('Dati data cu elementele separate printr-o liniuta: ')
    date = date_str.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    return datetime.date(year,month, day)


def handle_add(cheltuieli):
    nr_apartament = int(input('Dati numarul apartamentului: '))
    suma = float(input('Dati suma ce trebuie cheltuita: '))
    date = read_date()
    tip = input('Dati tipul: ')
    return create(cheltuieli, nr_apartament, suma, date, tip)


def handle_modify(cheltuieli):
    nr_apartament = int(input('Dati numarul apartamentului ce ii trebuie modificata cheltuiala: '))
    suma = float(input('Dati noua suma: '))
    data = read_date()
    tip = input('Dati noul tip: ')
    return update(cheltuieli, creeaza_cheltuiala(nr_apartament, suma, data, tip) )


def handle_delete(cheltuieli):
    nr_apartament = int(input('Dati numarul apartamentului ce se a sterge: '))
    cheltuieli = delete(cheltuieli, nr_apartament)
    print('Stergerea a fost efectuata cu succes!')


def handle_show_all(cheltuieli):
    for chelt in cheltuieli:
        print(get_str(chelt))


def handle_show_details(cheltuieli):
    nr_apartament = int(input('Dati numarul apartamentului pentru care doriti detalii: '))
    chelt = read(cheltuieli, nr_apartament)
    print(f'Suma ce trebuie cheltuita este: {get_suma(chelt)}')
    print(f'Data la care s-au generat costurile: {get_data(chelt)}')
    print(f'Tipul cheltuielii este: {get_tipul(chelt)}')


def handel_crud(cheltuieli):
    while True:
        print('1. Adaugare cheltuiala')
        print('2. Modificare cheltuiala')
        print('3. Stergere cheltuiala')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('r. Revenire')

        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            handle_add(cheltuieli)
        elif optiune == '2':
            handle_modify(cheltuieli)
        elif optiune == '3':
            handle_delete(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'r':
            break
        else:
            print('Optiune invalida, incercati din nou! ')
    return cheltuieli



def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Alegeti o optiune: ')
        print()
        if optiune == '1':
            cheltuieli = handel_crud(cheltuieli)
        elif optiune == '2':
            pass
        elif optiune == '3':
            pass
        elif optiune == '4':
            pass
        elif optiune == '5':
            pass
        elif optiune == '6':
            pass
        elif optiune == 'x':
            break
        else:
            print('Optiune incorecta, incercati din nou! ')
    return cheltuieli