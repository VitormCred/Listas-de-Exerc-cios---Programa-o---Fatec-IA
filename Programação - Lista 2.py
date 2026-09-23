# exercício 1
def exercicio_01():
    num1 = int(input("Favor inserir o primeiro número: "))
    num2 = int(input("Favor inserir o segundo número: "))
    if num1 == num2:
        print("Seus números são iguais!")

def exercicio_02():
    num1 = int(input("Favor inserir o primero número: "))
    num2 = int(input("Favor inserir o segundo número: "))
    if num1 > num2:
        print("O primeiro número é maior que o segundo!")

def exercicio_03():
    num1 = int(input("Favor inserir o primero número: "))
    num2 = int(input("Favor inserir o segundo número: "))
    if num1 != num2:
        print("Seus números são diferentes!")

def exercicio_04():
    num1 = int(input("Favor inserir o primero número: "))
    num2 = int(input("Favor inserir o segundo número: "))
    if num1 >= num2:
        print("O primeiro número é maior ou igual ao segundo!")

def exercicio_05():
    num1 = int(input("Favor inserir o primero número: "))
    num2 = int(input("Favor inserir o segundo número: "))
    if num1 <= num2:
        print("O primeiro número é menor ou igual ao segundo!")

def exercicio_06():
    idade = int(input("Favor informe sua idade: "))
    if idade >= 18:
        print("Você é maior de idade!")

def exercicio_07():
    salario = int(input("Favor informe seu salário: "))
    if salario > 1000:
        print("Seu salário é maior que 1000R$ (wow)")

def exercicio_08():
    salario = int(input("Favor informe seu salário: "))
    idade = int(input("Favor informe sua idade: "))
    if salario > 1000 and idade >= 18:
        print("Seu salário é maior que 1000R$ e sua idade é maior ou igual a 18 anos!")

def exercicio_09():
    salario = int(input("Favor informe seu salário: "))
    idade = int(input("Favor informe sua idade: "))
    if salario > 1000 or idade >= 18:
        print("Seu salário é maior que 1000R$ ou/e sua idade é maior ou igual a 18 anos!")

def exercicio_10():
    idade = int(input("Favor inserir sua idade: "))
    if idade < 18:
        print("Você é menor de idade!")

def exercicio_11():
    num1 = int(input("Favor inserir o 1º número: "))
    num2 = int(input("Favor inserir o 2º número: "))
    num3 = int(input("Favor inserir o 3º número: "))
    if num1 == num2 == num3:
        print("Seus números são iguais!")

def exercicio_12():
    num = int(input("Favor inserir um número: "))
    if num < 20 and num > 10:
        print("Seu número está entre 10 & 20!")

def exercicio_13():
    num = int(input("Favor inserir um número: "))
    if num < 20 or num > 10:
        print("Seu número está entre 10 & 20!")

def exercicio_14():
    num = int(input("Favor inserir um número: "))
    if not 10 > num < 20:
        print("Seu número está entre 10 & 20!")

def exercicio_15():
    media = int(input("Favor inserir sua média final: "))
    frequencia = int(input("Favor inserir sua frequência (em %): "))
    if media >= 6 and frequencia >= 75:
        print("Aprovado!")
    else:
        print("Reprovado!")

def exercicio_16():
    ano = int(input("Favor inserir um ano: "))
    if ano % 4 == 0:
        print("Esse ano é bissexto")
    else:
        print("Esse ano não é bissexto")

def exercicio_17():
    sexo = input("Favor inserir seu sexo (M/F): ")
    if sexo == "M" or sexo == "m":
        print("Você é do sexo masculino!")
    if sexo == "F" or sexo == "f":
        print("Você é do sexo feminino!")

def exercicio_18():
    senha = input("Favor inserir senha: ")
    if senha == "fatec123":
        print("Senha correta!")
    else:
        print("Senha incorreta")

def exercicio_19():
    num = int(input("Favor inserir um número:"))
    if num % 2 == 0 and num > 10:
        print("Seu número é par e maior que 10")
    else:
        print("Seu número não é par ou/e não é maior que 10")

