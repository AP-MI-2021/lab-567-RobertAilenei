def getNewObject(_id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    if len(_locatie) != 4:
        raise ValueError("Lungimea locatiei trebuie sa aiba exact 4 caractere")
    obiect = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret': _pret,
        'locatie': _locatie
        }
    return obiect


def get_id(obiect):
    return obiect['id']


def get_nume(obiect):
    return obiect['nume']


def get_descriere(obiect):
    return obiect['descriere']


def get_pret(obiect):
    return obiect['pret']


def get_locatie(obiect):
    return obiect['locatie']


def get_obiect_string(obiect):
    return f"Obiectul cu id {get_id(obiect)}, cu numele de {get_nume(obiect)} " \
           f"se poate gasi in locatia: {get_locatie(obiect)}"
