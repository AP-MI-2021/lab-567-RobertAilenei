from Domain.institutie import get_locatie, get_descriere
from Logic.crud import create, read
from Logic.mutare import switch_locations, concatenate_strings, ascending_order, det_price, sum_of_prices


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


def test_ascending_order():
    lista = []
    lista = create(lista, 1, "tabla", "alba", 300, "s201")
    lista = create(lista, 2, "birou", "lemn", 200, "s202")
    lista = create(lista, 3, "scaune", "tapitate", 100, "s203")
    lista_noua = ascending_order(lista)

    assert lista not in lista_noua


def test_det_price():
    lista = []
    lista = create(lista, 1, "tabla", "alba", 300, "s202")
    lista = create(lista, 2, "birou", "lemn", 200, "s202")
    lista = create(lista, 3, "scaune", "tapitate", 100, "s201")
    lista = create(lista, 4, "scaune", "tapitate", 150, "s201")
    lista = det_price(lista)

    assert lista == {'s202': {'id': 1, 'nume': "tabla", 'descriere': "alba", 'pret': 300, 'locatie': "s202"},
                     's201': {'id': 4, 'nume': "scaune", 'descriere': "tapitate", 'pret': 150, 'locatie': "s201"}}


def test_sum_of_prices():
    lista = []
    lista = create(lista, 1, "tabla", "alba", 300, "s202")
    lista = create(lista, 2, "birou", "lemn", 200, "s202")
    rezult = sum_of_prices(lista)
    assert rezult == {"s202": 500}


test_sum_of_prices()
test_det_price()
test_ascending_order()
test_concatenate()
test_switch_locations()
