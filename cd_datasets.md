# Cross-Document Datasets
In this section listed all datasets annotated with event-event relations (single or more). 

## Table Of Contents 

- [Automatic Content Extraction (ACE)](#automatic-content-extraction-ace)
- [CaTeRS](#caters-causal-and-temporal-relation-scheme)
- [EventCorefBank Extension (ECB+)](#eventcorefbank-extension-ecb)
- [Entities, Relations and Events (ERE)](#entities-relations-and-events-ere)
- [Event-Event Relations (EER)](#event-event-relations-eer)
- [Event StoryLine Corpus (ESC)](#event-storyline-corpus-esc)
- [Gun Violence Corpus (GVC)](#gun-violence-corpus-gvc)
- [HyperCoref](#hypercoref)
- [MEANTIME](#meantime)
- [Richer Event Description (RED)](#richer-event-description-red)
- [Wikipedia Event Coreference (WEC)](#wikipedia-event-coreference-wec)


## Automatic Content Extraction (ACE)
ACE is a thorough event annotation guidelines which include guidelines in multiple languages. Addtinoally, ACE is used as the base annotation scheme to many following event annotation guidelines.

- [English Annotation Guidelines for
Events](https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-events-guidelines-v5.4.3.pdf)
- [Annotation Tasks and Specifications](https://www.ldc.upenn.edu/collaborations/past-projects/ace/annotation-tasks-and-specifications)


## CaTeRS: Causal and Temporal Relation Scheme
WIP


## EventCorefBank Extension (ECB+)
An extended version of the EventCorefBank (ECB), this dataset is the most commonly used dataset for training and testing models for the CD event coreference task. ECB+ consists of documents partitioned into 43 clusters, each corresponding to a certain news topic.

### References
- [Using a sledgehammer to crack a nut? Lexical diversity and event coreference resolution](https://aclanthology.org/L14-1646/)
- [ECB+ Dataset](http://www.newsreader-project.eu/results/data/the-ecb-corpus/)

| Data Source | Documents | Events | Density | Annotation | Lang | License |
| ------------- | :-------------: | :-------------: | :-------------: | ------------- | :-------------: | :-------------: |
| News | 982 | 6,833 | partial-exhaustive | events<br/> entities<br/> coreference | eng | [CC-BY](http://creativecommons.org/licenses/by/2.0/) |



## Entities, Relations and Events (ERE)
- Light ERE - was designed as a lighter-weight version of ACE and a simple approach to entity, relation, and event annotation, with the goal of making annotation easier and more consistent.
    - TBD link to paper and dataset
- Rich ERE - annotation expands on both the inventories and taggability of Light ERE
    - [Entities, Relations and Events](https://tac.nist.gov/2016/KBP/guidelines/summary_rich_ere_v4.2.pdf)
    - [From Light to Rich ERE: Annotation of Entities, Relations, and Events](https://aclanthology.org/W15-0812.pdf)

## Event-Event Relations (EER)
EER Annotation focuses on relations between events in the ERE/ACE taxonomy, both within document and cross-document.

### References
- [Building a Cross-document Event-Event Relation Corpus](https://aclanthology.org/W16-1701)
- Dataset-TBD link in paper doesn't work]

| Data Source | Documents | Events | Density | Annotation | Lang | License |
| ------------- | :-------------: | :-------------: | :-------------: | ------------- | :-------------: |:-------------: |
| News | 125 | 863 | exhaustive | events<br/> coreference<br/> temporal<br/> causal<br/> subevent | TPD | Free |


## Event StoryLine Corpus (ESC)
Annotation scheme and benchmark dataset for the temporal and causal relation detection.

## Gun Violence Corpus (GVC)
WIP

## HyperCoref
WIP

## MEANTIME
MEANTIME corpus is a semantically annotated corpus of Wikinews articles. MEANTIME and ECB+ uses the same [NewsReader annotation guideliness](http://www.newsreader-project.eu/files/2014/12/NWR-2014-2-2.pdf), The corpus consists of 480 news articles in English, Spanish, Italian, and Dutch.

### References
- [MEANTIME, the NewsReader Multilingual Event and Time Corpus](https://aclanthology.org/L16-1699/)
- [MEANTIME Dataset](http://www.newsreader-project.eu/results/data/wikinews/)

| Data Source | Documents | Events | Density | Annotation | Lang | License |
| ------------- | :-------------: | :-------------: | :-------------: | ------------- | :-------------: | :-------------: |
| Wikinews | 480 | 863 | exhaustive | events<br/> entities<br/> coreference<br/> | eng<br/> it<br/> de<br/> sp | CC-BY |


## Richer Event Description (RED)
Richer Event Description is an attempt to bring together a number of existing and well-researched veins of document annotation into a single representation of the events and participants in a discourse. It is not concerned with semantic role annotation in the traditional sense

### References
- [Richer Event Description: Integrating event coreference with temporal, causal and bridging annotation](https://aclanthology.org/W16-5706)
- [RED Annotation Guidelines](https://github.com/timjogorman/RicherEventDescription/blob/master/guidelines.md)
- [RED Dataset](https://catalog.ldc.upenn.edu/LDC2016T23)

| Data Source | Docs | Events | Density | Annotation | Setting | License |
| ------------- | :-------------: | :-------------: | :-------------: | ------------- | :-------------: | :-------------: |
| News | 95 | 8731 | Exhaustive | entities, events, coreference, temporal, causal and subevent | Cross-Document | LDC |


## Wikipedia Event Coreference (WEC)
WIP