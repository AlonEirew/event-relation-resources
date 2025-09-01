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
  "The", "OmniTemp", "dataset", "is", "a", "comprehensive", "collection", "of", "temperature", "data", "from", "various", "sources", ".", 
  "It", "includes", "historical", "records", ",", "real-time", "measurements", ",", "and", "predictions", ".", 
  "The", "data", "is", "sourced", "from", "weather", "stations", ",", "satellites", ",", "and", "climate", "models", "."
]
```

### Mentions Object Example:
```json
{
  "tokens": "felt",
  "eventIndex": 0,
  "m_id": "47",
  "doc_id": "summary",
  "tokens_ids": [
    9
  ],
  "axisType": "not_event",
  "rootAxisEventId": -1,
  "corefState": "unknown"
}
```

Field Descriptions:
- `tokens`: The text of the mention.
- `eventIndex`: The index of the event this mention is associated with
- `m_id`: Unique identifier for the mention.
- `doc_id`: Identifier for the document containing the mention.
- `tokens_ids`: List of token indices that make up the mention (indices are correlated with the `toknes` list).
- `axisType`: Type of axis (e.g., "not_event", "actual_event", etc.).
- `rootAxisEventId`: Identifier for the root axis event, if applicable.
- `corefState`: Coreference state (e.g., "unknown", "coreferent", etc.).
