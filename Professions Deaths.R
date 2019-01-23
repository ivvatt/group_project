library(tidyverse)

# actors most common deaths
ggplot() +
  geom_bar(data = actors, aes(x = deathCause_label, color = deathCause_label, fill = deathCause_label)) +
    theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
       labs(title = 'Most Common Causes of Death among Actors', x = 'Cause of Death', y = 'Proportion', fill = 'Cause of Death', color = 'Cause of Death') +
         scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

# actresses most common death causes
ggplot() +
  geom_bar(data = actresses, aes(x = deathCause_label, color = deathCause_label, fill = deathCause_label)) +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death among Actresses', x = 'Cause of Death', y = 'Proportion', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

# combining datasets for acting profession (without other diseases)
all_acting <- rbind(actors, actresses)

ggplot() +
  geom_bar(data = all_acting, aes(x = deathCause_label, color = deathCause_label, fill = deathCause_label)) +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death in the Acting Profession', x = 'Cause of Death', y = 'Proportion', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

#testing actors and other diseases
ggplot() +
  geom_bar(data = actors_copy, aes(x = deathCause_label, color = deathCause_label, fill = deathCause_label)) +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death among Actors', x = 'Cause of Death', y = 'Proportion', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

# merging other dis acting sets
actingotherdis <- rbind(actors_copy, actresses_copy)

# creating proportions for acting, new dataset.
actingperc <- count(actingotherdis, deathCause_label)
actingperc$perc <- actingperc$n / sum(actingperc$n)


#FINAL graph acting profession with other diseases
ggplot() +
  geom_bar(data = actingperc, aes(x = deathCause_label, y = perc, color = deathCause_label, fill = deathCause_label), stat='identity') +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death in the Acting Profession', x = 'Cause of Death', y = 'Proportion of Deaths', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

#FINAL writers professions (percentages, graph)

writersperc <- count(writers, deathCause_label)
writersperc$perc <- writersperc$n / sum(writersperc$n)

ggplot() +
  geom_bar(data = writersperc, aes(x = deathCause_label, y=perc, color = deathCause_label, fill = deathCause_label), stat='identity') +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death in the Writing Profession', x = 'Cause of Death', y = 'Proportion of Deaths', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

# FINAL civil servants (perc, graph)

poliperc <- count(politicians, deathCause_label)
poliperc$perc <- poliperc$n / sum(poliperc$n)

ggplot() +
  geom_bar(data = poliperc, aes(x = deathCause_label, y=perc, color = deathCause_label, fill = deathCause_label), stat='identity') +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death in the Civil Service', x = 'Cause of Death', y = 'Proportion of Deaths', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")

professions_total <- rbind(politicians, all_acting, writers)

# businesspeople FINAL (perc, graph)

busiperc <- count(business, deathCause_label)
busiperc$perc <- busiperc$n / sum(busiperc$n)

ggplot() +
  geom_bar(data = busiperc, aes(x = deathCause_label, y=perc, color = deathCause_label, fill = deathCause_label), stat='identity') +
  theme(axis.text.x = element_text(angle = 70, hjust = 1)) +
  labs(title = 'Most Common Causes of Death in the Business Industry', x = 'Cause of Death', y = 'Proportion of Deaths', fill = 'Cause of Death', color = 'Cause of Death') +
  scale_y_continuous(labels = scales::percent_format()) +
  theme(legend.position = "none")
  
  
  