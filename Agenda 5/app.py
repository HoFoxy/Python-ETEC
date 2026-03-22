aparelho = input('Qual o aparelho ?')
potenciaAparelho = int(input('Insira a potência do aparelho em Watts'))
usoDiarioHoras = int(input('Insira o tempo médio que o aparelho permanece ligado em horas'))
consumoMensal = (potenciaAparelho * usoDiarioHoras * 30) / 1000
gastoMensal = consumoMensal * 0.72

print(f'''

    ° Aparelho medido: {aparelho}
    ° Consumo estimado: {consumoMensal:.2f} kwh
    ° Gasto mensal estimado: R${gastoMensal:.2f}

''')

input('Pressione algo para sair')