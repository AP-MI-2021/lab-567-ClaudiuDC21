from Tests.tests_functionalitati import test_delete_all_costs_for_apartement, test_add_sum_to_date, \
    test_the_biggest_chelt_for_every_type, test_ordering_chelt_descending_by_amount
from Tests.tests_crud import test_create, test_read, test_update, test_delete


def run_all_tests():
    test_create()
    test_read()
    test_update()
    test_delete()
    test_delete_all_costs_for_apartement()
    test_add_sum_to_date()
    test_the_biggest_chelt_for_every_type()
    test_ordering_chelt_descending_by_amount()