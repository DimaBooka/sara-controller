#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Procedure(ABC):
    @property
    def procedure_name(self):
        return ''

    @property
    def activators(self):
        return {}

    @abstractmethod
    def proceed(self):
        pass

    def get_activators(self, lang):
        if lang in self.activators:
            return self.activators[lang], None
        return None, 'language is not supported'
