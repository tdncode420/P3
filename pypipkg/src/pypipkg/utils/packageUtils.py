import os
import importlib.util
from licenses import *
from tmps import *

def createNewPkgStruct(cfg):
    '''Create a new package structure using the provided cfg dictionary'''

    out = cfg.out
    if not os.path.isdir(out):
        os.mkdir(out)
    os.mkdir(os.path.join(out, 'tests'))
    return True


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


def writeReadme(path):
    '''Create/write the packages README.md with default contents'''

    raw = readme.RAW
    f = open(path, 'a')
    f.write(raw)
    f.close()


def writeLicense(_type, path):
    '''Create/write the packages LICENSE file'''

    f = open(path, 'a')
    f.write(eval(_type).RAW)
    f.close()
    return True

def writeToml(cfg, path):
    pass