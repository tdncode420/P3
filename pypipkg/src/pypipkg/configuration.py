import os
import json
from utils import randomKey

def interactiveCreate():
    '''Interactively configures a configuration dictionary for a new package'''

    # an empty cfg dictionary
    cfg = {}

    # get the project name from user
    name = input('Package name (default = \'new_project\'): ')

    # if the name provided is empty
    if len(name) == 0:

        # add a default name
        cfg.name = "new_project" + randomKey.generate()

    # get the path to the source directory from user
    src = input("Source directory path (default='.'): ")

    # if no src path was provided
    if len(src) == 0:

        # default to the current directory
        src = os.getcwd()

    # start by getting the output directory from user
    out = input('Package directory: ')

    # if the directory provided is already created
    if os.path.isdir(out):

        # set it on the cfg dict
        cfg.out = out
    else:

        # else ask to create this dir
        ans = input(
            "Directory {} doesn't exist. Create it now? [y,n] Default=y : ").strip()

        # if user doesn't agree
        if ans != 'n':

            # rerun this method to start over
            interactiveCreate()

        # else create the dir
        os.mkdir(out)

        # set it on the cfg dict
        cfg.out = out
        
    def getBTools():
        validBTools = ['1', '2', '3', '4']
        bToolsList = ['setuptools', 'Hatchling', 'Flit', 'PDM']

        _bTools = input('Build tools to use (enter a number):\n\t1) setuptools (default)\n\t2) Hatchling\n\t3) Flit\v\t4) PDM') 
        
        if bToolsArg not in validBTools:
            print('bTools is not a valid selection')
            getBTools()
        else:
            return _bToolsList[int(bToolsArg) - 1]
    
    bTools = getBTools()

    cfg.build_tools = bTools
    
    def getLicense():
        validPkgLs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        lsList = ['none', 'apache', 'boost', 'agpl', 'gpl', 'lgpl', 'mit', 'moz', 'un']
        _pkgL = input('Choose a license to use (enter a number):\n\t1) None (default)\n\t2) Apache 2.0\n\t3) Boost Software 1.0\n\t4) GNU AGPLv3\n\t5) GNU GPLv3\n\t6) GNU LGPLv3\n\t7) MIT (recommended)\n\t8)Mozilla Public 2.0\n\t9) Unlicense')
        if pkgL not in validPkgLs:
            getLicense()
        else:
            return lsList[int(_pkgL) - 1]

    pkgL = getLicense()
    
    cfg.license = pkgL
    
    # create the project structure
    return cfg


def noninteractiveCreate():
    '''Non-Interactively configures a configuration dictionary for a new package
    
        Requires a 'p3conf.json' to be present at the oot of the directory
    '''

    def buildOut():
        outPath = os.path.join(os.getcwd(), 'out')
        os.mkdir(outPath)
        return outPath

    defaults = {
        'name': 'new_package' + randomKey.generate(),
        'src': os.getcwd(),
        'out': buildOut(),
        'build_tools': 'setuptools',
        'license': 'none'
    }

    cfg = {}
    
    cfgPath = os.path.join(os.getcwd(), 'p3conf.json')

    def getCfg():
        _cfgJson = None
        try:
            f = open(cfgPath, 'r')
            _cfgJson = json.loads(f.read())
        except FileNotFoundError:

            print('You are trying to use this script in \'Non-interactive\' mode but no \'p3conf.json\' file was found.')
            print('Please create one and place it at the root of the directory that you are running this command in.')
            print('For more help/info about the \'p3conf.json\' file, run the command: `p3 -help conf`')
            _cfgJson =  False
        finally:
            return _cfgJson

    cfgJson = getCfg()

    if cfgJson == False:
        return False

    for key in defaults:
        if key in cfgJson:
            cfg[key] = cfgJson[key]
        else:
            cfg[key] = defaults[key]

    return cfg
    