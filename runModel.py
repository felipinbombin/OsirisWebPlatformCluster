# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'models'))

# model modules
from models.SMinit import SMinit
from models.FM import FM
from models.EM_main import EM_main
from models.TM import TM
from models.test import Test
from models.ECM import energy_center_model

import pickle
import gzip


def run_model(model_id, model_input_file_path, output_file_name):
    """ choose model and execute """

    with gzip.open(model_input_file_path, mode='rb') as data_file:
        input_dict = pickle.load(data_file)
        # global properties given by user
        model_input = input_dict["input"]
        # output of previous models
        model_output = input_dict["output"]

    if model_id == "S":
        model_output["SM"] = SMinit(model_input)
    elif model_id == "F":
        model_output["FM"] = FM(model_input, model_output)
    elif model_id == "E":
        model_output["EM"] = EM_main(model_input, model_output)
    elif model_id == "ECM":
        model_output["ECM"] = energy_center_model(model_input, model_output)
    elif model_id == "T":
        model_output["TM"] = TM(model_input, model_output)
    elif model_id == "Test":
        # for testing purpose
        model_output = Test(input_dict)

    output_dict = {
        "input": model_input,
        "output": model_output,
    }

    pickle_file = gzip.open(output_file_name, "wb")
    pickle.dump(output_dict, pickle_file, protocol=2)
    pickle_file.flush()
    pickle_file.close()


if __name__ == "__main__":
    """ run model """
    run_model(sys.argv[1], sys.argv[2], sys.argv[3])
