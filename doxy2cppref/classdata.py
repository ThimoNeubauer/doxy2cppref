# -*- encoding: utf-8 -*-

import xml.etree.ElementTree as ElementTree


class DocThing:

    def __init__(self):
        self.what = None

        self.kind = None
        self.protection = None

        self.brief = None


# TODO: use the <para> elements and such
def doxy2wiki(description):
    return " ".join(description.itertext())


class ClassData:

    def __init__(self, filename: str):
        tree = ElementTree.parse(filename)
        self.root = tree.getroot()

    def methods(self):
        for memberdef in self.root.findall('.//memberdef'):
            dc = DocThing()

            dc.what = memberdef.find('definition').text
            dc.kind = memberdef.attrib['kind']
            dc.brief = doxy2wiki(memberdef.find('briefdescription'))

            yield dc
