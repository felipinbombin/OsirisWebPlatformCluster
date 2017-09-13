# -*- coding: utf-8 -*-

# model modules
from models.speedModel import SM

import sys
import pickle


def run_model(model_id, model_input_file_path, output_file_name):
    """ choose model and execute """
    
    data_file = open(model_input_file_path, mode='rb')
    input_dict = pickle.load(data_file)
    data_file.close()
    output_dict = None

    if model_id == "S":
        output_dict = SM(input_dict)
    elif model_id == "F":
        output_dict = SM(input_dict)
    elif model_id == "E":
        output_dict = SM(input_dict)
    elif model_id == "T":
        output_dict = SM(input_dict)
    
    pickle_file = open(output_file_name, "wb")
    pickle.dump(output_dict, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle_file.flush()
    pickle_file.close()


if __name__ == "__main__":
    """ run model """
    run_model(sys.argv[1], sys.argv[2], sys.argv[3])

