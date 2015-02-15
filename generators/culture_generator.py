# -*- coding: utf-8 -*-

"""This script parses culture related data
Folders to check:
/history/provinces
"""
from os import listdir, path
import time, re, json

def read_culture_colours():

    colours = {}

    f = open("00_cultures.txt")
    skip_re = re.compile('graphical')

    for line in f:
        tabs = len(line) - len(line.lstrip('\t'))
        
        if tabs == 1 and not re.search(skip_re, line):
            print line

def read_cultures_from_provinces():
    date_re = re.compile('\Aculture')

    cultures = {}

    for prov in listdir("history/provinces"):
        prov_id = int((prov.split(' '))[0])
        provp = path.join("history/provinces", prov)

        f = open(provp)

        culture = None
        for line in f:
            if re.search(date_re, line):
                tmp = line.split(' = ')
                tmp = tmp[1].split('#')
                culture = tmp[0].strip()
                break

        if culture is not None:
            cultures[prov_id] = culture

    for key in cultures:
        print (key, cultures[key])

    with open('cultures.js', 'w') as f:
        f.write("var cultures = ") 
        json.dump(cultures, f, separators=(',',':'))

def generate():
    read_cultures_from_provinces()
    read_culture_colours()

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating cultures.js took %.3f seconds" %delta)
