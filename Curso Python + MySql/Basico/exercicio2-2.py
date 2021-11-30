
arquivo = input("Digite o nome do arquivo que deseja abrir: ")

meuArquivo = open(arquivo, 'r')
print(meuArquivo.read())