# -*- encoding: utf-8 -*-

import os

from doxy2cppref.doxyxml import DoxyIndex

MYDIR = os.path.dirname(__file__)


def test_with_simple_data():
    index_filename = os.path.join(MYDIR, "simple_data", "index.xml")

    index = DoxyIndex(index_filename)

    all_classes = index.classes()
    assert len(all_classes) == 1

    # -- check documentation of class

    simple_class = all_classes[0]
    assert simple_class.short_name == "Whatever"
    assert simple_class.full_name == "Simple::Whatever"

    assert simple_class.brief_doc == "Does something."
    # TODO model all content of doc elements
    assert "still doesn't do anything useful" in simple_class.detailed_doc

    # -- check documentation of public methods

    public_methods = simple_class.public_methods()
    assert len(public_methods) == 3

    # argument-less constructor
    method = public_methods[0]
    assert method.short_name == "Whatever"
    assert method.brief_doc == "the trivial constructor"
