'''PyPiPackagePacker

    A CLI to package python code into a distributable pip package with optional wheel distribution

'''

import os
import sys
import importlib.util
import constants as _C
import configuration as _CFG
from tmps import *
from licenses import *
from utils import *

# shorten package command
_pu = packageUtils


def initNew(args):
    '''Init a new package'''

    if len(args) == 0:
        cfg = _CFG.interactiveCreate()
    if args[0] == 'skip':
        cfg = _CFG.noninteractiveCreate()
    _pu.createNewPkgStruct(cfg)


def buildPkg(args):
    '''Build a package pre-generated by the 'init' method'''

    pass

def createPkg(args):
    '''Build a package from a pre-existing code source (one not created by the 'init' method)'''

    pass

def showHelp(args):
    '''Show one of the help messages'''

    # if no other args were given
    if len(args) == 0:

        # display the 'General Help' message
        helpDisplay.gen()
        return

    # possible strings to invoke the 'conf' message
    cfg_strs = ['conf', 'cfg', 'config', 'configuration']

    # if it's found
    if args[0] in cfg_strs:

        # display the conf message
        helpDisplay.conf()
        return


# main entry point
def __init__():

    # this library's methods to invoke
    RESP_MTHDS = {'init': initNew, 'build': buildPkg,
                'create': createPkg, 'help': showHelp}

    # the args passed from cmd line
    ARGS_LIST = list(sys.argv)

    # remove the 'calling script' arg value as it's not needed
    ARGS_LIST.pop(0)

    # the first arg passed should be one of this libs methods ('init', 'bundle', '-help')
    arg1 = ARGS_LIST.pop(0).strip()

    # if the '-help' flag was passed
    if arg1 == '-help':

        # remove the prepending hyphen (-)
        # it's only required for syntatic sugaring
        arg1 = 'help'

    # if first arg is valid...
    if arg1 in RESP_MTHDS:

        # run it
        RESP_MTHDS[arg1](ARGS_LIST)
