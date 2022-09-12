# available backend tools
# these are used to create distribution packages
BACKENDS = ['hatchling', 'setuptools', 'flit', 'pdm']

# required packages
REQ_PKGS = ['setuptools', 'wheel', 'twine']

# new package files
PKG_CONTENTS = [
    'pyproject.toml', 'README.md', 'LICENSE.remove',
    'tests', 'src', 'src/example_package', 'src/example_package/__init__.py',
]

TOML_DEFS = {
    'setuptools': '''[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"''',
    'hatchling': '''[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"''',
    'flit': '''[build-system]
requires = ["flit_core>=3.2"]
build-backend = "flit_core.buildapi"''',
    'pdm': '''[build-system]
requires = ["pdm-pep517"]
build-backend = "pdm.pep517.api"'''
}