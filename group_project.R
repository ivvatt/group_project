library(tidyverse)
library(maps)

middle_ages <- read.csv('middle_ages.csv', stringsAsFactors = FALSE)
renaissance <- read.csv('renaissance.csv', stringsAsFactors = FALSE)
enlight_industrial <- read.csv('enlight_industrial.csv', stringsAsFactors = FALSE)
modern <- read.csv('modern.csv', stringsAsFactors = FALSE)

birthYear <- format(as.Date(birthYear, format="%Y-%M-%D"),"%Y")

ggplot() +
  geom_bar(data=middle_ages, mapping = aes(x = deathCause_label)) 

ggplot() +
  geom_bar(data=renaissance, mapping = aes(x= deathCause_label)) 
  
ggplot() +
  geom_bar(data=enlight_industrial, mapping = aes(x= deathCause_label))

library('plyr')
count(enlight_industrial, 'deathCause_label')

ggplot() +
  geom_bar(data=modern, mapping = aes(x=deathCause_label))
