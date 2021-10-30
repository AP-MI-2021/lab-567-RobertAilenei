from Domain.institutie import get_id, get_pret, get_descriere, getNewObject, get_nume, get_locatie


def switch_locations(lista, locatie_dorita):
    """
    Aceasta functie  muta toate obiectele dintr-o locatie in alta
    :param lista: Aceasta functie primeste o lista de obiecte
    :param locatie_dorita:  Aceasta functie primeste o noua locatie
    :return: Functia returneaza o lista noua in care toate obiectele sunt mutate din locatiile lor in locatie dorita
    """
    if len(locatie_dorita) != 4:
        raise ValueError('Sirul trebuie sa aiba exact 4 caratere!')
    lista_noua = []
    for obiect in lista:
        lista_noua.append(getNewObject(get_id(obiect), get_nume(obiect),
                                       get_descriere(obiect), get_pret(obiect), locatie_dorita))
    return lista_noua


def concatenate_strings(lista, string, valoare):
    """
    :param lista: Aceasta functie primeste o lista de obiecte
    :param string: Aceasta functie primeste un string
    :param valoare: Aceasta functie primeste o valoare de tip float
    :return: Aceasta functie returneaza aceeasi lista, iar in cazul in care
    exista valori mai mari decat cea data o lista in care obiectele au atasate stringuri la descriere
    """
    rezult = []
    for obiect in lista:
        if valoare < get_pret(obiect):
            rezult.append(getNewObject(get_id(obiect), get_nume(obiect),
                                       get_descriere(obiect)+string, get_pret(obiect), get_locatie(obiect)))
        else:
            rezult.append(obiect)
    return rezult
