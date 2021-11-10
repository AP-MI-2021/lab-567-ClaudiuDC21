def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Stergerea operatiei anterioare din "baza de date".
    :param undo_list: lista de undo-uri
    :param redo_list: lista de redo-uri
    :param current_list: Lista curenta
    :return: Lista fara ultimul element modificat.
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(top_undo)
        return top_undo[0](current_list)
    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Refacerea operatiei pe care a modificat-o "do_undo".
    :param undo_list: lista de undo-uri
    :param redo_list: lista de redo-uri
    :param current_list: lista curenta
    :return: Lista modificata, refacand ultima operatie care a fost stearsa.
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(top_redo)
        return top_redo[1](current_list)
    return None