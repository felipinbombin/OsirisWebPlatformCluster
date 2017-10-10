# -*- coding: utf-8 -*-

# model modules
from models.SMinit import SMinit
from models.FM import FM
from models.EM_main import SMinit
from models.test import Test

import sys
import pickle


def run_model(model_id, model_input_file_path, output_file_name):
    """ choose model and execute """
    
    with open(model_input_file_path, mode='rb') as data_file:
        input_dict = pickle.load(data_file)
        # global properties given by user
        first_input = input_dict["first_input"]
        # output of previous models
        second_input = input_dict["second_input"]

    output_dict = None

    if model_id == "S":
        output_dict = SMinit(first_input)
    elif model_id == "F":
        output_dict = FM(first_input, second_input)
    elif model_id == "E":
        output_dict = EM_main(first_input, second_input)
    elif model_id == "T":
        output_dict = FM(first_input, second_input)
    elif model_id == "Test":
        # for testing purpose
        output_dict = Test(input_dict)
    
    output_dict = {
        "first_input": first_input,
        "second_input": output_dict,
    }

    pickle_file = open(output_file_name, "wb")
    pickle.dump(output_dict, pickle_file, protocol=2)
    pickle_file.flush()
    pickle_file.close()


if __name__ == "__main__":
    """ run model """
    run_model(sys.argv[1], sys.argv[2], sys.argv[3])

