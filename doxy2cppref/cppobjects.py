# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class CppDoc:
    """
    Pieces of documentation connected to a C++ thing
    """

    def __init__(self):
        self.brief_doc = None
        self.detailed_doc = None

        self.short_name = None
        self.full_name = None


class CppClass(CppDoc, metaclass=ABCMeta):
    """
    Documentation for a C++ class and access to the parts (e.g. methods, types, ...)
    """

    def __init__(self):
        super(CppClass, self).__init__()

    @abstractmethod
    def public_methods(self):
        pass
