def conf():
    helpstr = '''
                        P3 CONFIGURATION
                        ================
    
    Rules:

        - Must be named 'p3conf.json'
        - Must be located at the root of the package directory

    Options:
    
        name - the name of the package
        
        description - a description of the package
        
        src - the path to the codes source files
        
        out - the path to place the packaged output

        license - the license to use for your package
            Possible values are: 
                'none' (default) - uses an Unlicense  
                'mit' - uses the MIT License 
                'agpl' - uses the GNU AGPLv3 License 
                'gpl' - uses the GNU GPLv3 License
                'lgpl' - uses the GNU LGPLv3 License 
                'moz' - uses the Mozilla Public 2.0 License
                'apache' - uses the Apache 2.0 License
                'boost' - uses the Boost Software 1.0 License
    '''
    print(helpstr)
    return True


def gen():
    helpstr = '''
                        !! Welcome to P3 (PyPi Package Packer) !!
                        
    A cli to aid in the creation of a PyPi package and optional wheel distribution.

                                INIT A NEW PACKAGE
                                ==================

        When a new package is initialized, the following directory structure is 
        created within the output directory:

                { package_name }/
                    LICENSE
                    README.md
                    pyproject.toml
                    src/
                        { package_name }/
                            __init__.py
                            main.py
                    tests/


                To initialize a new package directory, run:
                            
                            `p3 init`


                The above command will run the setup interactively.

                To run the program non-interactively, the '-skip' flag can be added:
                            
                            `p3 init -skip`


                For non-interactive mode, a 'p3conf.json' file must be 
                present in the root directory.

                For more help and available options for a 'p3conf.json' file, run:
                            
                            `p3 -help config`



                                BUNDLING A PACKAGE
                                ==================
                Bundles a package that was created using the 'init' method.

                                CREATING A PACKAGE
                                ==================
                This creates a package from an existing code base.

'''
    print(helpstr)
