Steps to run the experiment on English News dataset:
	1. save all the data in ./ENGdatasets/Raw_data/
	2. run ./ENGdatasets/data_r2f.py
		get formatted data
	3. run ./ENGdatasets/build_dict.py
		get dictionary for this dataset
	4. run ./ENGdatasets/data_f2id.py
		convert each word to its index in the dictionary
	5. run ./Paper-model-main.py (-mode train)

