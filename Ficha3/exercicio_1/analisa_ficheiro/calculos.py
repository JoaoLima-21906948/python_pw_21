def calcula_linhas(nome):
    f = open(f"{nome}.txt", "r")
    lines = len(f.readlines())
    f.close()
    return lines

def calcula_caracteres(nome):
    caracteres = 0
    f = open(f"{nome}.txt")
    lines = len(f.readlines())
    f.close()
    with open(f'{nome}.txt') as file:
        for line in file:
            caracteres += len(line)
    caracteres -= lines - 1
    return caracteres

def calcula_palavra_comprida(nome):
    maior = ""
    with open(f'{nome}.txt') as file:
        for line in file:
            words = line.split()
            maiorAtual = max(words, key=len)
            if len(maiorAtual) > len(maior):
                maior = maiorAtual

    return maior

def calcula_ocorrencia_de_letras(nome):
    ocorrencias = {}
    f = open(f"{nome}.txt")
    texto = f.readlines()
    f.close()
    textoStr = ''.join(texto).lower()
    for letra in set(textoStr):
        if letra.isalpha():
            ocorrencias[letra] = textoStr.count(letra)
    return ocorrencias
