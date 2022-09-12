'''Command-Line Arg Controller

    Easily handle command-line args, both keyworded and positional/non-keyworded/variable-length args

'''

import os
import sys
import importlib.util

def cfgArgObjs(args):

    # valid 'vflag' types
    validTypes = ['string', 'number', 'date', 'email', 'url', 'age', 'gender', 'phone']
    
    # configure a 'valFlag' dict
    def valFlag(vfOpts):

        # 'vFlag' dict
        vflag = {

            # set to True if this arg doesn't require/accept a value
            # usually used for boolean args
            'novalue': False,

            # set to True if this arg only accepts a single character value
            #
            # Ex: 'Y', 'N', '0', etc
            'single': False,

            # allowed value type; Overrides 'single' arg.
            'type': 'any'
        }

        # configure passed in args for 'vFlags'
        for key in vfOpts:

            # if the key is valid
            if key in vflag:

                # if the key is 'type' and the value is allowed
                if key == 'type' and vfOpts[key] in validTypes:

                    # add it
                    vflag['type'] = vfOpts[key]
                else:

                    # else it should be of type 'bool' and if it is
                    if isinstance(vfOpts[key], bool):

                        # add it
                        vflag[key] = vfOpts[key]

        # return the configured 'vflag'
        return vflag

    # the 'configuration' dict
    _cfg = {

        # the name of the arg; can have multiple names; therefore, will convert to a list in the chance multiple names are passed
        #
        # Ex: 'n' and 'name' can be the same arg
        'name': None,

        # a description of this arg; will be used in the 'help' section display
        'description': None,

        # a default value (if any)
        'default': None,

        # 'value' dict
        'value': None
    }

    # configure passed in args for '_cfg' dict
    for key in args:

        # if the key is allowed
        if(key in _cfg):

            # if it's 'valueFlags', make sure it's of type 'dict' and if so
            if key == 'valueFlags' and isinstance(args[key], dict):

                # add it
                _cfg['valueFlags'] = valFlag(args[key])

            else:

                # else it should be of type 'str' and if so
                if isinstance(args[key], str):

                    # add it
                    _cfg[key] = args[key]

    # return configured '_cfg' dict
    return _cfg



def sameType(a, b):
    ta = type(a)
    tb = type(b)
    return ta == tb

def handleCfg(cfg):
    opts = {
        'description': None,
        'args': None,
        'version': None,
        'usage': None
    }
    optTypes = {
        'description': "", 
        'args': [], 
        'version':"", 
        'usage': ""
    }
    cfgObj = {}
    for key in cfg:
        if key in opts and sameType(optTypes[key], cfg[key]):
            opts[key] = cfg[key]
    if opts['args'] is not None:
        cfgArgObjs(opts['args'])

def checkForHelp(args):
    if len(args) == 1 and args[0].strip() == '-help':
        return True

# configure args for this library
def cfgArgs(argsList):
    legend = {
        'n': 'project_name',
        'name': 'project_name',
        's': 'source',
        'source': 'source',
        'u': 'username',
        'username': 'username',
        'nw': 'wheel',
        'nowheel': 'wheel',
        'nt': 'useTestSite',
        'notest': 'useTestSite'
    }
    options = {
        'project_name': None,
        'source': None,
        'username': None,
        'wheel': True,
        'useTestSite': True
    }
    optWaiting = False
    for i in range(len(argsList)):
        _arg = argsList[i].strip()
        if not optWaiting:
            arg = list(_arg.split(' '))
            if arg[0][0] == '-':
                aarg = arg[0][1:].strip()
                if aarg in legend:
                    if options[aarg] is None or isinstance(options[aarg], str):
                        optWaiting = aarg
                    elif isinstance(options[aarg], bool):
                        options[aarg] = False
        else:
            options[optWaiting] = _arg
            optWaiting = False
    print(options)

class FlagController:
    def __init__(self,cfg=None):
        pass
        





'''

cli = cli()
cli.defineArgs([
    {
        name: ['n', 'name'],
        description: 'Your name',
        default: 'new_user',
        value:
    }
])

'''
