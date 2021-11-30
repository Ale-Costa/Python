from os import close


print("Ola seja bem vindo!!!\nEscolha uma das opções abaixo.\n1) Abrir um arquivo\n2) Abrir e ler um arquivo\n3) Fechar o programa")

codigo = input(": ")

def abrirArquivo():

    arquivo = input("Digite o nome do arquivo que deseja abrir: ")

    ##open(arquivo, 'r')
    ##close()
    print(arquivo+" lido com sucesso")
    print("Fim.")



def lerArquivo():

    arquivo = input("Digite o nome do arquivo que deseja abrir: ")

    meuArquivo = open(arquivo, 'r')
    print(meuArquivo.read())
    print("Fim.")



if codigo == "1":
    abrirArquivo()

elif codigo == "2":
    lerArquivo()

elif codigo == "3":
    print("Fim.")

else:   
    print("Codigo Invalido.")