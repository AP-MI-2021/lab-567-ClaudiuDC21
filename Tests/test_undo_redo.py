import datetime

from Logic.crud import create, read
from Logic.undo_redo import do_undo, do_redo
from UserInterface.console import handle_add


def test_undo_redo():
    # 1 lista initiala goala
    lst_cheltuieli = []
    undo_list = []
    redo_list = []

    # 2 adaugam un obiect
    lst_cheltuieli = handle_add(lst_cheltuieli, undo_list, redo_list, obiect)

    # 3 adaugam inca un obiect
    lst_cheltuieli = handle_add(lst_cheltuieli, 312, 2, 193.2, datetime.date(2015, 1, 21), 'alte cheltuieli')

    # 4 adaugam inca un obiect
    lst_cheltuieli = handle_add(lst_cheltuieli, 313, 3, 300, datetime.date(2010, 10, 8), 'intretinere')
    assert len(lst_cheltuieli) == 3

    # 5 undo scoate ultimul obiect
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 311) is not None
    assert read(lst_cheltuieli, 312) is not None
    assert read(lst_cheltuieli, 313) is None

    # 6 inca un undo scoate penultimul obiect adaugat
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 311) is not None
    assert read(lst_cheltuieli, 312) is None
    assert read(lst_cheltuieli, 313) is None
    # 7 inca un undo si primul element adaugat
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 311) is None
    assert read(lst_cheltuieli, 312) is None
    assert read(lst_cheltuieli, 313) is None

    # 8 inca un undo si nu face nimic
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 311) is None
    assert read(lst_cheltuieli, 312) is None
    assert read(lst_cheltuieli, 313) is None

    # 9 adaugam trei obiecte
    lst_cheltuieli = create(lst_cheltuieli, 314, 3, 503, datetime.date(2020, 7, 16), 'intretinere')
    lst_cheltuieli = create(lst_cheltuieli, 315, 4, 93, datetime.date(2017, 4, 8), 'alte cheltuieli')
    lst_cheltuieli = create(lst_cheltuieli, 316, 5, 103, datetime.date(2014, 3, 18), 'alte cheltuieli')
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is not None

    # 10 redo nu face nimic
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is not None

    # 11 doua undo-uri scot ultimele 2 obiecte
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None

    # 12 redo anuleaza ultimul redo, daca ultima operatie e undo
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is None

    # 13 redo anuleaza si primul undo
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is not None
    assert read(lst_cheltuieli, 316) is not None

    # 14 doua undo-uri scot ultimele 2 obiecte
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None

    # 15 adaugam un obiect
    lst_cheltuieli = create(lst_cheltuieli, 317, 23, 3644, datetime.date(2021, 11, 10), 'canal')
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # 16 redo nu face nimic, deoarece ultima operatie nu este un redo
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # 17 undo anuleaza adaugarea lui o4
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is None

    # 18 undo anuleaza stergerea lui o1 - practic se continua sirul de undo de la 14
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 314) is None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is None

    # 19 se anuleaza ultimele 2 undo-uri
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None

    # 20 redo nu face nimic
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 314) is not None
    assert read(lst_cheltuieli, 315) is None
    assert read(lst_cheltuieli, 316) is None
    assert read(lst_cheltuieli, 317) is not None
