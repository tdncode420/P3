from datetime import date, datetime
from random import choice

def generate():
    '''Generate a random key value (a collection of str(int)'s)(Example: "43547")'''

    # a list of a few positive integers
    POSINTS = [3, 4, 5, 6]

    # choose a random int from the POSINTS list
    POSINT = choice(POSINTS)

    # a str of integers created by concatenating todays date and the current time
    FULLSTR = str(datetime.today()).replace(':', '').replace(' ', '').replace('-', '').replace('.', '')

    # pull a random int from FULLSTR
    KEYADDER = int(choice(FULLSTR))

    # if the key is of low value or 0
    if KEYADDER < 3:

        # add the POSINT to it since POSINT is guaranteed to be a +int between 3 - 6
        KEYADDER = KEYADDER + POSINT

    # pull another random int from FULLSTR to use as a range for iteration
    # this number must be + and would be more valuable with a value above 3 so add the KEYADDER which guarantees that
    FILEKEYS = int(choice(FULLSTR)) + KEYADDER

    # an empty filekey to build on
    filekey = ""

    # iterate through the range equal to the value of FILEKEYS
    for i in range(FILEKEYS):

        # append a random str(int) from FULLSTR to the filekey
        filekey = filekey + str(choice(FULLSTR))

    # return the newly generated filekey (a randomly generated str(int) with a length guaranteed to be above 3)
    return filekey
