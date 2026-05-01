from identificar_nivel_e_alerta import mensagem_alerta

nivel = int(input('Qual o nível do reservatório ? (1-5)'))
mensagem = mensagem_alerta(nivel)

print(f'O reservatório está no {mensagem}. Relatório encaminhado.')