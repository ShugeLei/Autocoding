import pandas as pd


import spacy
# import scispacy
from negspacy.negation import Negex
import os 
import pandas as pd

# bc5_model = "en_ner_bc5cdr_md"
bc5_model = "en_core_web_trf"

def negation_model(nlp_model):
    nlp = spacy.load(nlp_model)
    nlp.add_pipe('sentencizer')
    nlp.add_pipe("negex")
    return nlp
nlp = negation_model(bc5_model)


df = pd.read_csv("bioscope_negated_test.csv")

df["spacy_negation"] = df["sentence"].apply(lambda x: 1 if [e._.negex for e in nlp(x).ents] else 0)
df.to_csv("bioscope_negated_test_spacy_trf.csv", index=False)