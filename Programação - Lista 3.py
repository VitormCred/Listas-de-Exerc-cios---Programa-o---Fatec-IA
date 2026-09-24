def exercicio_01():
    # Pedir ao usuário um número e exibir os números de 1 até o número informado.
    num = int(input("Olá, favor inserir um número: "))
    i = 1
    while i in range(num+1):
        print(i)
        i += 1

def exercicio_02():
    # Pedir ao usuário um número e exibir os números do número informado até 1.
    num = int(input("Olá, favor inserir um número: "))
    while num >= 1:
        print(num)
        num -= 1

def exercicio_03():
    # Pedir ao usuário um número, exibir os números, do número informado até 1 e exibir "Liberado o vôo!"
    num = int(input("Olá, favor inserir um número: "))
    while num >= 1:
        print(num)
        num -= 1
    print("Liberado o vôo!")

def exercicio_04():
    # Calcular e exibir a soma de todos os números inteiros de 1 até 10.
    i = 0
    soma = 0
    while i <= 10:
        soma = soma + i
        i += 1
    print(soma)

def exercicio_05():
    # Pedr 5 números e calcular a soma deles.
    i = 0
    soma = 0
    while i <= 5:
        num = int(input("Favor inserir um número: "))
        soma += num
        i += 1
    print(soma)

def exercicio_06():
    # Pedir números ao usuário, quando o mesmo digitar 0, exibir a soma dos número digitados e finalizar -
        # o código.
    soma = 0
    num = ""
    while num != 0:
        num = int(input("Favor inserir um número: "))
        soma += num
    print(f"A soma total é {soma}")

def exercicio_07():
    # Definir uma senha no código e pedir repetidamente para o usuário inserir uma senha, até que a senha -
        # correta seja inserida.
    senha = input("Favor inserir senha: ")
    while senha != "batatinha123":
        senha = input("Favor inserir a senha correta: ")
    print("Acesso liberado!")

def exercicio_08():
    # Pedir ao usuário um número positivo e contar quantos dígitos esse número possui.
    num = int(input("Favor inserir um número: "))
    i = 1
    while num / 10 > 1:
        num = num / 10
        i +=1
    print(i)

def exercicio_09():
    # Pedir ao usuário um número inteiro e calcular o fatorial do mesmo.
    num = int(input("Inserir número: "))
    i = num
    while i > 1:
        fatorial = num * (i-1)
        num = fatorial
        i -= 1
    print(num)

def exercicio_10():
    # Pedir ao usuário repetidamente números positivos até que o mesmo insira um número negativo -
        # contar quantos números positivos foram inseridos.
    num = int(input("Favor inserir número, digite um número negativo para sair: "))
    i = 0
    while num >= 0:
        num = int(input("Favor inserir outro número: "))
        i += 1
    print(f"A quantidade de números positivos foi de {i}")

def exercicio_11():
    # Pedir ao usuário um número inteiro e maior que 1 e verificar se o número é primo ou não.
    num = int(input("Favor inserir um número inteiro em maior que 1: "))
    i = 2
    if num == 2:
        print(f"O número {num} é primo")
    while i in range(2, num):
        if num % i == 0:
            print(f"O número {num} não é primo!")
            break
        else:
            print(f"O número {num} é primo")
            break

def exercicio_12():
    # Simular uma contagem regressiva de 10 até 0 e exibir "Feliz ano novo!" ao chegar no 0.
    i = 11
    while i > 0:
        i -= 1
        print(i)
    print("Feliz ano novo!")

def exercicio_13():
    # Pedir ao usuário, repetidamente, notas de alunos até que o mesmo digite -1, após isso calcular -
        # a média das notas.
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

def exercicio_14():
    # Pedir ao usuário um número inteiro e calcular a soma dos dígitos desse número.
    num = int(input("Favor inserir um número: "))
    soma = 0
    while num / 10 > 1:
        resto = num % 10
        soma = soma + resto
        num = num // 10
    print(soma)

