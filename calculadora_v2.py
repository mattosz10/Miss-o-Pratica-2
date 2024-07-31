
saida = ''

def adicao (num1, num2):
    soma = num1 + num2
    return soma

def subracao (num1, num2):
    subracao = num1 - num2
    return subracao

def multiplicacao (num1, num2):
    multiplicacao = num1 * num2
    return multiplicacao

def divisao (num1, num2):
    divisao = num1 / num2
    
    if num1 == 0:
        return print("Não foi possível realizar a divisão po 0")
    elif num1 == '-':
        return divisao
    if num2 == 0:
        return print("Não foi possível fazer a divisão por 0")
    elif num2 == '-':
        return divisao
    
def calculadora (num1, num2, escolha):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    escolha = float(input("Digite sua escolha: 1 para adição - 2 para subtração - 3 para multiplicação - 4 para divisão"))
    if escolha == 1:
        resultado = adicao(num1, num2)
    elif escolha == 2:
        resultado = subracao(num1, num2)
    elif escolha == 3:
        resultado = multiplicacao(num1, num2)
    elif escolha == 4:
        resultado = divisao(num1, num2)
    else:
        print("Escolha inválida")

    print("Resultado da operação escolhida"), resultado
    


    
