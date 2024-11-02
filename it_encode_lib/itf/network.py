'''input ip address and subnet mask output network id'''
def networkid(address,subnet):
    '''input address [255, 082, 255, 000] subnet [252, 127, 063, 006] list[4][3] '''
    netid = []
    for i in range(4):
        atemp = ""
        stemp = ""
        kaddress = int(address[i])
        ksubnet = int(subnet[i])
        atmp = bin(kaddress).replace("0b","")
        stmp = bin(ksubnet).replace("0b","")
        atemp = "0"*(8-len(atmp))+atmp
        stemp = "0"*(8-len(stmp))+stmp
        addsub = [int(i) and int(j) for (i, j) in zip(atemp, stemp)]
        astemp = ""
        for i in addsub:
            astemp += str(i)
        netid.append(int(astemp,2))
    return netid
