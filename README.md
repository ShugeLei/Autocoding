# AutoCoding
This repository contains the work necessary for AutoCoding Container

AutoCoding/resources: Contains resources for the BERT model
AutoCoding/src: Contains the main body of code
AutoCoding/src/bin, AutoCoding/src/lib, AutoCoding/src/resources: Contain cTakes resources

bot_3.0.py: Can be run using python3 bot_3.0.py, contains some example code for running the pipeline.

utils/test_utils.py contains methods for testing the prediction capability of the pipeline

Note: The CTakesExtractor takes the "reextract" field, which indicates whether extraction should
be reperformed. Currently, its input files created from extraction are preserved in a specified
input directory. The "reextract" field was included to save time during training/testing.
