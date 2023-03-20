from Tests.testCRUD import testAdaugaVanzare, testStergeVanzare, testModificaVanzare
from Tests.testDomain import testVanzare
from Tests.testfunctionalitati import testModificareGen, testdiscountptrreducere, testpretminim, testordonare, \
    testnumar_titluri, test_undo_redo


def runAllTests():
    testVanzare()
    testAdaugaVanzare()
    testModificareGen()
    testdiscountptrreducere()
    testStergeVanzare()
    testModificaVanzare()
    testpretminim()
    testordonare()
    testnumar_titluri()
    test_undo_redo()