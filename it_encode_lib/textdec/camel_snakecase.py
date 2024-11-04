"""to camel case and snake case"""

def toCamelCase(str_snake, delimiter='_'):
    """camel"""
    if delimiter == '':
        delimiter = '_'
    init, *temp = str_snake.split(delimiter)
    res = ''.join([init.lower(), *map(str.title, temp)])
    return res

def to_snakecase(strCamel, delimiter='_'):
    """snake"""
    if delimiter == '':
        delimiter = '_'
    return ''.join([delimiter+i.lower() if i.isupper() 
        else i for i in strCamel]).lstrip(delimiter)
