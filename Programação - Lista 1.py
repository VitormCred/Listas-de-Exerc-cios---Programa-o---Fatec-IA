def exercicio_01():
    # trocar a variável "nome" para o seu (caso copie o código)
    nome = "Vitor Morgado Credendio"
  
    print(f"Meu nome é {nome}")
    print("Meu curso é Inteligência Artificil")

def exercicio_02():
    print("0   0")
    print("  v  ")
    print(" ... ")

def exercicio_03():
    print("5x1=5")
    print("5x2=10")
    print("5x3=15")
    print("5x4=20")
    print("5x5=25")
    print("5x6=30")
    print("5x7=35")
    print("5x8=40")
    print("5x9=45")
    print("5x10=50")

def exercicio_04():
    nome = input("Favor inserir seu nome: ")
    print("Seja bem vindo " + nome + "!")

def exercicio_05():
    cidade = input("Qual é sua cidade natal ? ")
    time = input("e qual é seu time favorito ? ")
    print("Você nasceu em: " + cidade +" e seu time favorito é: " + time)

def exercicio_06():
    nome = input("Favor inserir seu nome: ")
    cor_favorita = input("e qual é sua cor favorita ? ")
    comida_favorita = input("por fim, sua comida favorita: ")
    print("Olá, eu sou:" + nome)
    print("minha cor favorita é " + cor_favorita + " e minha comida favorita é " + comida_favorita + "!")

def exercicio_07():
    ano = int(input("Qual é seu ano de nascimento ?: "))
    idade = 2026 - ano
    idade_str = str(idade)
    print("Você tem " + idade_str + " anos de idade!")

def exercicio_08():
    altura = input("Qual é sua altura (em cm): ")
    altura_flt = float(altura)
    print("Sua altura é " + altura + " metros!")

def exercicio_09():
    num1 = input("Favor inserir o primeiro número: ")
    num2 = input("e agora inserir o segundo número: ")
    num1_int = int(num1)
    num2_int = int(num2)
    soma_str = str(num1_int+num2_int)
    print("A soma dos números é " + soma_str)

def exercicio_10():
    preco = float(input("Favor inserir o valor do produto (unitário): "))
    qtd = int(input("E agora inserir a quantidade desejada: "))
    total_str = str(preco*qtd)
    print("O valor total é de "+ total_str +"R$")

def exercicio_11():
    num1 = int(input("Favor inserir o primeiro número: "))
    num2 = int(input("E agora inserir o segundo número: "))
    soma = str(num1 + num2)
    sub = str(num1 - num2)
    mult = str(num1 * num2)
    div = str(num1 / num2)
    print("A soma dos números é: "+ soma)
    print("A subtração do números é: "+ sub)
    print("A multiplicação dos números é: "+ mult)
    print("A divisão dos números é: "+ div)

def exercicio_12():
    num = int(input("Favor inserir um número inteiro: "))
    dobro = str(num*2)
    triplo = str(num*3)
    metade = str(num/2)
    print("O dobro do número inserido é: "+ dobro) 
    print("O triplo do número inserido é: "+ triplo)
    print("A metade do número inserido é: "+metade)

def exercicio_13():
    nota1 = int(input("Favor inserir a primeira nota: "))
    nota2 = int(input("E a segundan nota: "))
    media_str = str((nota1+nota2)/2)
    print("A média aritimética é "+ media_str)

def exercicio_14():
    valor = int(input("Favor inserir o valor do lado do quadrado: "))
    area_str = str(valor*valor)
    perimetro_str = str(valor*4)
    print("A área do quadrado é de: "+area_str)
    print("O perímetro do quadrado é de: "+perimetro_str)


def exercicio_15():
    base = int(input("Favor informar o valor da base do triângulo: "))
    altura = int(input("E favor informar o valor da altura do triângulo: "))
    area_str = str((base*altura)/2)
    print("A área do triângulo é de: "+area_str)

def exercicio_16():
    salario = int(input("Favor inserir seu salário: "))
    aumento = int(input("e a porcentagem de aumento: "))
    salario_final_str = str(salario*(aumento/100)+salario)
    print("O salário com aumento é de: "+ salario_final_str +"R$")

def exercicio_17():
    reais = int(input("Favor inserir o valor em reais para converter a dolar: "))
    dolar_str = str(reais/5)
    print("O valor em dólares é "+ dolar_str +"$")

def exercicio_18():
    nome = input("Qual é seu nome ? ")
    idade = int(input("E qual é sua idade ? "))
    ano_centenario_str = str((100-idade)+2026)
    print("Olá "+ nome +", você completará 100 anos no ano de "+ ano_centenario_str)

def exercicio_19():
    horas = int(input("Favor informar o número de horas trabalhadas no mês: "))
    val_hora = float(input("e agora informar o valor recebido por hora: "))
    salario_str = str(horas*val_hora)
    print("O seu salário bruto esse mês é de "+ salario_str +"R$")

def exercicio_20():
    nome = input("Favor inserir seu nome: ")
    idade = input("inserir sua idade: ")
    nota = input("e agora inserir sua nota final: ")
    print("\n    - CADASTRO DE ALUNO -    ")
    print("Nome: "+ nome)
    print("Idade: "+ idade)
    print("Nota final: "+ nota)
    print("\n")
