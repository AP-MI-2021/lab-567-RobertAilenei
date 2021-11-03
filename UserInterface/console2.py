from Domain.institutie import get_obiect_string, getNewObject
from Logic.crud import create,  update, delete
from Logic.mutare import switch_locations, concatenate_strings


def show_menu():
    print("""
    *Lista comenzi posibile*

    Adaugare: id, nume, descriere, pret, locatie   -> comanda: add
    Exemplu:add,1,pix,pixnou,200,down
    Stergere: id obiect     -> comanda: delete
    Exemplu:delete,
    Modificare: id, nume, descriere, pret, locatie -> comanda: update
    Exemplu:update,1,pix,pixnou,200,down
    Afisare lista vanzari.    -> comanda: showall
    Modificarea locatiei tuturor obiectelor : locatie,    -> comanda:mod
    Exemplu:mod, upst
    Concatenare_str: string, valoare  -> comanda: conc
    Exemplu: conc,desc,100
    Oprire. -> comanda: exit
    """)


def show_all(obiecte):
    for obiect in obiecte:
        print(get_obiect_string(obiect))


def run_ui(obiecte):
    stop = True
    show_menu()
    command_line = input("""
                               Linia de comenzi trebuie sa contina separatorul ; intre seriile de comenzi.
                               Separatorul comenzilor va fi , .
                               La sfarsitul liniei de comenzi se va pune exit pentru oprire, tot separat prin ;
                               Introduceti comenzile: """)
    while stop:
        serie_comanda = command_line.split(";")
        for comanda in serie_comanda:
            comanda = comanda.split(",")
            if comanda[0] == "add":
                try:
                    obiecte = create(obiecte, int(comanda[1]), comanda[2], comanda[3], int(comanda[4]), comanda[5])
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "delete":
                try:
                    obiecte = delete(obiecte, int(comanda[1]))
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "update":
                try:
                    obiecte = update(obiecte, getNewObject(int(comanda[1]),
                                                           comanda[2], comanda[3], int(comanda[4]), comanda[5]))
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif comanda[0] == "showall":
                show_all(obiecte)
            elif comanda[0] == "mod":
                print(switch_locations(obiecte, comanda[1]))
            elif comanda[0] == "conc":
                print(concatenate_strings(obiecte, comanda[1], float(comanda[2])))
            elif comanda[0] == "exit":
                stop = False
                break
