library(tidyverse)
#Load file
modern <- read.csv("modern_death_noother.csv", stringsAsFactors = TRUE)
#View(modern)
#Count the number of occurences for all the causes and make it into a data frame
Counts1 <- count(modern, deathCause_label)
#Add a new column in the Counts1 dataframe for each factor's respective percentage (in decimal form)
Counts1$percent <- (Counts1$n / sum(Counts1$n))
#Add a new column idicating the factors' time periods, which are all "modern"
Counts1$time_period <- c("Time_Period")
Counts1$time_period <- "Modern" 

industrial <- read.csv("enlight_industrial_death_noother.csv", stringsAsFactors = TRUE)
#View(industrial)
#Count the number of occurences for all the causes and make it into a data frame
Counts2 <- count(industrial, deathCause_label)
#Add a new column in the Counts2 dataframe for each factor's respective percentage (in decimal form)
Counts2$percent <- (Counts2$n / sum(Counts2$n))
#Add a new column idicating the factors' time periods, which are all "Enlightenment/Industrial"
Counts2$time_period <- c("Time_Period")
Counts2$time_period <- "Enlightenment/Industrial"

#Bind the Counts1 and Counts2 frames and replace '_' in variable names to spaces
total_eras<- rbind(Counts1, Counts2) %>% mutate(deathCause_label= str_replace_all(deathCause_label,'_',' '))

#Count the number of occurences for all the causes and make it into a data frame
Counts <- count(total_eras, deathCause_label)
#Add a new column for each factors respective percentage (in decimal form)
total_eras$percent <- Counts$n / sum(Counts$n)

#Plot the percentages as a bar chart 
ggplot()+
  #stat= 'identity' allows for the y variable mapped in the aesthetic to be computed
  geom_bar(data=total_eras, mapping=aes(x= deathCause_label, y= percent, color= time_period, fill= time_period), stat= 'identity', position= 'dodge')+
  #Increase size of the x and y variable labels as well
  theme(axis.text.x.bottom = element_text(size=10))+
  theme(axis.text.y.left = element_text(size=12))+
  #Make a title as well as a new x and y axis label
  labs(title = "Comparing Deaths in the Modern Era and the Enlightenment/Industrial Era", x= "Cause of Death", y= "Percentage of Total Deaths", color= "Time Period", fill= "Time Period")+
  #Turn the y variable into percentage format
  scale_y_continuous(labels = scales::percent_format())+
  #Flip the graph horizontally for legibility
  coord_flip()

Modern_Industrial <- rbind(modern,industrial)
