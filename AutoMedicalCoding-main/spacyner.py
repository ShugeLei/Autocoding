import spacy
import scispacy
from negspacy.negation import Negex
import os 
import pandas as pd

bc5_model = "en_ner_bc5cdr_md"

current_cwd = os.getcwd()

def negation_model(nlp_model):
    nlp = spacy.load(nlp_model)
    nlp.add_pipe('sentencizer')
    nlp.add_pipe("negex")
    return nlp

input_folder = os.path.join(current_cwd, "test")
with open(os.path.join(input_folder,"fracture_demo.txt"), 'r') as file:
    medical_note = file.read()

nlp = negation_model(bc5_model)

text_negation = {"entities":[], "negations":[]}
doc = nlp(medical_note)
for e in doc.ents:
    text_negation["entities"].append(e.text)
    text_negation["negations"].append(e._.negex)
    print(e.text, e._.negex)

pd.DataFrame(text_negation).to_csv("test_negation.csv")
