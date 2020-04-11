#!/usr/bin/env python3

import speech_recognition as sr
from playsound import playsound

from sara.constants import Melody, get_constants, SARA_ACTIVATOR
from procedures.registry import ProcedureRegistry
from sara.timer import Timer
from sara.decorators import log


class SaraController:
    cancelling = None

    def __init__(self, language):
        self.language = language
        self.constants = get_constants(language)
        self.timer = Timer()
        self.activated = False
        self.recognizer = sr.Recognizer()
        self.procedures = ProcedureRegistry(language)
        self.listen()

    @log('Sara waiting to be activated')
    def listen(self):
        m = sr.Microphone()
        with m as source:
            # we only need to calibrate once, before we start listening
            self.recognizer.adjust_for_ambient_noise(source)

        self.cancelling = self.recognizer.listen_in_background(m, self.callback, 5)

    def callback(self, recognizer, sound):
        phrase = self.recognize_phrase(sound)

        if self.constants[SARA_ACTIVATOR] in phrase:
            self.activate()

        if not self.activated:
            return

        # detect procedures
        self.detect_and_run_procedure(phrase)

    def recognize_phrase(self, audio):
        phrase = ''

        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            phrase = self.recognizer.recognize_google(audio, language=self.language)
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

    def detect_and_run_procedure(self, phrase):
        procedures = self.procedures.detect_procedures(phrase)

        for p in procedures:
            p.proceed(phrase)
            # self.play_sound(Melody.RUN_PROCEED)
            self.play_sound(Melody.ACTIVATING)
