def exercicio_01():
    # Função deve exibir: "Olá, mundo!"
        # Argumentos = ""
    print("Olá, mundo!")

def exercicio_02(nome):
    # A Função deve exibir: "Seja bem-vindo(a)" <nome>
        # Argumentos = Nome(string)
    print(f"Seja bem-vindo(a), {nome}!")

def exercicio_03(a, b):
    # A função deve somar os números e exibir "Olá, a soma dos números é:" <a+b>
        # Argumentos = a(int), b(int)
    print(f"Olá, a soma dos números é {a+b}!")

def exercicio_04(a, b):
    # A função deve subtrair os números e exibir "Olá, a subtração dos números é:" <a-b>
        # Argumentos = a(int), b(int)
    print(f"Olá, a subtração dos números é {a-b}!")

def exercicio_05(a, b):
    # A função deve multiplicar os números e exibir "Olá, a multiplicação dos números é:" <a*b>
        # Argumentos = a(int), b(int)
    print(f"Olá, a multiplicação dos números é {a*b}!")

def exercicio_06(a, b):
    # A função deve divir os números e exibir "Olá, a divisão dos números é:" <a/b>
        # Argumentos = a(int), b(int)
    print(f"Olá, a divisão dos números é {a/b}!")

def exercicio_07(a):
    # A função deve duplicar o número e exibir: "Olá, o dobro do número é:" <a*2>
        # Argumentos = a(int)
    print(f"Olá, o dobro do número é {a*2}!")

def exercicio_08(a):
    # A função deve triplicar o número e exibir: "Olá, o triplo do número é:" <a*3>
        # Argumentos = a(int)
    print(f"Olá, o triplo do número é {a*3}!")

def exercicio_09(a):
    # A função deve dividir em 2 o número e exibir: "Olá, a metade do número é:" <a/2>
        # Argumentos = a(int)
    print(f"Olá, a metade do número é {a/2}!")

def exercicio_10(a):
    # A função deve elevar o número ao quadrado e exibir: "Olá, o quadrado do número é:" <a**2>
        # Argumentos = a(int)
    print(f"Olá, o quadrado do número é {a**2}!") # o símbolo de "**" indica uma operação com raizes.

def exercicio_11(a):
    # A função deve elevar o número ao cubo e exibir: "Olá, o cubo do número é:" <a**3>
        # Argumentos = a(int)
    print(f"Olá, o cubo do número é {a**3}!")

def exercicio_12(a, b):
    # A função deve realizar a média aritimética dos números e exibir: "Olá, a média aritimética dos números é:" <(a+b)/2>
        # Argumentos = a(int), b(int)
    print(f"Olá, a média aritimética dos números é {(a+b)/2}!")

def exercicio_13(a):
    # A função deve divir o número por 2, caso o módulo da divisão seja igual 0, exibir: "O número é par"
        # Argumentos = a(int)
    if a % 2 == 0:
        print("O número é par")
        
def exercicio_14(a):
    # A função deve divir o número por 2, caso o módulo da divisão seja diferente 0, exibir: "O número é ímpar"
        # Argumentos = a(int)
    if a % 2 != 0:
        print("O número é ímpar")

def exercicio_15(a, b):
    # A função deve multiplicar os números e exibir: "A área do retángulo é:" <a*b>
        # Argumentos = a(int), b(int)
    print(f"A área do retángulo é {a*b}")

def exercicio_16(a, b):
    # A função deve somar os números, o multiplicar os resultado por 2 e exibir: "O perímetro do retángulo é:" <(a+b)*2>
        # Argumentos = a(int), b(int)
    print(f"O perímetro do retángulo é {(a+b)*2}!")

def exercicio_17(a):
    # A função deve aplicar a fórmula de conversão ao número e exibir: "A temperatura" <a> "Cº em Fahrenheit é" <(a-32)*(5/9))> "Fº"
        # Argumentos = a(int)
    print(f"A temperatura {a}Cº em Fahrenheit é {(a*(9/5)+32):00.2f}Fº") # O Argumento ":00.2f" dento de um F-String faz com que o decimal de um número seja reduzido apenas a 2 casas ~ Exemplo: 190.32962 --> 190.32

