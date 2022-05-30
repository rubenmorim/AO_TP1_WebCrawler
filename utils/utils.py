def parse_preco(preco):
    if preco is not None:
        stringPreco = ''.join(filter(str.isdigit, preco))
        return int(stringPreco)
    else:
        return 0


def parseType(type):
    if type is None:
        return "No Type"

    return type
