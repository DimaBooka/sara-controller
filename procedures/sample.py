#!/usr/bin/env python3

from sara.language import EN, RU, UA
from sara.decorators import log
from procedures.procedure import Procedure


class SampleProcedure(Procedure):
    procedure_name = 'sample_procedure'
    activators = {
        EN: ['run sample'],
        RU: ['запусти пример'],
        UA: ['запусти приклад']
    }

    @log('call sample proceed')
    def proceed(self):
        print('sample procedure executed')
