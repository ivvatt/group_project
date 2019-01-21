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

#selecting data for the middle ages
if __name__ == "__main__":
    header = read_header()
    middle_ages = [] #create an empty list for the middle ages
    for year in range(400, 1300): #middle ages years
        padded_year = ('0000' + str(year))[-4:] #add 0's in front of numbers
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: #filter for death cause
                    if 'description' in person: #filter for profession
                        middle_ages.append(person) #add filtered info to list
#save in a json file (list of dictionaries)
with open('middle_ages.json', 'w', encoding='utf-8') as file: #w = writing
    json.dump(middle_ages, file, indent=4)

#selecting data for the renaissance
if __name__ == "__main__":
    header = read_header()
    renaissance = []
    for year in range(1300, 1600): 
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    if 'description' in person:
                        renaissance.append(person)
#save in a json file
with open('renaissance.json', 'w', encoding='utf-8') as file: 
    json.dump(renaissance, file, indent=4)

#selecing data for the enlightenment + industrial revolution
if __name__ == "__main__":
    header = read_header()
    enlight_industrial = []
    for year in range(1700, 1900): 
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    if 'description' in person:
                        if 'deathYear' in person: #filtering for death year (had a problem with that)
                            enlight_industrial.append(person)
#save in a json file
with open('enlight_industrial.json', 'w', encoding='utf-8') as file: 
    json.dump(enlight_industrial, file, indent=4)

#selecting data for the modern era 
if __name__ == "__main__":
    header = read_header()
    modern = []
    for year in range(1900, 2015): 
        padded_year = ('0000' + str(year))[-4:]
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person: 
                    if 'description' in person:
                        modern.append(person)
#save in a json file
with open('modern.json', 'w', encoding='utf-8') as file: 
    json.dump(modern, file, indent=4)

#make it into a csv file
#middle ages
with open('middle_ages.csv', 'w', newline='', encoding='utf-8') as file: 
    filewriter = csv.writer(file)
    filewriter.writerow(['birthYear', "birthDate", "deathYear", "deathCause_label", "profession"])
    for person in middle_ages:
        filewriter.writerow([person['birthYear'], person['birthDate'], person['deathYear'], person['deathCause_label'], person['description']])

#renaissance
with open('renaissance.csv', 'w', newline='', encoding='utf-8') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['birthYear', "birthDate", "deathYear", "deathCause_label", "profession"])
    for person in renaissance:
        filewriter.writerow([person['birthYear'], person['birthDate'], person['deathYear'], person['deathCause_label'], person['description']])

#enlightenment + industrial revolution
with open('enlight_industrial.csv', 'w', newline='', encoding='utf-8') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['birthYear', "birthDate", "deathYear", "deathCause_label", "profession"])
    for person in enlight_industrial:
        filewriter.writerow([person['birthYear'], person['birthDate'], person['deathYear'], person['deathCause_label'], person['description']])

#modern
with open('modern.csv', 'w', newline='', encoding='utf-8') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['birthYear', "birthDate", "deathYear", "deathCause_label", "profession"])
    for person in modern:
        filewriter.writerow([person['birthYear'], person['birthDate'], person['deathYear'], person['deathCause_label'], person['description']])