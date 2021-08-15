#Guilherme Frutuoso de Almeida
#Número da Matrícula : 508299

#Importando módulo como 'tt' por questões usuabilidade e velocidade
import turtle as tt

# Criando a janela
window = tt.Screen()
# A tartaruga
my_turtle = tt.Turtle()

lista_primitivas = []

#Primitivas
def retangulo(dados, largura, altura):
    my_turtle.begin_fill()
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
    my_turtle.end_fill()

def poliReg(dados, lado, nlados):
    my_turtle.begin_fill()
    for ld in range(nlados):
        my_turtle.forward(lado)
        if orientacao == "r":
            my_turtle.right(ori_valor / nlados)
        if orientacao == "l":
            my_turtle.left(ori_valor / nlados)
    my_turtle.end_fill()

def circulo(dados, raio):
    my_turtle.begin_fill()
    if orientacao == "r":
        my_turtle.right(ori_valor)
        my_turtle.circle(raio)
    if orientacao == "l":
        my_turtle.left(ori_valor)
        my_turtle.circle(raio)
    my_turtle.end_fill()

def triangRet(dados, cateto1, cateto2):
    my_turtle.begin_fill()
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
    my_turtle.end_fill()

#Dicionários com as cores e formatos do módulo Turtle
colors = {
    'red' : "red",
    'blue' : "blue",
    'green' : "green",
    'white' : "white",
    'yellow' : "yellow",
    'pink' : "pink",
    'lightblue' : "lightblue",
    'lightgrey' : "lightgrey",
    'grey' : "grey",
    'darkblue': "darkblue",
    'lightgreen': "lightgreen"
}

shape = {
    'turtle': "turtle",
    'circle': "circle",
    'classic': "classic",
    'arrow': "arrow"
}

