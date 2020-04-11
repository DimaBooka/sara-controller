#!/usr/bin/env python3

from sara.language import EN, RU, UA
from sara.decorators import log
from procedures.procedure import Procedure
from wakeonlan import send_magic_packet


LGTV_MAC = '7C.1C.4E.9B.CB.CB'


class LGTVProcedure(Procedure):
    procedure_name = 'lgtv_procedure'
    activators = {
        EN: ['turn on tv'],
        RU: ['включи телевизор'],
        UA: ['ввімкни телевізор']
    }

    @log('call lgtv proceed')
    def proceed(self, phrase):
        send_magic_packet(LGTV_MAC)
