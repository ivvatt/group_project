#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

## In python3,

import argparse, json, logging, csv, re, sys, codecs
import os.path

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="h.txt"):
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

def process_csv(file, header):
    out=[]
    stdin = file == "-"
    fd = sys.stdin if stdin else codecs.open('years/' + file, "r", "UTF-8")
    reader = csv.reader(fd)
    for nr, row in enumerate(reader):
        logging.debug("%d fields in line %d", len(row), nr)
        d = dict()
        out.append(d)
        for i, field in enumerate(row):
            if field != "NULL":
                if floatre.match(field):
                    d[header[i]] = float(field)
                elif intre.match(field):
                    d[header[i]] = int(field)
                else:
                    d[header[i]] = field
    if not stdin:
        fd.close()
    return out

if __name__ == "__main__":
    header = read_header()
    middle_ages = []
    #philosophers = []
    for year in range(400, 1300): #middle ages
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    #if 'description' in person and "scientist" in str(person["description"]):
                        middle_ages.append(person)

with open('middle_ages.json', 'w', encoding='utf-8') as file: #w = writing; r = reading (read-only file); output is in another file named 'output.json'
    json.dump(middle_ages, file, indent=4)
    #json.dump(out, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    header = read_header()
    renaissance = []
    #philosophers = []
    for year in range(1300, 1600): #renaissance
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    #if 'description' in person and "scientist" in str(person["description"]):
                        renaissance.append(person)

with open('renaissance.json', 'w', encoding='utf-8') as file: #w = writing; r = reading (read-only file); output is in another file named 'output.json'
    json.dump(renaissance, file, indent=4)

if __name__ == "__main__":
    header = read_header()
    enlight_industrial = []
    #philosophers = []
    for year in range(1700, 1900): #enlightenment + industrial revolution
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    #if 'description' in person and "scientist" in str(person["description"]):
                        enlight_industrial.append(person)

with open('enlight_industrial.json', 'w', encoding='utf-8') as file: #w = writing; r = reading (read-only file); output is in another file named 'output.json'
    json.dump(enlight_industrial, file, indent=4)

if __name__ == "__main__":
    header = read_header()
    modern = []
    #philosophers = []
    for year in range(1900, 2015): #modern
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    #if 'description' in person and "scientist" in str(person["description"]):
                        modern.append(person)

with open('modern.json', 'w', encoding='utf-8') as file: #w = writing; r = reading (read-only file); output is in another file named 'output.json'
    json.dump(modern, file, indent=4)


