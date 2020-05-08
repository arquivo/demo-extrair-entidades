import spacy
import requests
import sys
from collections import defaultdict

nlp = spacy.load("pt_core_news_sm")

url = sys.argv[1]

r = requests.get("https://arquivo.pt/textsearch?versionHistory={}&maxItems=50".format(url))

results = r.json()["response_items"]

linkToExtractedText = None

for r in results:
	if r["linkToExtractedText"]:
		linkToExtractedText = r["linkToExtractedText"]
		break

if not linkToExtractedText:
	print("No results for URL \"{}\"".format(url))
	sys.exit(1)

r = requests.get(linkToExtractedText)
r.encoding = "utf-8"
document = r.text
doc = nlp(document)

entities = defaultdict(set)
for entity in doc.ents:
    entities[entity.label_].add(entity.text)

for label in entities:
    print(spacy.explain(label) + ": ")
    print("; ".join(sorted(entities[label])))
    print()
