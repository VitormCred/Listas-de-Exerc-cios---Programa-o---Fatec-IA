#### QUARTA LISTA DE EXERCÍCIOS ###
Aluno = "Vitor Morgado Credendio"

### EXERCÍCIOS PARTE 1 ###
def saudacao():
    print("Olá, mundo!")

def exibir_nome(nome):
    print(f"Olá, {nome}")

def soma_simple(a, b):
    print(f"Olá, a soma dos números é {a+b}!")

def subtracao_simple(a, b):
    print(f"Olá, a subtração dos números é {a-b}!")

def mult_simple(a, b):
    print(f"Olá, a multiplicação dos números é {a*b}!")

def div_simple(a, b):
    print(f"Olá, a divisão dos números é {a/b}!")

def dobro(a):
    print(f"Olá, o dobro do número é {a*2}!")

def triplo(a):
    print(f"Olá, o triplo do número é {a*3}!")

def metade(a):
    print(f"Olá, a metade do número é {a/2}!")

def quadrado(a):
    print(f"Olá, o quadrado do número é {a*a}!")

def cubo(a):
    print(f"Olá, o cubo do número é {a*a*a}!")

def media_aritimetica(a, b):
    print(f"Olá, a média aritimética dos números é {(a+b)/2}!")

def par_impar(a):
    if a % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

def area_retangulo(a, b):
    print(f"A área do retángulo é {a*b}")

def perimetro_triangulo(a, b):
    print(f"O perímetro do retangulo é {(a+b)*2}!")

def conv_fahr_cel(a):
    print(f"A temperatura em {a}F em Celsius é {int((a-32)*(5/9))}Cº")

def rept_char(a, b):
    i = 0
    texto = ""
    for i in range (a):
        texto = texto + b
        i = i + 1
    print(texto)
  
def maioridade(a):
    if a >= 18:
        print("Você é maior de idade")
    else:
        print("Você não é maior de idade")

### PARTE 2 ###

def saudacao_perso(nome, saudacao="olá"):
    ## 'nome' é argumento requerido, 'saudacao' é argumento opcional
    print(f"{saudacao}, {nome}")

def potencia(num, exponencial=2):
    i = 0
    initial = num
    for i in range (1, exponencial):
        resolucao = num * initial
        num = resolucao
        i = i + 1
    print(num)

def desconto(valor, desconto=10):
    print(f"O valor com desconto é {float(valor*(1-(desconto/100)))}R$")

def tabuada(num, multiplo=10):
    i = 1
    for i in range(1,multiplo):
        calc = num * i
        i = i + 1
        print(calc)
    
def area_circulo(raio):
    print(f"A área do circulo é {(raio*raio)*3.14}")

def saudacao_por_hora(hora):
    if hora in range(6,12):
        print("Bom, dia!")
    elif hora in range(12, 18):
        print("Boa tarde!")
    elif hora in range(5) or hora in range(19,23):
        print("Boa noite!")

def maior(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)

