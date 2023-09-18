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
    ordemdoproduto += 1
    codigoproduto = int(input(f"Produto {ordemdoproduto}: "))
    if (codigoproduto) in codigos:
        for ordemdalista in range (len(codigos)):
            if (codigoproduto == codigos[ordemdalista]):
                print (f"{(codigos[ordemdalista])}, {(produtos[ordemdalista])}, R$ {(precos[ordemdalista])}")
    precototal += precos[0]
    respostaexecucao = str.upper(input("Deseja reiniciar outro registro? "))
print (f"Total: R$ {precototal}")
dinheirorecebido = float(input("Dinheiro: R$ "))
troco = dinheirorecebido - precototal
print (f"Troco: R$ {troco:.2f}")
