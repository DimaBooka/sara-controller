#!/usr/bin/env python3

from sara.language import EN, RU
from sara.decorators import log
from procedures.procedure import Procedure


class SampleProcedure(Procedure):
    procedure_name = 'sample_procedure'
    activators = {
        EN: ['run sample'],
        RU: ['запусти пример']
    }

    @log('call sample proceed')
    def proceed(self):
        print('sample procedure executed')
