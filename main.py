from Domain.librarie import creeazaVanzare
from Logic.CRUD import adaugaVanzare
from Tests.testALL import runAllTests
from UserInterface.console import runMenu
from UserInterface.fisiernou import comenzi


def main():
    runAllTests()
    lista = []
    lista = adaugaVanzare(1, "Harap-Alb", "Basm", 15.0, "none",lista)
    lista = adaugaVanzare(2, "Ion", "Roman", 10.0, "none", lista)
    runMenu(lista)
    comenzi(lista)
if __name__ == '__main__':
    main()