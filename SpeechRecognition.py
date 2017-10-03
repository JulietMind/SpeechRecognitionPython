import webbrowser
import string
import speech_recognition as sr
import subprocess


# Record audio
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Di algo!")
	audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print ("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print ("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print ("Could not request results from Google Speech Recognition service; {0}".format(e))

if "wake up" in r.recognize_google(audio):
	r2 = sr.Recognizer()
	url = 'https://es.wikipedia.org/wiki/'
	with sr.Microphone() as source:
		print ("Say something: ")
		audio2 =r2.listen(source)

		try:
			print("Google Speech recognition thinks you said " + r2.recognize_google(audio) + webbrowser.open_new(url+r2.recognize_google(audio2)))
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition.")


if "video" in r.recognize_google(audio):
	r3 = sr.Recognizer()
	url3 = 'https://youtube.com/results?search_query='
	with sr.Microphone() as source:
		print ("Say something: ")
		audio3 =r3.listen(source)

		try:
			print("Google Speech recognition thinks you said " + r3.recognize_google(audio) + webbrowser.open_new(url3+r3.recognize_google(audio3)))
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition.")


if "tomato" in r.recognize_google(audio):
	r4 = sr.Recognizer()
	url4 = 'https://tomato-timer.com/'
	with sr.Microphone() as source:
		print ("Say something: ")
		audio4 =r4.listen(source)

		try:
			# print("Google Speech recognition thinks you said " + r4.recognize_google(audio) + webbrowser.open_new(url4+r4.recognize_google(audio4)))
			print("Google Speech recognition thinks you said " + webbrowser.open_new(url4))
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition.")

if "Photoshop" in r.recognize_google(audio):
	print (subprocess.Popen(r'explorer "C:\Program Files\Adobe\Adobe Photoshop CC 2017\Photoshop.exe"'))

if "internet" in r.recognize_google(audio):
	print (subprocess.Popen(r'explorer "C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"'))