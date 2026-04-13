print("Essa é a avaliação de satisfação, por favor, preencha os dados abaixo...")
contRuim = 0 #Inicia a váriavel para contar as avaliações ruins
contExcelente = 0 #Incicia a váriavel para contar as avaliações excelentes


for contador in range(50): #Laço de repetição for que se repete por 50 vezes
    nome = input('Insira seu nome!') #Pergunta o nome do usuário
    idade = int(input('Insira sua idade!')) #Pergunta a idade do usuário
    opiniao = int(input("Insira sua opinão: 1 (EXCELENTE), 2 (BOM) ou 3 (RUIM)")) #Pergunta a opinião do usuário dentre as opções disponíveis

    if(opiniao == 1): #Compara se a opinião é igual a 1
        print('Obrigado por sua participação')
        contExcelente = contExcelente + 1 #Incrementa 1 unidade ao contador excelente

    elif(opiniao == 2): #Compara se a opinião é igual a 2, não faz nada se resultado for true
        print('Obrigado por sua participação') 

    elif(opiniao == 3): #Compara se a opinião é igual a 3
        print('Obrigado por sua participação')
        contRuim = contRuim + 1 #Incremente 1 unidade ao contador ruim

    else:
        print('Opinião não contabilizada') #Se usuário não inserir nenhuma opção válida, não contabiliza e continua a execução do loop

#Exibe o resultado final
print(f'Foram contabilizadas {contExcelente} opiniões excelentes')
print(f'Foram contabilizadas {contRuim} opiniões ruins')