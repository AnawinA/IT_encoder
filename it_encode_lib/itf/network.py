'''input ip address and subnet mask output network id'''
def networkid(address, subnet):
    '''input address [255, 082, 255, 000] subnet [252, 127, 063, 006] list[4][3] '''
<<<<<<< HEAD
=======
    address = address.replace("[", '').replace("]", '').split(",")
    subnet = subnet.replace("[", '').replace("]", '').split(",")
>>>>>>> 5bd696d18076aee405ca3352e43d59ac4ad0ed71
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
<<<<<<< HEAD
=======
# print(networkid([161,246,38,35],[255,255,0,128]))
>>>>>>> 5bd696d18076aee405ca3352e43d59ac4ad0ed71
