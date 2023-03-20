from Domain.librarie import getId, getTitlucarte, getGencarte, getPret, getTipReducere
from Logic.CRUD import adaugaVanzare, getById, stergeVanzare, modificaVanzare


def testAdaugaVanzare():
    lista = []
    lista = adaugaVanzare(1, "Harap-Alb", "Basm", 15,"silver",lista)
    assert getId(getById(1,lista)) == 1
    assert getTitlucarte(getById(1,lista)) == "Harap-Alb"
    assert getGencarte(getById(1,lista)) == "Basm"
    assert getPret(getById(1,lista)) == 15
    assert getTipReducere(getById(1,lista)) == "silver"

def testStergeVanzare():
    lista = []
    lista = adaugaVanzare(1, "Harap-Alb", "Basm", 15, "none",lista)
    lista = adaugaVanzare(2, "Ion", "Roman", 10, "none", lista)
    lista = stergeVanzare(1,lista)
    assert len(lista) == 1
    assert getById(1, lista) is None
    assert getById(2, lista) is not None


def testModificaVanzare():
    lista = []
    lista = adaugaVanzare(1, "Harap-Alb", "Basm", 15, "none",lista)
    lista = adaugaVanzare(2, "Ion", "Roman", 10, "none", lista)
    lista = modificaVanzare(2, "Ion", "Roman realist", 10, "gold", lista)
    vanzarenoua = getById(2,lista)
    assert getId(vanzarenoua) == 2
    assert getTitlucarte(vanzarenoua) == "Ion"
    assert getGencarte(vanzarenoua) == "Roman realist"
    assert getPret(vanzarenoua) == 10
    assert getTipReducere(vanzarenoua) =="gold"