def exercicio_15():
    # Pedir ao usuário, repetidamente, valores a serem depositados, até o mesmo inserir 0, calcular -
        # o saldo acumulado.
    deposito = int(input("Favor inserir um valor: "))
    saldo = 0 + deposito
    while deposito != 0:
        deposito = int(input("Inserir um novo valor: "))
        saldo = saldo + deposito
    print(f"Saldo final: {saldo}R$")

def exercicio_16():
    # Exibir números de 1 a 10.
    i = 0
    for i in range (1, 11):
        print(i)
        i += 1
    
def exercicio_17():
    # Exibir números de 10 a 1.
    i = 0
    for i in range (10, 0, -1):
        print(i)
        i += 1

def exercicio_18():
    # Exibir todos os pares de 0 até 20.
    for i in range(0, 20, 2):
        print(i)

def exercicio_19():
    # Exibir todos os ímpares de 0 a 20.
    for i in range(1, 20, 2):
        print(i)

def exercicio_20():
    # Soma de todos números inteiros, 1 a 100.
    i = 0
    soma = 0
    for i in range(101):
        soma += i
        i += 1
    print(soma)

def exercicio_21():
    # Fatorial do número.
    num = int(input("Inserir número: "))
    i = num
    soma = 1
    for i in range(num, 0, -1):
        fatorial = soma * (i)
        soma = fatorial
    print(soma)

def exercicio_22():
    ## Tabuada completa de um número.
    num = int(input("Favor inserir um número: "))
    for i in range(1, 11, 1):
        print(f"{num}x{i}={num*i}")
    
def exercicio_23():
    # Tabuadaa completa dos números 1 até 10.
    for i in range(1, 11, 1):
        for b in range (1, 11, 1):
            print(f"{i}x{b}={i*b}")

def exercicio_24():
    # Contar quantidade de números pares de 0 até 50.
    contador = 0
    for i in range(0, 51, 2):
        contador += 1
    print(contador)

def exercicio_25():
    # Soma de todos números pares de 0 até 100.
    soma = 0
    for i in range(0, 101, 2):
        soma += i
    print(soma)

def exercicio_26():
    # Calcular a média dentre 5 números.
    nota = 0
    for i in range(1, 6):
        nota += int(input("Favor inserir uma nota "))
    print(f"A média final é de {nota/5}")

def exercicio_27():
    # Exibir todos os múltiplos de 3, de 0 a 60.
    for i in range(0, 61, 3):
        print(i)

def exercicio_28():
    # Tabela de conversão 0 a 100 de Cº para Fº.
    for i in range (0, 100, 10):
        print(f"{i}C° em Fahrenheit é {(i*(9/5))+32}F°")

def exercicio_29():
    # Contagem regressiva, depois exibir "lançamento".
    for i in range(10, 0, -1):
        print(i)
    print("Lançamento!")

def exercicio_30():
    # Exibir todos múltiplos de 4, de 0 a 20.
    for i in range(0, 21, 4):
        print(i)

def exercicio_31():
    # Classificar todos os números, de 1 a 20, em par ou ímpar.
    for i in range(0, 21, 1):
        if i % 2 == 0:
            print(f"{i} é par")
        else:
            print(f"{i} é impar")

def exercicio_32():
    # Pedir números para o usuário, a cada número exibir se é positivo ou negativo, parar quando
        # o usuário digitar o númer 0
    num = ""
    while num != 0:
        num = int(input("Favor inserir um número: "))
        if num > 0:
            print(f"{num} é positivo!")
        elif num < 0:
            print(f"{num} é negativo!")
        else:
            print("Obrigado por utilizar!")

