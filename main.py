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

def poliReg(dados, lado, nlados):
    for ld in range(nlados):
        my_turtle.forward(lado)
        if orientacao == "r":
            my_turtle.right(ori_valor / nlados)
        if orientacao == "l":
            my_turtle.left(ori_valor / nlados)

def circulo(dados, raio):
    if orientacao == "r":
        my_turtle.right(ori_valor)
        my_turtle.circle(raio)
    if orientacao == "l":
        my_turtle.left(ori_valor)
        my_turtle.circle(raio)

def triangRet(dados, cateto1, cateto2):
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

#Laço principal
while True:
    print("Vamos desenhar uma imagem vetorial!")
    #Se o usuário vai ralmente jogar
    user_decisao = input("Espere, mas você quer realmente jogar?\n"
                         "Se não, digite 'Exit'\n"
                         "Se sim, digite 'Tartaruga': ").capitalize()
    if user_decisao == "Tartaruga":
        #Definindo o formato da tartaruga antes de escolhermos alguma primitiva
        print("Vamos definir algumas coisas básicas antes de prosseguir")
        dados_shape = input("Me diga o shape da caneta: ").lower()
        caneta = my_turtle.shape(dados_shape)
        dados_cor = input("Qual a cor de sua preferência? ")
        cor = my_turtle.color(dados_cor)
        while True:
            esc_primitiva = input("Escolha uma primitiva para comerçarmos o desenho e para parar digite 'Bye'\n"
                                  "Para escolher o retângulo digite '1'\n"
                                  "Para escolher o poligono regular digite '2'\n"
                                  "Para escolher o círculo digite '3'\n"
                                  "Para escolher o triângulo retângulo digite '4'\n").capitalize()
            if esc_primitiva == "1":
                dados_posXret = float(input("Me diga a posição x da caneta: "))
                dados_posYret = float(input("Me diga a posição y da caneta: "))
                posicaoRet = my_turtle.goto(dados_posXret, dados_posYret)

                ori_valor = float(input("Valor da orientação : "))
                orientacaoRet = input("Orintação: ")

                Largura = float(input("Qual a largura ? "))
                Altura = float(input("Qual a altura ? "))

                tupla_dados = (caneta, posicaoRet, orientacaoRet, cor)
                retangulo(tupla_dados, Largura, Altura)
                lista_primitivas.append([(dados_shape, dados_cor, dados_posXret, dados_posYret, ori_valor, orientacaoRet ), Largura, Altura])

            if esc_primitiva == "2":
                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor = 360
                orientacao = input("Orintação: ")

                num_lados = int(input("Qual o número de lados do nosso polígone? "))
                tam_lado = float(input("O tamanho, por favor? "))

                tupla_dados = (caneta, posicao, orientacao, cor)
                poliReg(tupla_dados, tam_lado, num_lados)
                lista_primitivas.append([tupla_dados, num_lados, tam_lado])

            if esc_primitiva == "3":
                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor = float(input("Valor da orientação : "))
                orientacao = input("Orintação: ")

                valor_raio = float(input("Diga o raio, diga:  "))

                tupla_dados = (caneta, posicao, orientacao, cor)
                circulo(tupla_dados, valor_raio)
                lista_primitivas.append([tupla_dados, valor_raio])

            if esc_primitiva == "4":
                dados_posX = float(input("Me diga a posição x da caneta: "))
                dados_posY = float(input("Me diga a posição y da caneta: "))
                posicao = my_turtle.goto(dados_posX, dados_posY)

                ori_valor1 = float(input("Valor da orientação : "))
                ori_valor2 = float(input("Valor da orientação : "))
                orientacao = input("Orintação: ")

                valor_ctt1 = float(input("Diga o primeiro cateto, digaaa: "))
                valor_ctt2 = float(input("Diga o segundo cateto, digaaa: "))
                hip = float(input("Hipotenusa, por favor: "))

                tupla_dados = (caneta, posicao, orientacao, cor)
                triangRet(tupla_dados, valor_ctt1, valor_ctt2)
                lista_primitivas.append([tupla_dados, valor_ctt1, valor_ctt2, hip])

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