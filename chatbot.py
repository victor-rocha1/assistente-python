from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sys
import time
import os
import tempfile
import funcoes_so
import funcoes_noticias
import funcoes_moedas

# Função principal
def main():
    cria_audio("Sou seu assistente. Em que posso te ajudar?")
    while True:
        monitora_audio()

# Função que cria o áudio (converte texto para voz)
def cria_audio(mensagem):
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio:
        tts = gTTS(mensagem, lang='pt-br')
        tts.save(temp_audio.name)
        playsound(temp_audio.name)

# Função que cria o áudio das notícias com espaçamento
def cria_audio_noticias():
    noticias = funcoes_noticias.ultima_noticias()
    for noticia in noticias:
        cria_audio(noticia)
        time.sleep(2)  # Pausa de 2 segundos entre as notícias

# Microfone (voz para texto)
def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga alguma coisa...")
            try:
                audio = recon.listen(source, timeout=5, phrase_time_limit=5)
                mensagem = recon.recognize_google(audio, language='pt-br').lower()
                print("Você disse:", mensagem)
                executa_comandos(mensagem)
                break
            except sr.UnknownValueError:
                print("Desculpe, não entendi o que você disse. Tente novamente.")
            except sr.RequestError:
                print("Erro de conexão com o serviço de reconhecimento de fala.")
                break

# Executa os comandos baseados no reconhecimento de voz
def executa_comandos(acao):
    if 'fechar assistente' in acao:
        sys.exit()
    elif 'horas' in acao:
        cria_audio(funcoes_so.verifica_hora())
    elif 'desligue em 5' in acao:
        cria_audio(funcoes_so.desligar_5_minutos())
    elif 'desligue em 10' in acao:
        cria_audio(funcoes_so.desligar_10_minutos())
    elif 'desligue em 15' in acao:
        cria_audio(funcoes_so.desligar_15_minutos())
    elif 'cancele' in acao or 'cancelar' in acao:
        cria_audio(funcoes_so.cancela_desligamento())
    elif 'notícias' in acao:
        cria_audio_noticias()
    elif 'cotação' in acao and 'dólar' in acao:
        cria_audio(funcoes_moedas.cotacao_moeda('Dólar'))
    elif 'cotação' in acao and 'euro' in acao:
        cria_audio(funcoes_moedas.cotacao_moeda('Euro'))
    elif 'cotação' in acao and 'bitcoin' in acao:
        cria_audio(funcoes_moedas.cotacao_moeda('Bitcoin'))
    elif 'ajuda' in acao:
        exibir_ajuda()

# Exibe mensagens de ajuda
def exibir_ajuda():
    comandos = (
        "Comandos disponíveis:\n"
        "- \"Que horas são?\": Para saber o horário atual.\n"
        "- \"Desligue em 5/10/15 minutos\": Para agendar o desligamento.\n"
        "- \"Cancelar desligamento\": Para cancelar o desligamento agendado.\n"
        "- \"Notícias\": Para ouvir as últimas notícias.\n"
        "- \"Cotação do dólar/euro/bitcoin\": Para saber as cotações.\n"
        "- \"Fechar assistente\": Para encerrar."
    )
    cria_audio(comandos)

if __name__ == "__main__":
    main()