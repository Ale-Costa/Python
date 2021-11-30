import random
def jogar_adv():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,31)
    tentativas = 0
    rodada = 1
    pontos = 100


    print(" Selecione um nivel ")
    print(" (1) Facil (2) Moderado (3) Dificil ")
    nivel = int(input())

    if nivel == 1:
        tentativas = 7
    elif nivel == 2:
        tentativas = 5
    else:
        tentativas = 3

    print(3 // 2)

    for rodada in range(1, tentativas +1):
                print("\nTentativas {} de {}".format(rodada,tentativas))
                chute_str = int(input("Digite um numero entre 1 e 30: "))
                print("Voce digitou: ",chute_str)
                #chute = (int(chute_str))

                if (chute_str < 1 or chute_str > 30):
                    print("Voce deve digitar um numero entre 1 e 30!! Tente novamente.")
                    continue 
                acertou = chute_str == numero_secreto
                maior   = chute_str > numero_secreto
                menor   = chute_str < numero_secreto


                if (acertou):
                    print("Voce acertou e fez {} pontos".format(pontos))
                    break
                else:
                    if (menor):
                        print("O numero secreto é maior !!!")
                    elif (maior):
                        print("O numero secreto é menor !!!")
                    
                    pontos_perdidos = abs(numero_secreto - chute_str)
                    pontos = pontos - pontos_perdidos

    print("\nO numero secreto era {}.".format(numero_secreto))
    print("Fim do Jogo\n")
if(__name__ == "__main__"): 
    jogar_adv()