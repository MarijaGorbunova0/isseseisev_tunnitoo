def loe_failist(fail:str):
    """ Loeme failist read ja salvestame j�rjendisse. Funktsioon
    tagastab j�rjend
    :param str faili
    :rtype: list
    """
    f = open(fail, "r", encoding= "uft-8")#try
    j�rjend = []
    for rida in f:
        j�rjend.append(rida.strip())
    f.close()
    return j�rjend
paevad  = loe_failist("paevad.txt")
print(paevad)