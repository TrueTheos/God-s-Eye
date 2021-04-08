"""
    Author : Micah Hoffman (@WebBreacher)
    Description : Takes each username from the web_accounts_list.json file and performs the lookup to see if the discovery entry is still valid
"""
import codecs
from datetime import datetime
import json
import os
import random
import signal
import string
import sys
import time

import requests
import urllib3
import threading

##########################
# Variables && Functions #
##########################

# Set HTTP Header info.
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate'
           }

all_found_sites = []

# Create the final results dictionary
_username = ""
overall_results = {}
username_results = []


def check_os():
    """
    # check operating system or adjust output color formatting
    :return: operating_system
    """
    # set default operating system to windows
    operating_system = "windows"

    if os.name == "posix":
        operating_system = "posix"
    return operating_system


#
# Class for colors
#
class Bcolors:
    # if os is windows or something like that then define colors as nothing
    CYAN = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    ENDC = ''

    # if os is linux or something like that then define colors as following
    if check_os() == "posix":
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'

    def disable(self):
        self.CYAN = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.ENDC = ''


def signal_handler(*_):
    """
    If user pressed Ctrl+C close all connections and exit
    """
    finaloutput()
    sys.exit(130)


def web_call(location):
    try:
        # Make web request for that URL, timeout in X secs and don't verify SSL/TLS certs
        resp = requests.get(location, headers=headers, timeout=60, verify=False, allow_redirects=False)
    except requests.exceptions.Timeout:
        return f' !  ERROR: {location} CONNECTION TIME OUT. Try increasing the timeout delay.'
    except requests.exceptions.TooManyRedirects:
        return f' !  ERROR: {location} TOO MANY REDIRECTS. Try changing the URL.'
    except requests.exceptions.RequestException as e:
        return f' !  ERROR: CRITICAL ERROR. {e}'
    else:
        return resp


def random_string(length):
    return ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(length))


def finaloutput():
    print('\n-------------------------------------------')

    if _username:
        print(f'Searching for sites with username ({_username}) > Found {len(username_results)} results:\n')
        for result in username_results:
            print(result)
    else:
        if len(overall_results) > 0:
            print('The following previously "valid" sites had errors:')
            for site_with_error, results in sorted(overall_results.items()):
                print(Bcolors.YELLOW + '     %s --> %s' % (site_with_error, results) + Bcolors.ENDC)
        else:
            print(':) No problems with the JSON file were found.')


# Suppress HTTPS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################
#      Main       #
###################

# Add this in case user presses CTRL-C
signal.signal(signal.SIGINT, signal_handler)

inputfile = os.path.dirname(os.path.realpath(__file__)) + '/web_accounts_list.json'

with open(inputfile, encoding='utf-8') as data_file:
    data = json.load(data_file)

def check_site(site, username=None):
    # Examine the current validity of the entry
    if not site['valid']:
        return

    if not site['known_accounts'][0]:
        return

    # Set the username
    if username:
        uname = username
    else:
        # if no username specified Pull the first user from known_accounts and replace the {account} with it
        known_account = site['known_accounts'][0]
        uname = known_account

    url = site['check_uri'].replace("{account}", uname)

    # Perform initial lookup
    r = web_call(url)
    if isinstance(r, str):
        # We got an error on the web call
        return
    else:

        # Analyze the responses against what they should be
        code_match = r.status_code == int(site['account_existence_code'])
        string_match = r.text.find(site['account_existence_string']) >= 0

        if username:
            if code_match and string_match:
                username_results.append(Bcolors.GREEN + '[+] Found user at %s' % url + Bcolors.ENDC)
                all_found_sites.append(url)
                return
        else:
            if code_match and string_match:
                # logging.info('     [+] Response code and Search Strings match expected.')
                # Generate a random string to use in place of known_accounts
                url_fp = site['check_uri'].replace("{account}", random_string(20))
                r_fp = web_call(url_fp)
                if isinstance(r_fp, str):
                    # If this is a string then web got an error
                    return

                code_match = r_fp.status_code == int(site['account_existence_code'])
                string_match = r_fp.text.find(site['account_existence_string']) > 0

                if code_match and string_match:
                    overall_results[site['name']] = 'False Positive'
                else:
                    # logging.info('     [+] Passed false positives test.')
                    pass
            elif code_match and not string_match:
                # TODO set site['valid'] = False                
                overall_results[site['name']] = 'Bad detection string.'

            elif not code_match and string_match:
                # TODO set site['valid'] = False
                overall_results[site['name']] = 'Bad detection code. Received Code: %s; Expected Code: %s.' % \
                                                (str(r.status_code), site['account_existence_code'])
            else:
                # TODO set site['valid'] = False
                overall_results[site['name']] = 'Bad detection code and string. Received Code: %s; Expected Code: %s.' \
                                                % (str(r.status_code), site['account_existence_code'])

def whatsmyname(target):
    # Start threads
    _username = target
    threads = []

    start_time = datetime.utcnow()
    for site_ in data['sites']:
        x = threading.Thread(target=check_site, args=(site_, _username), daemon=True)
        threads.append(x)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Print result
    finaloutput()

    return username_results
