#!/usr/bin/env python3
#  -*- encoding: utf-8 -*-

import logging

from doxy2cppref.classdata import ClassData


def main():
    cd = ClassData('example/xml/class_simple_1_1_whatever.xml')

    for member in cd.methods():
        print("-" * 20)
        print(member.what)
        print(member.kind)
        print(member.brief)


try:
    main()
except Exception as ex:
    logging.exception(ex)
