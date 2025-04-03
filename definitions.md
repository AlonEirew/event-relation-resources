# Definitions, Settings, and Tasks  
Below are general and informal definitions of key components and tasks in event-based NLP, including core concepts and the various settings in which event and event-event relation tasks are performed.


## Table Of Contents
- [Event](#event-)
    - [Mention](#event-mention-)
    - [Span](#event-span-)
    - [Cluster](#event-cluster-)
    - [Arguments](#event-arguments-)
- [Event Relations](#event-event-relations-)
    - [Hierarchical Relationships](#hierarchical-relationships)
        - [Coreference](#coreference-)
        - [Subevent](#subevent-)
    - [Non-Hierarchical Relationship](#non-hierarchical-relationships)
        - [Causal](#causal-)
        - [Temporal](#temporal-)
- [Tasks](#tasks)
    - [Event Detection](#event-detection-)
    - [Event Extraction](#event-extraction-)
    - [Event Linking](#event-linking-)
    - [Event Coreference Resolutkon](#event-coreference-resolution-)
    - [Event Coreference Search](#event-coreference-search-)
    - [Temporality Identification](#event-temporality-identification-eti-)
    - [Causality Identification](#event-causality-identification-eci-)
    - [Subevent Identification](#subevent-identification-)

---

## Event  
An **event** is a specific occurrence situated in time and space that involves participants. Events may be expressed through various linguistic forms, such as verbs (e.g., *investigate*), nominalizations (e.g., *crash*), common nouns (e.g., *party*, *accident*), or proper nouns (e.g., *Cannes Festival 2016*).

An event typically consists of four components:
1. **Action** – What happens or holds.
2. **Time** – When the event occurs.
3. **Location** – Where the event takes place.
4. **Participants** – Who or what is involved.

**Example:** *I met with John yesterday in Tel-Aviv.*

| Action | Time     | Location | Who   |
|--------|----------|----------|-------|
| Met    | yesterday | Tel-Aviv | John  |

> ℹ️ Except for the action, not all slots must be filled for an event. In many cases, some components (time, location, or participants) may be missing.

---

### Event Mention  
An event may be mentioned multiple times within a document or across documents. An **event mention** refers to a single textual occurrence of an event.

> ℹ️ **Event Trigger**: The word that most clearly expresses the event taking place.

---

### Event Span  
The **event span** refers to the word or phrase in the text that expresses the event (e.g., in the example above, the span for the event *meet* is the word *met*).

> ℹ️ There are two common approaches to event span annotation:  
> • **Minimum-span** – Used in [RED annotation guidelines](datasets.md#richer-event-description-red)  
> • **Maximum-span** – Used in [ACE annotation guidelines](datasets.md#automatic-content-extraction-ace)

---

### Event Cluster  
A group of discrete event mentions that refer to the same real-world event forms an **event cluster**. In other words, an event cluster consists of multiple event mentions that [corefer](#coreference-resolution) to one another.

---

### Event Arguments  
**Event arguments** specify the contextual details of an event—such as who was involved, when and where it happened, or what it was about. In the example above, *yesterday*, *Tel-Aviv*, and *John* are arguments of the *meet* event.

> ℹ️ An **entity** is any text span that refers to a participant, location, organization, time, date, object, or any other relevant element in the discourse.  
> ℹ️ Event arguments are entities, but not all entities serve as event arguments.

---

## Event-Event Relations  
Events can be related to one another through **temporal**, **causal**, **spatial**, or **hierarchical** relationships.  
The task of identifying such relations is crucial for deeper natural language understanding.

---

### Hierarchical Relationships

#### Coreference  
Two event mentions are said to **corefer** if they refer to the same real-world event in space and time.

**Example:**
1. *The 2018 Nobel Prize for Physics* **goes to** *Donna Strickland.*  
2. *Prof. Strickland is* **awarded** *the Nobel Prize for Physics.*

The event **"goes to"** in sentence (1) corefers with the event **"awarded"** in sentence (2).

The coreference relation is **symmetric** and **transitive**.

> ℹ️ An **event cluster** consists of a set of event mentions that share a coreference relation.  
> ℹ️ **Symmetric relation**: If A → B, then B → A.  
> ℹ️ **Transitive relation**: If A → B and B → C, then A → C.

---

#### Subevent  
A **subevent** relationship is defined for a pair of events \((e_1, e_2)\), where event \(e_2\) is considered a subevent of event \(e_1\) if it is **spatiotemporally contained** within \(e_1\).

In practical terms:
- \(e_1\) is a **parent event** representing a broader or composite activity.
- \(e_2\) is a **child event** representing a specific activity that takes place within the time and location boundaries of \(e_1\).

To establish a subevent relation:
1. \(e_1\) is a **collector event**, representing a complex or extended event.  
2. \(e_2\) is one of the activities or steps that compose \(e_1\).  
3. \(e_2\) is **temporally and spatially contained** within \(e_1\).

**Example:**
- *Prof. Strickland was* **awarded** *the Nobel Prize for Physics at the 2018 Nobel Prize* **ceremony**.

In this case, the event **"awarded"** is a **subevent** of the **"ceremony"** event.

---

Here is your refined **Non-Hierarchical Relationships** section, edited for grammar, clarity, and consistency:

---

### Non-Hierarchical Relationships

#### Causal  
A **causal relation** refers to a case where one event **causes** another event to occur. Causality can be expressed in two main ways:

- **Explicit causality**: Marked by explicit connectives such as *cause*, *lead to*, *because of*, etc.  
- **Implicit causality**: Implied through context, without the use of explicit markers.

**Event Causality Identification (ECI)** is the task of determining whether a causal relation exists between two events—that is, identifying that event A **caused** event B to happen.

**Example:**  
*Donna Strickland was* **awarded** *the Nobel Prize for the* **implementation** *of chirped pulse amplification.*

**Causal link:** `implementation` → *caused* → `awarded`

Causal relations are:
- **Asymmetric**: If A causes B, then B does not cause A.  
- **Transitive**: If A causes B and B causes C, then A causes C.


#### Temporal  
**Temporal relations** capture the ordering and duration of events, helping to construct timelines and understand event sequences in a narrative.

**Event Temporality Identification (ETI)** is the task of identifying temporal relations between events in context—for example, determining that event A happens *before* event B, or that event B occurs *after* event A.

> ℹ️ There are many subtypes of temporal relations, which vary across annotation schemes. Common types include:  
> • *before*  
> • *after*  
> • *overlap*  
> • *during*  
> • *meet*

---

## Tasks

### Event Detection  
The **Event Detection** task involves identifying event mentions in text and classifying them into specific event types.  
In other words, an event detection system must locate the **event trigger** and assign it an appropriate **event type**.

**Example:**  
Identify that the mention *“fired”* (meaning *shot*, not *layoff*) should be labeled with the type **Attack**.

---

### Event Extraction  
**Event Extraction** is the process of identifying event mentions along with their **arguments** (i.e., the entities involved in the event).

> ℹ️ Some approaches model event detection and extraction jointly—predicting the trigger, type, and arguments in one unified task.

**Event extraction is typically categorized into:**
- *_Closed-Domain Event Extraction_* — Uses a predefined schema to detect and extract specific types of events.  
- *_Open-Domain Event Extraction_* — Does not assume predefined structures; the goal is to detect and extract any event mentioned in the text.

#### Input:
- Text passage or document

#### Output (extended task):
- All event instances in the text, along with their types, participants (arguments), and attributes (roles)

---

### Event Linking  
**Event Linking** attempts to associate an event mention with its most relevant **Wikipedia page**, providing external background knowledge.

#### Input:
- An article and an event mention *m*

#### Output:
- A Wikipedia title *t* that best explains the meaning of *m*

---

### Event Coreference Resolution  
**Event Coreference Resolution** is the task of clustering together event mentions that refer to the same real-world event.

The task can be performed in two settings:
- **Within-Document (WD)** — Mentions in the same document  
- **Cross-Document (CD)** — Mentions across multiple documents

> ℹ️ CD coreference is considered more challenging, as it includes both WD and CD resolution.

#### Input:
- A single document (WD)  
- A set of documents (CD)

#### Output:
- Sets of clusters containing coreferring event mentions

---

### Event Coreference Search  
**Event Coreference Search** focuses on efficiently finding all event mentions that corefer with a specific **query event** in a large corpus.

#### Input:
- A query containing a marked event mention in context  
- A document or passage collection

#### Output:
- All coreferring event mentions, along with their contexts

---

### Event Temporality Identification (ETI)  
**ETI** is the task of identifying **temporal relations** between events, helping to establish timelines and event durations.

#### Input:
- A sentence, passage, or document with marked events

#### Output:
- A directed **temporal graph**, where nodes are events and edges represent temporal relations between them

---

### Event Causality Identification (ECI)  
**ECI** is the task of identifying **causal relations** between events—specifically, determining whether one event **caused** another to occur.

#### Input:
- A sentence, passage, or document containing a marked event pair

#### Output:
- The causal relation (if any) between the two events

---

### Subevent Identification  
**Subevent Identification** is the task of discovering **hierarchical structures** between events—specifically, recognizing when one event is a **subevent** of another.

#### Input:
- A sentence or document containing multiple events

#### Output:
- A structured graph or hierarchy indicating parent-child (composite-subevent) relationships between events

