"""Temperature"""

def c_to_f(c):
    """Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def c_to_k(c):
    """Celsius to Kelvin"""
    return c + 273.15

def c_to_r(c):
    """Celsius to Rankine"""
    return (c * 9/5) + 491.67

def all_to_c(x, type_in):
    """All to Celsius"""
    expression = 0
    if type_in == "F":
        expression = (x - 32) * 5/9
    elif type_in == "K":
        expression = x - 273.15
    elif type_in == "R":
        expression = (x - 491.67) * 5/9
    return expression

def temperature(temp: float, type_temp="C", to_type="F"):
    """Temperature"""
    type_temp = type_temp.strip().upper()
    to_type = to_type.strip().upper()
    c_temp = temp
    if type_temp != "C":
        c_temp = all_to_c(temp, type_temp)
    new_temp = c_temp
    if to_type == "F":
        new_temp = c_to_f(c_temp)
    elif to_type == "K":
        new_temp = c_to_k(c_temp)
    elif to_type == "R":
        new_temp = c_to_r(c_temp)
    return new_temp