def exercicio_18(a):
    # A função deve aplicar a fórmula de conversão ao número e exibir: "A temperatura" <a> "Fº em Celsius é" <(a-32)*(5/9))> "Cº"
        # Argumentos = a(int), b(int)
    print(f"A temperatura {a}Fº em Celsius é {(a-32)*(5/9):00.2f}Cº") # O Argumento ":00.2f" dento de um F-String faz com que o decimal de um número seja reduzido apenas a 2 casas ~ Exemplo: 190.32962 --> 190.32

def exercicio_19(char, num):
    # A função deve repetir o caractere inserido pelo número de vezes inserido e exibir: <char*num>
        # Argumentos = char(str), num(int)
    print(f"{char*num}")

def exercicio_20(a):
    # A função deve avaliar se a idade corresponde a maioridade ou não e exibir: "Você é maior de idade!" ou "Você não é maior de idade!"
        # Argumentos = a(int)
    if a >= 18:
        print("Você é maior de idade!")
    else:
        print("Você não é maior de idade!")

def exercicio_21(nome, saudacao="Olá"):
    # A função deve organizer nome e saudação, sendo que o valor padrão da saudação é "Olá" e exibir: <saudação>, <nome>
        # Argumentos = nome(str), saudacao(str)
    print(f"{saudacao}, {nome}")

def exercicio_22(num, expoente=2):
    # A função deve elevar um número a um expoente, sendo que o valor padrão do expoente é 2 e exibir: <num**expoente>
        # Argumentos = num(int), expoente(int)
        print(f"{num**expoente}")

def exercicio_23(valor, desconto=10):
    # A função deve calcular o valor final com desconto, sendo que o valor padrão do desconto é 10 e exibir: "O valor com desconto é:" <valor>*((100-<desconto>)/100))
        # Argumentos = valor(int), desconto(int)
    print(f"O valor com desconto é {valor*((100-desconto)/100):00.2f}R$")

def exercicio_24(num, limite=10):
    # A função deve fazer a tabuada do número do 1 até o valor limite, sendo que o valor padrão do limite é 10 e exibir: <1 até num> x (1 até <limite>)
        # Argumentos = num(int), limite(int)
        for i in range (1,num+1,1):
            for u in range(1,limite+1,1):
                print(f"{i}x{u}={i*u}")

def exercicio_25(raio):
    # A função deve aplicar a fórmula ao número e exibir: "A área do cículo é:" <raio>**2*3.14
        # Argumentos = raio(int)
    print(f"A área do circulo é {(raio**2)*3.14}")

def exercicio_26(hora):
    # A Função deve selecionar uma saudação de acordo com o horário informado e exibir: "Bom dia!" ou "Boa tarde!" ou "Boa noite!"
        # Argumentos = hora(int)
    if hora in range(6,12):
        print("Bom dia!")
    elif hora in range(12, 18):
        print("Boa tarde!")
    elif hora in range(5) or hora in range(19,23):
        print("Boa noite!")

def exercicio_27(a, b, c):
    # A função deve selecionar qual dos números é o maior e exibir: "O maior número é:" <a> ou <b> ou <c>
        # Argumentos = a(int), b(int), c(int)
    if a > b and a > c: 
        print(f"O maior número é {a}!")
    elif b > a and b > c:
        print(f"O maior número é {b}!")
    elif c > a and c > b:
        print(f"O maior número é {c}!")

def exercicio_28(a, b, c):
    # A função deve selecionar qual dos números é o menor e exibir: "O menor número é:" <a> ou <b> ou <c>
        # Argumentos = a(int), b(int), c(int)
    if a < b and a < c: 
        print(f"O menor número é {a}!")
    elif b < a and b < c:
        print(f"O menor número é {b}!")
    elif c < a and c < b:
        print(f"O menor número é {c}!")
        
def exercicio_29(Nota):
    # A função deve classificar a valor da nota(Nota>=9:A, Not>=7:B, Nota>=5:C, Nota<5:D) e exibir: "Sua nota é A" ou "Sua nota é B" ou "Sua nota é C" ou "Sua nota é D".
        # Argumentos = Nota(int)
    if Nota >=9:
        print("Sua nota é A")
    elif Nota >= 7 and Nota <= 9:
        print("Sua nota é B")
    elif Nota >= 5 and Nota <= 7:
        print("Sua nota é C")
    else:
        print("Sua nota é C")

