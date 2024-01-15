
import argparse
import sys
import requests, json
from sys import argv
import os


parser = argparse.ArgumentParser()

parser.add_argument("-t", help="target ip", type=str, dest='target', required=True)

args = parser.parse_args()


lightblue = '\033[94m'
lightgreen = '\033[92m'
clear = '\033[0m'
boldblue = '\033[01m''\033[94m'
cyan = '\033[36m'
bold = '\033[01m'
red = '\033[31m'
lightcyan = '\033[96m'
yellow = '\033[93m'
ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = yellow+bold+"[~]"
        print(a, "", data['query'])
        print(a, ":", data['as'])
        print(a, "ISP:", data['isp'])
        print(a, "ORG:", data['org'])
        print(a, "Country:", data['country'])
        print(a, "Region:", data['regionName'])
        print(a, "City:", data['city'])
        print(a, "Zip code:", data['zip'])
        print(a, "Timezone:", data['timezone'])
        print(a, "Latitude:", data['lat'])
        print(a, "Longitude:", data['lon'])
# Error Handling
except KeyboardInterrupt:
        print('Exiting,Good Bye'+clear)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red+bold+"[!]"+" Non-existent Wi-Fi"+clear)
