import os
import csv
from matplotlib import pyplot as plt


def pede_pasta():
    nome = input("Insira o caminho de uma pasta.\n")
    return nome


def faz_calculos(nome):
    listaFicheiros = os.listdir(nome)
    listaTipoFicheiro = []

    for ficheiro in listaFicheiros:
        if len(ficheiro.split('.')) > 1:
            listaTipoFicheiro.append(f"{ficheiro.split('.')[1]}")

    dic_ficheiros = {tipoFicheiro: {"volume": round(sum([(os.stat(os.path.join(nome, ficheiro)).st_size / 1024)
                                                         for ficheiro in listaFicheiros if len(ficheiro.split('.')) > 1
                                                         if ficheiro.split('.')[1] == tipoFicheiro]), 2),
                                    "quantidade": sum([1 for tipo in listaTipoFicheiro if tipoFicheiro == tipo])}
                     for tipoFicheiro in set(listaTipoFicheiro)}
    return dic_ficheiros


def guarda_resultados():
    with open('resultados.csv', 'w', newline='') as ficheiro:
        campos = ['Extensao', 'Quantidade', 'Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        pasta = faz_calculos(pede_pasta())
        values = list(pasta.values())
        for i in pasta:
            writer.writerow(
                {'Extensao': i, 'Quantidade': values[0]["volume"], 'Tamanho[kByte]': values[1]["quantidade"]})


def faz_grafico_queijos(titulo, resultados):
    values = list(resultados.values())
    lista_valores = []
    for i in range(len(resultados)):
        lista_valores.append(values[i]["volume"])
    plt.pie(lista_valores, labels=resultados.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, resultados):
    values = list(resultados.values())
    lista_valores = []
    for i in range(len(resultados)):
        lista_valores.append(values[i]["quantidade"])

    plt.bar(resultados.keys(), sorted(lista_valores))
    plt.title(titulo)
    plt.show()