def exercicio_30(linhas):
    # A função deve desenhar um triângulo com asteriscos, seguindo o número de linhas e exibir <char> (o desenho do triângulo).
        # Argumentos = linhas(int)
    i = 0
    desenho = ""
    for i in range(linhas):
        desenho = desenho + "\n" + ((linhas-i) * " " + i * "*" + "*" + i * "*" + (linhas-i) * " ")
        i = i + 1
    print(desenho)

def exercicio_31(num=5):
    # A função deve somar 1 a cada repetição a uma variável global chamada de "contador", onde o valor padrão do número de repetições é 5 e exibir: "Valor inicial do contador:" <contador> & "Valor final do contador:" <contador>
        # Argumentos = num(int)
    global contador
    contador = 0
    print(f"Valor inicial do contador: {contador} ")
    for i in range (num):
        contador = contador + 1
    print(f"Valor final do contador: {contador}")

def exercicio_32(nota1, nota2, peso1=1, peso2=1):
    # A função deve calcular a média ponderada, multiplicando as notas por seus pesos, o valor padrão dos pesos é 1 e exibir: "A nota final é de:" <((nota1*peso1)+(nota2*peso2))/(peso1+peso2)>
        # Argumentos = nota1(int), nota2(int), peso1(int), peso2(int)
    print(f"A nota final é de {(nota1*peso1)+(nota2*peso2)/(peso1+peso2)}!")

def exercicio_33(num):
    # A função deve decidir se o número é primo ou não e exibir: "O número" <num> "não é primo!" ou "O número" <num> "é primo!"
        # Argumentos = num(int)
    if num == 1 or num == 2 or num == 3: # São números primos
        print(f"O número {num} é primo")
    if num % 2 == 0 or num % 3 == 0: # Todo número divisivel por 2 e 3 não é primo.
        print(f"O número {num} não é primo")
    # Se a raiz quadrada de um número é um número inteiro o numero necessariamente não é primo, se o número tiver um divisor ele estará abaixo ou exatamente 1 número acima de sua raiz quadrada e todo número par maior que 2 também não é primo, com isso montamos a equação:
    i = 5 # Primeiro número primo depois de 3.
    maximo = int(num**0.5)+1 # Encontramos o número exatamente acima da raiz quadrada do número desejado.
    while i < maximo:
        if num % i == 0 or num % (i+2) == 0:
            print(f"O número {num} não é primo")
            return
        i += 6 # Como todos os números estão posicionados ao redor de múltiplos de 6, eliminamos os múltiplos de 2 & 3 e fazemos a conta com os múltiplos de 6 somando ou subtraindo 1. Exemplo:  11 - 12(6) - 13 - 14(2) - 15(3) - 16(2) - 17 - 18(6) - 19 - 20(2)
    print(f"O número {num} é primo")

def exercicio_34(num):
    # A função deve calcular o fatorial do número e exibir: "O valor do fatorial de" <num> "é" <fatorial>
        # Argumentos = num(int)
    i = 1
    fatorial = num
    while i < num:
        fatorial = fatorial * (num-i)
        i = i + 1
    print(f"O valor do fatorial de {num} é {fatorial}!") 

def exercicio_35(a,b):
    # A função deve calcular o máximo divisor comum entre 2 números e exibir: "O MDC de" <a> "e" <b> "é" <i>
        # Argumentos = a(int), b(int)
    if a > b:
        i = a
    else:
        i = b
    while i != 0 and (a % i != 0 or b % i != 0):
        i = i - 1
    print(f"O MDC de {a} e {b} é {i}")
    return(i)

def exercicio_36(a,b):
    # A função deve calcular o mínimo múltiplo comum dentre 2 números e exibir: "O MMC de" <a> "e" <b> "é" <mmc>
        # Argumentos = a(int), b(int)
    mmc = (a*b)/exercicio_32(a,b)
    print(f"O MMC de {a} e {b} é {mmc}")
    return mmc

