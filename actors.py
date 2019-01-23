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

amw = ['attack', 'kill', 'murder', 'homicide', 'accident', 'shoot', 'fly', 'holocaust', 'terror', 'opposition', 'strangl', 'stab', 'shot', 'gun', 'injury', 'bomb', 'McCall',\
'motorcycle', 'collision', 'milicja', 'martyr', 'war', 'Prussia', 'trade', 'Qing', 'crash', 'hit', 'heroin', 'hang', 'cocaine', 'guillotine', 'chamber', 'armed', 'exsanguination',\
'airborne', 'opioid', 'execution', 'overdose', 'drug', 'drown', 'channel', 'electr', 'decapitation', 'poison', 'burn', 'trauma', 'explosion', 'ballistic', 'avalanche', 'barbiturate',\
'assassination', 'asphyxia', 'bulldozer', 'tragedy', 'dissection', 'flight', 'ammunition', 'alcohol', 'alfredo', 'fire', 'earthquake', 'unrest', 'eruption', 'military', 'police',\
'abuse', 'punish', 'benghazi', 'battle', 'genocide', 'railway', 'birth', 'delirium', 'duel', 'fall', 'fatigue', 'gallows', 'purge', 'henriette', 'massacre', 'lynch', 'morphine',\
'laudunum', 'nazi', 'NKVD', 'sallekhana', 'snake', 'sokushinbutsu', 'water speed']

#selecting data for actors 
if __name__ == "__main__":
    header = read_header()
    actors = [] #create an empty list for actors
    for year in range(400, 2015): 
        padded_year = ('0000' + str(year))[-4:] #add 0's in front of numbers
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person and 'description' in person:
                    causes = person['deathCause_label'][1:-1].split('|') if '{' in person['deathCause_label'] else [person['deathCause_label']]
                    for deathCause in causes:
                        if 'actor' in person['description'].lower():
                            if re.search('(cancer|tumor|leukemia|\w+oma)($|\W)', deathCause, flags=re.I):
                                person['deathCause_label'] = 'cancer'
                            elif 'bronch' in deathCause.lower() or 'asthma' in deathCause.lower() or 'lung' in deathCause.lower() or 'pulmon' in deathCause.lower() or 'respirat' in deathCause.lower() or 'tubercolosis' in deathCause.lower():
                                person['deathCause_label'] = 'other_respiratory_problems' 
                            elif 'pneumonia' in deathCause.lower():
                                person['deathCause_label'] = 'pneumonia'
                            elif 'cardi' in deathCause.lower() or 'heart' in deathCause.lower() or 'circulatory' in deathCause.lower() or 'arterio' in deathCause.lower():
                                person['deathCause_label'] = 'cardiovascular_problems'
                            elif 'cerebral' in deathCause.lower() or 'stroke' in deathCause.lower() or 'aneurysm' in deathCause.lower() or 'alzheimer' in deathCause.lower():
                                person['deathCause_label'] = 'cerebral_problems'  
                            elif 'suicide' in deathCause.lower():
                                person['deathCause_label'] = 'suicide'  
                            elif 'natural' in deathCause.lower() or 'old' in deathCause.lower():
                                person['deathCause_label'] = 'natural_death'  
                        #elif 'attack' in deathCause.lower() or 'kill' in deathCause.lower() or 'murder' in deathCause.lower() or 'homicide' in deathCause.lower() or 'accident' in deathCause.lower() or 'shoot' in deathCause.lower() or 'fly' in deathCause.lower() or 'holocaust' in deathCause.lower() or 'terror' in deathCause.lower() or 'opposition' in deathCause.lower() or 'strangl' in deathCause.lower() or 'stab' in deathCause.lower() or 'shot' in deathCause.lower() or 'gun' in deathCause.lower() or 'injury' in deathCause.lower() or 'bomb' in deathCause.lower() or 'McCall' in deathCause.lower() or 'motorcycle' in deathCause.lower() or 'collision' in deathCause.lower() or 'milicja' in deathCause.lower() or 'martyr' in deathCause.lower() or 'war' in deathCause.lower() or 'Prussia' in deathCause.lower() or 'trade' in deathCause.lower() or 'Qing' in deathCause.lower() or 'crash' in deathCause.lower() or 'hit' in deathCause.lower() or 'heroin' in deathCause.lower() or 'hang' in deathCause.lower() or 'cocaine' in deathCause.lower() or 'guillotine' in deathCause.lower() or 'chamber' in deathCause.lower() or 'armed' in deathCause.lower() or 'exsanguination' in deathCause.lower() or 'airborne' in deathCause.lower() or 'opioid' in deathCause.lower() or 'execution' in deathCause.lower() or 'overdose' in deathCause.lower() or 'drug' in deathCause.lower() or 'drown' in deathCause.lower() or 'channel' or deathCause.lower() or 'electr' in deathCause.lower() or 'decapitation' in deathCause.lower() or 'poison' in deathCause.lower() or 'burn' in deathCause.lower() or 'trauma' in deathCause.lower() or 'explosion' in deathCause.lower() or 'ballistic' in deathCause.lower() or 'avalanche' in deathCause.lower() or 'barbiturate' in deathCause.lower() or 'assassination' in deathCause.lower() or 'asphyxia' in deathCause.lower() or 'bulldozer' in deathCause.lower() or 'tragedy' in deathCause.lower() or 'dissection' in deathCause.lower() or 'flight' in deathCause.lower() or 'ammunition' in deathCause.lower() or 'alcohol' in deathCause.lower() or 'alfredo' in deathCause.lower() or 'fire' in deathCause.lower() or 'earthquake' in deathCause.lower() or 'unrest' in deathCause.lower() or 'eruption' in deathCause.lower() or 'military' in deathCause.lower() or 'police' in deathCause.lower() or 'abuse' in deathCause.lower() or 'punish' in deathCause.lower() or 'benghazi' in deathCause.lower() or 'battle' in deathCause.lower() or 'genocide' in deathCause.lower() or 'railway' in deathCause.lower() or 'birth' in deathCause.lower() or 'delirium' in deathCause.lower() or 'duel' in deathCause.lower() or 'fall' in deathCause.lower() or 'fatigue' or deathCause.lower() or 'gallows' in deathCause.lower() or 'purge' in deathCause.lower() or 'henriette' in deathCause.lower() or 'massacre' in deathCause.lower() or 'lynch' in deathCause.lower() or 'morphine' in deathCause.lower() or 'laudunum' in deathCause.lower() or 'nazi' in deathCause.lower() or 'NKVD' in deathCause.lower() or 'sallekhana' in deathCause.lower() or 'snake' in deathCause.lower() or 'sokushinbutsu' in deathCause.lower() or 'water speed' in deathCause.lower(): 
                            elif True in [cause in deathCause.lower() for cause in amw]:
                                person['deathCause_label'] = 'accidents_murder_and_war' 
                            else:
                                person['deathCause_label'] = 'other_diseases'    
                           #modern_death_noother.remove('other_diseases') 
                            if person['deathCause_label'] != 'other_diseases':                                                                                
                                actors.append(person.copy())
