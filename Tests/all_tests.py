from Tests.tests_crud import test_create, test_read, test_update, test_delete


def run_all_tests():
    test_create()
    test_read()
    test_update()
    test_delete()