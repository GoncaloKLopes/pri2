Ex1:
	python 1.py [-text_input_file] [-ideal_summary_file]
	Will use our chosen input file and summary file by default.

Ex2:		
	python 2.py [-d source_texts_folder_path ideal_summary_folder_path] [-p prior_method] 
		    [-w weights_method]
	prior_method : degree_centrality_prior | sentence_position_prior (default) | uniform_prior
	weights_method : uniform_weight | cos_sim_weight (default

Ex3:		
	python 3.py [-d source_texts_folder_path ideal_summary_folder_path training_source_texts_folder_path training_ideal_summary_folder_path]

Ex4:
    python 4.py
