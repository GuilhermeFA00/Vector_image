import turtle as tt

window = tt.Screen()

tarta = tt.Turtle()



while True:
    primitivas_lista = []
    print("Vamos desenhar uma imagem vetorial!")
    # Se o usuário vai ralmente jogar
    user_decisao = input("Espere, mas você quer realmente jogar?\n"
                         "Se não, digite 'Exit'\n"
                         "Se sim, digite 'Tartaruga': ").capitalize()
    if user_decisao == "Tartaruga":
        print("Vamos definir algumas coisas básicas antes de prosseguir")
        dados_shape = input("Me diga o shape da caneta: ").lower()
        caneta = tarta.shape(dados_shape)
        dados_cor = input("Qual a cor de sua preferência? ")
        cor = tarta.color(dados_cor)
        primitivas_lista.append([])


        while True:
            esc_primitiva = input("Escolha uma primitiva para comerçarmos o desenho e para parar digite 'Bye'\n"
                                  "Para escolher o retângulo digite '1'\n"
                                  "Para escolher o poligono regular digite '2'\n"
                                  "Para escolher o círculo digite '3'\n"
                                  "Para escolher o triângulo retângulo digite '4'\n").capitalize()
            if esc_primitiva == "1":
                dados_posXret = float(input("Me diga a posição x da caneta: "))
                dados_posYret = float(input("Me diga a posição y da caneta: "))
                posicaoRet = tarta.goto(dados_posXret, dados_posYret)

                ori_valor = float(input("Valor da orientação : "))
                orientacaoRet = input("Orintação: ")

                Largura = float(input("Qual a largura ? "))
                Altura = float(input("Qual a altura ? "))

                tupla_dados = (caneta, posicaoRet, orientacaoRet, cor)
                def retangulo(dados, largura, altura):
                    tarta.forward(largura)
                    if orientacaoRet == "r":
                        tarta.right(ori_valor)
                    if orientacaoRet == "l":
                        tarta.left(ori_valor)
                    tarta.forward(altura)
                    if orientacaoRet == "r":
                        tarta.right(ori_valor)
                    if orientacaoRet == "l":
                        tarta.left(ori_valor)
                    tarta.forward(largura)
                    if orientacaoRet == "r":
                        tarta.right(ori_valor)
                    if orientacaoRet == "l":
                        tarta.left(ori_valor)
                    tarta.forward(altura)
                retangulo(tupla_dados, Largura, Altura)
                primitivas_lista.append([])
            if esc_primitiva == "Bye":
                print("Voltando ao menu...")
                break
            else:
                print("Por favor user, siga as regras...")
    if user_decisao == "Exit":
        print("Valeuuu")
        break
    if user_decisao != "Tartaruga" and user_decisao != "Exit":
        print("Eu falei em romeno com você?? É exit ou tartaruga!!!!!!!!!!!!!!!!")

window.exitonclick()