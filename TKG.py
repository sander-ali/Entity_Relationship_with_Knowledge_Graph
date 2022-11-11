import spacy
from spacy import displacy
from utils import get_relation
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('dbpedia_spotlight')
doc = nlp("Roger Federer is married to Mirka Federer, who studied at University of Geneva")
# Tokenization
print([token.text for token in doc], sep=' ')

#Lemmatisation
print([token.lemma_ for token in doc], sep=' ')

#part of speech tagging
print([(token.lemma_, token.pos_) for token in doc], sep=' ')

#Dependency Parsing
print([(token.lemma_, token.dep_) for token in doc], sep=' ')

#Display dependency
displacy.render(doc, style="dep")

#Name Entity Recognition
print([(ent.text, ent.label_) for ent in doc.ents], sep = ' ')

ents = [ent for ent in doc.ents]
ents_t = [ent.text for ent in doc.ents]
print("Before:", [token.text for token in doc])

with doc.retokenize() as retokenizer:
    for i in range(len(ents)):
        retokenizer.merge(doc.ents[i])
print("After:", [token.text for token in doc])

#Named Entity Linking
print([ent.kb_id_ for ent in doc.ents])


#Relation Extraction
rels = get_relation("Roger Federer is married to Mirka Federer, who studied at University of Geneva")
print(rels)

g = Graph()

for ent in doc.ents:
    # add the label of the entity
    g.add((URIRef(ent.kb_id_), RDFS.label, Literal(ent.text)))
    prev = URIRef(ent.kb_id_)

g.add((URIRef('http://dbpedia.org/resource/Roger_Federer'), URIRef("https://dbpedia.org/ontology/"+rels[0]), URIRef('http://dbpedia.org/resource/Mirka_Federer')))
g.add((URIRef('http://dbpedia.org/resource/Mirka_Federer'), URIRef("https://dbpedia.org/ontology/"+rels[1]), URIRef('http://dbpedia.org/resource/Geneva')))

for s, p, o in g:
    print(s,p,o)

G = rdflib_to_networkx_multidigraph(g)

# Plot Networkx instance of RDF Graph
pos = nx.spring_layout(G, scale=2)
edge_labels = nx.get_edge_attributes(G, 'r')
plt.figure(figsize=(10,10))
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, with_labels=True)

#if not in interactive mode for 

plt.show()