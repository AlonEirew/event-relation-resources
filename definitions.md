# Definitions and Settings
Below are some general and informal fundamental components definitions, which are critical to the understanding of the of the event-event relation extraction task and settings.


## Table Of Contents
- [Event](#event)
- [Mention/Span](#event-mentionspan)
- [Detection](#event-detection)
- [Annotation Density](#event-annotation-density)
- [Coreference Resolution](#coreference-resolution)
- [Subevent Identification](#subevent-identification)
- [Causality Identification](#event-causality-identification-eci)
- [Temporality Identification](#event-temporality-identification-eti)
- [Settings](#settings)
    - [Within Document](#within-document)
    - [Cross Document](#cross-document)


## Event
An event is any punctual, durational, or stative situation which happens or holds, and which results from a combination of four components such as: 1) an action component referring to what happens or holds; 2) a time slot which is responsible for anchoring the action in time ; 3) a location component which links the action component to a place/location; and 4) a participant component, which illustrates the “who” or “what” is involved in the action component.
I meet yesterday with John for lunch in Tel-Aviv.

| Action | Time | Location | Who/What |
| ------------- | ------------- | ------------- | ------------- |
| Meet | yesterday | Tel-Aviv | John/Lunch |

> ℹ️  It’s not mandatory of all slots to be filled for any given event, in many cases some of the event’s slots will be empty.


## Event Mention/Span
In general, the event mention or span is usually referred to the word or phrase which corresponds to the action component of the event (i.e., “meet” in the above example).

> ℹ️ There are two main definitions to the how event span should be annotated: Minimum-Span (see RED annotation guideliness) and Maximum-Span (see ACE annotation guideliness).


## Event Detection
Event detection is the process of identifying the event mention or span within text. In most event-event relation extraction settings, part of the task is to detect the event mentions as well. This end-to-end event detection and event relation extraction, is more realistic as in real world scenarios event mentions will not be provided with the text.


## Event Annotation Density
Annotating events and event relations, is considered a very challenging and expensive task. Consequentially, while some datasets were exhaustively annotated to have all events covered in the text, other datasets (usually much larger ones) only contain annotations to part of the existing events. 

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