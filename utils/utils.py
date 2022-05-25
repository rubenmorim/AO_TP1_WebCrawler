def parse_preco(preco):
    if preco is not None:
        stringPreco = ''.join(filter(str.isdigit, preco))
        return int(stringPreco)
    else:
        return 0

