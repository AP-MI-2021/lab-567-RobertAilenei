from Domain.institutie import get_locatie, get_descriere
from Logic.crud import create, read
from Logic.mutare import switch_locations, concatenate_strings


def test_switch_locations():
    lista = []
    lista = create(lista, 1, "tabla", "alba", 300, "s201")
    lista = create(lista, 2, "birou", "lemn", 200, "s202")
    lista = create(lista, 3, "scaune", "tapitate", 100, "s203")

    lista = switch_locations(lista, "s204")

    assert get_locatie(read(lista, 1)) == "s204"
    assert get_locatie(read(lista, 2)) == "s204"
    assert get_locatie(read(lista, 3)) == "s204"


def test_concatenate():
    lista = []
    lista = create(lista, 1, "tabla", "alba", 300, "s201")
    lista = create(lista, 2, "birou", "lemn", 200, "s202")
    lista = create(lista, 3, "scaune", "tapitate", 100, "s203")
    lista = concatenate_strings(lista, "mobilier", 150)

    assert get_descriere(read(lista, 1)) == "albamobilier"
    assert get_descriere(read(lista, 2)) == "lemnmobilier"
    assert get_descriere(read(lista, 3)) == "tapitate"
