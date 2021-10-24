lista_obiecte = []


def get_all_objects():
    return lista_obiecte


def addObject(_id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    obiect = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret': _pret,
        'locatie': _locatie
    }
    lista_obiecte.append(obiect)
