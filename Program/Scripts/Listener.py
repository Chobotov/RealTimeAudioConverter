import speech_recognition
import threading

class Listener:
    record:speech_recognition.Recognizer
    mic:speech_recognition.Microphone
    isListenning = False

    def __init__(self):
        self.record = speech_recognition.Recognizer()
        self.mic = speech_recognition.Microphone()

    def listenning(self):
        self.isListenning = True
        while(self.isListenning == True):
            with self.mic as source:
                audio = self.record.listen(source)
                speech = self.record.recognize_google(audio, language='ru-RUS')
                print(speech)

    def startListenning(self):
        threading.Thread(target=self.listenning(), daemon=True).start()

    def stopListenning(self):
        self.isListenning = False
