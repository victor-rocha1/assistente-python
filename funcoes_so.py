import os
from datetime import datetime

def verifica_hora():
    hora = datetime.now().strftime("%H:%M")
    return f"Agora são {hora}"

def desligar_5_minutos():
    os.system('shutdown /s /t 300')
    return 'Desligamento agendado para 5 minutos.'

def desligar_10_minutos():
    os.system('shutdown /s /t 600')
    return 'Desligamento agendado para 10 minutos.'

def desligar_15_minutos():
    os.system('shutdown /s /t 900')
    return 'Desligamento agendado para 15 minutos.'

def cancela_desligamento():
    os.system('shutdown /a')
    return 'O desligamento foi cancelado.'