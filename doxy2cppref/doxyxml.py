# -*- encoding: utf-8 -*-

import os
import xml.etree.ElementTree as ElementTree

from doxy2cppref.cppobjects import CppClass, CppDoc


class DoxyIndex:

    def __init__(self, filename):
        self.basedir = os.path.dirname(filename)

        tree = ElementTree.parse(filename)
        self.root = tree.getroot()

    def classes(self):
        result = list()

        for node in self.root.findall("./compound[@kind='class']"):
            cppname = node.find('name').text

            refid = node.attrib['refid']
            filename = os.path.join(self.basedir, refid + ".xml")

            doxyclass = DoxyClass(filename)
            result.append(doxyclass)

        return result


# TODO: use the <para> elements and such
def doxy2wiki(description):
    return " ".join(description.itertext()).strip()


# TODO add unit test
def cpp_basename(name: str):
    """
    Remove all namespaces from name
    :param name:
    :return:
    """

    return name[name.rfind('::')+2:]


class DoxyClass(CppClass):

    def __init__(self, filename: str):
        super(DoxyClass, self).__init__()

        tree = ElementTree.parse(filename)
        self.root = tree.getroot().find('.//compounddef')

        self.full_name = self.root.find('compoundname').text
        self.short_name = cpp_basename(self.full_name)

        self.brief_doc = doxy2wiki(self.root.find('briefdescription'))
        self.detailed_doc = doxy2wiki(self.root.find('detaileddescription'))

    def variables(self):
        return self.__memberdefs("[@kind='variable']")

    def public_methods(self):
        return self.__memberdefs("[@kind='function'][@prot='public']")

    def __memberdefs(self, selector):
        results = list()

        for memberdef in self.root.findall('.//memberdef' + selector):
            doc = CppDoc()

            # TODO What is correct here?
            doc.kind = memberdef.attrib['kind']

            doc.full_name = memberdef.find('definition').text
            doc.short_name = memberdef.find('name').text

            doc.brief_doc = doxy2wiki(memberdef.find('briefdescription'))
            doc.detailed_doc = doxy2wiki(memberdef.find('detaileddescription'))

            results.append(doc)

        return results