def exercicio_37(num):
    # A função deve calcular a soma dos dígitos de um número inteiro e exibir: "A soma dos dígitos de" <numini> "é" <soma>
        # Argumentos = num(int)
    numini = num
    soma = 0
    while num / 10 > 1:
        resto = num % 10
        soma = soma + resto
        num = num // 10
    print(f"A soma dos dígitos de {numini} é {soma}") 

def exercicio_38(num):
    # A função deve calcular e exibir a ordem reversa dos dígitos de um número inteiro e exibir: "A inversão dos dígitos de" <numini> "é" <digitos>
        # Argumentos = num(int)
    numini = num
    digitos = ""
    while num / 10 > 0:
        resto = num % 10
        digitos = digitos + str(resto)
        num = num // 10
    print(f"A inversão dos dígitos de {numini} é {digitos}") 

def exercicio_39(palavra):
    # A função deve contar o número de vogais em uma palavra e exibir "Há" <qtd_vogais> "vogais em" <palavra>
        # Argumentos = palavra(str)
    qtd_vogais = 0
    for letra in palavra:
        if letra == "A" or letra == "a" or letra == "E" or letra == "e" or letra == "I" or letra == "i" or letra == "O" or letra == "o" or letra == "U" or letra == "o":
            qtd_vogais += 1
    print(f"Há {qtd_vogais} vogais em {palavra}")

def exercicio_40(palavra):
    # A função deve checar se uma string e o seu inverso são iguais e exibir: "A palavra" <palavra> "e seu inverso" <caracteres> "são iguais, logo é um palíndromo." OU "A palavra" <palavra> "e seu inverso" <caracteres> "não são iguais, logo não é um palíndromo."
        # Argumentos = palavra(str)
    palavra_str = str(palavra)
    caracteres = ""
    for i in range(len(palavra_str)-1, -1,-1):
        caracteres = caracteres + palavra_str[i]
    if palavra == caracteres:
        print(f'A palavra "{palavra}" e seu inverso "{caracteres}" são iguais, logo é um palíndromo.')
    elif palavra != caracteres:
        print(f'A palavra "{palavra}" e seu inverso "{caracteres}" não são iguais, logo não é um palíndromo.')


def exercicio_41(senha_correta, tentativas=3):
    # A função deve simular uma tentativa de insersão de senha, pedindo repetidamente a senha para o usuário, até a senha correta ser inserida ou o limite tentativas, cujo o valor padrão é 3, for atingido e Exibir: "Senha correta, acesso liberado" ou "Número máximo de tentativas atingido"
        # Argumentos = senha_correta(str), tentativas(int)
    senha = input("Favor inserir a senha: ")
    i = 1
    while senha != senha_correta:
        print("senha incorreta digitada, tente novamente")
        print(f"Número de tentativas restante {3-i}")
        if i in range(tentativas):
            senha = input("Favor inserir a senha correta: ")
            i = i + 1
        else: 
            print("Número máximo de tentativas atingido!")
            break
    if senha == senha_correta:
        print("Senha correta, acesso liberado!")
    
    
def exercicio_42(peso, altura):
    # A função deve realizar o cálculo do imc dado altura e peso (peso/(altura**2)) e classificar segundo o parâmetro(imc<18.5:Abaixo do peso, imc>=18.5:peso adequado, imc>=24.9:sobrepeso, imc>=29.9:Obesidade,imc>39.9:Obesidade grave) e exibir: "O seu IMC de" <imcc> "indica que você está" <resultado>
        # Argumentos = peso(float), altura(float)  
    imc = peso/(altura**2)
    def classificar_imc(imc):
        resultado = ""
        if imc < 18.5:
            resultado = "com peso abaixo do normal"
        elif imc >= 18.5 and imc <= 24.9:
            resultado = "com peso normal"
        elif imc >= 24.9 and imc <= 29.9:
            resultado = "peso acima da média"
        elif imc >= 29.9 and imc <= 39.9:
            resultado = "obeso"
        elif imc > 39.9:
            resultado = "gravemente obeso"
        print(f"O seu IMC de {imc:00.2f} indica que você está {resultado}.")
    classificar_imc(imc)

