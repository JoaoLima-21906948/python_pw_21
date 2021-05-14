import json
from exercicio_1.analisa_ficheiro.calculos import *

def pede_nome():
    ficheiro = False
    while not ficheiro:
        try:
            nome = input("Insira o nome do ficheiro.\n")
            f = open(f"{nome}.txt","r")
            ficheiro = True
            return nome
        except OSError:
            print("Não existe ficheiro com esse nome Try again.\n")

def gera_nome(nome):
    f = open(f"{nome}.txt", "r")
    conteudo_dict = f"O ficheiro tem {calcula_linhas(nome)} linhas" + "  |  "
    conteudo_dict += f"O ficheiro tem {calcula_caracteres(nome)} caracteres" + "  |  "
    conteudo_dict += f"A maior palavra do ficheiro e : {calcula_palavra_comprida(nome)}" + "  |  "
    conteudo_dict += f"Numero de ocorrencias de letras: {calcula_ocorrencia_de_letras(nome)}" + "  |  "
    f.close()
    with open(f'{nome}.json', 'w') as json_file:
        json.dump(conteudo_dict, json_file, indent=4)
