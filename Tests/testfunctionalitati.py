from Domain.librarie import getGencarte, getTipReducere, getPret, getId
from Logic.CRUD import adaugaVanzare, getById
from Logic.functionalitati import modificaGenulCartii, discountptrreducere, pretminim, ordonareDupaPret, numar_titluri


def testdiscountptrreducere():
    lista = []
    lista = adaugaVanzare(1, "Enigma Otiliei", "Roman realist", 20.0, "gold", lista)
    lista = adaugaVanzare(2, "Harap-Alb", "basm", 15.0, "none", lista)
    lista = adaugaVanzare(3, "Moara cu noroc", "Nuvela", 30.0, "gold", lista)
    lista = discountptrreducere(lista)
    assert getPret(lista[0]) == 18.0
    assert getPret(lista[1]) == 15.0
    assert getPret(lista[2]) == 27.0
def testModificareGen():

    lista = []
    lista = adaugaVanzare(1, "Enigma Otiliei", "Roman realist", 12, "gold", lista)
    lista = adaugaVanzare(2, "Harap-Alb", "basm", 15, "none", lista)
    lista = adaugaVanzare(3, "Moara cu noroc", "Nuvela", 30, "gold", lista)

    lista = modificaGenulCartii("basm cult", "Harap-Alb", lista)

    assert getGencarte(getById(1, lista)) == "Roman realist"
    assert getGencarte(getById(2, lista)) == "basm cult"
    assert getGencarte(getById(3, lista)) == "Nuvela"
def testpretminim():
    lista = []
    lista = adaugaVanzare(1, "Enigma Otiliei", "Roman realist", 12, "gold", lista)
    lista = adaugaVanzare(2, "Harap-Alb", "basm", 15, "none", lista)
    lista = adaugaVanzare(3, "Ion", "Roman realist", 30, "gold", lista)
    rezultat = pretminim(lista)
    assert rezultat["basm"] == 15
    assert rezultat["Roman realist"] == 12
def testordonare():
    lista = []
    lista = adaugaVanzare(1, "Enigma Otiliei", "Roman realist", 12, "gold", lista)
    lista = adaugaVanzare(2, "Harap-Alb", "basm", 15, "none", lista)
    lista = adaugaVanzare(3, "Ion", "Roman realist", 30, "gold", lista)
    rezultat = ordonareDupaPret(lista)
    assert getId(rezultat[0]) == 1
    assert getId(rezultat[1]) == 2
    assert getId(rezultat[2]) == 3
def testnumar_titluri():
    lista = []
    lista = adaugaVanzare(1, "Enigma Otiliei", "Roman realist", 12, "gold", lista)
    lista = adaugaVanzare(2, "Harap-Alb", "basm", 15, "none", lista)
    lista = adaugaVanzare(3, "Ion", "Roman realist", 30, "gold", lista)
    rezultat = numar_titluri(lista)
    assert len(rezultat) == 2
    assert rezultat["Roman realist"] == 2
    assert rezultat["basm"] == 1

def test_undo_redo():
    undoList = []
    redoList = []
    lista = []

    lista = adaugaVanzare("1", "Ion", "roman", 15, "gold", lista)
    assert len(lista) == 1
    undoList.append(lista)

    lista = adaugaVanzare("2", "Fluturi", "drama", 10, "silver", lista)
    assert len(lista) == 2
    undoList.append(lista)

    lista = adaugaVanzare("3", "Moara cu noroc", "nuvela", 20, "silver", lista)
    assert len(lista) == 3
    undoList.append(lista)

    assert len(undoList) == 3
    redoList.append(lista)
    lista = undoList.pop()
    print(lista)
    assert len(undoList) == 2

    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 1

    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 0
    assert len(redoList) == 3

    redoList = []
    lista.clear()
    lista = adaugaVanzare("1", "Ion", "roman", 15, "gold", lista)
    assert len(lista) == 1
    undoList.append(lista)
    redoList.clear()

    lista = adaugaVanzare("2", "Fluturi", "drama", 10, "silver", lista)
    assert len(lista) == 2
    undoList.append(lista)
    redoList.clear()

    lista = adaugaVanzare("4", "A", "roman realist", 10, "silver", lista)
    undoList.append(lista)
    redoList.clear()
    assert len(redoList) == 0
    assert len(undoList) == 3

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 2
    assert len(undoList) == 1

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 0
    assert len(undoList) == 3

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    lista = adaugaVanzare("5", "B", "comedie", 10, "silver", lista)
    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 2
    assert len(undoList) == 1

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 3
    assert len(undoList) == 0

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 2
    assert len(undoList) == 1

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    if len(redoList) > 0:
        redoList.pop()
    assert len(redoList) == 0