idade_em_humano =  int (input ('Qual a idade humana do Pet? '))
nome_do_pet =  (input ('Qual o nome do Pet? '))
porte_do_pet = (input("Qual o Porte do Pet? "))
banhos = int (input ('Quantos banhos o Pet toma por ano? '))

idade_do_cachorro = (idade_em_humano * 7)

print (f'A idade do Pet é {idade_do_cachorro}')

grande_p = int (75 + 20)
medio_p = int (60 + 15)
pequeno_p = int (75 + 5)


if (porte_do_pet == 'Grande' or "grande"):
    valor_banho = 75
    custo_banho = 20

elif (porte_do_pet == "Medio" or "medio"):
    valor_banho = 75
    custo_banho = 20
    
elif (porte_do_pet == "Pequeno" or "pequeno"):
    valor_banho = 75
    custo_banho = 20

else:
    print ("Porte Invalido, informe pequeno, medio ou grande")
    exit()

lucro = (valor_banho - custo_banho) * banhos

print (f"Olá, {nome_do_pet} tem {idade_do_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro}")