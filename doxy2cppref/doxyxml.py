# -*- encoding: utf-8 -*-

import xml.etree.ElementTree as ElementTree
import os


class ClassInfo:

    def __init__(self):
        self.cppname = None
        self.refid = None


class DoxyIndex:

    def __init__(self, filename):
        self.basedir = os.path.dirname(filename)

        tree = ElementTree.parse(filename)
        self.root = tree.getroot()

    def classes(self):
        result = list()

        for node in self.root.findall("./compound[@kind='class']"):
            classinfo = ClassInfo()

            classinfo.cppname = node.find('name').text
            classinfo.refid = node.attrib['refid']

            result.append(classinfo)

        return result

    def class_details(self, classinfo):
        return DoxyClass(classinfo.cppname, os.path.join(self.basedir, classinfo.refid + ".xml"))


class DocThing:

    def __init__(self):
        self.what = None

        self.kind = None
        self.protection = None

        self.brief = None


# TODO: use the <para> elements and such
def doxy2wiki(description):
    return " ".join(description.itertext()).strip()


class DoxyClass:

    def __init__(self, cppname, filename: str):
        self.cppname = cppname

        tree = ElementTree.parse(filename)
        self.root = tree.getroot()

    def name(self):
        return self.root.find('.//compoundname').text

    def variables(self):
        return self.__memberdefs("[@kind='variable']")

    def public_members(self):
        return self.__memberdefs("[@kind='function'][@prot='public']")

    def __memberdefs(self, selector):
        results = list()

        for memberdef in self.root.findall('.//memberdef' + selector):
            dc = DocThing()

            dc.what = memberdef.find('definition').text
            dc.kind = memberdef.attrib['kind']
            dc.brief = doxy2wiki(memberdef.find('briefdescription'))

            results.append(dc)

        return results
