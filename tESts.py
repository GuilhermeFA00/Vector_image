#Importando módulo como 'tt' por questões usuabilidade e velocidade
import turtle as tt


#Laço principal
while True:
    print("Vamos desenhar uma imagem vetorial!")
    #Se o usuário vai ralmente jogar
    user_decisao = input("Espere, mas você quer realmente jogar?\n"
                         "Se não, digite 'Exit'\n"
                         "Se sim, digite 'Tartaruga': ").capitalize()
    if user_decisao == "Tartaruga":
        while True:
            esc_primitiva = input("Escolha uma primitiva para comerçarmos o desenho e para parar digite 'Bye'\n"
                                  "Para escolher o retângulo digite '1'\n"
                                  "Para escolher o poligono regular digite '2'\n"
                                  "Para escolher o quadrado digite '3'\n"
                                  "Para escolher o triângulo retângulo digite '4'\n").capitalize()
            if esc_primitiva == "1":
                # Criando a janela
                window = tt.Screen()
                # A tartaruga
                my_turtle = tt.Turtle()

                while True:
                    dados_shape = input("Me diga o shape da caneta: ").lower()
                    if dados_shape != "arrow" and dados_shape != "circle" and dados_shape != "classic" and dados_shape != "turtle" and dados_shape != "triangle" and dados_shape != "square":
                        print("Escolha um modo existente no módulo")
                    else:
                        break
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor = float(input("Valor da orientação : "))
                orientacao = input("Orintação: ")

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                Largura = float(input("Qual a largura ? "))
                Altura = float(input("Qual a altura ? "))

                Dados = (caneta, posicao, orientacao, cor)
                def retangulo(dados, largura, altura):
                    my_turtle.forward(largura)
                    if orientacao == "r":
                        my_turtle.right(ori_valor)
                    if orientacao == "l":
                        my_turtle.left(ori_valor)
                    my_turtle.forward(altura)
                    if orientacao == "r":
                        my_turtle.right(ori_valor)
                    if orientacao == "l":
                        my_turtle.left(ori_valor)
                    my_turtle.forward(largura)
                    if orientacao == "r":
                        my_turtle.right(ori_valor)
                    if orientacao == "l":
                        my_turtle.left(ori_valor)
                    my_turtle.forward(altura)

                    window.exitonclick()
                retangulo(Dados, Largura, Altura)

            if esc_primitiva == "2":
                # Criando a janela
                window = tt.Screen()
                # A tartaruga
                my_turtle = tt.Turtle()

                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor = 360
                orientacao = input("Orintação: ")

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                num_lados = int(input("Qual o número de lados do nosso polígone? "))
                tam_lado = float(input("O tamanho, por favor? "))

                Dados = (caneta, posicao, orientacao, cor)
                def poligonoReg(dados, lado, nlados):
                    for ld in range(nlados):
                        my_turtle.forward(lado)
                        if orientacao == "r":
                            my_turtle.right(ori_valor / nlados)
                        if orientacao == "l":
                            my_turtle.left(ori_valor / nlados)
                poligonoReg(Dados, tam_lado, num_lados )

            if esc_primitiva == "3":
                # Criando a janela
                window = tt.Screen()
                # A tartaruga
                my_turtle = tt.Turtle()

                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor = float(input("Valor da orientação : "))
                orientacao = input("Orintação: ")

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                valor_raio = float(input("Diga o raio, diga:  "))

                Dados = (caneta, posicao, orientacao, cor)

                def circulo(dados, raio):
                    if orientacao == "r":
                        my_turtle.right(ori_valor)
                        my_turtle.circle(raio)
                    if orientacao == "l":
                        my_turtle.left(ori_valor)
                        my_turtle.circle(raio)
                circulo(Dados, valor_raio)

            if esc_primitiva == "4":
                # Criando a janela
                window = tt.Screen()
                # A tartaruga
                my_turtle = tt.Turtle()

                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor1 = float(input("Valor da orientação : "))
                ori_valor2 = float(input("Valor da orientação : "))
                orientacao = input("Orintação: ")

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                valor_ctt1 = float(input("Diga o primeiro cateto, digaaa: "))
                valor_ctt2 = float(input("Diga o segundo cateto, digaaa: "))
                hip = float(input("Hipotenusa, por favor: "))

                Dados = (caneta, posicao, orientacao, cor)

                def trianguloRet(dados, cateto1, cateto2):
                    if hip > valor_ctt1 and hip > valor_ctt2:
                        if orientacao == "r":
                            my_turtle.forward(cateto1)
                            my_turtle.right(ori_valor1)
                            my_turtle.forward(cateto2)
                            my_turtle.right(ori_valor2)
                            my_turtle.forward(hip)
                        if orientacao == "l":
                            my_turtle.forward(cateto1)
                            my_turtle.left(ori_valor1)
                            my_turtle.forward(cateto2)
                            my_turtle.left(ori_valor2)
                            my_turtle.forward(hip)
                    else:
                        print("Bicho, tu estudou matemática em marte? Hipotesuna > qualquer cateto")
                trianguloRet(Dados, valor_ctt1, valor_ctt2)

            if esc_primitiva == "Bye":
                print("Voltando ao menu")
                break
            else:
                print("Por favor user, siga as regras...")

    if user_decisao == "Exit":
        print("Valeuuu")
        break
    if user_decisao != "Tartaruga" and user_decisao != "Exit":
        print("Eu falei em romeno com você?? É exit ou tartaruga!!!!!!!!!!!!!!!!")