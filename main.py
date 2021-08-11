#Guilherme Frutuoso de Almeida
#Número da Matrícula : 508299

#Importando módulo como 'tt' por questões usuabilidade e velocidade
import turtle as tt

# Criando a janela
window = tt.Screen()
# A tartaruga
my_turtle = tt.Turtle()

#Primitivas
def retangulo(dados, largura, altura):
    window.exitonclick()

def poliReg(dados, lado, nlado):
    window.exitonclick()

def triangReto(dados, cateto1, cateto2):
    window.exitonclick()

def circ(dados, raio):
    window.exitonclick()

#Laço principal
while True:
    print("Vamos desenhar uma imagem vetorial!")
    #Se o usuário vai ralmente jogar
    user_decisao = input("Espere, mas você quer realmente jogar?\n"
                         "Se não, digite 'Exit'\n"
                         "Se sim, digite 'Tartaruga': ").capitalize()
    if user_decisao == "Tartaruga":
        esc_primitiva = input("Escolha uma primitiva para comerçarmos o desenho e para parar digite 'Bye'\n"
                              "Para escolher o retângulo digite '1'\n"
                              "Para escolher o poligono regular digite '2'\n"
                              "Para escolher o quadrado digite '3'\n"
                              "Para escolher o triângulo retângulo digite '4'\n").capitalize()
        escPrim_list = list(esc_primitiva)
        while esc_primitiva == "1" or esc_primitiva == "2" or esc_primitiva == "3" or esc_primitiva == "4":
            lista_primitivas = []
            print("Here we go!")
            if esc_primitiva == "1":
                # Inserindo informações dentro do parâmetro dados
                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                #Decisão do usuário por qual orientação seguir
                orientacao = my_turtle
                x = 0
                while x < 4:
                    ori_decisao = input("Qual orientação quer seguir agora? ")
                    ori_valor = float(input("Qual o valor da orientação agora? "))
                    if ori_decisao == "r":
                        orientacao = my_turtle.right(ori_valor)
                        info_largura = float(input("Me diga o valor da largura: "))
                        info_altura = float(input("Me diga a altura: "))
                    if ori_decisao == "l":
                        orientacao = my_turtle.left(ori_valor)
                        info_largura = float(input("Me diga o valor da largura: "))
                        info_altura = float(input("Me diga a altura: "))

                    x+=1

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                Dados = (caneta, posicao, orientacao, cor)


                # Largura e Altura
                Largura = my_turtle.forward(info_largura)

                Altura = my_turtle.forward(info_altura)

                retangulo(Dados, Largura, Altura)
                lista_primitivas.insert(escPrim_list[1])

            if esc_primitiva == "2":
                # Inserindo informações dentro do parâmetro dados
                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                # Decisão do usuário por qual orientação seguir
                orientacao = my_turtle
                x = 0
                while x < 4:
                    ori_decisao = input("Qual orientação quer seguir agora? ")
                    ori_valor = float(input("Qual o valor da orientação agora? "))
                    if ori_decisao == "r":
                        orientacao = my_turtle.right(ori_valor)
                    if ori_decisao == "l":
                        orientacao = my_turtle.left(ori_valor)
                    x += 1

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                Dados = (caneta, posicao, orientacao, cor)

                #Lados e número de lados
                lista_primitivas.insert(escPrim_list[2])

            if esc_primitiva == "3":
                # Inserindo informações dentro do parâmetro dados
                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                # Decisão do usuário por qual orientação seguir
                orientacao = my_turtle
                x = 0
                while x < 4:
                    ori_decisao = input("Qual orientação quer seguir agora? ")
                    ori_valor = float(input("Qual o valor da orientação agora? "))
                    if ori_decisao == "r":
                        orientacao = my_turtle.right(ori_valor)
                    if ori_decisao == "l":
                        orientacao = my_turtle.left(ori_valor)
                    x += 1

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                Dados = (caneta, posicao, orientacao, cor)

                lista_primitivas.insert(escPrim_list[3])

            if esc_primitiva =="4":
                # Inserindo informações dentro do parâmetro dados
                dados_shape = input("Me diga o shape da caneta: ").lower()
                caneta = my_turtle.shape(dados_shape)

                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                # Decisão do usuário por qual orientação seguir
                orientacao = my_turtle
                x = 0
                while x < 4:
                    ori_decisao = input("Qual orientação quer seguir agora? ")
                    ori_valor = float(input("Qual o valor da orientação agora? "))
                    if ori_decisao == "r":
                        orientacao = my_turtle.right(ori_valor)
                    if ori_decisao == "l":
                        orientacao = my_turtle.left(ori_valor)
                    x += 1

                dados_cor = input("Qual a cor de sua preferência? ")
                cor = my_turtle.color(dados_cor)

                Dados = (caneta, posicao, orientacao, cor)

                lista_primitivas.insert(escPrim_list[4])

            quer_cont = input("Quer continuar ou voltar ao menu? ").capitalize()
            if quer_cont == "Sim":
                print("Yeahhhhh")
            if quer_cont == "Nao":
                    break
            if esc_primitiva == "Bye":
                break
            else:
                print("Usuário,por favor,siga as regras...")

    if user_decisao == "Exit":
        print("Valeuuu")
        break
    if user_decisao != "Tartaruga" and user_decisao != "Exit":
        print("Eu falei em romeno com você?? É exit ou tartaruga!!!!!!!!!!!!!!!!")
