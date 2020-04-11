#!/usr/bin/env python3

from procedures.sample import SampleProcedure


class Register:
    def __init__(self, activator, procedure):
        self.activator = activator
        self.procedure = procedure


class ProcedureRegistry:

    def __init__(self, language):
        self.procedure_registry = []
        self.add_to_registry(SampleProcedure, language)

    def add_to_registry(self, procedure, language):
        p = procedure()
        activators, err = p.get_activators(language)

        if err:
            print('Error[Procedure: %s]: %s.' % (procedure.procedure_name, err))
            return

        for a in activators:
            self.procedure_registry.append(Register(a, p))

    def get_registry(self):
        return self.procedure_registry
