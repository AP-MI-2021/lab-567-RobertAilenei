from Domain.institutie2 import getNewObject, get_id


def create(lista_obiecte: list, _id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    obiect = getNewObject(_id, _nume, _descriere, _pret, _locatie)
    return lista_obiecte + [obiect]


def read(lista_obiecte: list, id_obiect: int = None):
    obiect_gasit = None
    if id_obiect is None:
        return lista_obiecte
    for obiect in lista_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_gasit = obiect
    return obiect_gasit


def update(lista_obiecte, new_object):
    rezult = []
    for obiect in lista_obiecte:
        if get_id(obiect) == get_id(new_object):
            rezult.append(new_object)
        else:
            rezult.append(obiect)
    return rezult


def delete(lista_obiecte, id_obiect: int):
    rezult = []
    for obiect in lista_obiecte:
        if get_id(obiect) != id_obiect:
            rezult.append(obiect)
    return rezult