def exercicio_43(inicio, fim, passo=10):
    # A função deve fazer uma tabela de conversão de Cº para Fº, com temperatura inica, temperatura final & os passos, onde o valor padrão de passo é 10 e exibir: <i> "Cº em Fahreinheit é" <f> "Fº"
        # Argumentos = inicio(int), fim(int), passo(int)
    for i in range(inicio, fim, passo):
        exercicio_17(i) # Função de conversão de Celsius para Fahreinheit, realizada no exercício 17.

def exercicio_44(valor_saque, saldo):
    # A função deve realizar um saque, retornar o valor do saldo ou impedir o saque se o valor do saldo for insuficiente e exibir: "Extrato" "Valor sacado" <valor_saque> "Saldo atual" <saldo-valor_saque> OU "Valor solicitado maior que o saldo da conta"
        # Argumentos = valor_saque(int), saldo(int)
    if valor_saque in range(saldo):
        saldo = saldo - valor_saque
        print(f"Extrato: \nValor Sacado: {valor_saque}R$\nSaldo Atual: {saldo}R$")
    else:
        print("Valor solicitado maior que o saldo da conta")
        
def exercicio_45(capital, taxa, tempo):
    # A função deve calcular uma taxa de juros simples, de acordo com capital, taxa e tempo. Após isso exibir: "O valor final é de:" <capital*((1+(taxa/100)*tempo)>
        # Argumentos = capita(int), taxa(int), tempo(int)
    print(f"O valor final é de {capital*(1+(taxa/100)*tempo):00.2f}R$")

def exercicio_46(capital, taxa, tempo):
    # A função deve calcular uma taxa de juros compostos, de acordo com capital, taxa e tempo. Após isso exibir: "O valor final é de:" <capital*(1+taxa)**tempo>
        # Argumentos = capita(int), taxa(int), tempo(int)
    print(f"O valor final é de {capital*(1+(taxa/100))**tempo:00.2f}R$")

def exercicio_47(inicio, fim, num):
    # A função deve contar quantos números múltiplos de um número existe dentro do escopo e exibir: "Há" <qtd_multi> "números múltiplos de" <num> "dentre os números" <inicio> "e" <fim>
        # Argumentos = inicio(int), fim(int), num(int)
    qtd_multi = 0
    for i in range(inicio, fim):
        if i % num == 0:
            qtd_multi += 1
    print(f"Há {qtd_multi} números múltiplos de {num} dentro os números {inicio} e {fim}.")

def exercicio_48(inicio, fim):
    # A Função deve identificar e somar números pares dentro do escopo e exibir: "A soma dos números pares dentre" <inicio> "e" <fim> "é de:" <soma>
        # Argumentos = inicio(int), fim(int)
        soma = 0
        for i in range(inicio, fim):
            if i % 2 == 0:
                soma = soma + i
        print(f"A soma dos números pares entre {inicio} a {fim} é de: {soma}")

def exercicio_49(inicio, fim):
    # A Função deve identificar e somar números ímpares dentro do escopo e exibir: "A soma dos números ímpares dentre" <inicio> "e" <fim> "é de:" <soma>
        # Argumentos = inicio(int), fim(int)
        soma = 0
        for i in range(inicio, fim):
            if i % 2 != 0:
                soma = soma + i
        print(f"A soma dos números ímpares entre {inicio} a {fim} é de: {soma}")

def exercicio_50(a,b,c):
    # A função deve identificar se os números informados são medidas válidas de um triângulo e também informar o tipo do triângulo e exibir: "Não é um triângulo válido!" OU "Seu triângulo é equilátero!" OU "Seu triângulo é isoceles" OU "Seu triângulo é escaleno"
        # Argumentos = a(int), b(int), c(int)
    if a == 0 or b == 0 or c == 0:
        print("Não é um triângulo válido!")
    elif a == b and b == c:
        print("Seu triângulo é equilátero!")
    elif a == b or b == c or c == a:
        print("Seu triângulo é isoceles")
    elif a != b and b != c and a != c:
        print("Seu triângulo é escaleno")



