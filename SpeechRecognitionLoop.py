import speech_recognition as sr
import webbrowser
import subprocess
import string

listen = True


while listen == True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Di algo!")
		audio = r.listen(source)

		try:
			print("He entendido " + r.recognize_google(audio))
		except sr.UnknownValueError:
			print("No te he entendido bien")
		except sr.RequestError as e:
			print("No hemos podido conectar con el servicio de Google; {0}".format(e))

	# Wheater
	if "time" in r.recognize_google(audio):
		r1 = sr.Recognizer()
		url1 = 'https://www.eltiempo.es/'
		with sr.Microphone() as source:
			print('¿De que ciudad? ')
			audio1 =r1.listen(source)

			try:
				print("Google Speech recognition thinks you said " + r1.recognize_google(audio) + webbrowser.open_new(url1+r1.recognize_google(audio1)))
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio.")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition.")

	# Youtube
	if "video" in r.recognize_google(audio):
		r2 = sr.Recognizer()
		url2 = 'https://youtube.com/results?search_query='
		with sr.Microphone() as source:
			print ("Dime que quieres ver ")
			audio2 =r2.listen(source)

			try:
				print("Google Speech recognition thinks you said " + r2.recognize_google(audio2) + webbrowser.open_new(url2+r2.recognize_google(audio2)))
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio.")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition.")		
