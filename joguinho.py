print("***********************************")
print("Bem vindo a um jogo de adivinhaçãoo!")
print("***********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas > 0):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu numero: ")
    print("você digitou ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")
    print("fim do jogo!")
    rodada = rodada + 1