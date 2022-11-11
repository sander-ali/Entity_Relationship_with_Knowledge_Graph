#Utility functions for Relation Extraction
from spacy.matcher import Matcher
import spacy
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('dbpedia_spotlight')



def get_relation(sent):
  aux = []
  doc = nlp(sent)

  # Matcher class object 
  matcher = Matcher(nlp.vocab)

  #define the pattern 
  pattern = [[{'DEP' : 'ROOT'}],[{'DEP' : 'relcl'}],
            [{'POS' : 'VERB' }]]

  matcher.add("matching_1",pattern) 

  matches = matcher(doc)
  for x in matches:
    aux.append(doc[x[1]:x[2]].text)

  return(aux)