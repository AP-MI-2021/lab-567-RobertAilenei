from Logic.crud import create
from UserInterface.console import handle_new_list, handle_undo, handle_redo


def testare():
    lst_obiecte = []
    list_version = [lst_obiecte]
    current_version = 0
    lst_obiecte = create(lst_obiecte, 1, 'masa', 'desc', 150, 'erfs')
    list_version, current_version = handle_new_list(list_version, current_version, lst_obiecte)
    lst_obiecte = create(lst_obiecte, 2, 'dulap', 'desc', 70, 'arfs')
    list_version, current_version = handle_new_list(list_version, current_version, lst_obiecte)
    lst_obiecte = create(lst_obiecte, 3, 'sac', 'desc', 80, 'arss')
    list_version, current_version = handle_new_list(list_version, current_version, lst_obiecte)
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 2
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 1
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 0
    assert handle_undo(list_version, current_version) is None
    lst_obiecte = create(lst_obiecte, 1, 'masa', 'desc', 150, 'erfs')
    list_version, current_version = handle_new_list(list_version, current_version, lst_obiecte)
    lst_obiecte = create(lst_obiecte, 2, 'dulap', 'desc', 70, 'arfs')
    list_version, current_version = handle_new_list(list_version, current_version, lst_obiecte)
    lst_obiecte = create(lst_obiecte, 3, 'sac', 'desc', 80, 'arss')
    list_version, current_version = handle_new_list(list_version, current_version, lst_obiecte)
    assert handle_redo(list_version, current_version) is None
    assert len(lst_obiecte) == 3
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 1
    lst_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lst_obiecte) == 2
    lst_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lst_obiecte) == 3
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 1
    lst_obiecte = create(lst_obiecte, 4, 'masa', 'desc', 150, 'erfs')
    assert handle_redo(list_version, current_version) is None
    assert len(lst_obiecte) == 2
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 1
    lst_obiecte, current_version = handle_undo(list_version, current_version)
    assert len(lst_obiecte) == 0
    lst_obiecte, current_version = handle_redo(list_version, current_version)
    lst_obiecte, current_version = handle_redo(list_version, current_version)
    assert len(lst_obiecte) == 2
    assert handle_redo(list_version, current_version) is None
