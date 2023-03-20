def creeazaVanzare(id, titlucarte, gencarte, pret, tipreducere):
    '''
    creeaza o vanzare dintr-o librarie
    :param id: int
    :param titlucarte: string
    :param gencarte: string
    :param pret: float
    :param tipreducere: string
    :return: un dictionar ce retine o vanzare a unei librarii
    '''
    return {
        "id": id,
        "titlucarte": titlucarte,
        "gencarte": gencarte,
        "pret": pret,
        "tipreducere": tipreducere
    }
def getId(vanzare):
    '''
    ia id-ul unei vanzari
    :param vanzare: dictionar de tipul vanzare
    :return: id-ul vanzarii
    '''
    return vanzare["id"]

def getTitlucarte(vanzare):
    '''
    ia titlul unei carti
    :param vanzare: dictionar de tipul vanzare
    :return: titlul unei carti
    '''
    return vanzare["titlucarte"]

def getGencarte(vanzare):
    return vanzare["gencarte"]

def getPret(vanzare):
    return vanzare["pret"]

def getTipReducere(vanzare):
    return vanzare["tipreducere"]
def toString(vanzare):
    return "id: {}, titlu carte: {}, gen carte: {}, pret: {}, tip reducere: {}".format(
        getId(vanzare),
        getTitlucarte(vanzare),
        getGencarte(vanzare),
        getPret(vanzare),
        getTipReducere(vanzare)
    )
