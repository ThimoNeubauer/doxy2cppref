#!/usr/bin/env python3
#  -*- encoding: utf-8 -*-

import argparse
import logging
import os

from doxy2cppref.doxyxml import DoxyIndex
from doxy2cppref.output import output

logger = logging.getLogger("doxy2cppref")


class MyError(Exception):
    pass


def render_class(class_details, outdir):
    cppname = class_details.cppname

    filename = os.path.join(outdir, cppname)
    logging.info("Generating class file {}".format(filename))

    d = dict()
    d['title'] = cppname
    d['public_members'] = class_details.public_members()

    output(d, "class", filename)


def main():
    # -- setup

    parser = argparse.ArgumentParser(description='Process data storage definition files.')
    parser.add_argument('-d', '--debug', action='store_true', help='activate more output')
    parser.add_argument('indexfile', type=str, help="Doxygen index.xml")
    parser.add_argument('outdir', type=str, help="output directory")

    args = parser.parse_args()

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format="%(message)s")

    indexfile = args.indexfile
    if not os.path.isfile(indexfile):
        raise MyError("Could not find index file {}!".format(indexfile))

    outdir = args.outdir
    if os.path.isdir(outdir):
        logger.warn("Will re-generate {} directory now".format(outdir))
    if not os.path.isdir(outdir):
        logger.info("Creating {}".format(outdir))
        os.makedirs(outdir)

    # -- operation

    index = DoxyIndex(indexfile)
    for cls in index.classes():
        class_details = index.class_details(cls)
        render_class(class_details, outdir)


try:
    main()
except MyError as ex:
    logger.error(ex)
except Exception as ex:
    logging.exception(ex)
