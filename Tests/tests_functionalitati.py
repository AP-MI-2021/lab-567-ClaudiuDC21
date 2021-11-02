import datetime

from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tipul, get_id_cheltuiala
from Logic.functionalitate_2 import add_sum_to_all_chelt_by_date
from Logic.crud import read
from Logic.functionalitate_1 import delete_all_costs_for_apartement
from Logic.functionalitate_3 import the_biggest_chelt_for_every_type
from Logic.functionalitate_4 import ordering_chelt_descending_by_amount


def get_datas():
    return [
        creeaza_cheltuiala(311, 12, 230, datetime.date(2021, 12, 1), 'canal'),
        creeaza_cheltuiala(312, 1, 24, datetime.date(2021, 3, 10), 'intretinere'),
        creeaza_cheltuiala(313, 4, 342, datetime.date(2020, 12, 21), 'alte cheltuieli'),
        creeaza_cheltuiala(314, 1, 353, datetime.date(2019, 5, 28), 'intretinere')
    ]
# Functionalitate 1 \/
def test_delete_all_costs_for_apartement():
    cheltuieli = get_datas()
    cheltuieli = delete_all_costs_for_apartement(cheltuieli, 1)
    assert len(cheltuieli) == 2
    assert get_suma(read(cheltuieli, 311)) == 230
    assert get_data(read(cheltuieli, 313)) == datetime.date(2020, 12, 21)


def test_add_sum_to_date():
    cheltuieli = get_datas()
    cheltuieli = add_sum_to_all_chelt_by_date(cheltuieli, datetime.date(2021, 12, 1), 70)
    cheltuiala_noua = read(cheltuieli, 311)
    assert get_nr_apartament(cheltuiala_noua) == 12
    assert get_suma(cheltuiala_noua) == 300
    assert get_data(cheltuiala_noua) == datetime.date(2021, 12, 1)
    assert get_tipul(cheltuiala_noua) == 'canal'


def test_the_biggest_chelt_for_every_type():
    cheltuieli = get_datas()
    result = the_biggest_chelt_for_every_type(cheltuieli)
    assert len(result) == 3
    assert result['canal'] == 230
    assert result['intretinere'] == 353
    assert result['alte cheltuieli'] == 342


def test_ordering_chelt_descending_by_amount():
    cheltuieli = get_datas()
    result = ordering_chelt_descending_by_amount(cheltuieli)
    assert get_id_cheltuiala(result[0]) == 314
    assert get_id_cheltuiala(result[1]) == 313
    assert get_id_cheltuiala(result[2]) == 311
    assert get_id_cheltuiala(result[3]) == 312
