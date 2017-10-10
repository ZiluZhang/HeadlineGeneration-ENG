Steps to run the experiment on English News dataset:
	1. save all the data in ./ENGdatasets/Raw_data/
	2. run ./ENGdatasets/data_r2f.py
		get formatted data
	3. run ./ENGdatasets/build_dict.py
		get dictionary for this dataset
	4. run ./ENGdatasets/data_f2id.py
		convert each word to its index in the dictionary
	5. run ./Paper-model-main.py (-mode train) (-max_epochs xxx)

Outputs:
	1. ./log_output/ is the directory that keep log files for experiments.
		./log_output/exp_1007.txt is training only 1 epoch
		./log_output/exp_1007_10.txt is training 10 epochs
	2. ./ENGdatasets/Sample-output-* is results (output for some train/valid/test data)
		Sample-output-1 is for training only 1 epoch
		Sample-output-10 is for training 10 epochs


p.s. Now with debug version, the task is to duplicate the second sentence in the news.
