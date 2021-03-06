#Importando módulo como 'tt' por questões usuabilidade e velocidade
import turtle as tt

# Criando a janela
window = tt.Screen()
# A tartaruga
my_turtle = tt.Turtle()

primitivas_lista = []
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
                                  "Para escolher o círculo digite '3'\n"
                                  "Para escolher o triângulo retângulo digite '4'\n").capitalize()
            if esc_primitiva == "1":
                while True:
                    dados_shapeRet = input("Me diga o shape da caneta: ").lower()
                    if dados_shapeRet != "arrow" and dados_shapeRet != "circle" and dados_shapeRet != "classic" and dados_shapeRet != "turtle" and dados_shapeRet != "triangle" and dados_shapeRet != "square":
                        print("Escolha um modo existente no módulo")
                    else:
                        break
                canetaRet = my_turtle.shape(dados_shapeRet)

                dados_posXret = float(input("Me diga a posição x da caneta: "))
                dados_posYret = float(input("Me diga a posição y da caneta: "))
                posicaoRet = my_turtle.goto(dados_posXret, dados_posYret)


                ori_valor = float(input("Valor da orientação : "))
                orientacaoRet = input("Orintação: ")


                dados_corRet = input("Qual a cor de sua preferência? ")
                corRet = my_turtle.color(dados_corRet)

                Largura = float(input("Qual a largura ? "))
                Altura = float(input("Qual a altura ? "))

                dadosRet = (canetaRet, posicaoRet, orientacaoRet, corRet)
                def retangulo(dados, largura, altura):
                    my_turtle.forward(largura)
                    if orientacaoRet == "r":
                        my_turtle.right(ori_valor)
                    if orientacaoRet == "l":
                        my_turtle.left(ori_valor)
                    my_turtle.forward(altura)
                    if orientacaoRet == "r":
                        my_turtle.right(ori_valor)
                    if orientacaoRet == "l":
                        my_turtle.left(ori_valor)
                    my_turtle.forward(largura)
                    if orientacaoRet == "r":
                        my_turtle.right(ori_valor)
                    if orientacaoRet == "l":
                        my_turtle.left(ori_valor)
                    my_turtle.forward(altura)
                retangulo(dadosRet, Largura, Altura)
                primitivas_lista.insert(0, [dados_shapeRet, dados_posXret, dados_posYret, dados_corRet, Largura, Altura])

            if esc_primitiva == "2":
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
                primitivas_lista = primitivas_lista.insert(poligonoReg(Dados, tam_lado, num_lados))

            if esc_primitiva == "3":
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
                print("Voltando ao menu...")
                break
            else:
                print("Por favor user, siga as regras...")
    if user_decisao == "Exit":
        print("Valeuuu")
        break
    if user_decisao != "Tartaruga" and user_decisao != "Exit":
        print("Eu falei em romeno com você?? É exit ou tartaruga!!!!!!!!!!!!!!!!")
print(primitivas_lista)

window.exitonclick()