def exercicio_20():
    lado1 = int(input("Favor inserir o primeiro lado do triângulo: "))
    lado2 = int(input("Favor inserir o segundo lado do triângulo: "))
    lado3 = int(input("Favor inserir o terceiro lado do triângulo: "))
    if (lado1+lado2) > lado3 and (lado1+lado3) > lado2 and (lado2+lado3) > lado1:
        print("Seu triângulo é válido!")
    else:
        print("Seu triângulo não é válido!")

def exercicio_21():
    num = int(input("Favor inserir um número: "))
    if num > 0:
        print("Seu número é positivo!")

def exercicio_22():
    idade = int(input("Favor inserir sua idade: "))
    if idade >= 18:
        print("Maior de idade!")

def exercicio_23():
    nota = int(input("Favor inserir sua nota: "))
    if nota >= 6:
        print("Aprovado!")

def exercicio_24():
    num = int(input("Favor inserir um número: "))
    if num % 5 == 0:
        print("Seu número é divisível por 5!")

def exercicio_25():
    senha = input("Favor inserir senha: ")
    if senha == "python2026":
        print("Acesso liberado!")

def exercicio_26():
    temp = int(input("Favor inserir a temperatura: "))
    if temp > 35:
        print("Alerta de calor!")

def exercicio_27():
    saldo = int(input("Favor informar o saldo da conta: "))
    if saldo < 0:
        print("Atenção: Saldo negativo!")

def exercicio_28():
    num = int(input("Favor inserir um número inteiro: "))
    if num > 0:
        print("O número é positivo!")
    else: 
        print("O número é negativo!")

def exercicio_29():
    idade = int(input("Favor informar sua idade: "))
    if idade >= 18:
        print("Maior de idade!")
    else:
        print("Menor de idade!")

def exercicio_30():
    nota = int(input("Favor informar a nota final: "))
    if nota >= 6:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

def exercicio_31():
    num1 = int(input("Favor informar o primeiro número: "))
    num2 = int(input("Favor informar o segundo número: "))
    if num1 > num2:
        print("O primeiro número é maior!")
    else:
        print("O segundo número é maior!")

def exercicio_32():
    num = int(input("Favor informar um número: "))
    if num % 2 == 0:
        print("Seu número é par!")
    else:
        print("Seu número é ímpar!")

def exercicio_33():
    valor = int(input("Favor informar o valor da compra: "))
    total = 0
    if valor > 100:
        total = valor * 0.9
        print(f"O valor final é de {total}R$")
    else: 
        total = valor
        print(f"O valor final é de {total}R$")

def exercicio_34():
    socio = input("O cliente é sócio da loja ? (S/N): ")
    if socio == "s" or socio == "S":
        print("O valor do ingresso é de 20R$")
    if socio == "n" or socio == "N":
        print("O valor do ingresso é de 40R$")

def exercicio_35():
    senha = input("Favor inserir senha: ")
    if senha == "batatinha123":
        print("Acesso liberado!")
    else:
        print("Acesso negado!")

def exercicio_36():
    nota = int(input("Favor inserir a nota do aluno: "))
    if nota >= 9:
        print("Nota A")
    elif nota < 9 and nota >= 7:
        print("Nota B")
    elif nota < 7 and nota >= 5:
        print("Nota C")
    else:
        print("Nota D")

def exercicio_37():
    idade = int(input("Favor insira sua idade: "))
    if idade < 12:
        print("Criança!")
    elif idade >= 12 and idade < 18:
        print("Adolescente")
    elif idade >= 18 and idade < 60:
        print("Adulto")
    else:
        print("Idoso")

def exercicio_38():
    num_mes = int(input("Favor inserir o número do mês: "))
    if num_mes == 12 or  num_mes <= 2:
        print("Verão")
    elif 3 <= num_mes <= 5:
        print("Outono")
    elif 6 <= num_mes <= 8:
        print("Inverno")
    elif 9 <= num_mes <= 11:
        print("Primavera")

def exercicio_39():
    peso = int(input("Favor informar seu peso: "))
    altura = int(input("Favor informar sua altura: "))
    imc = peso/(altura**2)
    if imc < 18.5:
        print("Abaixo do peso!")
    elif 18.5 <= imc < 25:
        print("Peso normal!")
    elif 25 <= imc < 30:
        print("Sobrepeso!")
    elif imc >= 30:
        print("Obesidade")

