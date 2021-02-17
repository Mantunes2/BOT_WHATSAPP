# 1. Importar blibiotecas
import pywhatkit
import keyboard
import time
from datetime import datetime
# 2. Definir para qual contato enviaremos as msgs
Contatos = ['+5521979354287']
# 3. Definir intervalo de envio
while len(Contatos) >= 1:
    # Enviar mensagem.
    pywhatkit.sendwhatmsg(Contatos[0],"Drugs(MP3_128K)_1",datetime.now().hour,datetime.now().minute + 2)
    del Contatos[0]
    time.sleep(60)
    keyboard.press_and_release('Ctrl + h')
# 4. Testar!