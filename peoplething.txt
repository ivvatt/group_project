import json
import csv 

#from the dataset, select birthyears and causes of death from all of the entries (for each person) 
#save them in a new data set (make into csv) and work with that

people = []

with open ('', encoding='utf-8-sig') as file:
    people = json.load(file)
    for person in people:
        #select all entries for birth year
        if "Afghanistan" in conflict['country']:
            #select all entries for cause of death
            if conflict['year'] == 1998 or conflict['year'] == 2004:
                if 'Taleban' in conflict['side_b'] or 'UIFSA' in conflict['side_b']:
                    people.append(person)


#make it into a csv file
headers = ['Birth.Year', 'Cause.of.Death', 'Death.Date']
with open('people.csv', 'w', newline='') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(headers)
    for conflict in conflicts_afg:
        filewriter.writerow([person['birthDate'], person['deathCause'], person['deathYear']])
