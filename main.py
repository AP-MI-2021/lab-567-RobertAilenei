from Domain.institutie import getNewObject
from Logic.crud import create, read, update, delete

lista = []
lista = create(lista, 1, "caiet", "caiet bun", 2, "upst")
lista = create(lista, 2, "dosar", "dosar bun", 5, "dwst")


NewObject = getNewObject(1, "caiet nou", "caiet bun nou", 2, "upst")
lista = update(lista, NewObject)

lista = delete(lista, 1)
obiect1 = read(lista, 1)
print(obiect1)
