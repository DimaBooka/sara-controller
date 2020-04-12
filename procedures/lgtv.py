#!/usr/bin/env python3

import LGTV
import json
import subprocess
from wakeonlan import send_magic_packet

from sara.decorators import log
from procedures.procedure import Procedure

LGTV_NAME = 'MyLG'


class LGTVProcedure(Procedure):
    procedure_name = 'lgtv_procedure'
    activators = []

    def __init__(self):
        self.config = {}
        self.connect_to_device()

        self.commands = {
            'turn on tv': lambda: self.__on(),
            'turn off tv': lambda: self.__run("lgtv %s off" % LGTV_NAME),
            'open youtube on tv': lambda: self.__run("lgtv %s startApp 'youtube.leanback.v4'" % LGTV_NAME),
            'open netflix on tv': lambda: self.__run("lgtv %s startApp 'netflix.leanback.v4'" % LGTV_NAME),
            'open films on tv': lambda: self.__run("lgtv %s openBrowserAt 'https://rezka.ag/films/'" % LGTV_NAME)
        }

        self.activators = self.commands.keys()

    def connect_to_device(self):
        filename = LGTV.find_config()
        if filename is not None:
            with open(filename) as f:
                self.config = json.loads(f.read())

    def __on(self):
        send_magic_packet(self.config[LGTV_NAME]['mac'])

    def __run(self, command):
        subprocess.call(command, shell=True)

    @log('call lgtv proceed')
    def proceed(self, phrase):
        try:
            self.commands[phrase]()
        except KeyError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))
