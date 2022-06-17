import gtts
from playsound import playsound

# List supported languages FOR TEST PURPOSES ONLY
# print(gtts.lang.tts_langs())

print("Indica lo que deseas decir a continuacion: ")

text = str(input())

# make request to google to get speech synthesis
tts = gtts.gTTS(text, lang="es")

tts.save("speech.mp3")

playsound("speech.mp3")
