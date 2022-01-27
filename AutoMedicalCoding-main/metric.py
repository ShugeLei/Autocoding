import pandas as pd

df_spacy = pd.read_csv("bioscope_negated_test_spacy_trf.csv")
# df_ctakes = pd.read_csv("bioscope_negated_test_ctakes.csv")

correct_spacy = df_spacy["spacy_negation"].sum()
# correct_ctakes = df_ctakes["ctakes_negated"].sum()
print(correct_spacy/len(df_spacy)*100)
# print(correct_ctakes/len(df_ctakes)*100)

