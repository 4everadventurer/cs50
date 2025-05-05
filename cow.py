import cowsay
import pyttsx3

engine=pyttsx3.init()
engine.setProperty('rate', 150)  # 속도 설정 (기본값: 200)
engine.setProperty('volume', 1)  # 음량 설정 (0.0~1.0)
engine.setProperty('voice', 'english')  # 음성 설정 (예: 영어)


this=input("what's this?")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()