## OmniTemp File Structure
```json
{
  "tokens": ["List Of All Tokens In The Document"],
  "allMentions": ["List of all Mentions objects"],
  "allPairs": ["List of all Pair objects"]
}
```

### Tokens List Examples:
```json
[
  "The", "OmniTemp", "dataset", "features", "exhaustive", "temporal", "relations", "annotations", "providing", 
  "full", "temporal", "relation", "coverage", "for", "all", "targeted", "events", "within", "the", "dataset", "."
]
```

### Mentions Object Example:
```json
{
  "tokens": "features",
  "eventIndex": 0,
  "m_id": "0",
  "tokens_ids": [
    3
  ]
}
```

Field Descriptions:
- `tokens`: The text of the mention.
- `eventIndex`: The index of the event this mention is associated with
- `m_id`: Unique identifier for the mention.
- `tokens_ids`: List of token indices that make up the mention (indices are correlated with the `toknes` list).


### Pair Object Example:
```json
{
  "_firstId": 0,
  "_secondId": 1,
  "_relation": "equal"
}
```

Field Descriptions:
- `_firstId`: The `m_id` of the first mention in the pair.
- `_secondId`: The `m_id` of the second mention in the pair.
- `_relation`: The type of relationship between the two mentions
