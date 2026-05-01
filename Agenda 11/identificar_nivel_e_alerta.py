from colorama import Fore, Style
niveis_e_alertas = [
    'Nível 1 - Muito baixo (crítico)',
    'Nível 2 - Baixo',
    'Nível 3 - Médio',
    'Nível 4 - Alto',
   'Nível 5 - Muito alto (alerta)'
    ]

def mensagem_alerta(nivel):
    nivel_reservatorio = 'Código indefinido'

    if nivel == 1:
        nivel_reservatorio = Fore.RED  + niveis_e_alertas[0] + Style.RESET_ALL
    elif nivel == 2:
        nivel_reservatorio = Fore.YELLOW + niveis_e_alertas[1] + Style.RESET_ALL
    elif nivel == 3:
            nivel_reservatorio = Fore.GREEN + niveis_e_alertas[2] + Style.RESET_ALL
    elif nivel == 4:
            nivel_reservatorio = Fore.CYAN + niveis_e_alertas[3] + Style.RESET_ALL
    elif nivel == 5:
            nivel_reservatorio = Fore.BLUE + niveis_e_alertas[4] + Style.RESET_ALL

    return nivel_reservatorio
    