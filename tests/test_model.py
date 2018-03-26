# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from runModel import run_model

from collections import defaultdict

import numpy as np
import datetime
import unittest
import pickle
import os
import gzip

test_input_path = os.path.join("inputs", "{0}")
test_output_path = os.path.join("outputs", "{0}")


class TestHelper:
    """ helper to run models """

    def __init__(self, model_id, input_file_path, output_file_path):
        self.model_id = model_id
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def run_model(self):
        """ run model and return dict """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with gzip.open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user or previous model
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        return model_input, model_output

    def delete_output_file(self, fake_remove=True):
        """ delete file """
        if os.path.exists(self.output_file_path) and not fake_remove:
            os.remove(self.output_file_path)

    def print_dictionary(self, val, spaces=0):
        if isinstance(val, defaultdict) or isinstance(val, dict):
            for a in val:
                print("{0}{1}:".format(' ' * spaces, a))
                self.print_dictionary(val[a], spaces + 4)
        elif isinstance(val, np.ndarray) or isinstance(val, list) or isinstance(val, tuple):
            for b in val:
                self.print_dictionary(b, spaces + 4)
        elif not (isinstance(val, int) or
                  isinstance(val, float) or
                  isinstance(val, str) or
                  isinstance(val, datetime.time) or
                  isinstance(val, datetime.timedelta) or
                  isinstance(val, np.float64) or
                  isinstance(val, np.int64) or
                  isinstance(val, np.int32)):
            print("{0}{1}:".format(' ' * spaces, type(val)))


class TestSpeedModel(unittest.TestCase):
    """  run speed model """

    def setUp(self):
        model_id = 'S'
        input_file_path = test_input_path.format("speed.model_input.gz")
        output_file_path = test_output_path.format("speed.model_output.gz")

        self.helper = TestHelper(model_id, input_file_path, output_file_path)

    def test_run(self):
        """ validate output dict """
        _, model_output = self.helper.run_model()

        # check dict answer here
        self.helper.delete_output_file()


class TestForceModel(unittest.TestCase):
    """  run force model """

    def setUp(self):
        model_id = 'F'
        input_file_path = test_input_path.format("force.model_input.gz")
        output_file_path = test_output_path.format("force.model_output.gz")

        self.helper = TestHelper(model_id, input_file_path, output_file_path)

    def test_run(self):
        """ validate output dict """
        _, model_output = self.helper.run_model()

        # check dict answer here

        self.helper.delete_output_file()


class TestEnergyModel(unittest.TestCase):
    """  run energy model """

    def setUp(self):
        model_id = 'E'
        input_file_path = test_input_path.format("energy.model_input.gz")
        output_file_path = test_output_path.format("energy.model_output.gz")

        self.helper = TestHelper(model_id, input_file_path, output_file_path)

    def test_run(self):
        """ validate output dict """
        _, model_output = self.helper.run_model()

        # check dict answer here

        self.helper.delete_output_file()


class TestThermalModel(unittest.TestCase):
    """  run thermal model """

    def setUp(self):
        model_id = 'T'
        input_file_path = test_input_path.format("heat.model_input.gz")
        self.output_file_path = test_output_path.format("heat.model_output.gz")

        self.helper = TestHelper(model_id, input_file_path, self.output_file_path)

    def test_run(self):
        """ validate output dict """
        _, model_output = self.helper.run_model()

        # check dict answer here

        self.helper.delete_output_file()

    def test_check_output(self):
        # check dict answer here

        # check file
        with gzip.open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user or previous model
            # model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        # self.print_dictionary(model_input)
        # self.print_dictionary(model_output)
        self.assertIn("lines", model_output["TM"].keys())
