import os
from datetime import datetime

def verfica_hora():
    hora = datetime.now().strftime("%H:%M")
    frase = f'Agora são {hora}'
    return frase

# Funções de desligamento (3600 = 1 hora)
def desligar_5_minutos():
    os.system('shutdown /s /t 300')  # 300 segundos = 5 minutos
    return 'Desligamento agendado para 5 minutos.'

def desligar_10_minutos():
    os.system('shutdown /s /t 600')  # 600 segundos = 10 minutos
    return 'Desligamento agendado para 10 minutos.'

def desligar_15_minutos():
    os.system('shutdown /s /t 900')  # 900 segundos = 15 minutos
    return 'Desligamento agendado para 15 minutos.'

def cancela_desligamento():
    os.system('shutdown /a')  # Cancela o desligamento
    return 'Desligamento cancelado.'