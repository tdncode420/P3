# available backend tools
# these are used to create distribution packages
BACKENDS = ['Hatchling', 'setuptools', 'Flit', 'PDM']

# required packages
REQ_PKGS = ['setuptools', 'wheel', 'twine']

# new package files
PKG_CONTENTS = [
    'pyproject.toml', 'README.md', 'LICENSE.remove',
    'tests', 'src', 'src/example_package', 'src/example_package/__init__.py',
]
