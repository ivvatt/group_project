library('tidyverse')

#adding columns in disease categories 

century$accidents_murder_and_war <- cbind(century$`Accidents (deaths per 100,000)`, century$`Road accidents (deaths per 100,000)`, na.rm = TRUE)
century$cancer <- cbind(century$`Cancers (deaths per 100,000)`, na.rm = TRUE)
century$cadiovascular_problems <- cbind(century$`Heart disease (deaths per 100,000)`, century$`Stroke (deaths per 100,000)`, na.rm = TRUE)

century <- century %>%
  rowwise() %>%
  mutate(
    other_diseases = sum(`Diabetes (deaths per 100,000)`, `Diarrheal disease (deaths per 100,000)`, na.rm=TRUE)
  )

century$other_respiratory_diseases <- cbind(century$`Tuberculosis (deaths per 100,000)`, na.rm = TRUE)
century$pneumonia <- cbind(century$`Pneumonia and influenza (deaths per 100,000)`, na.rm = TRUE)
century$suicide <- cbind(century$`Suicide (deaths per 100,000)`, na.rm = TRUE)

#deleting extra columns in dataset 
america_data = century %>% select(accidents_murder_and_war, cancer, cadiovascular_problems, other_diseases, other_respiratory_diseases, pneumonia, suicide)

#finding the total sums of each column 
sum(as.numeric(data$accidents_murder_and_war), na.rm = TRUE)
sum(as.numeric(data$cancer), na.rm = TRUE)
sum(as.numeric(data$cadiovascular_problems), na.rm = TRUE)
sum(as.numeric(data$other_diseases), na.rm = TRUE)
sum(as.numeric(data$other_respiratory_diseases), na.rm = TRUE)
sum(as.numeric(data$pneumonia), na.rm = TRUE)
sum(as.numeric(data$suicide), na.rm = TRUE)

#after finding the totals for each disease category, the data was manually converted into a csv file using a excel
#The new csv file is now called "america_dataset"

#plotting the graph 
americaperc <- america_dataset %>%
  mutate(
    total_deaths = sum(Total),
    frequency = Total/total_deaths,
    Cause_of_death = ifelse(str_detect(Cause_of_death, 'cadio'), 'cardiovascular_diseases', Cause_of_death),
    Cause_of_death = str_replace_all(Cause_of_death, '_', ' ')
  )

ggplot(data=americaperc)+
  geom_bar(stat = 'identity', mapping=aes(x=Cause_of_death, y = frequency, color = Cause_of_death, fill = Cause_of_death)) +
  labs(title = "Most Common Causes of Death in the 20th Century", x = "Cause of Death", y = "Percentage of Deaths", color = "Cause of Death") +
  scale_y_continuous(labels= scales::percent_format()) +
  theme(legend.position = "none") +
  coord_flip()


