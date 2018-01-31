from runModel import run_model

import unittest
import pickle
import os

test_input_path = "tests/inputs/{0}"
test_output_path = "tests/outputs/{0}"


class CommonTest:
    """ base to other tests """

    def __init__(self):
        self.model_id = None
        self.input_file_path = None
        self.output_file_path = None

    def run_model(self):
        """ run model and return dict """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user or previous model
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        return model_input, model_output

    def delete_output_file(self):
        """ delete file """
        if os.path.exists(self.output_file_path):
            pass
            # os.remove(self.output_file_path)

    def print_dictionary(self, val, spaces=0):
        from collections import defaultdict
        import numpy as np
        import datetime
        if isinstance(val, defaultdict) or isinstance(val, dict):
            for a in val:
                print("{0}{1}:".format(' ' * spaces, a))
                self.rec(val[a], spaces + 4)
        elif isinstance(val, np.ndarray) or isinstance(val, list) or isinstance(val, tuple):
            for b in val:
                self.rec(b, spaces + 4)
        elif not (isinstance(val, int) or
                  isinstance(val, float) or
                  isinstance(val, str) or
                  isinstance(val, datetime.time) or
                  isinstance(val, datetime.timedelta) or
                  isinstance(val, np.float64) or
                  isinstance(val, np.int64) or
                  isinstance(val, np.int32)):
            print("{0}{1}:".format(' ' * spaces, type(val)))

class TestSpeedModel(unittest.TestCase, CommonTest):
    """  run speed model """

    def setUp(self):
        self.model_id = 'S'
        self.input_file_path = test_input_path.format("speed.model_input")
        self.output_file_path = test_output_path.format("speed.model_output")

    def test_run(self):
        """ validate output dict """
        # _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


class TestForceModel(unittest.TestCase, CommonTest):
    """  run force model """

    def setUp(self):
        self.model_id = 'F'
        self.input_file_path = test_input_path.format("force.model_input")
        self.output_file_path = test_output_path.format("force.model_output")

    def test_run(self):
        """ validate output dict """
        # _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


class TestEnergyModel(unittest.TestCase, CommonTest):
    """  run energy model """

    def setUp(self):
        self.model_id = 'E'
        self.input_file_path = test_input_path.format("energy.model_input")
        self.output_file_path = test_output_path.format("energy.model_output")

    def test_run(self):
        """ validate output dict """
        # _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


class TestThermalModel(unittest.TestCase, CommonTest):
    """  run thermal model """

    def setUp(self):
        self.model_id = 'T'
        self.input_file_path = test_input_path.format("heat.model_input")
        self.output_file_path = test_output_path.format("heat.model_output")

    def test_run(self):
        """ validate output dict """
        _, model_output = self.run_model()

    def test_check_output(self):
        # check dict answer here

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user or previous model
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        #self.print_dictionary(model_input)
        #self.print_dictionary(model_output)
        self.assertIn("lines", model_output["TM"].keys())
