import speech_recognition
import threading

class Listener:
    thread:threading.Thread
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
        if (self.isListenning == True): return
        self.thread = threading.Thread(target=self.listenning, daemon=True)
        self.thread.start()

    def stopListenning(self):
        self.isListenning = False
