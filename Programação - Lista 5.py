def exercicio_01():
    nota_lab = int(input("Nota do trabalho de laboratório: "))
    nota_av = int(input("Nota da avaliação semestral: "))
    nota_exame = int(input("Nota do exame final: "))
    media = ((nota_lab*2) + (nota_av*3) + (nota_exame*5))/(10)
    print(media)
    if media >= 8:
        print("Nota A")
    elif 7.9 >= media >= 7:
        print("Nota B")
    elif 6.9 >= media >= 6:
        print("Nota C")
    elif 5.9 >= media >= 5:
        print("Nota D")
    elif 4.9 >= media:
        print("Nota E")

def exercicio_02():
    dia = int(input("Favor inserir o dia do mês: "))        
    mes = int(input("Inserir o mês: "))-1 # O range da lista é de 0 até n (onde n é maior número do índice)
    ano = int(input("Inserir o ano: "))
    meses = ["Janeiro","Fevereiro","Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro","Outubro","Novembro","Dezembro"]
    print(f"{dia} de {meses[mes]} de {ano}")

def exercicio_03():
    print("Favor selecionar seu cargo:\n1 - Escrituário\n2 - Secretário\n3 - Caixa\n4 - Gerente\n5 - Diretor")
    cargo = int(input(""))-1
    salarios = [2_500, 3_200, 3_800, 7.500, 12_000]
    beneficios = [300, 450, 600, 1_000, 2_000]
    taxas = [0.08, 0.1, 0.12, 0.15, 0.2]
    print(f"O salário líquido é de {(salarios[cargo]+beneficios[cargo])-((salarios[cargo]+beneficios[cargo])*taxas[cargo]):00.2f}R$")

def exercicio_04():
    idade = int(input("Favor inserir sua idade: "))
    if idade < 14:
        print("Não pode entrar!")
    elif 14 <= idade < 18:
        print("Pode entrar acompanhado dos pais e não pode beber!")
    elif idade >= 18:
        print("Pode entrar e pode beber!")
    
def exercicio_05():
    salario = float(input("Favor inserir o salário: "))
    if salario <= 2_112:
        aliquota = 0.0
        deducao = 0
    elif 2_112.01 <= salario <= 2_826.65:
        aliquota = 0.075
        deducao = 158.40
    elif 2_826.66 <= salario <= 3_751.05:
        aliquota = 0.15
        deducao = 370.40
    elif 3_751.06 <= salario <= 4_664.68:
        aliquota = 0.225
        deducao = 651.73
    elif salario > 4_664.68:
        aliquota = 0.275
        deducao = 884.96
    print(f"O imposto de renda a pagar é de {(salario*aliquota)-deducao:00.2f}R$")

def exercicio_06():
    idade = int(input("Favor inserir sua idade para a classificação de escoteiro: "))
    if 6 <= idade <= 10:
        print("De acordo com sua idade, você é lobinho!")
    elif 10 < idade <= 14:
        print("De acordo com sua idade, você é escoteiro!")
    elif 14 < idade <= 17:
        print("De acordo com sua idade, você é sênior!")
    elif 17 < idade <= 21:
        print("De acordo com sua idade, você é pioneiro!")
    elif 21 < idade:
        print("De acordo com sua idade, você é líder!")
    else:
        print("Erro, crianças com menos de 6 anos de idade não são permitidas")

def exercicio_07():
    inicial = int(input("Favor digitar um número inicial: "))
    passo = int(input("informe agora, quantos números devemos percorrer a partir do número inicial: "))
    for i in range(inicial, inicial+passo, 1):
        soma = 1
        for u in range(1, i+1, 1):
            fatorial = soma * u
            soma = fatorial
        print(f"{i} e seu fatorial é {soma}")

def exercicio_08():
    soma = 0
    for i in range(0, 101,2):
        soma += i
    print(soma)

def exercicio_09():
    for i in range(1, 7, 1):
        nota1 = int(input("Favor inserir a primeira nota: "))
        nota2 = int(input("inserir a segunda nota: "))
        media = (nota1+nota2)/2
        if  media <= 3:
            print("Aluno reprovado!")
        elif 3 < media <= 7:
            print("Aluno de exame!")
        elif media >= 7:
            print("Aluno aprovado!")

def exercicio_10():
    soma_id_mulheres = 0
    soma_id_homens = 0
    qtd_mulheres = 0
    qtd_homens = 0
    for i in range (1, 11, 1):
        sexo = input("Favor inserir seu sexo (M/F): ")
        idade = int(input("Favor inserir sua idade: "))
        if sexo == "F" or sexo == "f":
            qtd_mulheres += 1
            soma_id_mulheres += idade
        elif sexo == "M" or sexo == "m":
            qtd_homens += 1
            soma_id_homens += idade
    print(f"A quantidade de mulheres é de {qtd_homens} e a média de idade é de {(soma_id_homens/qtd_homens):00.2f}!")
    print(f"A quantidade de homens é de {qtd_homens} e a média de idade é de {(soma_id_homens/qtd_homens):00.2f}!")
