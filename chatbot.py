from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sys
import time
import funcoes_so
import funcoes_noticias

# Função que cria o áudio (converte texto para voz)
def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save(audio)
    playsound(audio)

# Função que cria o áudio das notícias com espaçamento
def cria_audio_noticias():
    noticias = funcoes_noticias.ultima_noticias()
    for i, noticia in enumerate(noticias):
        audio_file = f'noticia{i+1}.mp3'
        cria_audio(audio_file, noticia)
        time.sleep(2)  # Pausa de 2 segundos entre as notícias

# Microfone (voz para texto)
def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga alguma coisa")
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language='pt-br')
                mensagem = mensagem.lower()
                print("Você disse: ", mensagem)
                executa_comandos(mensagem)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return mensagem

def executa_comandos(acao):
    if 'fechar assistente' in acao:
        sys.exit()
    elif 'horas' in acao:
        cria_audio('mensagem.mp3', funcoes_so.verfica_hora())
    elif 'notícias' in acao:
        cria_audio_noticias()

def main():
    cria_audio("welcome.mp3", "Olá, sou seu assistente. Em que posso te ajudar?")
    while True:
        monitora_audio()

main()