import os
import importlib.util
import constants as _C
from licenses import *
from tmps import *

def createNewPkgStruct(cfg):
    '''Create a new package structure using the provided cfg dictionary'''

    out = cfg.dir
    if not os.path.isdir(out):
        os.mkdir(out)

    os.mkdir(os.path.join(out, 'src'))
    os.mkdir(os.path.join(out, 'tests'))

    return True

def writeReqPkgFiles(cfg):


    def writeReadme(path):
        '''Write the packages README.md with default contents'''

        raw = readme.RAW
        f = open(path, 'a')
        f.write(raw)
        f.close()
        return True


    def writeLicense(_type, path):
        '''Write the packages LICENSE file'''

        f = open(path, 'a')
        f.write(eval(_type).RAW)
        f.close()
        return True


    def writeExInit(path):
        '''Write the example modules 'init' file'''

        f = open(path, 'a')
        f.write("# A blank '__init__' file for a python module")
        f.close()
        return True


    def writeToml(build, path):
        '''Write the required package files'''

        f = open(path, 'a')
        f.write(_C.TOML_DEFS[build])
        f.close()
        return True

    
    try:
        # create the LICENSE file path
        lFile = os.path.join(cfg.dir, 'LICENSE')

        # create the README file path
        rFile = os.path.join(cfg.dir, 'README.md')

        # create the 'pyproject.toml' file path
        pFile = os.path.join(cfg.dir, 'pyproject.toml')

        # create the 'Example Module' path
        exMod = os.path.join(cfg.src_path, cfg.name)

        # make the 'Example Module' directory
        os.mkdir(exMod)

        # create the '__init__.py' file for the example module
        eFile = os.path.join(exMod, '__init__.py')

        # write the LICENSE file
        writeLicense(cfg.license, lFile)

        # write the README file
        writeReadme(rFile)

        # write the example module's '__init__' file
        writeExInit(efile)
        
        # write the 'pyproject.toml' file
        writeToml(cfg.build, pFile)

        return True

    except Exception as e:
        print('An error was thrown during package init. Error message: ' + e)
        return False


def getSrcFiles(src):
    '''Guarantee a returned list of files, even for a single file'''

    isDir = os.path.isdir(src)
    if not isDir:
        files = [src]
    else:
        files = list(os.listdir(src))
    return files


def checkPkgs(pkgs):
    '''Check if the list of passed in packages are currently installed and available'''

    results = {}
    for pkg in pkgs:
        spec = importlib.util.find_spec(pkg)
        if spec is None:
            results[pkg] = False
        else:
            results[pkg] = True
    return results
