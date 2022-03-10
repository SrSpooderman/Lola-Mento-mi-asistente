#Import
import webbrowser
import random
import subprocess
import os
from playsound import playsound
#Variables
playsound("hini.wav")
cumbia = ['https://www.youtube.com/watch?v=N85YNZVVgZc',
          'https://www.youtube.com/watch?v=gwgLj51eW0U',
          'https://www.youtube.com/watch?v=F4wf-W4j3m4',
          'https://www.youtube.com/watch?v=MUUrW7xJSw4']
cumbioso = random.choice(cumbia)
cosas_random = ['https://www.youtube.com/watch?v=jyKja2vcpQo',
                'https://www.youtube.com/watch?v=pxw-5qfJ1dk',
                'https://www.youtube.com/watch?v=B4LvDiIi128',
                'https://www.youtube.com/watch?v=kxSOhBdwmc4',
                'https://www.youtube.com/watch?v=9b0pjB9XO8w',
                'https://www.youtube.com/watch?v=G1IbRujko-A',
                'https://www.youtube.com/watch?v=Kob0G2hE8IY',
                'https://www.youtube.com/watch?v=KAZ1spXEU80',
                'https://www.youtube.com/watch?v=pL5aqJ50bQQ',
                'https://www.youtube.com/watch?v=TRc85qoNo6w']
cosas_randome = random.choice(cosas_random)
#inicio del programa
print("Hola soy tu asistenta")
print("Que desea hacer el dia de hoy")
accion = (input(": "))
if (accion == "golaso"):
    playsound("yes.wav")
    webbrowser.open("https://www.youtube.com/watch?v=IpVUXr_jGkY&t=15s")
#
elif (accion == "eminem"):
    playsound("yes.wav")
    webbrowser.open("https://www.youtube.com/watch?v=hzVm_Cdcsew")
#
elif (accion == "cumbia"):
    playsound("yes.wav")
    webbrowser.open(cumbioso)
#
elif (accion == "google"):
    playsound("yes.wav")
    webbrowser.open("https://www.google.es")
#
elif (accion == "youtube"):
    playsound("yes.wav")
    webbrowser.open("https://www.youtube.com")
#
elif(accion == "anime"):
    playsound("yes.wav")
    webbrowser.open("https://www3.animeflv.net")
#
elif(accion == "random"):
    playsound("yes.wav")
    webbrowser.open(cosas_randome)
#
elif(accion == "apagate"):
    playsound("yes.wav")
    subprocess.call("shutdown -s")
#
elif(accion == "reinicia"):
    playsound("yes.wav")
    subprocess.call("shutdown -r")
#
elif(accion == "ayuda"):
    print("golaso-eminem-cumbia-google-youtube-anime-random-apagate-reinicia-ayuda")
#
else:
    print ("Eso no es un comando")
