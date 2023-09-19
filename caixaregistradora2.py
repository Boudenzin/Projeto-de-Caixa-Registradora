codigos = [7123456789012, 7987654321098, 7456789012345, 7321098765432, 7567890123456, 7890123456789, 7234567890123, 7678901234567, 7345678901234, 7789012345678]
produtos = ["Macarrão Espaguete", "Molho de Tomate", "Arroz Integral",  "Feijão Preto", "Leite Desnatado", "Pão de Forma Integral", "Iogurte Natural", "Cereal Matinal", "Salmão Fresco", "Maçãs Gala"]
precos = [2.99,1.49,3.25,2.75,1.99,4.49,2.29,3.99,10.99,0.79]

precototal = 0
ordemdoproduto = 0
precoproduto = 1
valordeparada = 0
respostaexecucao = "SIM"
print ("Mercado Bom Todo")
while (respostaexecucao == "SIM"):
    codigoproduto = 7777777777777
    ordemdoproduto += 1
    while (codigoproduto not in codigos):
        codigoproduto = int(input(f"Produto {ordemdoproduto}: "))
        if (codigoproduto not in codigos):
            print ("Ops, acho que você errou a numeração do código de barras, tente novamente")
    for ordemdalista in range (len(codigos)):
        if (codigoproduto == codigos[ordemdalista]):
            unidades = int(input(f"Quantas unidades de {produtos[ordemdalista]}: "))
            print (f"{(codigos[ordemdalista])}, {unidades}x {(produtos[ordemdalista])}, R$ {(precos[ordemdalista])} UN")    
    precototal += (precos[0] * unidades)
    respostaexecucao = str.upper(input("Deseja iniciar outro registro? "))
print (f"Total: R$ {precototal}")
formadepagamento = str.upper(input("Qual o método de pagamento? (CRÉDITO / DÉBITO / DINHEIRO) "))
if (formadepagamento == "CRÉDITO") or (formadepagamento == "DÉBITO"):
    print ("Insira sua senha: ")
    senha = str(input())
    while ((len(senha) > 4)):
        print ("Sua senha é inválida, tente de novo")
        senha = str(input())
    print (f"Sua compra de R$ {precototal} foi efetuada com sucesso") 
else:         
    dinheirorecebido = float(input("Dinheiro: R$ "))
    troco = dinheirorecebido - precototal
    print (f"Troco: R$ {troco:.2f}")
