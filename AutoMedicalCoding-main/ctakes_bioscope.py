import pandas as pd
import os
import json 
from ctakes_parser import ctakes_parser as parser

# df = pd.read_csv("bioscope_negated_test.csv")
# input_folder = os.path.join(os.getcwd(), "bioscope","input")

# for index, row in df.iterrows():
#     # write the row to the file
#     with open(os.path.join(input_folder, "{}.txt".format(index)), "w", encoding="utf-8") as f:
#         f.write(row["sentence"])
#         f.write("\n")
#     print(index)
    


# current_cwd = os.getcwd()
# ctakes_folder = os.path.join(current_cwd, "apache-ctakes-4.0.0.1-bin")

# os.environ["CTAKES_HOME"] = ctakes_folder
# # print(os.environ["CTAKES_HOME"])

# clinical_pipeline_file_path = os.path.join(ctakes_folder, "bin", "runClinicalPipeline.bat")

# # print(clinical_pipeline_file_path)

# umls_key = "6c14437a-be2a-4147-a6d9-db1d6bb3358a"

output_dir =  os.path.join(os.getcwd(), "bioscope","result") # output directory to store the output files of cTakes
parsed_dir =  os.path.join(os.getcwd(), "bioscope","parsed")# parsed directory to store the parsed files of cTakes into csv
# os.system("{} -i {} --xmiOut {} --key {}".format(clinical_pipeline_file_path, input_folder, output_dir, umls_key))




# files = os.listdir(os.path.join(os.getcwd(), "bioscope","result"))
# err_count =0
# for i, file in enumerate(files):
#     print(i)
#     try:
#         df = parser.parse_file(os.path.join(output_dir, file))
#         df.to_csv(os.path.join(parsed_dir, "{}.csv".format(file.split(".")[0])), index=False)
#     except:
#         err_count+=1
#         continue
# print(err_count)
# parser.parse_dir(in_directory_path=output_dir, out_directory_path=parsed_dir)

parsed_files = os.listdir(parsed_dir)
bioscope_df = pd.read_csv("bioscope_negated_test.csv")
bioscope_df["ctakes_negated"] = 0

print(bioscope_df.head())
for i, file in enumerate(parsed_files):
    print(file)
    df = pd.read_csv(os.path.join(parsed_dir, file))
    if len(df[df["negated"]==True]) > 0:
        df.loc[file.split(".")[0], "ctakes_negated"] = 1
    print(i)    

bioscope_df.to_csv("bioscope_negated_test_ctakes.csv", index=False)