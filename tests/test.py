from runModel import run_model

import unittest
import pickle


class TestSpeedModel(unittest.TestCase):
    """  run speed model """
    def setUp(self):
        self.model_id = 'S'

    def test_run(self):
        """  """
        input_file_path = "tests/speed.model_input"
        output_file_path = "tests/aa.model_output"
        run_model(self.model_id, input_file_path, output_file_path)

        # check file
        with open(output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]


class TestForceModel(unittest.TestCase):
    """  run force model """
    def setUp(self):
        self.model_id = 'F'

    def test_run(self):
        """  """
        input_file_path = "tests/speed.model_input"
        output_file_path = "tests/speed.model_output"
        run_model(self.model_id, input_file_path, output_file_path)

        # check file
        with open(output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]


class TestEnergyModel(unittest.TestCase):
    """  run energy model """
    def setUp(self):
        self.model_id = 'E'

    def test_run(self):
        """  """
        input_file_path = "tests/energy.model_input"
        output_file_path = "tests/energy.model_output"
        run_model(self.model_id, input_file_path, output_file_path)

        # check file
        with open(output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]


class TestThermalModel(unittest.TestCase):
    """  run thermal model """
    def setUp(self):
        self.model_id = 'T'

    def test_run(self):
        """  """
        input_file_path = "tests/heat.model_input"
        output_file_path = "tests/heat.model_output"
        run_model(self.model_id, input_file_path, output_file_path)

        # check file
        with open(output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]


if __name__ == '__main__':
    unittest.main()