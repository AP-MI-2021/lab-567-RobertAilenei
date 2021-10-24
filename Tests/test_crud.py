from Domain.institutie import getNewObject, get_id
from Logic.crud import create, read, delete, update


def get_data():
    return [
        getNewObject(1, "caiet", "caiet bun", 2, "upst"),
        getNewObject(2, "dosar", "dosar bun", 5, "dwst"),
        getNewObject(3, "pix", "pix bun", 1, "dwst"),
        getNewObject(4, "penar", "penar bun", 20, "upst"),
        getNewObject(5, "lampa", "lampa bun", 50, "mdst"),

    ]


def test_create():
    lista = get_data()
    new_object = getNewObject(6, "lampa", "lampa bun", 50, "mdst")
    lista_noua = create(lista, 6, "lampa", "lampa bun", 50, "mdst")
    assert len(lista_noua) == len(lista) + 1
    assert new_object in lista_noua


def test_read():
    lista = get_data()
    random_object = lista[2]
    assert read(lista, get_id(random_object)) == random_object
    assert read(lista, None) == lista


def test_update():
    lista = get_data()
    new_object = getNewObject(5, "lampan", "lampan bun", 50, "mdst")
    lista_noua = update(lista, new_object)
    assert len(lista) == len(lista_noua)
    assert new_object in lista_noua
    assert lista[4] != lista_noua[4]


def test_delete():
    lista = get_data()
    delete_id = 3
    deleted_object = read(lista, delete_id)
    lista_noua = delete(lista, delete_id)
    assert len(lista_noua) == len(lista) - 1
    assert deleted_object not in lista_noua


def test_crud():
    test_create()
    test_read()
    test_update()


test_crud()
