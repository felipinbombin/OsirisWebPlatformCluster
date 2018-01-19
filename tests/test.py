from runModel import run_model

import unittest
import pickle
import os


class BaseTest(unittest.TestCase):
    """ base to other tests """

    def __init__(self):
        self.model_id = None
        self.input_file_path = None
        self.output_file_path = None

        super(BaseTest, self).__init__()

    def delete_output_file(self):
        """ delete file """
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)


class TestSpeedModel(BaseTest):
    """  run speed model """

    def setUp(self):
        self.model_id = 'S'
        self.input_file_path = "tests/speed.model_input"
        self.output_file_path = "tests/aa.model_output"

    def test_run(self):
        """  """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        self.delete_output_file()


class TestForceModel(BaseTest):
    """  run force model """

    def setUp(self):
        self.model_id = 'F'
        self.input_file_path = "tests/speed.model_input"
        self.output_file_path = "tests/speed.model_output"

    def test_run(self):
        """  """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        self.delete_output_file()


class TestEnergyModel(BaseTest):
    """  run energy model """

    def setUp(self):
        self.model_id = 'E'
        self.input_file_path = "tests/energy.model_input"
        self.output_file_path = "tests/energy.model_output"

    def test_run(self):
        """  """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        self.delete_output_file()


class TestThermalModel(BaseTest):
    """  run thermal model """

    def setUp(self):
        self.model_id = 'T'
        self.input_file_path = "tests/heat.model_input"
        self.output_file_path = "tests/heat.model_output"

    def test_run(self):
        """  """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        self.delete_output_file()


if __name__ == '__main__':
    unittest.main()