#Laço principal
while True:
    print("Vamos desenhar uma imagem vetorial!")
    #Se o usuário vai ralmente jogar
    user_decisao = input("Espere, mas você quer realmente jogar?\n"
                         "Se não, digite 'Exit'\n"
                         "Se sim, digite 'Tartaruga': ").capitalize()
    if user_decisao == "Tartaruga":
        #Definindo o formato da tartaruga antes de escolhermos alguma primitiva
        print("Vamos definir o formato de seu cágado antes proseguirmos")
        while True:
            dados_shape = input("Me diga o shape da caneta: ").lower()
            if dados_shape in shape:
                break
            else:
                print("Olhe os formatos !")
                print(shape)
        caneta = my_turtle.shape(dados_shape)
        while True:
            esc_primitiva = input("Escolha uma primitiva para comerçarmos o desenho e para parar digite 'Bye'\n"
                                  "Para escolher o retângulo digite '1'\n"
                                  "Para escolher o poligono regular digite '2'\n"
                                  "Para escolher o círculo digite '3'\n"
                                  "Para escolher o triângulo retângulo digite '4'\n").capitalize()
            if esc_primitiva == "1":
                while True:
                    dados_cor = input("Qual a cor de sua preferência? ")
                    if dados_cor in colors:
                        break
                    else:
                        print("Olhe as cores disponiveis")
                        print(colors)
                cor = my_turtle.fillcolor(dados_cor)

                while True:
                    try:
                        dados_posX = float(input("Me diga a posição x da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        dados_posY = float(input("Me diga a posição Y da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                posicao = my_turtle.goto(dados_posX, dados_posY)

                while True:
                    try:
                        ori_valor = float(input("Valor da orientação : "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    orientacao = input("Orintação('l' para left e 'r' para right): ").lower()
                    if orientacao != "r" and orientacao != "l":
                        print("Sr, l ou r, por favor")
                    else:
                        break

                while True:
                    try:
                        Largura = float(input("Qual a largura ? "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        Altura = float(input("Qual a altura ? "))
                        break
                    except:
                        print("Isso não é um número")

                tupla_dados = (caneta, posicao, orientacao, cor)
                retangulo(tupla_dados, Largura, Altura)
                lista_primitivas.append([(dados_shape, dados_cor, dados_posX, dados_posY, ori_valor, orientacao), Largura, Altura])

            if esc_primitiva == "2":
                while True:
                    dados_cor = input("Qual a cor de sua preferência? ")
                    if dados_cor in colors:
                        break
                    else:
                        print("Olhe as cores disponiveis")
                        print(colors)
                cor = my_turtle.fillcolor(dados_cor)

                while True:
                    try:
                        dados_posX = float(input("Me diga a posição x da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        dados_posY = float(input("Me diga a posição Y da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor = 360

                while True:
                    orientacao = input("Orintação('l' para left e 'r' para right): ").lower()
                    if orientacao != "r" and orientacao != "l":
                        print("Sr, l ou r, por favor")
                    else:
                        break

                num_lados = int(input("Qual o número de lados do nosso polígone? "))
                tam_lado = float(input("O tamanho, por favor? "))

                tupla_dados = (caneta, posicao, orientacao, cor)
                poliReg(tupla_dados, tam_lado, num_lados)
                lista_primitivas.append([(dados_shape, dados_cor, dados_posX, dados_posY, ori_valor, orientacao), num_lados, tam_lado])

            if esc_primitiva == "3":
                while True:
                    dados_cor = input("Qual a cor de sua preferência? ")
                    if dados_cor in colors:
                        break
                    else:
                        print("Olhe as cores disponiveis")
                        print(colors)
                cor = my_turtle.fillcolor(dados_cor)

                while True:
                    try:
                        dados_posX = float(input("Me diga a posição x da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        dados_posY = float(input("Me diga a posição Y da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                posicao = my_turtle.goto(dados_posX, dados_posY)

                while True:
                    try:
                        ori_valor = float(input("Valor da orientação : "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    orientacao = input("Orintação('l' para left e 'r' para right): ").lower()
                    if orientacao != "r" and orientacao != "l":
                        print("Sr, l ou r, por favor")
                    else:
                        break
                while True:
                    try:
                        valor_raio = float(input("Diga o raio, diga:  "))
                        break
                    except:
                        print("Isso não é um número")

                tupla_dados = (caneta, posicao, orientacao, cor)
                circulo(tupla_dados, valor_raio)
                lista_primitivas.append([(dados_shape, dados_cor, dados_posX, dados_posY, ori_valor, orientacao), valor_raio])

            if esc_primitiva == "4":
                while True:
                    dados_cor = input("Qual a cor de sua preferência? ")
                    if dados_cor in colors:
                        break
                    else:
                        print("Olhe as cores disponiveis")
                        print(colors)
                cor = my_turtle.fillcolor(dados_cor)

                while True:
                    try:
                        dados_posX = float(input("Me diga a posição x da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        dados_posY = float(input("Me diga a posição Y da caneta: "))
                        break
                    except:
                        print("Isso não é um número")
                posicao = my_turtle.goto(dados_posX, dados_posY)

                while True:
                    try:
                        ori_valor1 = float(input("Valor da orientação : "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        ori_valor2 = float(input("Valor da orientação : "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    orientacao = input("Orintação('l' para left e 'r' para right): ").lower()
                    if orientacao != "r" and orientacao != "l":
                        print("Sr, l ou r, por favor")
                    else:
                        break

                while True:
                    try:
                        valor_ctt1 = float(input("Diga o primeiro cateto, digaaa: "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        valor_ctt2 = float(input("Diga o segundo cateto, digaaa: "))
                        break
                    except:
                        print("Isso não é um número")
                while True:
                    try:
                        hip = float(input("Hipotenusa, por favor: "))
                        break
                    except:
                        print("Isso não é um número")

                tupla_dados = (caneta, posicao, orientacao, cor)
                triangRet(tupla_dados, valor_ctt1, valor_ctt2)
                lista_primitivas.append([(dados_shape, dados_cor, dados_posX, dados_posY, ori_valor1, ori_valor2, orientacao), valor_ctt1, valor_ctt2, hip])

            if esc_primitiva == "Bye":
                print("Voltando ao menu...")
                break
            else:
                print("Por favor user, siga as regras...")
    if user_decisao == "Exit":
        print("Valeuuu")
        break
    if user_decisao != "Tartaruga" and user_decisao != "Exit":
        print("Eu falei em romeno com você?? É exit ou tartaruga!!!!!!!!!!!!!!!")
window.exitonclick()
print(lista_primitivas)