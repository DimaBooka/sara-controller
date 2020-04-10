#!/usr/bin/env python3

from sara.decorators import log
from procedures.procedure import Procedure


class SampleProcedure(Procedure):
    procedure_name = 'sample_procedure'
    activators = ['run sample']

    @log('call sample proceed')
    def proceed(self):
        print('sample procedure executed')
