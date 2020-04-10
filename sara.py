#!/usr/bin/env python3

import speech_recognition as sr
from playsound import playsound

from constants import Melody, Phrase
from procedures.registry import ProcedureRegistry
from timer import Timer
from decorators import log


class SaraController:
    cancelling = None

    def __init__(self):
        self.timer = Timer()
        self.activated = False
        self.recognizer = sr.Recognizer()
        self.procedures = ProcedureRegistry().get_registry()
        self.listen()

    @log('Sara waiting to be activated')
    def listen(self):
        m = sr.Microphone()
        with m as source:
            # we only need to calibrate once, before we start listening
            self.recognizer.adjust_for_ambient_noise(source)

        self.cancelling = self.recognizer.listen_in_background(m, self.callback)

    def callback(self, recognizer, sound):
        phrase = self.recognize_phrase(sound)

        if Phrase.HEY_SARA in phrase:
            self.activate()

        if not self.activated:
            return

        # detect procedures
        self.detect_procedure(phrase)

    def recognize_phrase(self, audio):
        phrase = ''

        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            phrase = self.recognizer.recognize_google(audio)
            print("Recognized phrase: " + phrase)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service: {0}".format(e))

        if phrase != '':
            phrase = phrase.lower()
        return phrase

    def play_sound(self, melody):
        playsound(melody)

    @log('Sara activated!')
    def activate(self):
        self.activated = True
        self.play_sound(Melody.ACTIVATING)

        self.timer.set_timeout(self.deactivate, 10.0)

    @log('Sara deactivated!')
    def deactivate(self):
        self.activated = False
        # self.play_sound(Melody.DEACTIVATING)

    def detect_procedure(self, phrase):
        for p in self.procedures:
            if p.activator in phrase:
                p.procedure.proceed()
                # self.play_sound(Melody.RUN_PROCEED)
                self.play_sound(Melody.ACTIVATING)
