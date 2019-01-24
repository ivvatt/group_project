

ggplot() +
  geom_table(data = enlight_industrial, aes(x = deathCause_label))

pneumonia %>% enlight_industrial %>% select('deathCause_label') %>% filter(deathCause_label = 'pneumonia')

summary.data.frame("deathCause_label")

library('plyr')

# counting number of occurrences of a disease
count(enlight_industrial, 'deathCause_label')

# sorting data by disease
cancer <- enlight_industrial %>% filter(str_detect(deathCause_label, '(?i)Cancer'))

suicide <- enlight_industrial %>% filter(str_detect(deathCause_label, '(?i)suicide'))

# merging data sets
cancerandsuicide <- rbind(cancer, suicide)

carcinoma <- enlight_industrial %>% filter()
topcauses_death <- enlight_industrial %>% group_by(deathCause_label) %>% 
  filter(deathCause_label == 'Cancer', 'Cardiovascular disease', 'Cerebral hemorrhage', 'Death by natural causes', 'Heart failure', 'Myocardial infarction', 'Pneumonia', 'Stroke', 'Suicide', 'Tuberculosis')

# graph showing cancer death type distribution with fixed labels and color.
Cancers <- cancer$deathCause_label # changing name of legend by changing variable name
ggplot() +
  geom_bar(data = cancerandsuicide, aes(x = Cancers))
ggplot() +
  geom_bar(data = cancer, aes(x = Cancers, color = Cancers, fill = Cancers)) +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Deaths by Cancer during the Enlightenment and the Industrial Revolution', x = 'Type of Cancer', y = 'Frequency')

# graphing all newly categorized causes of death
ggplot() +
  geom_bar(data = enlight_industrial_death, aes(x = deathCause_label, color = deathCause_label, fill = deathCause_label)) +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Deaths during the Enlightenment and the Industrial Revolution', x = 'Cause of Death', y = 'Frequency', fill = 'Cause of Death', color = 'Cause of Death') 

count(enlight_industrial_death, 'deathCause_label')
# sorting data by death cause (omitting other diseases)

total_deaths_noother <- enlight_industrial_death %>% filter(deathCause_label %in% c('cancer', 'suicide', 'natural_death', 'accidents_murder_and_war', 'cardiovascular_problems', 
                                                                                    'other_respiratory_problems', 'pneumonia' ))

# transforming into percentages data set
counts <- count(enlight_industrial_death_noother, 'deathCause_label')
counts$perc <- counts$freq / sum(counts$freq)

# proportional FINAL GRAPH DEATHS INDUST/ENLIGHT
ggplot() +
  geom_bar(data = counts, aes(x = deathCause_label, y = perc, color = deathCause_label, fill = deathCause_label), stat='identity') +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Deaths during the Enlightenment and the Industrial Revolution', x = 'Cause of Death', y = 'Proportion of Total Deaths', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")




 