'''Create a new pyproject.toml file

    The 'pyproject.toml' file is used to build a PyPi Package

    Possible args within 'cfg' dictionary:
        cfg.name
        cfg.version
        cfg.authors
        cfg.description
        cfg.pyversion
        cfg.classifiers
        cfg.project_urls

    For args not provided, their values will default to an empty string ("")
'''

def makeToml(build, cfg_):
    vals = ['name', 'version', 'authors', 'description', 'pyversion', 'classifiers', 'project_urls']
    cfg = {}
    for key in vals:
        if key in cfg_:
            cfg[key] = cfg_[key]
        else:
            cfg[key] = ""

    raw_part1 = '''[project]
name = {}
version = {}
authors = {}
description = {}\n'''.format(cfg.name, cfg.version, cfg.authors, cfg.description)

    raw_part2 = '''
readme = "README.md"
license = { file="LICENSE" }\n'''

    raw_part3 = '''
requires-python = ">={}"
classifiers = {}
[project.urls]
{}'''.format(cfg.pyversion, cfg.classifiers, cfg.project_urls)

    full = build + raw_part1 + raw_part2 + raw_part3
    return full
