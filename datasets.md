# Datasets
Below is a list of prominent datasets focused on the tasks of event detection, event extraction, and event-event relation extraction. 

---

## Tables / Column Descriptions  
This page contains tables that provide details about various datasets. The following section explains the meaning of each column:  

### **Data Source**  
The origin of the documents in the dataset (e.g., news articles, Wikipedia, etc.).

### **Annotation**  
The types of annotations included in the dataset (e.g., events, entities, coreference, etc.).

### **Density**  
Event and event-relation annotation is a complex and resource-intensive task. As a result, some datasets are *exhaustively* annotated—covering all events in a given text—while others contain only *partial* annotations.

> ℹ️ **Partial-exhaustive** annotation means that only a portion of each document is selected for annotation (e.g., the first *x* sentences), and within those selected sentences, all events are exhaustively annotated.  
>
> ℹ️ In **non-exhaustive** settings, event detection or extraction typically cannot be performed independently; instead, the spans of event mentions are provided as input to the model.

### **Scope**  
Describes the setting under which event-event relations are extracted.

> ℹ️ **Within-Document (WD)** relation extraction focuses on identifying relations between events occurring in the same document.  
>
> ℹ️ **Cross-Document (CD)** relation extraction involves identifying relations between events that may appear in different documents.

### **Lang**  
The languages for which the dataset includes annotated data.

### **License**  
Describes the licensing conditions of the dataset. Some datasets are freely available and open-source, while others have more restrictive usage terms—this may influence their usability in certain projects.