def exercicio_33():
    # Exibir todos os múltiplos de 3 que também são múltiplos de 5, do 1 ao 50.
    for i in range(0, 50, 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

def exercicio_34():
    # Realizar uma verificação de senha com até 3 tentativas.
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
    
def exercicio_35():
    # Pedir e classificar notas de 5 alunos, exibindo "Aprovado" caso maior ou igual a 6 -
        # reprovado caso menor do que 6.
    for i in range(0,5,1):
        nota = int(input("Favor inserir um número: "))
        if nota >= 6:
            print(f"{nota}, aluno aprovado!")
        else:
            print(f"{nota}, aluno reprovado!")
            
def exercicio_36():
    # Pedir diversas idades, para cada idade classificar em menor ou maior de idade até -
        # que o usuário digite -1
    idade = ""
    while idade != -1:
        idade = int(input("Favor inserir sua idade: "))
        if idade >= 18:
            print("Você é maior de idade!")
        elif idade == -1:
            print("Obrigado por utilizar!")
        else:
            print("Você é menor de idade!")
    
def exercicio_37():
    # Classificar números do 1 ao 3 em multiplos de 3, 5, 3 & 5 ou nenhum dos dois.
    for i in range (0, 31,1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} é múltiplo de 3 & 5")
        elif i % 3 == 0:
            print(f"{i} é múltiplo de 3")
        elif i % 5 == 0:
            print(f"{i} é múltiplo de 5")
        else:
            print(f"{i} não é múltiplo de 3 ou 5")

def exercicio_38():
    # Jogo da adivinhação, informando se o número inserido é maior ou menor que o correto.
    tentativa = int(input("Favor inserir um número: "))
    while tentativa != 16:
        if tentativa > 16:
            print("Quase lá, o número é menor")
        else:
            print("Passou perto, o número é maior")
        tentativa = int(input("Tente novamente: "))
    if tentativa == 16:
        print("Parabéns você acertou!")
            
def exercicio_39():
    # Exibir múltiplos de 7, de 1 a 100.
    for i in range(0, 101, 7):
        print(i)

def exercicio_40():
    # Pedir números até que o usuário insira 0, contar e exibir a quantidade de positivos & negativos.
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

def exercicio_41(): 
    # Fazer tabuada completa dos números pares entre 0 e 10.
    for i in range(2, 11, 2):
        for b in range(1, 11, 1):
            print(f"{i}x{b}={i*b}")

def exercicio_42():
    # Caixa eletrônico com sacar, depositar & sair.
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

def exercicio_43():
    # Pedir 10 notas e classificar de acordo com o conceito(A>=9, B>=7, C>=5, D<5)
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

def exercicio_44():
    # Pedir temperaturas ao usuário e classificar com o conceito(Congelante<0,Fria<=15,Agradável<=24,Quente>=25) 
        # parar quando o usuário inserir uma temperatura menor que -100.
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

def exercicio_45():
    # Exibir um triângulo com 5 linhas onde cada linha contem uma quantidade de de asteriscos de acordo com seu número.
    for i in range(1, 6, 1):
        print(i * "*")
        
def exercicio_46():
    # Pedir idades ao usuário, classificar com o conceito(Idoso>60;Adult>=18;Adolescente>=12,Criança<12), contar o número -
        # de idades de cada classe e informar no final. Parar quando o usuário digitar 0
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

def exercicio_47():
    # De 1 a 20, passar por cada número e exibir "Fizz" para múltiplos de 3, "Buzz" para múltiplos de 5 e "FizzBuzz" para -
        # múltiplos de 3 & 5.
    for i in range(1,21,1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def exercicio_48():
    # Simular a vende de ingressos, com 50 ingressos iniciais, a cada venda subtrair um ingresso. Parar se o número de -
        # ingressos chegar a 0 ou o usuário escolher a opção Não(N)
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

def exercicio_49():
    # Pedir ao usuário 10 valores e exibir o menor e maior número após os números serem digitados.
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

def exercicio_50():
    valor_total = 0
    valor = float(input("Favor informar o valor da compra: "))
    while valor != -1:
        valor_total += valor
        valor = float(input("Favor informar o valor da compra: "))
    if valor_total < 500:
        print(f"De acordo com o valor gasto de {valor_total:00.2f}R$, não há desconto.")
        print(f"O valor total a pagar é de {valor_total:00.2f}R$")
    elif 500 <= valor_total < 1000:
        print(f"De acordo com o valor gasto de {valor_total:00.2f}R$, há desconto um desconto de 5%.")
        print(f"O valor total a pagar é de {(valor_total*0.95):00.2f}R$")
    elif 1000 <= valor_total:
        print(f"De acordo com o valor gasto de {valor_total:00.2f}R$, há desconto um desconto de 10%.")
        print(f"O valor total a pagar é de {(valor_total*0.90):00.2f}R$")

def exercicio_51():
    # Contar a quantidade de números primos entre 1 e 100.
    contador = 0
    for num in range (2, 100):
        for divisor in range(2, num+1):
            if num % divisor == 0 and num !=2:
                break
            elif num == 2 or (divisor == num-1 and num % divisor !=0):
                contador += 1             
    print(contador)

def exercicio_52():
    # Definir um estoque inicial e realizar vendas, impossibilitando uma venda maior que o estoque -
        # parar quando o estoque chegar a 0.
    estoque = 100
    while estoque > 0:
        vendas = int(input("Qual o número de produtos a vender ? "))
        if vendas <= estoque:
            estoque -= vendas
            print(f"Quantidade em estoque {estoque}")
        else:
            print("Não há mais produtos para atender essa venda.")

def exercicio_53():
    # Percorrer números de 1 a 15 e classifica-los de acordo com o conceito(Pequeno<=5, Médio<=10, Grande>10)
    for i in range(0,16,1):
        if i <= 5:
            print("Pequeno")
        elif i > 5 and i <= 10:
            print("Médio")
        else:
            print("Grande")

def exercicio_54():
    # Pedir ao usuário, repetidamente, um número, até que o mesmo esteja dentro do parâmetro(1 a 10).
    numero = int(input("Favor inserir um número a ser validado (de 1 a 10): "))
    while numero > 10 or numero < 0:
            numero = int(input("Favor inserir um número dentro dos parâmetros mencionados: "))
    print("Número dentro dos parâmetros mencionados!")

def exercicio_55():
    # Pedir a temperatura de cada dia da semana(7) e contar quantos dias a temperatura foi maior do que 30.
    contador = 0
    for i in range(1,8,1):
        temperatura = int(input(f"Favor inserir a temeperatura do {i}º dia da semana: "))
        if temperatura > 30:
            contador += 1 
    print(f"Nº de dias em que a temperatura foi maior que 30 graus Celsius é de {contador}")

def exercicio_56():
    # Perguntar se o usuário deseja jogar par ou ímpar (S/N), caso o mesmo aceito pedir um número e somar -
        # a esse número um valor pré-determinado e pedir ao usuário escolher par(1) ou ímpar(2), apresentar -
        # se o usuário ganhou ou perdeu e perguntar se ele deseja continuar jogando.
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

def exercicio_57():
    # Exibir quais números pares e maiores que vinte, do 1 ao 50.
    for i in range(20, 51,2):
        print(i)

def exercicio_58():
    # Pedir a carga horária do trabalho para usuário, por dia de semana, somar o total e classficar de acordo -
        # com o conceito(Pesada>=48, Moderada>=36, Leve<36)
    horas = 0
    for i in range(1,8):
        horas += int(input(f"Quantas horas trabalhadas no {i}º dia da semana ?  "))
    if horas >= 48:
        print("Carga de trabalho pesada")
    elif horas < 48 and horas >= 36:
        print("Carga de trabalho moderada")
    else:
        print("Carga de trabalho leve")

def exercicio_59():
    # Exibir a tabuada(1 a 10) de todos os números do 1 ao 5.
    for i in range(1, 6, 1):
        for u in range(1,11,1):
            print(f"{i}x{u}={i*u}")

def exercicio_60():
    # Definir usuário e senha no código e simular um sistema de login, exibindo ao final se alguma das tentatias -
        # liberou o acesso ao sistema.
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
        
