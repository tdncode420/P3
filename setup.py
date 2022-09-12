from setuptools import setup

setup(
    name='ScraperX',
    version='0.1.0',    
    description='A WebScraping Library',
    url='https://github.com/tdncode420/ScraperX',
    author='Renegade',
    author_email='renegade420@gmail.com',
    packages=['utils'],
    install_requires=['beautifulsoup4 == 4.11.1',
                      'bs4 == 0.0.1',
                      'certifi == 2022.6.15.1',
                      'charset-normalizer == 2.1.1',
                      'idna == 3.3',
                      'requests == 2.28.1',
                      'soupsieve == 2.3.2.post1',
                      'urllib3 == 1.26.12'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',  
        'Operating System:: MacOS',
        'Operating System:: Microsoft:: Windows',
        'Natural Language:: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ])
