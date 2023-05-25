# Definitions, Settings and Tasks
Below are some general and informal fundamental component and task definitions, explaining event and event-event relations tasks and settings in NLP.


## Table Of Contents
- [Event](#event)
    - [Mention](#event-mention)
    - [Span](#event-span)
    - [Cluster](#event-cluster)
    - [Arguments](#event-arguments)
- [Event Relations](#event-event-relations)
    - [Hierarchical Relationship](#hierarchical-relationship)
        - [Coreference](#coreference)
        - [Subevent](#subevent)
    - [Non-Hierarchical Relationship](#non-hierarchical-relationships)
        - [Causal](#causal)
        - [Temporal](#temporal)
- [Tasks](#tasks)
    - [Event Detection](#event-detection)
    - [Event Extraction](#event-extraction)
    - [Event Linking](#event-linking)
    - [Event Coreference Resolutkon](#event-coreference-resolution)
    - [Event Coreference Search](#event-coreference-search)
    - [Temporality Identification](#event-temporality-identification-eti)
    - [Causality Identification](#event-causality-identification-eci)
    - [Subevent Identification]()


## Event
An event is a specific occurrence in space and time that involving participants, such as verbs (e.g. investigate), nominalization (e.g. crash), common nouns (e.g. party, accident) and proper nouns (e.g. Cannes Festival 2016). An event is a combination of four components: 1) an action component referring to what happens or holds; 2) a time slot which is responsible for anchoring the action in time ; 3) a location component which links the action component to a place/location; and 4) a participant component, which illustrates the “who” or “what” is involved in the action component.

For example: I met with John yesterday in Tel-Aviv.

| Action | Time | Location | Who |
| ------------- | ------------- | ------------- | ------------- |
| Met | yesterday | Tel-Aviv | John |

> ℹ️  Except of the Action, It’s not mandatory for all slots to be filled for any given event, in many cases some of the event’s slots will be empty.


### Event Mention
An event might be mentioned multiple times within the same document or across different documents. An event mention refers to a single mention of an event.

> ℹ️ Event Trigger: is a word that most clearly expresses an event that happens.


### Event Span
The event span refers to the word or phrase which corresponds to the event (i.e., the span of the “meet” event from the above example is a single word).

> ℹ️ There are two main definitions to how event span should be annotated: Minimum-Span (explored in [RED annotation guideliness](datasets.md#richer-event-description-red) and Maximum-Span (explored in [ACE annotation guideliness](datasets.md#automatic-content-extraction-ace)).


### Event Cluster
Discrete event mentions which all refer to the same event in the real world, when clustered together they form an "event cluster". In other words, an event cluster consist of a set of event mentions which [corefer](#coreference-resolution) to each other.


### Event Arguments
Events are defined by their arguments, those arguments denote the what, when, where and who of the event (i.e., the entities involved in a purticular event). In above table - “yesterday”, “Tel-Aviv” and “Johnl” are the “meet” event argument.

> ℹ️ Entity is any text instance which indicate participant, location, organization, time, date, object, or any other text entity that might be tracked in the discourse. 

> ℹ️ Event arguments are entities, however not all entities are event arguments.


## Event-Event Relations
Events might have spatio-temporal, causal or hierarchical relation between them. 
The task of identifying the relation that might exist between events, is considered to be an important task in natural language understanding. 

Defined below the four most studied event-event relation identification tasks.

### Hierarchical Relationships
#### Coreference
Two event mentions are said to corefer, if they refer to the same real-world event in space and time. 
For example:
1. 2018 Nobel prize for physics **goes to** Donna Strickland 
2. Prof. Strickland is **awarded** the Nobel prize for physics

The event "goes to" in sentence (1) corefer with the "awarded" event from sentence (2).

The Coreference relation is a symmetrical and transitive relation.

> ℹ️ Event cluster consist of a set of event mentions that share a coreference relation between them.

> ℹ️ Symmetrical relation: if A->B, than B->A. 

> ℹ️ Transitive relation: if A->B and B->C, than A->C


#### Subevent
A subevent relationship is defined in terms of $(e_1,e_2)$, where $e_1$ and $e_2$ are events: event $e_2$ is a subevent of event $e_1$ if $e_2$ is spatiotemporally contained by $e_1$. More concretely, we say that an event $e_1$ is a parent event of event $e_2$, and $e_2$ is a child event of $e_1$ if: (1) $e_1$ is collector event that contains a complex sequence of activities; (2) $e_2$ is one of these activities; and (3) $e_2$ is spatially and temporally contained within $e_1$ (i.e., $e_2$ occurs within the same time and same place as $e_1$)

Example:
- Prof. Strickland was **awarded** the Nobel prize for physics at the 2018 Nobel prize **ceremony**. 

The event "awarded" is a sub-event of the "ceremony" event

### Non-Hierarchical Relationships
#### Causal
The causal relation refer to the case where one event caused another event to trigger. Two main types of causality, explicit and implicit. The former means that causality is guided by some explicit causal connectives, such as “cause”, “lead to” and “because of”. The latter means that there are no explicit causal connectives in the sentence.

Event Causality Identification (ECI) is the process of identifying causal relation between events. That is, identifying that event A “caused” event B to trigger. 

For example:
"Donna Strickland was *awarded* the Nobel Prize for the *implementation* of chirped pulse amplification"

Implementation -- cause --> awarded

Causal relation is asymmetric and transitive.


#### Temporal
Temporal relations can help figure out the temporality and duration of events, and summarize the timeline of a series of events.

Event Temporality Identification (ETI) is the process of identifying temporal event relations in context. That is, identifying that event A occurs in time *before* event B, and vice versa (B occurrs *after* A). 

> ℹ️ There are many sub-types to the temporal relations which differ from one annotation scheme to another (typical relations types are: before, after, meet, overlap, during, etc...).


## Tasks

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


### Event Linking
 Event linking tries to link an event mention appearing in an article to the most appropriate Wikipedia page. This page is expected to provide rich knowledge about what the event mention refers to.

#### Input:
- An article and an event mention *m* in it

#### Output (extended task):
- A title *t*, extracted from Wikipedia titles which provides the best explanation of *m*. 


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
