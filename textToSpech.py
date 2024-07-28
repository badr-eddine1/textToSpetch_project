from gtts import gTTS
txt = input("enter your text")
language = "en"
result = gTTS(text=txt,lang=language)
result.save("audio.mp3")