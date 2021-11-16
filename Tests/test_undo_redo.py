import datetime

from Domain.cheltuiala import get_suma
from Logic.crud import create, read, read_by_nr_apartament
from Logic.functionalitate_1 import delete_all_costs_for_apartement
from Logic.functionalitate_2 import add_sum_to_all_chelt_by_date
from Logic.undo_redo import undo, redo

def test_undo_redo():
    # 1 lista initiala goala
    lst_cheltuieli = []
    undo_list = []
    redo_list = []
    assert len(lst_cheltuieli) == 0

    # 2 adaugam un obiect
    lst_cheltuieli = create(lst_cheltuieli, 311, 1, 1234, datetime.date(2021, 11, 12), 'intretinere', undo_list, redo_list)

    # 3 adaugam inca un obiect
    lst_cheltuieli = create(lst_cheltuieli, 312, 2, 193.2, datetime.date(2015, 1, 21), 'alte cheltuieli', undo_list, redo_list)

    # 4 adaugam inca un obiect
    lst_cheltuieli = create(lst_cheltuieli, 313, 3, 300, datetime.date(2010, 10, 8), 'intretinere', undo_list, redo_list)
    assert len(lst_cheltuieli) == 3

    # 5 undo scoate ultimul obiect
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 311) is not None
    assert read(lst_cheltuieli, 312) is not None
    assert read(lst_cheltuieli, 313) is None

    # 6 inca un undo scoate penultimul obiect adaugat
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 311) is not None
    assert read(lst_cheltuieli, 312) is None
    assert read(lst_cheltuieli, 313) is None

    # 7 inca un undo si primul element adaugat
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 311) is None
    assert read(lst_cheltuieli, 312) is None
    assert read(lst_cheltuieli, 313) is None

    # 8 inca un undo si nu face nimic
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert read(lst_cheltuieli, 311) is None
    assert read(lst_cheltuieli, 312) is None
    assert read(lst_cheltuieli, 313) is None

    # 9 adaugam trei obiecte
    lst_cheltuieli = create(lst_cheltuieli, 314, 3, 503, datetime.date(2020, 7, 16), 'intretinere', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 315, 4, 93, datetime.date(2017, 4, 8), 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 316, 5, 103, datetime.date(2014, 3, 18), 'alte cheltuieli', undo_list, redo_list)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is not None

    # 10 redo nu face nimic
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is not None

    # 11 doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None

    # 12 redo anuleaza ultimul redo, daca ultima operatie e undo
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is None

    # 13 redo anuleaza si primul undo
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is not None

    # 14 doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None

    # 15 adaugam un obiect
    lst_cheltuieli = create(lst_cheltuieli, 317, 23, 3644, datetime.date(2021, 11, 10), 'canal', undo_list, redo_list)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # 16 redo nu face nimic, deoarece ultima operatie nu este un redo
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # 17 undo anuleaza adaugarea lui o4
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is None

    # 18 undo anuleaza stergerea lui o1 - practic se continua sirul de undo de la 14
    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 314) is None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is None

    # 19 se anuleaza ultimele 2 undo-uri
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # 20 redo nu face nimic
    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # test_undo_redo - stergerea tuturor cheltuielilor pentru un apartament dat
    lst_cheltuieli = []
    lst_cheltuieli = create(lst_cheltuieli, 313, 3, 300, datetime.date(2010, 10, 8), 'intretinere', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 314, 3, 503, datetime.date(2020, 7, 16), 'intretinere', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 315, 4, 93, datetime.date(2017, 4, 8), 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 316, 5, 103, datetime.date(2014, 3, 18), 'alte cheltuieli', undo_list, redo_list)

    nr_apartamet = 3
    lst_cheltuieli = delete_all_costs_for_apartement(lst_cheltuieli,nr_apartamet, undo_list, redo_list)
    assert len(lst_cheltuieli) == 2
    assert read_by_nr_apartament(lst_cheltuieli, 3) is None
    assert read_by_nr_apartament(lst_cheltuieli, 4) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 5) is not None

    if len(undo_list) > 0:
        lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)

    assert len(lst_cheltuieli) == 4
    assert read_by_nr_apartament(lst_cheltuieli, 3) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 4) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 5) is not None

    if len(redo_list) > 0:
        lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read_by_nr_apartament(lst_cheltuieli, 3) is None
    assert read_by_nr_apartament(lst_cheltuieli, 4) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 5) is not None

    # test_undo_redo - adunarea unei valori la toate cheltuielile dintr-o data citita
    lst_cheltuieli = []
    lst_cheltuieli = create(lst_cheltuieli, 313, 3, 300,
                            datetime.date(2010, 10, 8), 'intretinere',
                            undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 314, 3, 503,
                            datetime.date(2020, 7, 16), 'intretinere',
                            undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 315, 4, 93,
                            datetime.date(2017, 4, 8), 'alte cheltuieli',
                            undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 316, 5, 103,
                            datetime.date(2014, 3, 18), 'alte cheltuieli',
                            undo_list, redo_list)

    data = datetime.date(2020, 7, 16)
    valaore = 200
    lst_cheltuieli = add_sum_to_all_chelt_by_date(lst_cheltuieli,data, valaore, undo_list, redo_list)

    assert get_suma(read(lst_cheltuieli, 313)) == 300
    assert get_suma(read(lst_cheltuieli, 314)) == 703
    assert get_suma(read(lst_cheltuieli, 315)) == 93

    lst_cheltuieli = undo(undo_list, redo_list, lst_cheltuieli)
    assert get_suma(read(lst_cheltuieli, 313)) == 300
    assert get_suma(read(lst_cheltuieli, 314)) == 503
    assert get_suma(read(lst_cheltuieli, 315)) == 93

    lst_cheltuieli = redo(undo_list, redo_list, lst_cheltuieli)
    assert get_suma(read(lst_cheltuieli, 313)) == 300
    assert get_suma(read(lst_cheltuieli, 314)) == 703
    assert get_suma(read(lst_cheltuieli, 315)) == 93