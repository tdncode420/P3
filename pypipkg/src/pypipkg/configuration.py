import os
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

    # create the project structure
    return cfg


def noninteractiveCreate():
    '''Non-Interactively configures a configuration dictionary for a new package
    
        Requires a 'p3conf.json' to be present at the oot of the directory
    '''

    cfg = {}
    
    cfgPath = os.path.join(os.getcwd(), 'p3conf.json')

    try:

        cfgJson = open(cfgPath, 'r').read()

    except FileNotFoundError:

        print('You are trying to use this script in \'Non-interactive\' mode but no \'p3conf.json\' file was found.')
        print('Please create one and place it at the root of the directory that you are running this command in.')
        print('For more help/info about the \'p3conf.json\' file, run the command: `p3 -help conf`')
        cfgJson =  False
    finally:
        return cfgJson
