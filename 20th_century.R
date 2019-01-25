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
data = century %>% select(accidents_murder_and_war, cancer, cadiovascular_problems, other_diseases, other_respiratory_diseases, pneumonia, suicide)

#adding columns
#colSums(data.num)
library(data.table)
new_data <- as.data.frame.table(read.csv(data.choose(), header = T))
new_data[total = sum(cancer)]


total_cancer <- data %>% 
  #group_by(cancer) %>%
  summarise(total_cancer = sum(cancer))
sum(as.numeric(data$accidents_murder_and_war), na.rm = TRUE)
sum(as.numeric(data$cancer), na.rm = TRUE)
sum(as.numeric(data$cadiovascular_problems), na.rm = TRUE)
sum(as.numeric(data$other_diseases), na.rm = TRUE)
sum(as.numeric(data$other_respiratory_diseases), na.rm = TRUE)
sum(as.numeric(data$pneumonia), na.rm = TRUE)
sum(as.numeric(data$suicide), na.rm = TRUE)

ggplot(data=americaperc)+
  geom_bar(stat = 'identity', mapping=aes(x=Cause_of_death, y = frequency, color = Cause_of_death, fill = Cause_of_death)) +
  theme(axis.text.x = element_text(angle= 70, hjust = 1)) +
  labs(title = "Most Common Causes of Death in the 20th Century", x = "Cause of Death", y = "Percentage of Deaths", color = "Cause of Death") +
  scale_y_continuous(labels= scales::percent_format()) +
  theme(legend.position = "none")

americaperc <- america %>%
  mutate(
    total_deaths = sum(Total),
    frequency = Total/total_deaths,
    Cause_of_death = ifelse(str_detect(Cause_of_death, 'cadio'), 'cardiovascular_diseases', Cause_of_death)
  )
