def contar_ate_n():
    num = int(input("Olá, favor inserir um número: "))
    i = 1
    while i in range(num+1):
        print(i)
        i += 1

def contar_ate_n_regressivo():
    num = int(input("Olá, favor inserir um número: "))
    while num >= 1:
        print(num)
        num -= 1

def contar_regressivo_voo_liberado():
    num = int(input("Olá, favor inserir um número: "))
    while num >= 1:
        print(num)
        num -= 1
    print("Liberado o vôo!")

def soma_acumuladora():
    i = 0
    soma = 0
    while i <= 10:
        soma = soma + (1 * i)
        i += 1
    print(soma)

def calc_soma():
    i = 0
    soma = 0
    while i <= 5:
        num = int(input("Favor inserir um número: "))
        soma += num
        i += 1
    print(soma)

def calc_soma_0_to_break():
    soma = 0
    num = ""
    while num != 0:
        num = int(input("Favor inserir um número: "))
        soma += num
    print(f"A soma total é {soma}")

def pedir_senha():
    senha = input("Favor inserir senha: ")
    while senha != "batatinha123":
        senha = input("Favor inserir a senha correta: ")
    print("Acesso liberado!")

def numer_digitos():
    num = int(input("Favor inserir um número: "))
    i = 1
    while num / 10 > 1:
        num = num / 10
        i +=1
    print(i)

def fatorial_while():
    num = int(input("Inserir número: "))
    i = num
    while i > 1:
        fatorial = num * (i-1)
        num = fatorial
        i -= 1
    print(num)

def ate_negativo():
    num = int(input("Favor inserir número, digite um número negativo para sair: "))
    i = 0
    while num >= 0:
        num = int(input("Favor inserir outro número: "))
        i += 1
    print(f"A quantidade de números positivos foi de {i}")

def num_primo():
    num = int(input("Favor inserir um número: "))
    i = 2
    while i in range(num):
        if num % i == 0:
            print(f"O número {num} não é primo!")
            break
        else:
            print(f"O número {num} é primo")
            break

def ano_novo():
    i = 11
    while i > 0:
        i -= 1
        print(i)
    print("Feliz ano novo!")

def media_notas():
    i = 1
    nf = 0
    while True:
        nota = int(input("Favor inserir nota: "))
        if nota > 0:
            nf = nf + nota
            i += 1
            print (nf)
        else:
            media = nf / i
            print(f"A média dos alunos é {media}")
            break

def soma_digitos():
    num = int(input("Favor inserir um número: "))
    soma = 0
    while num / 10 > 1:
        resto = num % 10
        soma = soma + resto
        num = num // 10
    print(soma)

def caixa_eletronico():
    deposito = int(input("Favor inserir um valor: "))
    saldo = 0 + deposito
    while deposito != 0:
        deposito = int(input("Inserir um novo valor: "))
        saldo = saldo + deposito
    print(f"Saldo final: {saldo}R$")

def exibir_amplitude():
    i = 0
    for i in range (1, 11):
        print(i)
        i += 1
    
def exibir_amplitude_negativa():
    i = 0
    for i in range (10, 0, -1):
        print(i)
        i += 1

def exibir_pares():
    i = 0
    for i in range(0, 20, 2):
        print(i)
        i += 2

def exibir_impares():
    i = 1
    for i in range(1, 20, 2):
        print(i)
        i += 2

def soma_inteiros_0a100():
    i = 0
    soma = 0
    for i in range(101):
        soma += i
        i += 1
    print(soma)

def fatorial_for():
    num = int(input("Inserir número: "))
    i = num
    soma = 1
    for i in range(num, 0, -1):
        fatorial = soma * (i)
        soma = fatorial
    print(soma)

def tabela_tabuada():
    num = int(input("Favor inserir um número: "))
    for i in range(1, 11, 1):
        print(f"{num}x{i}={num*i}")
    
def tabuada_completa():
    for i in range(1, 11, 1):
        for b in range (1, 11, 1):
            print(f"{i}x{b}={i*b}")

def pares_ate50():
    contador = 0
    for i in range(0, 51, 2):
        contador += 1
    print(contador)

def soma_pares_ate100():
    soma = 0
    for i in range(0, 101, 2):
        soma += i
    print(soma)

def media_entre5():
    nota = 0
    for i in range(1, 6):
        nota += int(input("Favor inserir uma nota "))
    print(f"A média final é de {nota/5}")

def multiplos_de3():
    for i in range(0, 61, 3):
        print(i)

def tabela_celsius_fahrenheit():
    for i in range (0, 100, 10):
        print(f"{i}C° em Fahrenheit é {(i*(9/5))+32}F°")

def lancamento():
    for i in range(10, 0, -1):
        print(i)
    print("Lançamento!")

