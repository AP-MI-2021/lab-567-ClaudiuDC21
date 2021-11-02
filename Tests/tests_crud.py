from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tipul, get_id_cheltuiala
from Logic.crud import create, read, update, delete


def get_datas():
    return [
        creeaza_cheltuiala(311, 12, 230, 2020 - 12 - 1, 'canal'),
        creeaza_cheltuiala(312, 1, 24, 2021 - 3 - 10, 'intretinere'),
        creeaza_cheltuiala(313, 4, 342, 2020 - 12 - 21, 'alte cheltuieli'),
        creeaza_cheltuiala(314, 5, 353, 2019 - 5 - 28, 'intretinere')
    ]


def test_create():
    cheltuieli = get_datas()
    params = (315, 7, 123, 2021 - 9 - 27, 'alte cheltuieli')
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)

    assert c_new in new_cheltuieli
    assert len(new_cheltuieli) == len(cheltuieli) + 1
    assert get_id_cheltuiala(read(cheltuieli, 311)) == 311
    assert get_nr_apartament(read(cheltuieli, 312)) == 1
    assert get_suma(read(cheltuieli, 313)) == 342
    assert get_tipul(read(cheltuieli, 314)) == 'intretinere'


def test_read():
    cheltuieli = get_datas()
    some_c = cheltuieli[2]
    assert read(cheltuieli, get_id_cheltuiala(some_c)) == some_c
    assert read(cheltuieli, None) == cheltuieli


def test_update():
    cheltuieli = get_datas()
    c_updated = creeaza_cheltuiala(314, 5, 1243.9, 2021 - 11 - 12, 'intretinere')
    updated = update(cheltuieli, 314, 5, 1243.9, 2021 - 11 - 12, 'intretinere')
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(cheltuieli) == len(updated)


def test_delete():
    cheltuieli = get_datas()
    to_delete = 312
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1
