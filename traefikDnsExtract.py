#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Philippe Wauters"
__copyright__ = "Copyright 2011, carnimaniac"
__license__ = "GPL"
__version__ = "0.1"

import requests
import re
import argparse


# functions
def print_to_screen(list_sc):
    for element in list_sc:
        print('www.{0}'.format(element))


def save_to_file(list_sv, file):
    with open(file, 'w') as f:
        for element in list_sv:
            f.write("www.{}\n".format(element))


# Parser
parser = argparse.ArgumentParser(description='Get list of domaine from traefik web app')

parser.add_argument('url', action='store', type=str, help='URL (http://site:port/api/http/routers)')
parser.add_argument('-p', '--printsc', action='store_true', help='print to screen')
parser.add_argument('-s', '--sort', action='store_true', help='Sort the list of domain before print')
parser.add_argument('-o', '--output', metavar='FILE', help='Save to file')

args = parser.parse_args()

# Core
response = requests.get(args.url)

if response.status_code == 200:
    # load the json for traitement
    hosts = response.json()

    # vars
    listDomain = []

    # Extract hosts
    for host in hosts:

        h = host['rule']

        try:
            # Regex get domain
            found = re.search('www.' + '([A-Za-z_0-9.-]+).*', h).group(1)
            listDomain.append(found)
            # print(found)

        except AttributeError:
            # print("error")
            pass

    # Clean list
    listDomain = list(set(listDomain))

    # Argument traitment
    if args.sort:
        listDomain.sort()

    if args.printsc:
        print_to_screen(listDomain)

    if args.output:
        save_to_file(listDomain, args.output)
else:
    print("URL don't match")
