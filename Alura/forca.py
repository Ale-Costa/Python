import random



def jogar_forca():
    
    bem_vindo()
    palavra_secreta = carrega_palavra_secreta()
  
    letra_certa = ["_" for letra in palavra_secreta]
    

    acertou = False
    enforcou = False
    erros = 0

    while not enforcou and not acertou:

        chute = palpite()


        if chute in palavra_secreta:
            marca_chute_certo(chute, palavra_secreta, letra_certa)
        else:
            erros +=1
            desenha_forca(erros)        
        
        enforcou = erros == 7
        acertou = "_" not in letra_certa
        print(letra_certa)


    if acertou:
        msg_vencedor()
    else:
        msg_perdedor(palavra_secreta)

    print("Fim do Jogo\n")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def marca_chute_certo(chute, palavra_secreta, letra_certa):
    
    index = 0

    for letra in palavra_secreta:
        if chute == letra:
            letra_certa[index] = letra
        index += 1

def palpite():

    chute = input("Palpite: ")
    chute = chute.strip().upper()
    return chute

    

def bem_vindo():
    
    print("*********************************")
    print("Bem vindo ao jogo da forca!")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linhas in arquivo:
        linhas = linhas.strip().upper()
        palavras.append(linhas)

    arquivo.close()

    numero = random.randrange(0, len(palavras))


    palavra_secreta = palavras[numero]
    return palavra_secreta

if(__name__ == "__main__"): 
    jogar_forca()
