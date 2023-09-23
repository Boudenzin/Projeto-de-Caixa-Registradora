# Lista com os códigos de barras, nomes dos produtos, preços e os tipos de pagamento

codigos = [7123456789012, 7987654321098, 7456789012345, 7321098765432, 7567890123456, 7890123456789, 7234567890123, 7678901234567, 7345678901234, 7789012345678]
produtos = ["Macarrão Espaguete", "Molho de Tomate", "Arroz Integral",  "Feijão Preto", "Leite Desnatado", "Pão de Forma Integral", "Iogurte Natural", "Cereal Matinal", "Salmão Fresco", "Maçãs Gala"]
precos = [2.99,1.49,3.25,2.75,1.99,4.49,2.29,3.99,10.99,0.79]
tiposdepagamento = ["CRÉDITO", "DÉBITO", "DINHEIRO"]

# Limite de quantos digitos a maquininhas= suporta para senha

limitededigitosdesenha = 4

# Importação da Biblioteca Random para randomizar a variável "codigoproduto"

from random import randint

# Definição de Variavéis

precototal = 0
ordemdoproduto = 0
precoproduto = 1
valordeparada = 0
respostaexecucao = "SIM"

# Print do Nome do Mercado

print ("Mercado Bom Todo")

# Esquema de Repetição para toda vez que o usuário quiser registrar algum novo produto ele conseguir, digitando "sim"

while (respostaexecucao == "SIM"):

    # Criação de um código de barras aleatório 
    
    codigoproduto = randint(0,999999999999)
    ordemdoproduto += 1
    
    #Bloco de verificação se o código está na lista
    
    while (codigoproduto not in codigos):
        codigoproduto = int(input(f"Produto {ordemdoproduto}: "))
        if (codigoproduto not in codigos):
            print ("Ops, acho que você errou a numeração do código de barras, tente novamente")
    
    # Pergunta de unidades e print de dados do código de barras        
    
    for ordemdalista in range (len(codigos)):
        if (codigoproduto == codigos[ordemdalista]):
            unidades = int(input(f"Quantas unidades de {produtos[ordemdalista]}: "))
            print (f"{(codigos[ordemdalista])}, {unidades}x {(produtos[ordemdalista])}, R$ {(precos[ordemdalista])} UN")
    
    # Execução de soma dos preços dos produtos inseridos por código de barra    
    
    precototal += (precos[0] * unidades)
    
    # Pergunta se o usuário quer continuar cadastrando mais produtos
    
    respostaexecucao = str.upper(input("Deseja iniciar outro registro? "))

# Término da Repetição e print do valor a ser pago

print (f"Total: R$ {precototal}")

# Pergunta do tipo de pagamento

formadepagamento = str.upper(input(f"Qual o método de pagamento? {tiposdepagamento[0]} / {tiposdepagamento[1]} / {tiposdepagamento[2]} "))

# Verificação se o que foi digitado está dentre as opções de pagamento

while formadepagamento not in tiposdepagamento:
    print ("Ops, acho que você inseriu a operação errada, tente novamente")
    formadepagamento = str.upper(input(f"Qual o método de pagamento? {tiposdepagamento[0]} / {tiposdepagamento[1]} / {tiposdepagamento[2]} "))    

# Simulação de Maquininha, com senhas delimitadas pelo programador

if (formadepagamento == tiposdepagamento[0]) or (formadepagamento == tiposdepagamento[1]):
    print ("Insira sua senha: ")
    senha = str(input())
    
    # Se o limite for ultrapassado, o sistema pedirá mais uma vez que coloque sua senha
    
    while ((len(senha) > limitededigitosdesenha)):
        print ("Sua senha é inválida, tente de novo")
        senha = str(input())
    print (f"Sua compra de R$ {precototal} foi efetuada com sucesso") 

# Opção com Dinheiro

else:         
    dinheirorecebido = float(input(f"{tiposdepagamento[2]}: R$ "))
    
    # Verificação se está faltando dinheiro
    
    while (dinheirorecebido < precototal):
        print (f"Está faltando dinheiro, faltam R$ {precototal - dinheirorecebido} para essa operação ser concluída")
        dinheirorecebido += float(input(f"{tiposdepagamento[2]} a mais: R$ "))    
    troco = dinheirorecebido - precototal
    print (f"Troco: R$ {troco:.2f}")