## Datasets 
- [Automatic Content Extraction (ACE)](#automatic-content-extraction-ace)
- [CaTeRS](#caters-causal-and-temporal-relation-scheme-)
- [EventCorefBank Extension (ECB+)](#eventcorefbank-extension-ecb-)
- [Entities, Relations and Events (ERE)](#entities-relations-and-events-ere-)
- [Event-Event Relations (EER)](#event-event-relations-eer-)
- [Event StoryLine Corpus (ESC)](#event-storyline-corpus-esc-)
- [Gun Violence Corpus (GVC)](#gun-violence-corpus-gvc-)
- [HiEve](#hieve-)
- [HyperCoref](#hypercoref-)
- [MAVEN](#maven-)
- [MAVEN-ERE](#maven-ere-)
- [MATRES](#matres-)
- [MEANTIME](#meantime-)
- [Richer Event Description (RED)](#richer-event-description-red-)
- [TB-Dense](#timebank-dense-tb-dense-)
- [The Penn Discourse TreeBank](#the-penn-discourse-treebank-pdtb-)
- [Wikipedia Event Coreference (WEC)](#wikipedia-event-coreference-wec-)

---

## Automatic Content Extraction (ACE)
ACE provides comprehensive event annotation guidelines across multiple languages. Additionally, ACE serves as the foundational annotation scheme for many subsequent event annotation frameworks.

### References
- [English Annotation Guidelines for Events](https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-events-guidelines-v5.4.3.pdf)
- [Annotation Tasks and Specifications](https://www.ldc.upenn.edu/collaborations/past-projects/ace/annotation-tasks-and-specifications)

---

## CaTeRS: Causal and Temporal Relation Scheme  
CaTeRS is a semantic annotation framework designed to simultaneously capture a wide range of temporal and causal event relations.

The dataset includes 1,600 annotated sentences, drawn from 320 five-sentence stories sampled from the ROCStories corpus.

### References (2016)
- [CaTeRS: Causal and Temporal Relation Scheme for Semantic Annotation of Event Structures](https://aclanthology.org/W16-1007/)
- [CaTeRS Dataset](https://cs.rochester.edu/nlp/rocstories/CaTeRS/)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| [ROCStories](https://cs.rochester.edu/nlp/rocstories/) | 320 | 2,708 | Exhaustive | events<br/>causal<br/>temporal | Within document | eng | --- |

---

## EventCorefBank Extension (ECB+)  
An extension of the EventCorefBank (ECB), ECB+ is one of the most widely used datasets for cross-document event coreference tasks. It consists of 982 documents grouped into 43 clusters, each centered on a specific news topic.

### References
- [Using a Sledgehammer to Crack a Nut? Lexical Diversity and Event Coreference Resolution](https://aclanthology.org/L14-1646/)
- [ECB+ Corpus](http://www.newsreader-project.eu/results/data/the-ecb-corpus/)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| News | 982 | 6,833 | Partial-exhaustive | events<br/>entities<br/>coreference | Within and cross-document | eng | [CC-BY](http://creativecommons.org/licenses/by/2.0/) |

---

## Entities, Relations, and Events (ERE)  
- **Light ERE**: A simplified annotation scheme derived from ACE, designed for consistency and ease of use.  
- **Rich ERE**: Builds on Light ERE by expanding both the annotation inventory and taggability.

### References
- [Rich ERE Guidelines](https://tac.nist.gov/2016/KBP/guidelines/summary_rich_ere_v4.2.pdf)
- [From Light to Rich ERE: Annotation of Entities, Relations, and Events](https://aclanthology.org/W15-0812.pdf)

---

## Event-Event Relations (EER)  
EER provides annotation for event-event relations within the ERE/ACE taxonomy, covering both within- and cross-document settings.

### References
- [Building a Cross-document Event-Event Relation Corpus](https://aclanthology.org/W16-1701)

| Data Source | Documents | Events | Density | Annotation | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:----:|:-------:|
| News | 125 | 863 | Partial-exhaustive | events<br/>coreference<br/>temporal<br/>causal<br/>subevent | TPD | Free |

---

## Event StoryLine Corpus (ESC)  
ESC introduces an annotation scheme and benchmark for identifying temporal and causal relations between events. It builds upon and extends the ECB+ annotation framework.

### References (2017)
- [The Event StoryLine Corpus: A New Benchmark for Causal and Temporal Relation Extraction](https://aclanthology.org/W17-2711/)
- [GitHub](https://github.com/cltl/EventStoryLine)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| News | 258 | 7,275 | Partial-exhaustive | events<br/>entities<br/>coreference<br/>temporal<br/>causal | Within and cross-document | eng | [CC-BY](http://creativecommons.org/licenses/by/2.0/) |

---

## Gun Violence Corpus (GVC)  
GVC is an automatically annotated dataset developed for cross-document event coreference.

### References
- [Don’t Annotate, but Validate: a Data-to-Text Method for Capturing Event Data](https://aclanthology.org/L18-1480/)
- [GVC Corpus](https://github.com/cltl/GunViolenceCorpus)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| Police Reports | 510 | 7,298 | Non-exhaustive | events<br/>event arguments<br/>coreference | Within and cross-document | eng | [CC](https://github.com/cltl/GunViolenceCorpus/blob/master/LICENSE.md) |

---

## HiEve  
HiEve is a corpus for identifying spatiotemporal containment between events, forming hierarchical structures of superevent–subevent relations.

### References
- [HiEve: A Corpus for Extracting Event Hierarchies from News Stories](https://aclanthology.org/L14-1020/)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| News | 100 | ~32 per doc | Non-exhaustive | events<br/>coreference<br/>subevents | Within document | eng | CC BY-NC-SA 3.0 |

---

## HyperCoref  
HyperCoref automatically constructs large-scale cross-document event coreference data by mining hyperlinks in online news articles.

### References
- [Event Coreference Data (Almost) for Free: Mining Hyperlinks from Online News](https://aclanthology.org/2021.emnlp-main.38/)

---

## MAVEN  
MAssive eVENt detection (MAVEN) is a large-scale event detection dataset designed to address data scarcity and expand event type coverage.

### References
- [MAVEN: A Massive General Domain Event Detection Dataset](https://aclanthology.org/2020.emnlp-main.129/)
- [MAVEN GitHub](https://github.com/THU-KEG/MAVEN-dataset)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| Wikipedia | 4,480 | 118,732 | Exhaustive | events | Within document | eng | ?? |

---

## MAVEN-ERE  
MAVEN-ERE is a large, unified human-annotated dataset extending MAVEN, with annotations for coreference, temporal, causal, and subevent relations.

### References
- [MAVEN-ERE: A Unified Large-scale Dataset for Event Coreference, Temporal, Causal, and Subevent Relation Extraction](https://arxiv.org/abs/2211.07342)
- [MAVEN-ERE GitHub](https://github.com/THU-KEG/MAVEN-ERE)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| Wikipedia | 4,480 | 103,193 | Exhaustive | events<br/>coreference<br/>temporal<br/>causal<br/>subevents | Within document | eng | CC BY-NC-SA 3.0 |


---

## MATRES  
MATRES introduces a multi-axis temporal annotation framework to better capture the structure of event timelines. It focuses on annotating event temporal relations based on *start points* only, as event end-points were found to be a major source of annotation disagreement.

### References
- [A Multi-Axis Annotation Scheme for Event Temporal Relations](https://aclanthology.org/P18-1122/)

---

## MEANTIME  
The MEANTIME corpus is a semantically annotated multilingual dataset of Wikinews articles. It shares annotation guidelines with ECB+ via the [NewsReader annotation guidelines](http://www.newsreader-project.eu/files/2014/12/NWR-2014-2-2.pdf). It includes articles in English, Spanish, Italian, and Dutch.

### References
- [MEANTIME: The NewsReader Multilingual Event and Time Corpus](https://aclanthology.org/L16-1699/)
- [MEANTIME Corpus](http://www.newsreader-project.eu/results/data/wikinews/)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| Wikinews | 480 | 2,107 | Exhaustive | events<br/>entities<br/>coreference | Within and cross-document | eng<br/>it<br/>de<br/>sp | CC-BY |

---

## Richer Event Description (RED)  
RED aims to integrate multiple well-established annotation approaches into a single representation that captures events and their participants in discourse. Unlike some other schemes, it does not focus on traditional semantic roles.

### References
- [Richer Event Description: Integrating Event Coreference with Temporal, Causal and Bridging Annotation](https://aclanthology.org/W16-5706)
- [RED Annotation Guidelines](https://github.com/timjogorman/RicherEventDescription/blob/master/guidelines.md)
- [RED Corpus (LDC2016T23)](https://catalog.ldc.upenn.edu/LDC2016T23)

| Data Source | Documents | Events | Density | Annotation | License |
|-------------|:---------:|:------:|:-------:|------------|:-------:|
| News | 95 | 8,731 | Exhaustive | entities<br/>events<br/>coreference<br/>temporal<br/>causal<br/>subevents | [LDC](https://catalog.ldc.upenn.edu/license/ldc-non-members-agreement.pdf) |

---

## TimeBank-Dense (TB-Dense)  
TB-Dense is a temporally dense annotation of event-time and event-event relations over a subset of TimeBank. Unlike earlier TimeBank corpora that annotated only a few relations per document, TB-Dense provides annotations for all possible pairs of temporal entities (events and time expressions) in selected sections, making it a valuable resource for dense temporal reasoning.

### References
- [Towards a grounded and realistic annotation of time: The TimeBank-Dense corpus](https://aclanthology.org/P14-2082/)
- [TB-Dense Dataset](tre_datasets/TimeBankDense)

| Data Source | Documents | Events | Density | Annotation | Scope | Lang | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:----:|:-------:|
| TimeBank (subset) | 36 | 6,472 | Exhaustive (selected sections) | events<br/>timex3<br/>temporal relations | Within document | eng | [LDC](https://catalog.ldc.upenn.edu/LDC2006T08) |

---

## The Penn Discourse TreeBank (PDTB)  
PDTB provides discourse-level annotation over the 1M-word Wall Street Journal corpus. It includes annotations for events, event arguments (entities), and the relations between them—event-event, event-entity, and entity-entity.

### References
- [The Penn Discourse TreeBank](https://www.ling.upenn.edu/~elenimi/lrec04-lisbon-miltsakaki.pdf)
- [The Penn Discourse TreeBank 2.0](https://aclanthology.org/L08-1093/)
- [PDTB 3.0 Dataset Catalog](https://catalog.ldc.upenn.edu/LDC2019T05)

---

## Wikipedia Event Coreference (WEC)  
WEC is a large-scale automatically annotated corpus derived from Wikipedia using an event hyperlinking method. The WEC-Eng version focuses on English Wikipedia.

### References
- [WEC: Deriving a Large-scale Cross-document Event Coreference Dataset from Wikipedia](https://aclanthology.org/2021.naacl-main.198/)
- [WEC Annotation Process](https://github.com/AlonEirew/extract-wec)
- [WEC-Eng Corpus on HuggingFace](https://huggingface.co/datasets/Intel/WEC-Eng)

| Data Source | Documents | Events | Density | Annotation | Scope | License |
|-------------|:---------:|:------:|:-------:|------------|:------:|:-------:|
| Wikipedia | N/A | 43,672 | Non-exhaustive | events<br/>coreference | Cross-document | [CC BY-SA](https://creativecommons.org/licenses/by-sa/3.0/deed.en_US) |

---
