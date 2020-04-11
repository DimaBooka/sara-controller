Home assistant SARA

To run it, just type:

```python main.py```

and say "Hey, Sara!"

To change the language use 'ln' flag:

```python main.py -ln=ua```

By default 'en'. Supported languages: [ru, ua, en]

---

Requirements:


PyAudio

PyAudio and python3+ is unsupported by default with ```pip install pyaudio```.

So need to run next:

```sudo apt-get install portaudio19-dev python-pyaudio```

and then:

```pip install PyAudio```

---

Plasysound

If you faced with error ```Import Error: No module gi```

run next command:

```sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0```

and 

``` pip install pycairo pygobject```

---

For RaspberryPI

```sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools```

---

<a href="https://github.com/Uberi/speech_recognition">GIT SpeechRecognition</a>
