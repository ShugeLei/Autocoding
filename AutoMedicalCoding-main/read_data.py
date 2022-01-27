import pandas as pd
import os
import json 

df = pd.read_csv("hbs_analysis.csv")
text_folder = os.path.join(os.getcwd(), "hbs_analysis_text")

for index, row in df.iterrows():
    # write the row to the file
    input_row = json.loads(row["input"])
    if input_row["entities"]:
        
        with open(os.path.join(text_folder, "{}.txt".format(row["id"])), "w", encoding="utf-8") as f:
            f.write(input_row["entities"][0]["content"])
            f.write("\n")
    print(index)
    

