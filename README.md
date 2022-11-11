# Entity_Relationship_with_Knowledge_Graph
The code in this repository provides a simple and basic implementation of Enhanced Language Representation with Informative Entities [ERNIE](https://arxiv.org/abs/1905.07129) using various NLP packages. 

ERNIE uses Heterogeneous information fusion along with structured knowledge encoding. The latter refers to the extraction of informative facts using language representation models while the former combines the knowledge, syntactic, and lexical knowledge for specialized training of the language model. 

Following packages need to be installed before running the code

Spacy
networkx
rdflib
matplotlib

Make sure either you have downloaded en_core_web_sm or use python -m spacy download en_core_web_sm

alternatively you can add 

import en_core_web_sm if the load command does not work. 

A sample result is shown below:

![image](https://user-images.githubusercontent.com/26203136/201359506-eaa828cb-04f5-4d36-8ed0-4425adf7b7c2.png)