#save in a json file (list of dictionaries)
with open('actors.json', 'w', encoding='utf-8') as file: #w = writing
    json.dump(actors, file, indent=4)
#make csv file
with open('actors.csv', 'w', newline='', encoding='utf-8') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['birthYear', "birthDate", "deathYear", "deathCause_label", "profession"])
    for person in actors:
        filewriter.writerow([person['birthYear'], person['birthDate'], person['deathYear'], person['deathCause_label'], person['description']])

#selecting data for politicians
if __name__ == "__main__":
    header = read_header()
    politicians = [] #create an empty list for actors
    for year in range(400, 2015): 
        padded_year = ('0000' + str(year))[-4:] #add 0's in front of numbers
        if os.path.exists('years/'+padded_year): 
            data = process_csv(padded_year, header)
            for person in data:
                if 'deathCause_label' in person and 'description' in person:
                    causes = person['deathCause_label'][1:-1].split('|') if '{' in person['deathCause_label'] else [person['deathCause_label']]
                    for deathCause in causes:
                        if 'politician' in person['description'].lower() or 'president' in person['description'].lower() or 'minister' in person['description'].lower():
                            if re.search('(cancer|tumor|leukemia|\w+oma)($|\W)', deathCause, flags=re.I):
                                person['deathCause_label'] = 'cancer'
                            elif 'bronch' in deathCause.lower() or 'asthma' in deathCause.lower() or 'lung' in deathCause.lower() or 'pulmon' in deathCause.lower() or 'respirat' in deathCause.lower() or 'tubercolosis' in deathCause.lower():
                                person['deathCause_label'] = 'other_respiratory_problems' 
                            elif 'pneumonia' in deathCause.lower():
                                person['deathCause_label'] = 'pneumonia'
                            elif 'cardi' in deathCause.lower() or 'heart' in deathCause.lower() or 'circulatory' in deathCause.lower() or 'arterio' in deathCause.lower():
                                person['deathCause_label'] = 'cardiovascular_problems'
                            elif 'cerebral' in deathCause.lower() or 'stroke' in deathCause.lower() or 'aneurysm' in deathCause.lower() or 'alzheimer' in deathCause.lower():
                                person['deathCause_label'] = 'cerebral_problems'  
                            elif 'suicide' in deathCause.lower():
                                person['deathCause_label'] = 'suicide'  
                            elif 'natural' in deathCause.lower() or 'old' in deathCause.lower():
                                person['deathCause_label'] = 'natural_death'  
                        #elif 'attack' in deathCause.lower() or 'kill' in deathCause.lower() or 'murder' in deathCause.lower() or 'homicide' in deathCause.lower() or 'accident' in deathCause.lower() or 'shoot' in deathCause.lower() or 'fly' in deathCause.lower() or 'holocaust' in deathCause.lower() or 'terror' in deathCause.lower() or 'opposition' in deathCause.lower() or 'strangl' in deathCause.lower() or 'stab' in deathCause.lower() or 'shot' in deathCause.lower() or 'gun' in deathCause.lower() or 'injury' in deathCause.lower() or 'bomb' in deathCause.lower() or 'McCall' in deathCause.lower() or 'motorcycle' in deathCause.lower() or 'collision' in deathCause.lower() or 'milicja' in deathCause.lower() or 'martyr' in deathCause.lower() or 'war' in deathCause.lower() or 'Prussia' in deathCause.lower() or 'trade' in deathCause.lower() or 'Qing' in deathCause.lower() or 'crash' in deathCause.lower() or 'hit' in deathCause.lower() or 'heroin' in deathCause.lower() or 'hang' in deathCause.lower() or 'cocaine' in deathCause.lower() or 'guillotine' in deathCause.lower() or 'chamber' in deathCause.lower() or 'armed' in deathCause.lower() or 'exsanguination' in deathCause.lower() or 'airborne' in deathCause.lower() or 'opioid' in deathCause.lower() or 'execution' in deathCause.lower() or 'overdose' in deathCause.lower() or 'drug' in deathCause.lower() or 'drown' in deathCause.lower() or 'channel' or deathCause.lower() or 'electr' in deathCause.lower() or 'decapitation' in deathCause.lower() or 'poison' in deathCause.lower() or 'burn' in deathCause.lower() or 'trauma' in deathCause.lower() or 'explosion' in deathCause.lower() or 'ballistic' in deathCause.lower() or 'avalanche' in deathCause.lower() or 'barbiturate' in deathCause.lower() or 'assassination' in deathCause.lower() or 'asphyxia' in deathCause.lower() or 'bulldozer' in deathCause.lower() or 'tragedy' in deathCause.lower() or 'dissection' in deathCause.lower() or 'flight' in deathCause.lower() or 'ammunition' in deathCause.lower() or 'alcohol' in deathCause.lower() or 'alfredo' in deathCause.lower() or 'fire' in deathCause.lower() or 'earthquake' in deathCause.lower() or 'unrest' in deathCause.lower() or 'eruption' in deathCause.lower() or 'military' in deathCause.lower() or 'police' in deathCause.lower() or 'abuse' in deathCause.lower() or 'punish' in deathCause.lower() or 'benghazi' in deathCause.lower() or 'battle' in deathCause.lower() or 'genocide' in deathCause.lower() or 'railway' in deathCause.lower() or 'birth' in deathCause.lower() or 'delirium' in deathCause.lower() or 'duel' in deathCause.lower() or 'fall' in deathCause.lower() or 'fatigue' or deathCause.lower() or 'gallows' in deathCause.lower() or 'purge' in deathCause.lower() or 'henriette' in deathCause.lower() or 'massacre' in deathCause.lower() or 'lynch' in deathCause.lower() or 'morphine' in deathCause.lower() or 'laudunum' in deathCause.lower() or 'nazi' in deathCause.lower() or 'NKVD' in deathCause.lower() or 'sallekhana' in deathCause.lower() or 'snake' in deathCause.lower() or 'sokushinbutsu' in deathCause.lower() or 'water speed' in deathCause.lower(): 
                            elif True in [cause in deathCause.lower() for cause in amw]:
                                person['deathCause_label'] = 'accidents_murder_and_war' 
                            else:
                                person['deathCause_label'] = 'other_diseases'    
                           #modern_death_noother.remove('other_diseases') 
                            if person['deathCause_label'] != 'other_diseases':                                                                                
                                politicians.append(person.copy())
#save in a json file (list of dictionaries)
with open('politicians.json', 'w', encoding='utf-8') as file: #w = writing
    json.dump(politicians, file, indent=4)
#make csv file
with open('politicians.csv', 'w', newline='', encoding='utf-8') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['birthYear', "birthDate", "deathYear", "deathCause_label", "profession"])
    for person in politicians:
        filewriter.writerow([person['birthYear'], person['birthDate'], person['deathYear'], person['deathCause_label'], person['description']])

