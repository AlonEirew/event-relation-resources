# Tasks
List of event related tasks

## Table Of Contents
- [Detection](#event-detection)
- [Extraction](#event-extraction)
- [Coreference Resolutkon](#event-coreference-resolution)
- [Coreference Search](#event-coreference-search)
- [Temporality Identification](#event-temporality-identification-eti)
- [Causality Identification](#event-causality-identification-eci)
- [Subevent Identification]()

### Event Detection
The Event Detection task aims to find event mentions which correlate to specific event types in given texts. In other words, an event detection system should be able to identify the event trigger (mention) in text as well as recognize the event specific type. For example, identify that the event mention "fired" (corresponding to "shot" not "layoff") should be labeled with the type "Attack".


### Event Extraction
Event Extraction is the process of identifying the event mention along with its argument (entities) from input texts. 

> ℹ️ Some works jointly model event extraction and detection as a single task (that is, predicting the event trigger, type and arguments). 


**Event extraction can be divided into two groups:**
- *_Close-Domain Event Extraction_* -- Uses predefined event schema to detect and extract desired event from text
- *_Open-Domain Event Extraction_* -- does not assume predefined event structures, and the main task is to detect the existence of an event in text and extract it

#### Input:
- text (passage/document)

#### Output (extended task):
- all event instances in the text, and if existing, identify the events type as well as its participants (arguments) and attributes (roles)



### Event Coreference Resolution
The process of identifying and clustering together coreferring events. 

The task can be performed within a single document (usually referred to as "Within Document (WD)" event coreference) or across a set of documents (referred to as Cross Document (CD) event coreference).

> ℹ️ The CD task is considered more challenging as it usually covers both the WD and CD tasks.

#### Input:
- A single document (for the WD task) 
- Set of documents (for the CD task)

#### Output:
- Set of clusters containing event mentions which corefere with eachother



### Event Coreference Search
The task involved with searching (efficiently), in a large collection, all coreferring event mentions for a specific event of interest (query).

#### Input:
- A query containing a marked target event mention in context 
- A passage/document collection to search in

#### Output:
- all coreferring mentions, within their passages



### Event Temporality Identification (ETI)
he process of identifying temporal event relations in context. Temporal relations can help figure out the temporality and duration of events, and summarize the timeline of a series of events.

#### Input:
- A text sentence/passage/document with marked events

#### Output:
- a directed temporal graph whose nodes represent events and edges represent the temporal relations between them.



### Event Causality Identification (ECI)
the process of identifying event-causal pairs in context. That is, identifying that event  "caused" event B to trigger. 

#### Input:
- A text sentence/passage/document with a pair of events marked within it

#### Output:
- The causal relation between the two events



### Subevent Identification
The process of identifying the structure hierarchy between event. 