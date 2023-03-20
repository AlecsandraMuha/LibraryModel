from Domain.librarie import creeazaVanzare
from Logic.CRUD import stergeVanzare, modificaVanzare, adaugaVanzare
from UserInterface.console import showAll


def comenzi(lista):
    while True:
        try:
            print("help")
            optiune = input("Dati comanda ")
            if optiune == "help":
                print("Adaugare obiect nou->add")
                print("Pentru a modifica->update")
                print("Sterge obiect->delete")
                print("Pentru a afisa obiectele-> showall")
                print("Stop pentru iesire")
            elif optiune == "stop":
                break
            else:
                action = optiune.split(";")
                for i in range(len(action)):
                    comanda = action[i].split(",")
                    if comanda[0] == "add":
                        if len(comanda) != 6:
                            raise ValueError("Datele nu sunt introduse corect! ")
                        id = int(comanda[1])
                        titlucarte = comanda[2]
                        gencarte = comanda[3]
                        pret = float(comanda[4])
                        tipreducere= comanda[5]
                        lista =  adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere, lista)
                    elif comanda[0] == "delete":
                        id = int(comanda[1])
                        lista = stergeVanzare(id, lista)
                        print("Obiectul a fost sters")
                    elif comanda[0] == "update":
                        if len(comanda) != 6:
                            raise ValueError("Datele nu sunt introduse corect! ")
                        id = int(comanda[1])
                        titlucarte = comanda[2]
                        gencarte = comanda[3]
                        pret = float(comanda[4])
                        tipreducere = comanda[5]
                        lista =  modificaVanzare(id, titlucarte, gencarte, pret, tipreducere, lista)
                        print("Datele au fost modificate")
                    elif comanda[0] == "showall":
                        showAll(lista)
                    else:
                        print("Incorect!")
        except ValueError as ve:
            print("Eroare: {}".format(ve))