def multiplos_de4():
    for i in range(0, 21, 4):
        print(i)

def decidir_par_1a20():
    for i in range(0, 21, 1):
        if i % 2 == 0:
            print(f"{i} é par")
        else:
            print(f"{i} é impar")

def exibir_positivos():
    num = ""
    while num != 0:
        num = int(input("Favor inserir um número: "))
        if num > 0:
            print(f"{num} é positivo!")
        elif num < 0:
            print(f"{num} é negativo!")
        else:
            print("Obrigado por utilizar!")

def multiplos_3e5():
    for i in range(0, 50, 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

def verificacao_senhas():
    senha = input("Favor inserir senha: ")
    i = 1
    while senha != "batatinha123":
        if i < 3:
            print(f"Senha incorreta, tentativas restantes {3-i}")
            senha = input("Senha incorreta, favor inserir senha: ")
            i += 1
        else:
            print("Número de tentativas excedido")
            return
    print("Senha correta, acesso liberado!")
    
def notas_alunos():
    for i in range(0,5,1):
        nota = int(input("Favor inserir um número: "))
        if nota >= 6:
            print(f"{nota}, aluno aprovado!")
        else:
            print(f"{nota}, aluno reprovado!")
            
def maioridade():
    idade = ""
    while idade != 0:
        idade = int(input("Favor inserir sua idade: "))
        if idade >= 18:
            print("Você é maior de idade!")
        elif idade == 0:
            print("Obrigado por utilizar!")
        else:
            print("Você é menor de idade!")
    
def classificar_multi3e5():
    for i in range (0, 31,1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} é múltiplo de 3 & 5")
        elif i % 3 == 0:
            print(f"{i} é múltiplo de 3")
        elif i % 5 == 0:
            print(f"{i} é múltiplo de 5")
        else:
            print(f"{i} não é múltiplo de 3 ou 5")

def numero_secreto():
    tentativa =int(input("Favor inserir um número: "))
    while tentativa != 16:
        if tentativa > 16:
            print("Quase lá, o número é menor")
        else:
            print("Passou perto, o número é maior")
        tentativa = int(input("Tente novamente: "))
    if tentativa == 16:
        print("Parabéns você acertou!")
            
def multiplos_de7():
    for i in range(0, 100, 7):
        print(i)

def contar_positivosnegativos():
    num = int(input("Favor inserir um número "))
    neg = 0
    posi = 0
    while num != 0:
        if num > 0:
            posi += 1
        else:
            neg += 1
        num = int(input("Favor inserir mais um número "))
    print(f"O total de números positivos é {posi},  já o total dos negativos é {neg}")

def tabuada_pares():
    for i in range(2, 11, 2):
        for b in range(1, 11, 1):
            print(f"{i}x{b}={i*b}")

def caixa_eletronico2():
    saldo = 0
    while True:
        print("Favor escolher uma opção\n1 - Para realizar um depósito\n2 - Para realizar um saque\n 3 - Para terminar as operações")
        opc = int(input("Opção desejada: "))
        if opc == 1:
            quantia = int(input("Favor informar uma quantia para depósito: "))
            saldo += quantia
        elif opc == 2:
            quantia = int(input("Favor informar uma quantia para saque: "))
            saldo -= quantia
        elif opc == 3:
            print("Obrigado por utilizar")
            break

def classificar_notas():
    for i in range(1, 11):
        nota = int(input("Favor inserir nota: "))
        if nota >= 9:
            print("Nota A")
        elif nota < 9 and nota >=7:
            print("Nota B")
        elif nota < 7 and nota >=5:
            print("Nota C")
        else:
            print("Nota D")

def classificar_temperaturas():
    temp = int(input("Favor informar uma temperatura: "))
    while temp >= -100:
        if temp >= 25:
            print("A temperatura está quente")
        elif temp < 25 and temp >= 15:
            print("A temperatura está agradável")
        elif temp < 15 and temp >= 1:
            print("A temperatura está fria")
        elif temp < 1 and temp >= -100:
            print("A temperatura está congelante")
        temp = int(input("Favor informar umau nova temperatura: "))
    print("Obrigado por utilizar!")

def triangulo():
    for i in range(1, 6, 1):
        print(i * "*")
        
def classificar_idades():
    idade = int(input("Favor informar uma idade: "))
    criancas = 0
    adolecentes = 0
    adultas = 0
    idosas = 0
    while idade != 0:
        if idade < 12:
            criancas += 1
        elif idade >= 12 and idade < 18:
            adolecentes += 1
        elif idade >= 18 and idade < 60:
            adultas += 1
        elif idade >= 60:
            idosas += 1
        idade = int(input("Favor informar mais uma idade: "))
    print(f"De acordo com as idades existem:\n{criancas} crianças\n{adolecentes} adolescentes\n{adultas} adultos\n{idosas} idosos")

def FizzBuzz():
    for i in range(1,21,1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def vendaingresso():
    vagas = 50
    opt = input("Desejar vender um ingresso ? (Y/N): ")
    while vagas > 0 and (opt == "Y" or opt == "y"):
        print(f"Ingresso vendido, vagas restantes {vagas}")
        vagas -= 1
        opt = input("Deseja vender mais ingressos ? (Y/N): ")
    if vagas == 0:
        print("Todas as vagas já foram vendidas")
    else: 
        print("Obrigado por utilizar!")

def maior_e_menor():
    numinicial = int(input("Favor inserir um número: "))
    maior = numinicial
    menor = numinicial
    i = 1
    for i in range(1, 10):
        num = int(input("Favor inserir outro número: "))
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        numinicial = num
        i += 1
    print(f"O maior número foi {maior} e o menor número foi {menor}")

def contar_num_primos():
    contador = 0
    for num in range (2, 100):
        for divisor in range(2, num+1):
            if num % divisor == 0 and num !=2:
                break
            elif num == 2 or (divisor == num-1 and num % divisor !=0):
                print(f"{num} é primo")
                contador += 1             
    print(contador)

def estoque():
    estoque = 100
    while estoque > 0:
        vendas = int(input("Qual o número de produtos a vender ? "))
        if vendas <= estoque:
            estoque -= vendas
            print(f"Quantidade em estoque {estoque}")
        else:
            print("Não há mais produtos para atender essa venda.")

def de1a15():
    for i in range(0,16,1):
        if i <= 5:
            print("Pequeno")
        elif i > 5 and i <= 10:
            print("Médio")
        else:
            print("Grande")

def validacao_1a10():
    numero = int(input("Favor inserir um número a ser validado (de 1 a 10): "))
    while numero > 10 or numero < 0:
            numero = int(input("Favor inserir um número dentro dos parâmetros mencionados: "))


def temperatura_semana():
    contador = 0
    for i in range(1,8,1):
        temperatura = int(input(f"Favor inserir a temeperatura do {i}º dia da semana: "))
        if temperatura > 30:
            contador += 1 
    print(f"Nº de dias em que a temperatura foi maior que 30 graus Celsius é de {contador}")

def jogo_parouimpar():
    resposta = input("Deseja jogar par ou ímpar ? (Y/N): ")
    valor_computador = 3
    while resposta == "y" or resposta == "Y":
        escolha = int(input("Deseja par(1) ou ímpar(2): "))
        valor = int(input("insira o seu número:"))
        if escolha == 1:
            if (valor + valor_computador) % 2 == 0:
                print(f"{valor} + {valor_computador} = {valor+valor_computador}, que é par, você venceu!")
                resposta = input("Continuar jogando par ou ímpar ? (Y/N): ")
            else: 
                print(f"{valor} + {valor_computador} = {valor+valor_computador}, que é ímpar, você perdeu!")
                resposta = input("Continuar jogando par ou ímpar ? (Y/N): ")
        elif escolha == 2:
            if (valor + valor_computador) % 2 == 0:
                print(f"{valor} + {valor_computador} = {valor+valor_computador}, que é par, você perdeu!")
                resposta = input("Continuar jogando par ou ímpar ? (Y/N): ")
            else: 
                print(f"{valor} + {valor_computador} = {valor+valor_computador}, que é ímpar, você venceu!")
                resposta = input("Continuar jogando par ou ímpar ? (Y/N): ")
    if resposta == "N" or resposta == "n":
        print("Obrigado por jogar!")

def pares_maior20():
    for i in range(20, 51,2):
        print(i)

def horas_trabalhadas():
    horas = 0
    for i in range(1,8):
        horas += int(input(f"Quantas horas trabalhadas no {i}º dia da semana ?  "))
    if horas >= 48:
        print("Carga de trabalho pesada")
    elif horas < 48 and horas >= 36:
        print("Carga de trabalho moderada")
    else:
        print("Carga de trabalho leve")

def tabuada_1a5():
    for i in range(1, 6, 1):
        for u in range(1,11,1):
            print(f"{i}x{u}={i*u}")

def sistema_login():
    tentativa = 1
    acesso = "negado"
    while tentativa in range (1, 4):
        usuario = input("Favor inserir seu usuário: ")
        senha = input("Favor inserir sua senha: ")
        if usuario == "admin" and senha == "batatinha123":
            acesso = "liberado"
        tentativa += 1
    if acesso == "liberado":
        print("Seu acesso foi liberado!")
    else:
        print("Seu acesso foi negado")



