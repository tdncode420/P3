import os
import sys
import importlib.util

class CliMan:
    def __init__(self, opts = None):
        
        # the name of the 'CLI library' in creation
        self.name = None

        # a description about the library in creation
        self.description = None

        self.author = None

        self.usage = None
        
        self.version = None

        self.flags = []



    
    def defineFlags(self, flags):
        '''Define the allowed flags for the command line library in creation

        The 'flags' arg passed in must be an iterable collection of some sort (list, set, etc.)
        Each 'flag' within it should be of type dict with the following key/value pairs:

        'flag' - the flags char/s   Ex: 'n'  Would be shown as '-n' (Unless 'prependHyphen' was set to False)
                To specify more than one value here (Example: 'n' and 'name') use a list

        'description' -  a brief description of what this flag is intended for

        'filters' - filters are like rules, define them to assert a specified structure/pattern
                    Possible choices are: 
                    'string' - value given must be a string
                    'number' - value given must be a number 
                    'date' - value given must be a date (ex: in the form of XX?XX?XX|XXXX)
                    'email' - value given must be an email (ex: in the form of XXXXX?@XXXXX.ext)
                    'url' - value given must be a url (ex: in the form of xxxx?.ext)
                    'age' - value given must be an valid age ("valid age" starts at 13)
                    'gender' - value given must be a gender (ex: m | f | male | female)
                    'phone' - value given must be a phone number (ex: ###?###?####)
                    'yesno' - value given must be either 'y' | 'yes' | 'n' | 'no'

 

        Parameters:
            flags (list) - a list of 'flag' cfg dict's 

        '''
        

        # iterate through flags provided
        for flag in flags:
            # init and empty dictionary
            cfg = {}

            # verify that the 'name' arg was passed
            if 'name' not in flag:
                print('All flag dictionaries must include a "name" attribute')
                continue
            
            isDict = isinstance(flag, dict)
            # flag should be a dict
            if not isDict():
                print('Each flag in flags must be of type dict')
            
    