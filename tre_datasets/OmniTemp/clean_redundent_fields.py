import json
import os

input_dir = "train_orig"
output_dir = f"{input_dir}_fix"

# make output dir
os.makedirs(output_dir, exist_ok=False)

for file in os.listdir(input_dir):
    if not file.endswith('.json'):
        continue

    print("Processing file:", file)
    new_data = dict()
    with open(os.path.join(input_dir, file), 'r') as f:
        obj = json.load(f)

    output_lines = []
    tokens = obj['tokens']
    pairs = obj['allPairs']
    mentions = obj['allMentions']

    new_mentions = []
    for ment in mentions:
        if ment['axisType'] != 'main':
            continue

        del ment['axisType']
        del ment['rootAxisEventId']
        del ment['doc_id']
        new_mentions.append(ment)

    for pair in pairs:
        if pair['_relation'] == 'uncertain':
            pair['_relation'] = 'vague'

    new_data['tokens'] = tokens
    new_data['allMentions'] = new_mentions
    new_data['allPairs'] = pairs

    with open(os.path.join(output_dir, file), 'w') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)
