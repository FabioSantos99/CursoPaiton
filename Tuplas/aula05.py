lista_materiais = []
def cadastrarmateriais (nome, codigo, unidade, quantidade):
    tupla = (nome, codigo, unidade, quantidade)
    lista_materiais.append(tupla)
    return lista_materiais

def consultarmateriais (codigo):
    for material in lista_materiais:
        if material(1) == codigo:
            return print(material)
        
        else:
            pass

cadastrarmateriais('Borracha', 1, 'un', 500)
cadastrarmateriais('Lápis', 2, 'un', 500)
print(lista_materiais)

consultarmateriais(1)