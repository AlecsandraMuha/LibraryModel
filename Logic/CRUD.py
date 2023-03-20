from Domain.librarie import getId, creeazaVanzare, getPret, getTipReducere


def adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere, lista):
    '''
    adauga o vanzare noua in lista
    :param id: id carte, string
    :param titlucarte: titlul cartii, string
    :param gencarte: genul cartii , string
    :param pret: pretul cartii, float
    :param tipreducere: tipul reducerii, string
    :param lista: lista de vanzari de carti
    :return: lista noua, modificata
    '''
    vanzare = creeazaVanzare(id, titlucarte, gencarte, pret, tipreducere)
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if getPret(vanzare) < 0:
        raise ValueError("pretul nu poate fi negativ! ")
    if getTipReducere(vanzare) != "gold" and getTipReducere(vanzare) != "silver"and getTipReducere(vanzare) != "none":
        raise ValueError("Nu exista acest tip de reducere!")



    return lista + [vanzare]

def stergeVanzare(id, lista):
    '''
    sterge o vanzare din lista
    :param id: id carte, string
    :param titlucarte: titlul cartii, string
    :param gencarte: genul cartii , string
    :param pret: pretul cartii, float
    :param tipreducere: tipul reducerii, string
    :param lista: lista de vanzari de carti
    :return: lista noua, modificata
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    return [vanzare for vanzare in lista if getId(vanzare) != id]
def modificaVanzare(id, titlucarte, gencarte, pret, tipreducere, lista):
    '''
    modifica vanzarea unei carti
    :param id: id carte
    :param titlucarte: titlu carte
    :param gencarte: gen carte
    :param pret: pret carte
    :param tipreducere: tipul reducerii
    :param lista: lista de vanzari
    :return: o lista noua modificata de vanzari
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    listanoua = []
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzarenoua = creeazaVanzare(id, titlucarte, gencarte, pret, tipreducere)
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)
    return listanoua
def getById(id,lista):
    '''

    :param id:
    :param lista:
    :return:
    '''
    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None

