def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou= False
    acertou = False
    erros = 0

    #enquanto não enforcou E não acertou
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = erros +1
        else:
            erros = erros + 1
        enforcou = erros == 6

        print(letras_acertadas)




    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
