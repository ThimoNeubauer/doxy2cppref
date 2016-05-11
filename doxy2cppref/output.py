# -*- encoding: utf-8 -*-

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('doxy2cppref', 'templates'), trim_blocks=True, lstrip_blocks=True)


def output(data, templatename, outname):
    """
    Pass in a data dict and a template name in templates/ to render into the output file

    :param data: data dictionary which can be substituted into template
    :param templatename: name of template file
    :param outname: filename of output file
    :return:
    """

    with open(outname, "w", encoding="utf-8") as outfile:
        template = env.get_template(templatename + ".template")
        outfile.write(template.render(**data))
