import PySimpleGUI as sg
import asyncio
import Scripts.NeuroWeb.Listener as ls
import threading

listener = ls.Listener()
listener.__init__()

statusBarKey = 'status_bar'
outputKey = 'output'

clear = 'Очистить'
startListen = 'Начать прослушку'
stopListen = 'Остановить прослушку'
listenStatus = 'Прослушиваю микрофон...'
noListenStatus = 'Прослушивание отключено'
currentStatus = noListenStatus

layout = [
    [sg.StatusBar(currentStatus, key=statusBarKey)],
    [sg.Output(size=(88, 20), key=outputKey)],
    [sg.Submit(startListen), sg.Button(stopListen), sg.Button(clear), sg.Exit('Выход')]
]

window = sg.Window('Распознавания речи в режиме реального времени', layout)

def windowLife():
    while True:
        event, values = window.read()

        if event in (None, 'Выход', 'Cancel'):
            break

        if event == startListen:
            listener.startListenning()
            currentStatus = listenStatus
            window[statusBarKey].Update(currentStatus)

        if event == stopListen:
            listener.stopListenning()
            currentStatus = noListenStatus
            window[statusBarKey].Update(currentStatus)

        if event == clear:
            window[outputKey].Update('')

threading.Thread(target=windowLife(), daemon=True).start()