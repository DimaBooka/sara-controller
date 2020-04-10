#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Procedure(ABC):
    @property
    def procedure_name(self):
        return ''

    @property
    def activators(self):
        return []

    @abstractmethod
    def proceed(self):
        pass
