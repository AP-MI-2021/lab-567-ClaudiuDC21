import datetime

from Logic.crud import create
from Tests.all_tests import run_all_tests
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = create(cheltuieli,311, 1, 239.42, datetime.date(2019, 11, 28), 'canal')
    cheltuieli = create(cheltuieli,312, 2, 193.2, datetime.date(2015, 1, 21), 'alte cheltuieli')
    cheltuieli = create(cheltuieli,313, 3, 300, datetime.date(2010, 10, 8), 'intretinere')
    run_ui(cheltuieli)

if __name__ == '__main__':
    run_all_tests()
    main()