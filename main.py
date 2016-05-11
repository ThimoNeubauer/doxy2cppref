#!/usr/bin/env python3
#  -*- encoding: utf-8 -*-

import logging

from doxy2cppref.doxyxml import DoxyIndex


logger = logging.getLogger("doxy2cppref")


def render_page(title, docthings):

    print("{{cpp/title|%s}}" % title)

    print("===Member functions===")
    print("{{dsc begin}}")

    for doc in [doc for doc in docthings if doc.kind == "function"]:
        print(doc.what)

    print("{{dsc end}}")


def main():
    index = DoxyIndex('example/xml/index.xml')
    for cls in index.classes():
        class_details = index.class_details(cls)

        render_page(class_details.name(), class_details.methods())

try:
    main()
except Exception as ex:
    logging.exception(ex)
