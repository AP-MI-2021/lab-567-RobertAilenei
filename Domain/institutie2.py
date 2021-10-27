def getNewObject(_id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    return [_id, _nume, _descriere, _pret, _locatie]


def get_id(obiect):
    return obiect[0]


def get_nume(obiect):
    return obiect[1]


def get_descriere(obiect):
    return obiect[2]


def get_pret(obiect):
    return obiect[3]


def get_locatie(obiect):
    return obiect[4]


def get_obiect_string(obiect):
    return f"Obiectul cu id {get_id(obiect)}, cu numele de {get_nume(obiect)} " \
           f"se poate gasi in locatia: {get_locatie(obiect)}"
