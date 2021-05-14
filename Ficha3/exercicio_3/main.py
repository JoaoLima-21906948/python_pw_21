import os

def pede_pasta():
    while True:
        pathAtual = os.getcwd()
        path = input("Insira o path do ficheiro:")
        if os.path.exists(path):
            return path
        else:
            pathJunto = pathAtual + "\\" + path
            if os.path.exists(pathJunto):
                return pathJunto


def calcula_tamanho_pasta(pasta):
    listaFicheiros = os.listdir(pasta)
    soma = 0

    for ficheiro in listaFicheiros:
        if os.path.isdir(os.path.join(pasta, ficheiro)):
            soma += calcula_tamanho_pasta(os.path.join(pasta, ficheiro))
        elif os.path.isfile(os.path.join(pasta, ficheiro)):
            soma += (os.stat(os.path.join(pasta, ficheiro)).st_size / 1048576)
        else:
            soma += 0
    return soma


def main():
    print(f"{int(calcula_tamanho_pasta(pede_pasta()))} MB")


if __name__ == "__main__":
    main()
