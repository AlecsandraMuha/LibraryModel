from Domain.librarie import toString, getTitlucarte, getPret, getId, getTipReducere
from Logic.CRUD import stergeVanzare, adaugaVanzare, modificaVanzare
from Logic.functionalitati import discountptrreducere, modificaGenulCartii, pretminim, ordonareDupaPret, numar_titluri


def printMenu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Modifica vanzare")
    print("4.Aplica discount pentru reducerile de tip silver/gold")
    print("5.Modifica genul pentru un titlu dat.")
    print("6.Determinarea prețului minim pentru fiecare gen")
    print("7.Ordonarea vânzărilor crescător după preț")
    print("8.Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a.Afiseza lista de vanzari")
    print("x.Iesire")

def uiAdaugaVanzare(lista, undoList, redoList):
    try:
        id =int(input("Da-ti id-ul: "))
        titlucarte = input("Dati numele cartii: ")
        gencarte = input("Dati genul cartii: ")
        pret = float(input("Dati pretul cartii:"))
        tipreducere = input("Dati tipul reducerii none/silver/gold: ")
        rezultat = adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeVanzare(lista,undoList, redoList):
    try:
        id = int(input("Dati id-ul unei vanzari care ar trebui sa fie stearsa: "))
        rezultat = stergeVanzare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiModificaVanzare(lista,undoList, redoList):
    try:
        id = int(input("Da-ti id-ul: "))
        titlucarte = input("Dati noul nume al cartii: ")
        gencarte = input("Dati noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii:"))
        tipreducere = input("Dati noul tip de reducere none/silver/gold: ")
        rezultat = modificaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiDiscountVanzare(lista,undoList, redoList):
    rezultat = discountptrreducere(lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat

def uiModificaregen(lista,undoList, redoList):
    try:
        titlu = input("Dati titlul cartii: ")
        gencarte= input("Dati noul gen al cartii: ")
        rezultat =  modificaGenulCartii(gencarte,titlu,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiPretMinim(lista):
    rezultat = pretminim(lista)
    for gen in rezultat:
        print("Genul {} are pretul minim {}".format(gen, rezultat[gen]))
def uiOrdonareDupaPret(lista):

    showAll(ordonareDupaPret(lista))
def uinumar_titluri(lista):
    rezultat=numar_titluri(lista)
    for gen in rezultat:
        print("Numarul de titluri distincte pentru genul {} este {}".format(gen,rezultat[gen]))

def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))

def runMenu(lista):
    undoList=[]
    redoList =[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaVanzare(lista,undoList, redoList)
        elif optiune == "2":
            lista = uiStergeVanzare(lista,undoList, redoList)
        elif optiune == "3":
            lista = uiModificaVanzare(lista,undoList, redoList)
        elif optiune == "4":
            lista = uiDiscountVanzare(lista,undoList, redoList)
        elif optiune == "5":
            lista= uiModificaregen(lista,undoList, redoList)
        elif optiune == "6":
            uiPretMinim(lista)
        elif optiune == "7":
            uiOrdonareDupaPret(lista)
        elif optiune == "8":
            uinumar_titluri(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")
