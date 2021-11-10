import datetime

from Logic.crud import create
from Tests.all_tests import run_all_tests
from UserInterface.command_line_console import run_console
from UserInterface.console import run_ui


def show_optiuni():
    print('1. Interfata cu comenzi. ')
    print('2. Interfata cu optiuni. ')
    print('x. Iesire. ')

def main():
    cheltuieli = []
    cheltuieli = create(cheltuieli, 311, 1, 239.42, datetime.date(2019, 11, 28), 'canal')
    cheltuieli = create(cheltuieli, 312, 2, 193.2, datetime.date(2015, 1, 21), 'alte cheltuieli')
    cheltuieli = create(cheltuieli, 313, 3, 300, datetime.date(2010, 10, 8), 'intretinere')
    cheltuieli = create(cheltuieli, 314, 3, 503, datetime.date(2020, 7, 16), 'intretinere')
    cheltuieli = create(cheltuieli, 315, 4, 93, datetime.date(2017, 4, 8), 'alte cheltuieli')
    cheltuieli = create(cheltuieli, 316, 5, 103, datetime.date(2014, 3, 18), 'alte cheltuieli')
    while True:
        show_optiuni()
        optiune = input('Alegeti interfata pe care doriti sa o utilizati: ')
        if optiune == '1':
            run_console(cheltuieli)
        elif optiune == '2':
            run_ui(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita, incercati din nou! ')


if __name__ == '__main__':
    run_all_tests()
    main()
