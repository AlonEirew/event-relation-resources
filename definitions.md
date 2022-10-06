# Definitions and Settings
Below are some general and informal fundamental component and task definitions, explaining event and event-event relations tasks and settings in NLP.


## Table Of Contents
- [Event](#event)
- [Event Mention/Span](#event-mention-or-span)
- [Event Arguments](#event-arguments)
- [Event Detection](#event-detection)
- [Event Extraction](#event-extraction)
- [Annotation Density](#event-annotation-density)
- [Coreference Resolution](#coreference-resolution)
- [Subevent Identification](#subevent-identification)
- [Causality Identification](#event-causality-identification-eci)
- [Temporality Identification](#event-temporality-identification-eti)
- [Settings](#settings)
    - [Within Document](#within-document)
    - [Cross Document](#cross-document)


## Event
An event is a specific occurrence involving participants, and which results from a combination of four components such as: 1) an action component referring to what happens or holds; 2) a time slot which is responsible for anchoring the action in time ; 3) a location component which links the action component to a place/location; and 4) a participant component, which illustrates the “who” or “what” is involved in the action component.

For example: I meet yesterday with John in Tel-Aviv.

| Action | Time | Location | Who |
| ------------- | ------------- | ------------- | ------------- |
| Meet | yesterday | Tel-Aviv | John |

> ℹ️  Except of the Action, It’s not mandatory for all slots to be filled for any given event, in many cases some of the event’s slots will be empty.


## Event Mention (or Span)
In general, the event mention (or span) is usually referred to the word or phrase which corresponds to the action component of the event (i.e., “meet” in the above example).

> ℹ️ There are two main definitions to how event span should be annotated: Minimum-Span (see RED annotation guideliness) and Maximum-Span (see ACE annotation guideliness).


> ℹ️ Event Trigger: is a word that most clearly expresses an event that happens.


## Event Arguments
Events are defined by their arguments, those denote the what, when, where and who of the event (in other words the entities that are involved in the event). In above table - “yesterday”, “Tel-Aviv” and “Johnl” are the argument of the “meet” event.

> ℹ️ Entity is any text instance which indicate participant, location, organization, time, date, object, or any other text entity that might be tracked in the discourse. 

> ℹ️ Event arguments are entities, however not all entities are event arguments.


## Event Detection
Event detection aims to find event mentions with specific event types from given texts. In other words, an event detection system should be able to identify the event trigger (mention) in text as well as recognize the event specific type. For example, identified event "fired" (corresponding to "shot" not "layoff") should be labeled with the type "Attack".


## Event Extraction
Event extraction is the process of identifying the event mention along with its argument from input text. 

More information on Event Extraction [here](arguments.md).

> ℹ️ Some works jointly model event extraction and detection as a single task (that is, predicting the event trigger, type and arguments). 


## Event Annotation Density
Annotating events and event relations, is considered a very challenging and expensive task. Consequentially, while some datasets were exhaustively annotated to have all events covered in a given text, other datasets (usually much larger ones) only contain annotations to part of the events which exist in the text. 

> ℹ️ In the non-exhaustive case, the task of event detection usually cannot be performed, and the event mention spans are given as part of the input.


## Coreference Resolution
Two events are said to corefer, if they refer to the same event in space and time. 
For example:
1. 2018 Nobel prize for physics *goes to* Donna Strickland 
2. Prof. Strickland *is awarded* the Nobel prize for physics

Event "goes to" in sentence (1) corefer with "is awarded" event from sentence (2).

*_Coreference resolution_* is the process of identifying and clustering together events which corefer to each other.

The Coreference relation is symmetrical and transitive.

> ℹ️ Symmetrical relation: if A->B, than B->A. 

> ℹ️ Transitive relation: if A->B and B->C, than A->C


## Subevent Identification
A subevent relationship is defined in terms of ($e_1$,$e_2$), where $e_1$ and $e_2$ are events: event $e_2$ is a subevent of event $e_1$ if $e_2$ is spatiotemporally contained by $e_1$. More concretely, we say that an event $e_1$ is a parent event of event $e_2$, and $e_2$ is a child event of $e_1$ if: (1) $e_1$ is collector event that contains a complex sequence of activities; (2) $e_2$ is one of these activities; and (3) $e_2$ is spatially and temporally contained within $e_1$ (i.e., $e_2$ occurs within the same time and same place as $e_1$)


## Event Causality Identification (ECI)
The causal relation refer to the case where one event caused another event to trigger. Two main types of causality, explicit and implicit. The former means that causality is guided by some explicit causal connectives, such as “cause”, “lead to” and “because of”. The latter means that there are no explicit causal connectives in the sentence.

ECI is the process of identifying causal relation between events. That is, identifying that event A “caused” event B to trigger. 

For example:
"Donna Strickland was *awarded* the Nobel Prize for the *implementation* of chirped pulse amplification"

Implementation -- cause --> awarded

Causal relation is asymmetric and transitive.


## Event Temporality Identification (ETI)
ETI is the process of identifying temporal event relations in context. That is, identifying that event A occurs in time *before* event B, and vice versa (B occurrs *after* A). Temporal relations can help figure out the temporality and duration of events, and summarize the timeline of a series of events. Understanding temporal information described in natural language text is considered a key component of natural language understanding.

> ℹ️ There are many sub-types to the temporal relations which differ from one annotation scheme to another (such as: before, after, start, end, meet, overlab, during, etc...).


## Settings
Two main settings exist for the event-event relation extraction task


### Within Document
WD event-event relation extraction is the task of identifying event relations between pairs of event mentions within a single document. Thus, given as input a single document, an event-event relation extraction model will be required to examine all pairs of events within the document.


### Cross Document
CD event-event relation extraction is the task of identifying event relations between pairs of event mentions within a single document and across multiple documents. Thus, given a *set* of documents, an event-event relation extraction model will be required to examine the relation between all pair of events mentions within each document independently as well as between all pairs of event mentions across different documents.


> ℹ️ The cross-document is considered a more challenging task as it covers the within-document task as well.


> ℹ️ The within-document task is more studied in the academic litriture and larger dataset exist for the task evaluation. 
