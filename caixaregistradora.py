
precototal = 0
ordemdoproduto = 0
precoproduto = 1
valordeparada = 0
print ("Mercado Bom Todo")
while (precoproduto != valordeparada):
    ordemdoproduto += 1
    precoproduto = float(input(f"Produto {ordemdoproduto}: R$ "))
    precototal += precoproduto
print (f"Total: R$ {precototal}")
dinheirorecebido = float(input("Dinheiro: "))
troco = dinheirorecebido - precototal
print (f"Troco: R$ {troco}")
   
    