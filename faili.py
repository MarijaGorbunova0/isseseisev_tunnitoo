def loe_failist(fail:str):
    """ Loeme failist read ja salvestame järjendisse. Funktsioon
    tagastab järjend
    :param str faili
    :rtype: list
    """
    f = open(fail, "r", encoding= "uft-8")#try
    järjend = []
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
paevad  = loe_failist("paevad.txt")
print(paevad)