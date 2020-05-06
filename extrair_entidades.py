import spacy
import requests
from collections import defaultdict

nlp = spacy.load("pt_core_news_sm")

r = requests.get("https://arquivo.pt/textextracted?m=http://www.igot.ulisboa.pt/20181109014435")
r.encoding = "utf-8"
document = r.text
doc = nlp(document)

entities = defaultdict(set)
for entity in doc.ents:
    entities[entity.label_].add(entity.text)

for label in entities:
    print(spacy.explain(label) + ": ")
    print("; ".join(entities[label]))
    print()
