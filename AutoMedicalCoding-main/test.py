import os
from ctakes_parser import ctakes_parser as parser

current_cwd = os.getcwd()
ctakes_folder = os.path.join(current_cwd, "apache-ctakes-4.0.0.1-bin")

os.environ["CTAKES_HOME"] = ctakes_folder
# print(os.environ["CTAKES_HOME"])

clinical_pipeline_file_path = os.path.join(ctakes_folder, "bin", "runClinicalPipeline.bat")

# print(clinical_pipeline_file_path)

umls_key = "6c14437a-be2a-4147-a6d9-db1d6bb3358a"

input_dir = os.path.join(current_cwd, "hbs_analysis_text") # input directory contining medical texrt files
output_dir = os.path.join(current_cwd, "results") # output directory to store the output files of cTakes
parsed_dir = os.path.join(current_cwd, "parsed")# parsed directory to store the parsed files of cTakes into csv
os.system("{} -i {} --xmiOut {} --key {}".format(clinical_pipeline_file_path, input_dir, output_dir, umls_key))


parser.parse_dir(in_directory_path=output_dir, out_directory_path=parsed_dir)



