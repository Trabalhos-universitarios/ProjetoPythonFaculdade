# Projeto estruturado para aperfeiçoamento de lógica da programação

#cria linhas para separar o códico na hora da compilação e ficar mais facíl entendimento
def lin():
    print('_' * 30)


# semana 2 etapa 1 se apresentando e pedindo alguns dados do cliente 
def obter_limite():
    print ('Olá, seja bem-vindo a loja variados store, meu nome é Johnny Carvalho e eu estou aqui para te ajudar.')
    lin()
    print ('É um prazer ter você como nosso cliente, para isso iremos fazer um breve cadastro.')
    lin()
    print ('Iremos fazer uma breve análise de crédito para você, precisamos que forneça alguns dados pessoais para continuar:')
    lin()
    # abaixo segue os dados do cliente
    cargo = input ('Qual é o seu cargo na empresa aonde trabalha? ')
    print (cargo)
    lin()
    salario = float(input('Qual é o seu salário mensal atual? R$ '))
    print ('R$ {:.2f}'.format(salario))
    lin()
    #semana 3 etapa 2
    # abaixo segue a data de nascimento
    print('digite a data do seu nascimento separado entre dia, mês e ano: ')
    dia = input('dia: ')
    mes = input('mes: ')
    ano = int(input('ano: '))
    # calculo para saber a idade
    ano_atual = int(2020)
    lin()
    print('A data do seu nascimento é: {}/{}/{}'.format(dia, mes, ano))
    lin()
    idade = int(ano_atual-ano)
    lin()
    print ('você tem {} anos de idade'.format(idade))
    lin()
    # calculo para a análise de crédito
    x = float(idade / 1000)
    y = float(salario * x)
    z = int(100)
    credito = float(y + z)
    print('De acordo com os dados fornecidos lhe informamos que seu limite de credito é de: R${:.2f}'.format(credito))
    lin()
    return credito, idade


# semana 4 etapa 3 pedindo ao cliente que digite o nome do produto e o preço dele
def verificar_produto(limite):
    produto = input('Digite o nome de um produto escolhido: ')
    lin()
    valor = float(input('Digite o valor desse item: '))
    lin()
    print('O produto é um(a) {} e o valor dele é R${} reais'.format(produto, valor,))
    limite_disponivel = limite - valor
    print('Seu limite atual é de R$ {}'.format(limite_disponivel))
    lin()
    # calculo da porcentagem para ver se libera ou não o produto para o cliente
    percentual = float((valor) / (limite)) * 100
    lin()
    if percentual<=60:
        print('compra liberada, você utilizou {:.2f} % do seu limite'.format(percentual))
        lin()
    elif 60< percentual <90: 
        print('O seu produto irá utilizar {:.2f} % do seu limite\nNesse caso podemos liberar ao parcelar em 2 vezes!'.format(percentual))
        lin()
    elif 90< percentual <100:
        print('O seu produto irá utilizar {:.2f} % do seu limite\nNesse caso podemos liberar ao parcelar em 3 ou mais vezes!'.format(percentual))
        lin()
    else:
        print('Seu limite excedeu!\nEle utilizou {:.2f}% do seu limite total'.format(percentual))
        
                # abaixo segue o calculo para desconto ao cliente
    meu_nome = ('JohnnyEldodeCarvalho')
    numeros_meu_nome = len(meu_nome)
    primeiro_nome = ('Johnny')
    numero_primeiro_nome = float(len(primeiro_nome))
    lin()
    soma_idade_nome = int((idade) + (numeros_meu_nome))
    lin()
    desconto = float((valor) - (numero_primeiro_nome))
    if valor <=soma_idade_nome:
        print('Parabéns você acaba de ganhar um desconto de R${:.2f} na sua compra\nAgora o valor da sua compra é de R${:.2f} reais!'.format(numero_primeiro_nome, desconto))
        lin()
    return valor


#calcula limite disponível para gasto
def limite_disponivel():
    a = limite - valor
    print('Seu limite agora é de R$ {:.2f}'.format(a))
    return a


limite, idade = obter_limite()
valor = verificar_produto(limite)
disponivel = limite_disponivel()
if disponivel > 0:
    pergunta = str(input('Deseja cadastrar mais algum produto? \nDigite [s] para sim e [n] para não: '))
    lin()
    soma = 0
    if (pergunta == 's'):
        n = int(input('Quantos produtos o sr(a) deseja cadastrar?\nDigite aqui: '))
        lin()
        for i in range(n):
            prod = input('Digite o nome do {}º produto :'.format(i+1))
            lin()
            val = float(input('Digite o valor do {}º produto : '.format(i+1)))
            soma += val
            disp = disponivel - soma
            lin()
            print('Seu limite disponivel é: R$ {:.2f}'.format(disp))
            lin()
            if (soma > disponivel):
                print('limite excedido!\nObrigado volte sempre!', end='\n')
                lin()
                break
            print(end='\n')
    else:
        print('***Nós agradecemos a sua preferência***\n\n***Volte sempre!***')
else:
    print('###limite excedido!###\n***Obrigado volte sempre!***', end='\n')
