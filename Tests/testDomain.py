from Domain.librarie import creeazaVanzare, getId, getTitlucarte, getGencarte, getPret, getTipReducere


def testVanzare():
    vanzare = creeazaVanzare(1, "Harap-Alb", "Basm", 15, "None")
    assert getId(vanzare) == 1
    assert getTitlucarte(vanzare) == "Harap-Alb"
    assert getGencarte(vanzare) == "Basm"
    assert getPret(vanzare) == 15
    assert getTipReducere(vanzare) == "None"