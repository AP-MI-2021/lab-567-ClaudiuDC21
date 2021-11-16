

def undo(undo_list, redo_list, current_list):
    """
    Stergerea operatiei anterioare din "baza de date".
    :param undo_list: lista de undo-uri
    :param redo_list: lista de redo-uri
    :param current_list: Lista curenta
    :return: Lista fara ultimul element modificat.
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo
    return None


def redo(undo_list, redo_list, current_list):
    """
    Refacerea operatiei pe care a modificat-o "do_undo".
    :param undo_list: lista de undo-uri
    :param redo_list: lista de redo-uri
    :param current_list: lista curenta
    :return: Lista modificata, refacand ultima operatie care a fost stearsa.
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    return None