def exercicio_40():
    minutos = int(input("Favor informar a quantidade de minutos utilizados: "))
    valor = 0
    if minutos < 100:
        valor = minutos * 0.25
        print(f"O valor final é de {valor}R$")
    elif 100 > minutos <= 300:
        valor = minutos * 0.20
        print(f"O valor final é de {valor}R$")
    elif 300 < minutos <= 500:
        valor = minutos * 0.15
        print(f"O valor final é de {valor}R$")
    elif minutos > 500:
        valor = minutos * 0.1
        print(f"O valor final é de {valor}R$")

def exercicio_41():
    dia = int(input("Favor informar o número do dia: "))
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda-Feira")
    elif dia == 3:
        print("Terça-Feira")
    elif dia == 4:
        print("Quarta-Feira")
    elif dia == 5:
        print("Quinta-Feira")
    elif dia == 6:
        print("Sexta-Feira")
    elif dia == 7:
        print("Sábado")

def exercicio_42():
    nota = int(input("Favor inserir a nota final: "))
    faltas = int(input("Favor inserir o número de faltas: "))
    if faltas < 15:
        if nota >= 9:
            print("Nota A")
        elif nota < 9 and nota >= 7:
            print("Nota B")
        elif nota < 7 and nota >= 5:
            print("Nota C")
        else:
            print("Nota D")
    else: 
        print("Reprovado por faltas")

def exercicio_43():
    valor = int(input("Favor inserir o valor da compra: "))
    if valor <= 50:
        print(f"O valor final é de {valor}R$")
    elif 50 < valor <= 200:
        print(f"O valor final é de {int(valor*0.95)}R$")
    elif 200 < valor <= 500:
        print(f"O valor final é de {int(valor*0.90)}R$")
    elif valor > 500:
        print(f"O valor final é de {int(valor*0.85)}R$")

def exercicio_44():
    idade = int(input("Favor informar sua idade: "))
    sexo = input("agora informe seu sexo (F/M): ")
    if idade >= 18 and (sexo == "m" or sexo == "M"):
        print("Apto ao serviço militar!")

def exercicio_45():
    salario = int(input("Favor inserir seu salário: "))
    tempo = int(input("e também seu tempo de empresa (em anos): "))
    if salario < 2000 and tempo >= 5:
        print("Elegível a reajuste!")

def exercicio_46():
    nota1 = int(input("Favor inserir a primeira nota: "))
    nota2 = int(input(" e agora a segunda nota: "))
    freq = int(input("e agora a frequência do aluno (em %): "))
    if freq < 75:
        print("Aluno reprovado por faltas!")
    else:
        if (nota1+nota2)/2 >= 6:
            print("Aluno aprovado!")
        else:
            print("Aluno reprovado por notas!")
    
def exercicio_47():
    num1 = int(input("Favor inserir o primero número: "))
    num2 = int(input("segundo número: "))
    num3 = int(input("e terceiro número: "))
    if num1 > num2 and num1 > num3:
        print(f"{num1} é o maior número!")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} é o maior número!")
    elif num3 > num1 and num3 > num2:
        print(f"{num3} é o maior número")

def exercicio_48():
    ano = int(input("Favor informar o ano: "))
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print("O ano é bissexto!")
            else:
                print("O ano não é bissexto!")
        else:
            print("O ano não é bissexto!")
    else:
        print("O ano não é bissexto!")

def exercicio_49():
    temperatura = int(input("Favor informar a temperatura: "))
    umidade = int(input("Favor informar a umidade do ar (em %): "))
    if temperatura > 30:
        if umidade < 30:
            print("Alerta de incêndio!")
        else:
            print("Calor, mas sem risco de incêndio!")

def exercicio_50():
    valor = int(input("Favor informar o valor da compra: "))
    pag = input("e a forma de pagamento, cartão(c) ou dinheiro(d): ")
    if pag == "d" or pag == "D":
        print(f"O valor final é de {valor*0.9}R$")
    if pag == "c" or pag == "C":
        parcelas = int(input("Favor informar o número de parcelas, caso o mesmo seja maior que 3 há uma taxa de 2% ao mês: "))
        if parcelas <= 3:
            print(f"O valor final é de {valor}R$")
        else:
            print(f"O valor final é de {valor + ((valor*0.02)*parcelas)}R$")

