"""
    RenegadeSoftware© 2020

    "Web Scraping Utilities"

    A utlity module holding many different methods that
    aid in the process of "web scraping"

    Nothing is "hard-coded" and all methods below will work
    in any situation/environment

    To use this file, open a up a new terminal, cd into the 
    directory containing this file and install all required 
    modules by running the following command:
        `pip install -r requirements.txt`

    Optionally, you can manually pip install each needed module
    listed in the imports below
"""

import requests as req                      # *needs installation*
from bs4 import BeautifulSoup as bs         # *needs installation*
from random import choice                   # built-in
from requests.exceptions import HTTPError   # installs with 'requests'


def getSoup(url):

    """ Creates and returns a simple 'soup' object using the
        'BeautifulSoup4 (bs4)' library

        Parameters:
            url (str): the url in which to create the soup object from

        Returns:
            dict: {soup_object}
    """

    # create the soup object
    soup = bs(req.get(url).text, 'html.parser')

    # return it
    return soup



def randomProxy():

    """Returns a random proxy object to use
        
        Returns: 
            dict: {
                    ip
                    port
                    country
                }
    """

    # the url to the site holding the list of SSL proxies
    site_url = "https://sslproxies.org/"

    # create the soup object
    soup = getSoup(site_url)

    # grab the first <table>
    table = soup.find_all('table')[0]

    # grab all the table's rows holding the proxy information
    trows = table.find_all('tr')

    # pull a random row from the table
    trow = choice(trows)

    # get the rows data cells
    tds = trow.find_all('td')

    # pull the proxy's IP address
    ip = tds[0].get_text()

    # pull the proxy's port number
    port = tds[1].get_text()

    # pull the proxy's country of origin
    country = tds[3].get_text()

    # return proxy info
    return {
        "ip": ip,
        "port": port,
        "country": country
    }



def randomUserAgent():

    """Generates a random User Agent string to use
        Example:
            `Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAARJS; rv:11.0) like Gecko`

        Returns:
            str: random user agent
    """

    # open the file containing the list of user agents
    f = open('web_scraping/bin/user_agents.txt')

    # read the file
    uagents = f.read()

    # convert the giant string of agents into a list
    agentList = list(uagents.split('\n'))

    # return a random choice from the agents list
    return choice(agentList)




def getData(url, proxy):

    """Performs a GET requests and returns the response while handling any occuring errors or exceptions

        Parameters:
            url (str): the url in which to get data from
            proxy (str): a proxy host

        Returns:
            dict: {response_object}

    """

    try:
        # attempt to fetch a response
        res = requests.request(
            'get', url, proxies=proxy, timeout=7)

        # If the response was successful, no Exception will be raised
        res.raise_for_status()

    # handle any errors/ exceptions
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')
        return False
    else:

        # if successful, return response object
        return res



def data_scraper(url):

    """Performs a data scraping process by combining the 2 methods 'randomProxy()' and 'getData()' from above and returns the response

        Parameters:
            url (str): the url in which to get data from

        Returns:
            dict: {response_object}
    """

    # grab a random proxy
    proxy = randomProxy()

    # get a random user agent
    headers = {
        'User-Agent': randomUserAgent()
    }

    # send the request
    res = req.request(
        'get', url, proxies=proxy, timeout=7)
    
    # return the response
    return res




def writeFile(data, file_, json_):

    """Write the given data to a provided file. Optionally, the data can be written as valid JSON

        Parameters:
            data (str) - the data to write
            file_ (str) - the path to the file to write to/create
            json_ (bool) - write data as JSON?

        Returns:
            bool: True on success

    """

    # open the file
    f = open(file_, "w")

    # write the data
    if (json_ == True):

        # as json
        f.write(json.dumps(data, indent=4))
    else:

        # or as is (plain text)
        f.write(data)

    # close the file
    f.close()

    return True



