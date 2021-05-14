from analise_pasta import *


def main():
    nome = pede_pasta()
    resultados = faz_calculos(nome)
    faz_grafico_barras(nome,resultados)
    faz_grafico_queijos(nome,resultados)


if __name__ == "__main__":
    main()