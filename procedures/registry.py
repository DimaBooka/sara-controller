#!/usr/bin/env python3

from procedures.sample import SampleProcedure


class Register:
    def __init__(self, activator, procedure):
        self.activator = activator
        self.procedure = procedure


class ProcedureRegistry:

    def __init__(self):
        self.procedure_registry = []
        self.add_to_registry(SampleProcedure)

    def add_to_registry(self, procedure):
        p = procedure()

        for a in procedure.activators:
            self.procedure_registry.append(Register(a, p))

    def get_registry(self):
        return self.procedure_registry
