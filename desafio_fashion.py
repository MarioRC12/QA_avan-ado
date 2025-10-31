nome = (input("Coloque seu nome: "))
valor = int (input("Coloque o valor gasto: "))

if valor <= 250:
    print ("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")

elif valor >= 250 and valor <= 500:
    print ("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")

else:
    valor >= 500
    print ("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")