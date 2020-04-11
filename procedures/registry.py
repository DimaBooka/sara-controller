#!/usr/bin/env python3

from procedures.lgtv import LGTVProcedure


class Register:
    def __init__(self, activator, procedure):
        self.activator = activator
        self.procedure = procedure


class ProcedureRegistry:

    def __init__(self, language):
        self.procedure_registry = []
        self.add_to_registry(LGTVProcedure, language)

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

    def detect_procedures(self, phrase):
        procedures = []

        for p in self.procedure_registry:
            if p.activator in phrase:
                procedures.append(p.procedure)

        return procedures