def menor(a, b, c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    elif c < a and c < b:
        print(c)

def nota(nta):
    if nta >=9:
        print("Sua nota é A")
    elif nta >= 7 and nta <= 9:
        print("Sua nota é B")
    elif nta >= 5 and nta <= 7:
        print("Sua nota é C")
    else:
        print("Sua nota é C")

def piramide(linhas):
    i = 0
    char = ""
    for i in range(linhas):
        char = char + "\n" + ((linhas-i) * " " + i * "*" + "*" + i * "*" + (linhas-i) * " ")
        i = i + 1
    
    print(char)

### PARTE 2 ###
# Escopo de variáveis Locais & Globais, parâmetros nomeados fora de ordem, funções que chamam outras funções, laços e validações dentro de funções
contador = 0
def cont_global(num):
    global contador
    for i in range (num):
        contador = contador + 1
    print(contador)
        
def media_ponderada(nota1, nota2, peso1=1, peso2=1):
    print(f"A nota final é de {(nota1*peso1)+(nota2*peso2)/(peso1+peso2)}!")
    
def num_primo(num):
    i = 2
    for i in range(i, num):
        if num % i == 0:
            print(f"O número {num} não é primo!")
            break
        else:
            print(f"O número {num} é primo!")
            break
        
def fatorial_iterativo(num):
    i = 1
    fat = num
    while i < num:
        fat = fat * (num-i)
        i = i + 1
        
    print(fat)

def mdc(a,b):
    if a > b:
        i = a
    else:
        i = b
    while i != 0 and (a % i != 0 or b % i != 0):
        i = i - 1
    print(i)
    return(i)

def mmc(a,b):
    mmc = (a*b)/mdc(a,b)
    print(mmc)
    return mmc

def soma_digitos(numero):
    digitos = []
    soma = 0
    for i in str(numero):
        digitos.append(i)
    for char in digitos:
        soma = soma + int(char)
    print(soma)

def inverter_numero(numero):
    digitos = []
    final = ""
    for i in str(numero):
        digitos.append(i)
    digitos.reverse()
    for char in digitos:
        final = final + char
    print(final)

def conta_vogais(palavra):
    letras = []
    i = 0
    soma = 0
    vogais = ["a","e","i","o","u"]
    for char in palavra:
        letras.append(char)
    for i in range(len(vogais)):
        soma += letras.count(vogais[i])
        i = i + 1
    print(soma)
    
    
def palindromo(palavra):
    letras = []
    final = ""
    for i in palavra:
        letras.append(i)
    letras.reverse()
    for char in letras:
        final = final + char
    if final == palavra:
        print("é palíndromo")
    else:
        print("não é palíndromo")


def validar_senha(senha_correta, tentativas=3):
    senha = input("Favor inserir a senha: ")
    i = 1
    while senha != senha_correta:
        print("senha incorreta digitada, tente novamente")
        print(f"Número de tentativas restante {3-i}")
        if i in range(tentativas):
            senha = input("Favor inserir a senha correta: ")
            i = i + 1
        else: 
            print("Número máximo de tentativas excedido!")
            break
    if senha == senha_correta:
        print("Senha correta, acesso liberado!")
    
    
def calcular_imc(peso, altura):
    imcc = peso/(altura*altura)
    def classificar_imc(imcc):
        if imcc > 18.5:
            print("Abaixo do peso")
        elif imcc >= 18.5 and imcc <= 24.9:
            print("Peso adequado")
        elif imcc >= 24.9 and imcc <= 29.9:
            print("Sobrepeso")
        elif imcc >= 29.9 and imcc <= 39.9:
            print("Obesidade")
        else:
            print("Obesidade Grave")
    classificar_imc(imcc)

def tabela_conversao_temp(inicio, fim, passo=10):
    for i in range(inicio, fim, passo):
        conv_fahr_cel(i)
        
def sacar(valor_saque, saldo):
    if valor_saque in range(saldo):
        saldo = saldo - valor_saque
        print(f"Extrato: \nValor Sacado: {valor_saque}R$\nSaldo Atual: {saldo}R$")
    else:
        print("Valor solicitado maior que o montante em conta")
        
def juros_simples(capital, taxa, tempo):
    print(f"O valor final é de {int((capital)*((1+(taxa/100)*tempo)))}R$")

def juros_compostos(capital, taxa, tempo):
    print(f"O valor final é de {int(capital*(1+taxa)**tempo)}R$")

def conta_mult(inicio, fim, multiplo):
    i = 0
    contador = 0
    for i in range(inicio, fim):
        if i % multiplo == 0:
            contador += 1
            i += 1
        else:
            i += 1
    print(contador)
    
def soma_pares(num):
    i = 0
    soma = 0
    for i in range(num):
        if i % 2 == 0:
            soma = soma + i
            i = i + 1
        else:
            i = i + 1
    print(soma)
    
def soma_impares(num):
    i = 0
    soma = 0
    for i in range(num):
        if i % 2 != 0:
            soma = soma + i
            i = i + 1
        else:
            i = i + 1
    print(soma)
    
def class_triangulo(a,b,c):
    if a == 0 or b == 0 or c == 0:
        print("Não é um triângulo válido!")
    elif a == b and b == c:
        print("Seu triângulo é equilátero!")
    elif a == b or b == c or c == a:
        print("Seu triângulo é isoceles")
    else:
        print("Seu triângulo é escaleno")