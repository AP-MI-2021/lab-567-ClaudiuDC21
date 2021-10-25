from Logic.crud import create
from Tests.all_tests import run_all_tests
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = create(cheltuieli, 6, 194, 2020- 12- 12, 'alte cheltuieli')
    cheltuieli = run_ui(cheltuieli)


if __name__ == '__main__':
    run_all_tests()
    main()