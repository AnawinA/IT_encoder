'''parity bits'''
def parity_even_bit(data):
    '''evenbit'''
    dat = str(data)
    sum_dat = 0
    for i in dat:
        sum_dat += int(i)
    if not sum_dat %2:
        dat += "0"
    else:
        dat += "1"
    return dat

def parity_dff_bit(data):
    '''odd bit'''
    dat = str(data)
    sum_dat = 0
    for i in dat:
        sum_dat += int(i)
    if not sum_dat %2:
        dat += "1"
    else:
        dat += "0"
    return dat
