from math import factorial
from operator import truediv
from random import randint


listaProgramas = ["calculadora", "cat", "texto aleatório", "sair"]
primeira_vez = True

def sair() :
    return

def guardarArquivo(texto) :
    arquivo = open(input("Qual é o nome do arquivo? Se tiver um arquivo com o mesmo nome, o arquivo será apagado: "), "w")
    arquivo.write(str(texto))

def calculadora() :
    listaOperacoes = ["soma","subtetração", "mutiplicação", "divisão", "porcentagem", "módulo", "expoente", "raiz quadrada", "raiz cúbica", "média", "maior", "menor", "factorial"]
    igual = "="*18
    print(igual)
    print("escolha a operação")
    print(igual)
  
    # escreve as operações para o console

    for i in range(len(listaOperacoes)):
        if i < 9:
            iponto = str(i+1) + ". "
        else:
            iponto = str(i+1) + "."
        print(iponto, listaOperacoes[i])
    op = 0;  

    # escolhe a operação na calculadora

    while True:
        op = input("Qual é a operação? ")
        
        if op.isnumeric() :
            iop = int(op)-1
            if op.isnumeric() and int(op) <= len(listaOperacoes)+1:
                break
        print("\u001b[31m erro: operação inválida\u001b[0m")

    # input dos números 

    n1 = int(input("Qual é o primeiro número: "))
    if listaOperacoes[iop] != "raiz quadrada" and listaOperacoes[iop] != "raiz cúbica" and listaOperacoes[iop] != "factorial":
        n2 = int(input("Qual é o segundo número: "))

    guardar = input("Queres grardar o resultado para um arquivo? [Y/N] : ").strip().upper()
    print()

    # executa a operação e escreve o resultado para o console

    texto = 0
    resultado = 0

    if iop == 0:
        resultado = n1+n2
        texto ="A soma entre {} e {} é {} ".format(n1,n2,resultado)
    elif iop == 1:
        resultado = n1-n2
        texto = "A difrença entre {} e {} é {}".format(n1,n2,resultado)
    elif iop == 2:
        resultado = n1*n2
        texto = "O produto entre {} e {} é {}".format(n1,n2, resultado)
    elif iop == 3:
        resultado = n1/n2
        texto = "O quociente entre {} e {} é {}".format(n1,n2,resultado)
    elif iop == 4:
        resultado = n1*(100/n2)
        texto = "{} porcento de {} é {}".format(n1,n2,resultado)
    elif iop == 5:
         resultado = n1%n2
         texto ="{} módulo de {} é {}".format(n1,n2,resultado)
    elif iop == 6:
        resultado = n1**n2
        texto = "{} elevado a {} é {}".format(n1,n2,resultado)
    elif iop == 7:
        resultado = n1**0.5
        texto = "A raiz quadrada de {} é {}".format(n1,resultado)
    elif iop == 8:
        resultado = n1**(1/3)
        texto = "A raiz cúbica de {} é {}".format(n1,)
    elif iop == 9:
        resultado = (n1+n2)/2
        texto = "A média entre {} e {} é {}".format(n1,n2,resultado)
    elif iop == 10:
        resultado = (max(n1,n2))
        texto = "Entre {} e {}, o maior é {}".format(n1,n2,resultado)
    elif iop == 11:
        resultado = min(n1,n2)
        texto = "Entre {} e {}, o menor é ".format(n1,n2,)
    elif iop == 12:
        resultado = factorial(n1)
        texto = "{} factorial é {}".format(n1,resultado)
    else:
        print("Isso não devia acontecer")

    # escreve o resultado para o terminal e guarda o resultado para um arquivo se o usário pediu  

    print(texto)
    print("\n")
    if guardar == "Y":
        guardarArquivo(resultado)
   
    # volta para o início do programa

    return inicio()


    


def cat() :
    print(input("cat: "))
    return inicio()


def texto_aleatorio() :
    for i in range(int(input("Quantos caracteres queres que o texto tenha?: "))):
        try:
            print(chr(randint(0,0x10FFFD)),end="")
        except:
            0
    print()
    return inicio()

def inicio(): 
            # iniacialização
            print("\n")
            igual = "=" * 19
            print(igual)
            print("escolha a aplicação")
            print(igual,"")

            # escreve os programas para o console
            for i in range(len(listaProgramas)):
                iponto = str(i+1) + ". "
                print(iponto,  listaProgramas[i])

            # escolhe o programa na suite

            escolha = input("Qual é a aplicação que queres usar: ")
            if escolha.isnumeric() and int(escolha) <= len(listaProgramas)+1:
                if escolha == "1" :
                    calculadora()
                elif escolha == "2" :
                    cat()
                elif escolha == "3" :
                    texto_aleatorio()
                elif escolha != "4" :
                    inicio()
            else :
                print("\033[;31;m erro: operação inválida\033[;;;m")
                inicio()

if primeira_vez:
    primeira_vez = False
    a = inicio()

