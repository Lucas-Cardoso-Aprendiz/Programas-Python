#Para instalar o pacote: Vá ao terminal e digite > pip install pyttsx3

#Importa a biblioteca para o programa
import pyttsx3

#A variável robô receberá a inicalização do pacote
robo = pyttsx3.init()

#Taxa de fala inteira em palavras por minuto. O valor base é 200, mas pode ser mudada para mais ou menos
robo.setProperty('rate', 160)


voices = robo.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

robo.setProperty("voice", voices[1].id)#0para escolher Maria(Português) e (1)para escolher Zara(Inglês)


#Receberá a entrada de dados(input) e armazenará na variável (msg_robo)
msg_robo = input("Escreva algo: ")

#Esse método(robo.say) serve para falar tudo o que a variável (msg_robo)receber de entrada de dados
robo.say(msg_robo)

robo.runAndWait()
