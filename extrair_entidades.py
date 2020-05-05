import spacy
import requests

nlp = spacy.load("pt_core_news_sm")

r = requests.get("https://arquivo.pt/textextracted?m=http://www.igot.ulisboa.pt/20181109014435")
r.encoding = "utf-8"
document = r.text
doc = nlp(document)

entities = {}
for entity in doc.ents:
    if not entity.label_ in entities:
        entities[entity.label_] = []
    if not entity.text in entities[entity.label_]:
        entities[entity.label_].append(entity.text)

for label in entities:
    print(spacy.explain(label) + ": ")
    print(", ".join(entities[label]))
    print()
