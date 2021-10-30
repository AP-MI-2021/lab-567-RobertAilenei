from Domain.institutie import get_obiect_string, get_nume, get_locatie, get_pret, get_descriere, getNewObject
from Logic.crud import create, read, update, delete
from Logic.mutare import switch_locations, concatenate_strings


def handle_add(obiecte):
    try:
        id_obiect = int(input('Dati id-ul obiectului: '))
        nume = input('Dati numele obiectului: ')
        descriere = input('Dati descrierea obiectului: ')
        pret = int(input('Dati pretul obiectului: '))
        locatie = input('Dati locatia obiectului: ')
        return create(obiecte, id_obiect, nume, descriere, pret, locatie)
    except ValueError as ve:
        print("Eroare: ", ve)
    return obiecte


def handle_show_all(obiecte):
    for obiect in obiecte:
        print(get_obiect_string(obiect))


def handle_show_details(obiecte):
    id_obiect = int(input('Dati id-ul obiectului pentru care doriti detalii: '))
    obiect = read(obiecte, id_obiect)
    print(f'Nume: {get_nume(obiect)}')
    print(f'Descriere: {get_descriere(obiect)}')
    print(f'Pret: {get_pret(obiect)}')
    print(f'Locatie: {get_locatie(obiect)}')


def handle_update(obiecte):
    try:
        id_obiect = int(input('Dati id-ul obiectului pe care doriti sa-l actualizati: '))
        nume = input('Dati numele obiectului nou: ')
        descriere = input('Dati descrierea obiectului nou: ')
        pret = int(input('Dati pretul obiectului nou: '))
        locatie = input('Dati locatia obiectului nou: ')
        return update(obiecte, getNewObject(id_obiect, nume, descriere, pret, locatie))
    except ValueError as ve:
        print("Eroare: ", ve)


def handle_delete(obiecte):
    try:
        id_obiect = int(input('Dati id obiectului pe care doriti sa-l stergeti: '))
        obiecte = delete(obiecte, id_obiect)
        print("Steregerea a fost efectuata cu succes")
        return obiecte
    except ValueError as ve:
        print("Eroare: ", ve)


def handle_crud(obiecte):
    while True:
        print('1.Adaugare')
        print('2.Modificare')
        print('3.Stergere')
        print('a. Afisare')
        print('d.Detalii')
        print('b.Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            obiecte = handle_update(obiecte)
        elif optiune == '3':
            obiecte = handle_delete(obiecte)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'd':
            handle_show_details(obiecte)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')

    return obiecte


def handle_switch_locations(obiecte):
    locatie_noua = input('Dati locatia noua: ')
    return switch_locations(obiecte, locatie_noua)


def handle_concatenate_string(obiecte):
    string = str(input("Dati stringul: "))
    valoare = float(input("Dati valoarea: "))
    return concatenate_strings(obiecte, string, valoare)


def show_menu():
    print('1.Crud')
    print('2.Mutarea tuturor obiectelor dintr-o locație în alta.')
    print('3.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită')
    print('4.Determinarea celui mai mare preț pentru fiecare locație')
    print('5.Ordonarea obiectelor crescător după prețul de achiziție.')
    print('6.Afișarea sumelor prețurilor pentru fiecare locație')
    print('7. Afișarea sumelor prețurilor pentru fiecare locație.')
    print('x. Exit')


def run_ui(obiecte):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            obiecte = handle_crud(obiecte)
        elif optiune == '2':
            obiecte = handle_switch_locations(obiecte)
        elif optiune == '3':
            obiecte = handle_concatenate_string(obiecte)
        elif optiune == '4':
            pass
        elif optiune == '5':
            pass
        elif optiune == '6':
            pass
        elif optiune == '7':
            pass
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida")
