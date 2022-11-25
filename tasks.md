# Tasks
List of event related tasks

## Table Of Contents
- [Event Detection](#event-detection)
- [Event Extraction](#event-extraction)
- [Event Coreference Resolutkon](#event-coreference-resolution)
- [Event Coreference Search]()

### Event Detection
The Event Detection task aims to find event mentions which correlate to specific event types in given texts. In other words, an event detection system should be able to identify the event trigger (mention) in text as well as recognize the event specific type. For example, identify that the event mention "fired" (corresponding to "shot" not "layoff") should be labeled with the type "Attack".


### Event Extraction
Event Extraction is the process of identifying the event mention along with its argument (entities) from input texts. 

> ℹ️ Some works jointly model event extraction and detection as a single task (that is, predicting the event trigger, type and arguments). 


### Event Coreference Resolution
*_Evevt Coreference resolution_* is the process of identifying and clustering together coreferring events. 

The task can be performed within a single document (usually referred to as "Within Document (WD)" event coreference) or across a set of documents (referred to as Cross Document (CD) event coreference).

> ℹ️ The CD task is considered more challenging as it usually covers both the WD and CD tasks.


### Event Coreference Search
*_Event Coreference Search_* is the task of searching coreferring events to a query event in a large document collection.

